from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.connection_test_response import ConnectionTestResponse
from ...types import Response


def _get_kwargs(
    provider_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/providers/{provider_id}/test".format(
            provider_id=quote(str(provider_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | ConnectionTestResponse | None:
    if response.status_code == 200:
        response_200 = ConnectionTestResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ApiError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ApiError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ApiError.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ApiError.from_dict(response.json())

        return response_409

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
) -> Response[ApiError | ConnectionTestResponse]:
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
) -> Response[ApiError | ConnectionTestResponse]:
    """Test provider connection

     Validates credentials and connectivity to the provider. A test whose provider's credentials or
    settings changed while it ran answers 409 concurrency_conflict and records nothing. A connection is
    tested at most once a minute with the same credentials and settings; a test sooner answers 429
    rate_limit_exceeded with Retry-After and asks the provider nothing.

    Needs an organization token with `manageProviders`.

    Args:
        provider_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | ConnectionTestResponse]
    """

    kwargs = _get_kwargs(
        provider_id=provider_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider_id: str,
    *,
    client: AuthenticatedClient,
) -> ApiError | ConnectionTestResponse | None:
    """Test provider connection

     Validates credentials and connectivity to the provider. A test whose provider's credentials or
    settings changed while it ran answers 409 concurrency_conflict and records nothing. A connection is
    tested at most once a minute with the same credentials and settings; a test sooner answers 429
    rate_limit_exceeded with Retry-After and asks the provider nothing.

    Needs an organization token with `manageProviders`.

    Args:
        provider_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | ConnectionTestResponse
    """

    return sync_detailed(
        provider_id=provider_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    provider_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | ConnectionTestResponse]:
    """Test provider connection

     Validates credentials and connectivity to the provider. A test whose provider's credentials or
    settings changed while it ran answers 409 concurrency_conflict and records nothing. A connection is
    tested at most once a minute with the same credentials and settings; a test sooner answers 429
    rate_limit_exceeded with Retry-After and asks the provider nothing.

    Needs an organization token with `manageProviders`.

    Args:
        provider_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | ConnectionTestResponse]
    """

    kwargs = _get_kwargs(
        provider_id=provider_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider_id: str,
    *,
    client: AuthenticatedClient,
) -> ApiError | ConnectionTestResponse | None:
    """Test provider connection

     Validates credentials and connectivity to the provider. A test whose provider's credentials or
    settings changed while it ran answers 409 concurrency_conflict and records nothing. A connection is
    tested at most once a minute with the same credentials and settings; a test sooner answers 429
    rate_limit_exceeded with Retry-After and asks the provider nothing.

    Needs an organization token with `manageProviders`.

    Args:
        provider_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | ConnectionTestResponse
    """

    return (
        await asyncio_detailed(
            provider_id=provider_id,
            client=client,
        )
    ).parsed
