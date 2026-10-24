"""The hand-written layer over the generated client: authentication, retries, idempotency keys,
typed errors and pagination, with the same rules as the Costfluent Go client."""

from __future__ import annotations

import asyncio
import email.utils
import itertools
import random
import time
import uuid
from collections.abc import AsyncIterator, Awaitable, Callable, Iterator, Mapping, Sequence
from datetime import UTC, datetime
from typing import Any, Protocol, Self, TypeVar

import httpx

from ._contract import IDEMPOTENT_CREATES
from ._version import __version__
from .client import AuthenticatedClient
from .models.api_error import ApiError
from .models.api_error_entry import ApiErrorEntry
from .types import Unset

DEFAULT_BASE_URL = "https://api.costfluent.com"
DEFAULT_TIMEOUT = 30.0
USER_AGENT = f"costfluent-python/{__version__}"

MAX_RETRIES = 3
BASE_DELAY = 1.0
MAX_DELAY = 30.0
# The longest Retry-After a request waits out. A longer one means the token's hourly quota is spent,
# and the 429 is raised rather than held for most of an hour.
MAX_RETRY_WAIT = 60.0

IDEMPOTENCY_KEY = "Idempotency-Key"
PROBLEM_MEDIA_TYPE = "application/problem+json"
# The name the API files an error under when it names no request field.
GENERAL_ERRORS_FIELD = "generalErrors"

# Seams the tests replace, so a retry never really waits and an HTTP date has a fixed now.
_sleep: Callable[[float], None] = time.sleep
_async_sleep: Callable[[float], Awaitable[None]] = asyncio.sleep


def _now() -> datetime:
    return datetime.now(UTC)


def _segment_pattern(template: str) -> Callable[[str], bool]:
    segments = template.strip("/").split("/")

    def matches(path: str) -> bool:
        parts = path.strip("/").split("/")
        # A base URL with a path prefix puts it before the API's own path.
        parts = parts[len(parts) - len(segments) :] if len(parts) >= len(segments) else []
        return bool(parts) and all(
            segment.startswith("{") or segment == part for segment, part in zip(segments, parts, strict=True)
        )

    return matches


_CREATES = tuple(_segment_pattern(template) for template in IDEMPOTENT_CREATES)


class CostfluentError(Exception):
    """An error status from the API, raised by every call once its retries are spent.

    ``problem`` is the API's problem details when the response carried them; a response without
    them (a proxy's plain 404 or 502) leaves it ``None`` and ``code`` empty.
    """

    def __init__(self, status: int, problem: ApiError | None = None, request_id: str | None = None) -> None:
        self.status = status
        self.problem = problem
        self.request_id = request_id
        super().__init__(self._message())

    @classmethod
    def from_response(cls, response: httpx.Response) -> Self:
        problem = None
        if _is_problem(response):
            try:
                problem = ApiError.from_dict(response.json())
            except (KeyError, TypeError, ValueError):
                problem = None
        return cls(response.status_code, problem, response.headers.get("X-Request-Id"))

    @property
    def code(self) -> str:
        """The problem's snake_case code, such as ``not_found`` or ``idempotency_key_reused``."""
        return self.problem.code if self.problem else ""

    @property
    def detail(self) -> str | None:
        detail = self.problem.detail if self.problem else None
        return detail if isinstance(detail, str) else None

    @property
    def retryable(self) -> bool:
        return self.problem.retryable if self.problem else False

    @property
    def trace_id(self) -> str | None:
        trace_id = self.problem.trace_id if self.problem else None
        return trace_id if isinstance(trace_id, str) else None

    @property
    def field_errors(self) -> list[ApiErrorEntry]:
        errors = self.problem.errors if self.problem else None
        return errors if isinstance(errors, list) else []

    @property
    def is_not_found(self) -> bool:
        """The API found no such object. A proxy's plain 404 says nothing about the object, so it is not one."""
        return self.status == 404 and self.problem is not None

    @property
    def is_rate_limited(self) -> bool:
        return self.status == 429

    @property
    def is_idempotency_key_reused(self) -> bool:
        return self.code == "idempotency_key_reused"

    def _message(self) -> str:
        if self.problem is None:
            return f"Costfluent API answered {self.status}"
        # The detail, then each field error the detail does not already state. A refused command's
        # detail is only "One or more validation errors occurred", so the fields are what says what
        # to change; a single refusal's detail repeats its one entry, and a missing capability's
        # names it in another case.
        detail = self.detail or ""
        parts = [detail] if detail else []
        for entry in self.field_errors:
            if entry.reason and entry.reason.lower() not in detail.lower():
                named = entry.name and entry.name != GENERAL_ERRORS_FIELD
                parts.append(f"{entry.name}: {entry.reason}" if named else entry.reason)
        text = "; ".join(parts) or self.problem.title
        return f"Costfluent API answered {self.status} {self.problem.code}: {text}"


