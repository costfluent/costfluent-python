from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.submit_costs_request import SubmitCostsRequest
from ...models.submit_costs_response import SubmitCostsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    provider_id: str,
    *,
    body: SubmitCostsRequest,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/custom-providers/{provider_id}/costs".format(
            provider_id=quote(str(provider_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | SubmitCostsResponse | None:
    if response.status_code == 200:
        response_200 = SubmitCostsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ApiError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ApiError.from_dict(response.json())

        return response_404

    if response.status_code == 408:
        response_408 = ApiError.from_dict(response.json())

        return response_408

    if response.status_code == 409:
        response_409 = ApiError.from_dict(response.json())

        return response_409

    if response.status_code == 413:
        response_413 = ApiError.from_dict(response.json())

        return response_413

    if response.status_code == 422:
        response_422 = ApiError.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ApiError.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ApiError.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ApiError.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | SubmitCostsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    provider_id: str,
    *,
    client: AuthenticatedClient,
    body: SubmitCostsRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[ApiError | SubmitCostsResponse]:
    """Submit costs batch

     Submits a batch of cost records to a custom provider. A batch that another submission or upload for
    the same provider overtook while it ran answers 409 concurrency_conflict and commits nothing; send
    it again. Submitted costs count toward the organization's monthly volume, one row for each day a
    cost is spread over, and the batch is checked whole: one that would pass a monthly volume limit set
    for the organization commits nothing. Each entry becomes one daily record per day of its charge
    period; a request may become at most 37,500 records and, counting a spread entry once per day, 48
    MiB of entries, and is refused with 400 otherwise.

    Needs an organization token with `syncProviders` for every request, and `manageProviders` as well
    when it replaces lines (replaceLines: true), which removes their earlier days.

    Args:
        provider_id (str):
        idempotency_key (str | Unset):
        body (SubmitCostsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | SubmitCostsResponse]
    """

    kwargs = _get_kwargs(
        provider_id=provider_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider_id: str,
    *,
    client: AuthenticatedClient,
    body: SubmitCostsRequest,
    idempotency_key: str | Unset = UNSET,
) -> ApiError | SubmitCostsResponse | None:
    """Submit costs batch

     Submits a batch of cost records to a custom provider. A batch that another submission or upload for
    the same provider overtook while it ran answers 409 concurrency_conflict and commits nothing; send
    it again. Submitted costs count toward the organization's monthly volume, one row for each day a
    cost is spread over, and the batch is checked whole: one that would pass a monthly volume limit set
    for the organization commits nothing. Each entry becomes one daily record per day of its charge
    period; a request may become at most 37,500 records and, counting a spread entry once per day, 48
    MiB of entries, and is refused with 400 otherwise.

    Needs an organization token with `syncProviders` for every request, and `manageProviders` as well
    when it replaces lines (replaceLines: true), which removes their earlier days.

    Args:
        provider_id (str):
        idempotency_key (str | Unset):
        body (SubmitCostsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | SubmitCostsResponse
    """

    return sync_detailed(
        provider_id=provider_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    provider_id: str,
    *,
    client: AuthenticatedClient,
    body: SubmitCostsRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[ApiError | SubmitCostsResponse]:
    """Submit costs batch

     Submits a batch of cost records to a custom provider. A batch that another submission or upload for
    the same provider overtook while it ran answers 409 concurrency_conflict and commits nothing; send
    it again. Submitted costs count toward the organization's monthly volume, one row for each day a
    cost is spread over, and the batch is checked whole: one that would pass a monthly volume limit set
    for the organization commits nothing. Each entry becomes one daily record per day of its charge
    period; a request may become at most 37,500 records and, counting a spread entry once per day, 48
    MiB of entries, and is refused with 400 otherwise.

    Needs an organization token with `syncProviders` for every request, and `manageProviders` as well
    when it replaces lines (replaceLines: true), which removes their earlier days.

    Args:
        provider_id (str):
        idempotency_key (str | Unset):
        body (SubmitCostsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | SubmitCostsResponse]
    """

    kwargs = _get_kwargs(
        provider_id=provider_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider_id: str,
    *,
    client: AuthenticatedClient,
    body: SubmitCostsRequest,
    idempotency_key: str | Unset = UNSET,
) -> ApiError | SubmitCostsResponse | None:
    """Submit costs batch

     Submits a batch of cost records to a custom provider. A batch that another submission or upload for
    the same provider overtook while it ran answers 409 concurrency_conflict and commits nothing; send
    it again. Submitted costs count toward the organization's monthly volume, one row for each day a
    cost is spread over, and the batch is checked whole: one that would pass a monthly volume limit set
    for the organization commits nothing. Each entry becomes one daily record per day of its charge
    period; a request may become at most 37,500 records and, counting a spread entry once per day, 48
    MiB of entries, and is refused with 400 otherwise.

    Needs an organization token with `syncProviders` for every request, and `manageProviders` as well
    when it replaces lines (replaceLines: true), which removes their earlier days.

    Args:
        provider_id (str):
        idempotency_key (str | Unset):
        body (SubmitCostsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | SubmitCostsResponse
    """

    return (
        await asyncio_detailed(
            provider_id=provider_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
