"""A scripted stand-in for the API: each request gets the next response, and every request is kept."""

from __future__ import annotations

import json
from collections.abc import Callable
from typing import Any

import httpx

from costfluent import create_client
from costfluent.client import AuthenticatedClient

BASE_URL = "https://api.costfluent.test"
TOKEN = "cf_test_token"

Reply = httpx.Response | Callable[[httpx.Request], httpx.Response] | Exception


def json_response(status: int, body: Any, headers: dict[str, str] | None = None) -> httpx.Response:
    return httpx.Response(
        status, content=json.dumps(body).encode(), headers={"Content-Type": "application/json", **(headers or {})}
    )


def problem(status: int, code: str, headers: dict[str, str] | None = None, **fields: Any) -> httpx.Response:
    body = {"type": "about:blank", "title": "Problem", "status": status, "code": code, "retryable": False, **fields}
    return httpx.Response(
        status,
        content=json.dumps(body).encode(),
        headers={"Content-Type": "application/problem+json; charset=utf-8", "X-Request-Id": "req_1", **(headers or {})},
    )


def folders_page(ids: list[str], next_link: str | None) -> httpx.Response:
    return json_response(
        200,
        {
            "links": {"self": f"{BASE_URL}/v1/folders", "next": next_link},
            "data": [{"id": folder_id, "title": folder_id, "reportCount": 0} for folder_id in ids],
        },
    )


class FakeApi:
    def __init__(self, *replies: Reply) -> None:
        self.replies = list(replies)
        self.requests: list[httpx.Request] = []

    def handle(self, request: httpx.Request) -> httpx.Response:
        request.read()
        self.requests.append(request)
        reply = self.replies.pop(0)
        if isinstance(reply, Exception):
            raise reply
        if callable(reply):
            return reply(request)
        # A copy, so one scripted response can answer several requests and several tests.
        return httpx.Response(reply.status_code, headers=reply.headers, content=reply.content)

    def client(self, base_url: str = BASE_URL, max_retries: int | None = None) -> AuthenticatedClient:
        transport = httpx.MockTransport(self.handle)
        return create_client(
            TOKEN,
            base_url=base_url,
            transport=transport,
            async_transport=transport,
            **({} if max_retries is None else {"max_retries": max_retries}),
        )