def _is_problem(response: httpx.Response) -> bool:
    return response.headers.get("Content-Type", "").split(";")[0].strip().lower() == PROBLEM_MEDIA_TYPE


def _retryable(request: httpx.Request) -> bool:
    """Whether a request is safe to resend after a lost response or a 5xx. A POST triggers, so
    resending one the server may have run could run it twice unless it carries an Idempotency-Key,
    and a request with If-Match the server applied would be refused by its own now stale precondition."""
    if "If-Match" in request.headers:
        return False
    if request.method in ("GET", "HEAD", "PUT", "DELETE"):
        return True
    return request.method == "POST" and IDEMPOTENCY_KEY in request.headers


def _should_retry(request: httpx.Request, response: httpx.Response) -> bool:
    """A 429 is retried for every method: the rate limiter refuses a request before any endpoint runs
    it. A 404 without problem details is the proxy's, not the API's, and is retried as a 5xx is."""
    edge_not_found = response.status_code == 404 and not _is_problem(response)
    return response.status_code == 429 or ((response.status_code >= 500 or edge_not_found) and _retryable(request))


def _retry_after(headers: httpx.Headers, now: datetime) -> float | None:
    """Retry-After in seconds or as an HTTP date, or else the RateLimit-Reset seconds the API sends
    beside it on a 429."""
    value = headers.get("Retry-After") or headers.get("RateLimit-Reset")
    if not value:
        return None
    try:
        return max(float(int(value)), 0.0)
    except ValueError:
        pass
    try:
        at = email.utils.parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return None
    if at.tzinfo is None:
        at = at.replace(tzinfo=UTC)
    return max((at - now).total_seconds(), 0.0)


def _delay(attempt: int, response: httpx.Response | None) -> float:
    if response is not None and (after := _retry_after(response.headers, _now())) is not None:
        return after
    delay = min(BASE_DELAY * 2**attempt, MAX_DELAY)
    return delay + random.uniform(0, delay / 4)


class _RetryTransport(httpx.BaseTransport):
    def __init__(self, inner: httpx.BaseTransport, max_retries: int) -> None:
        self._inner = inner
        self._max_retries = max_retries

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        for attempt in itertools.count():
            last = attempt >= self._max_retries
            response: httpx.Response | None
            try:
                response = self._inner.handle_request(request)
            except httpx.TimeoutException:
                # The timeout bounds the call, not each try: three more would quadruple it.
                raise
            except httpx.TransportError:
                if last or not _retryable(request):
                    raise
                response = None
            else:
                if last or not _should_retry(request, response):
                    return response
            delay = _delay(attempt, response)
            if response is not None:
                if delay > MAX_RETRY_WAIT:
                    return response
                response.close()
            _sleep(delay)
        raise AssertionError("unreachable")

    def close(self) -> None:
        self._inner.close()


class _AsyncRetryTransport(httpx.AsyncBaseTransport):
    def __init__(self, inner: httpx.AsyncBaseTransport, max_retries: int) -> None:
        self._inner = inner
        self._max_retries = max_retries

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        for attempt in itertools.count():
            last = attempt >= self._max_retries
            response: httpx.Response | None
            try:
                response = await self._inner.handle_async_request(request)
            except httpx.TimeoutException:
                # The timeout bounds the call, not each try: three more would quadruple it.
                raise
            except httpx.TransportError:
                if last or not _retryable(request):
                    raise
                response = None
            else:
                if last or not _should_retry(request, response):
                    return response
            delay = _delay(attempt, response)
            if response is not None:
                if delay > MAX_RETRY_WAIT:
                    return response
                await response.aclose()
            await _async_sleep(delay)
        raise AssertionError("unreachable")

    async def aclose(self) -> None:
        await self._inner.aclose()


