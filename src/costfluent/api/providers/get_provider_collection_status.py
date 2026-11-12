from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.collection_status_response import CollectionStatusResponse
from ...types import Response


def _get_kwargs(
    provider_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/providers/{provider_id}/collection-status".format(
            provider_id=quote(str(provider_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | CollectionStatusResponse | None:
    if response.status_code == 200:
        response_200 = CollectionStatusResponse.from_dict(response.json())

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
) -> Response[ApiError | CollectionStatusResponse]:
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
) -> Response[ApiError | CollectionStatusResponse]:
    """Get provider collection status

     Returns one cost source's status with its months, newest first, back to the plan's history horizon:
    each month's rows, billed amount per currency, the latest restatement and the comparison with the
    provider's own total, and the days (or months) no committed collection covered. Missing means
    nothing was collected, not that the provider had no cost. Amounts are null, with
    amountsWithheldReason set, unless the token manages providers or reads the whole connection's cost;
    a source without a provider total says so in providerTotal.status rather than showing 0.

    Needs an organization token with `viewProviders`.

    Args:
        provider_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | CollectionStatusResponse]
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
) -> ApiError | CollectionStatusResponse | None:
    """Get provider collection status

     Returns one cost source's status with its months, newest first, back to the plan's history horizon:
    each month's rows, billed amount per currency, the latest restatement and the comparison with the
    provider's own total, and the days (or months) no committed collection covered. Missing means
    nothing was collected, not that the provider had no cost. Amounts are null, with
    amountsWithheldReason set, unless the token manages providers or reads the whole connection's cost;
    a source without a provider total says so in providerTotal.status rather than showing 0.

    Needs an organization token with `viewProviders`.

    Args:
        provider_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | CollectionStatusResponse
    """

    return sync_detailed(
        provider_id=provider_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    provider_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | CollectionStatusResponse]:
    """Get provider collection status

     Returns one cost source's status with its months, newest first, back to the plan's history horizon:
    each month's rows, billed amount per currency, the latest restatement and the comparison with the
    provider's own total, and the days (or months) no committed collection covered. Missing means
    nothing was collected, not that the provider had no cost. Amounts are null, with
    amountsWithheldReason set, unless the token manages providers or reads the whole connection's cost;
    a source without a provider total says so in providerTotal.status rather than showing 0.

    Needs an organization token with `viewProviders`.

    Args:
        provider_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | CollectionStatusResponse]
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
) -> ApiError | CollectionStatusResponse | None:
    """Get provider collection status

     Returns one cost source's status with its months, newest first, back to the plan's history horizon:
    each month's rows, billed amount per currency, the latest restatement and the comparison with the
    provider's own total, and the days (or months) no committed collection covered. Missing means
    nothing was collected, not that the provider had no cost. Amounts are null, with
    amountsWithheldReason set, unless the token manages providers or reads the whole connection's cost;
    a source without a provider total says so in providerTotal.status rather than showing 0.

    Needs an organization token with `viewProviders`.

    Args:
        provider_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | CollectionStatusResponse
    """

    return (
        await asyncio_detailed(
            provider_id=provider_id,
            client=client,
        )
    ).parsed