def _add_idempotency_key(request: httpx.Request) -> None:
    """Every create gets a fresh key unless the caller gave one, so a retry is answered with the
    first response instead of creating twice."""
    if (
        request.method == "POST"
        and IDEMPOTENCY_KEY not in request.headers
        and any(matches(request.url.path) for matches in _CREATES)
    ):
        request.headers[IDEMPOTENCY_KEY] = str(uuid.uuid4())


def _raise_for_status(response: httpx.Response) -> None:
    if response.status_code >= 400:
        response.read()
        raise CostfluentError.from_response(response)


async def _async_add_idempotency_key(request: httpx.Request) -> None:
    _add_idempotency_key(request)


async def _async_raise_for_status(response: httpx.Response) -> None:
    if response.status_code >= 400:
        await response.aread()
        raise CostfluentError.from_response(response)


def create_client(
    token: str,
    *,
    base_url: str = DEFAULT_BASE_URL,
    timeout: float = DEFAULT_TIMEOUT,
    max_retries: int = MAX_RETRIES,
    transport: httpx.BaseTransport | None = None,
    async_transport: httpx.AsyncBaseTransport | None = None,
) -> AuthenticatedClient:
    """A client for every generated operation, sync and async, sending ``token`` as a bearer token.

    Calls retry as described in the README, give each create an Idempotency-Key, and raise
    ``CostfluentError`` for any error status. ``transport`` and ``async_transport`` replace httpx's
    own, as ``httpx.MockTransport`` does in a test.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
    }
    client = AuthenticatedClient(base_url=base_url, token=token, raise_on_unexpected_status=True)
    client.set_httpx_client(
        httpx.Client(
            base_url=base_url,
            headers=headers,
            timeout=timeout,
            transport=_RetryTransport(transport or httpx.HTTPTransport(), max_retries),
            event_hooks={"request": [_add_idempotency_key], "response": [_raise_for_status]},
        )
    )
    client.set_async_httpx_client(
        httpx.AsyncClient(
            base_url=base_url,
            headers=headers,
            timeout=timeout,
            transport=_AsyncRetryTransport(async_transport or httpx.AsyncHTTPTransport(), max_retries),
            event_hooks={"request": [_async_add_idempotency_key], "response": [_async_raise_for_status]},
        )
    )
    return client


T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)


class _Links(Protocol):
    @property
    def next_(self) -> str | None | Unset: ...


class _Page(Protocol[T_co]):
    @property
    def links(self) -> _Links: ...

    @property
    def data(self) -> Sequence[T_co]: ...

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self: ...


def _as_page(result: object) -> _Page[Any]:
    if not (hasattr(result, "links") and hasattr(result, "data")):
        raise TypeError(f"expected a page with links and data, got {type(result).__name__}")
    return result  # type: ignore[return-value]


def _next_url(page: _Page[Any], base_url: httpx.URL) -> httpx.URL | None:
    """The next page on the client's own origin: the token goes only where the client was pointed,
    whatever host the link names."""
    link = page.links.next_
    if not isinstance(link, str) or not link:
        return None
    return base_url.copy_with(raw_path=httpx.URL(link).raw_path)


def paginate(
    operation: Callable[..., _Page[T] | ApiError | None], /, *, client: AuthenticatedClient, **kwargs: Any
) -> Iterator[T]:
    """Every item of a list, following ``links.next`` page by page.

    ``operation`` is a generated ``sync`` function, called once with ``client`` and ``kwargs``:
    ``paginate(list_workspaces.sync, client=client, limit=100)``.
    """
    page = _as_page(operation(client=client, **kwargs))
    httpx_client = client.get_httpx_client()
    while True:
        yield from page.data
        url = _next_url(page, httpx_client.base_url)
        if url is None:
            return
        page = type(page).from_dict(httpx_client.get(url).json())


async def apaginate(
    operation: Callable[..., Awaitable[_Page[T] | ApiError | None]], /, *, client: AuthenticatedClient, **kwargs: Any
) -> AsyncIterator[T]:
    """``paginate`` for a generated ``asyncio`` function."""
    page = _as_page(await operation(client=client, **kwargs))
    httpx_client = client.get_async_httpx_client()
    while True:
        for item in page.data:
            yield item
        url = _next_url(page, httpx_client.base_url)
        if url is None:
            return
        page = type(page).from_dict((await httpx_client.get(url)).json())
