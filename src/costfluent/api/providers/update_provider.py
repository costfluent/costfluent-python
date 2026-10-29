from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.provider_response import ProviderResponse
from ...models.update_provider_request import UpdateProviderRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    provider_id: str,
    *,
    body: UpdateProviderRequest,
    if_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/providers/{provider_id}".format(
            provider_id=quote(str(provider_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | ProviderResponse | None:
    if response.status_code == 200:
        response_200 = ProviderResponse.from_dict(response.json())

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

    if response.status_code == 412:
        response_412 = ApiError.from_dict(response.json())

        return response_412

    if response.status_code == 413:
        response_413 = ApiError.from_dict(response.json())

        return response_413

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
) -> Response[ApiError | ProviderResponse]:
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
    body: UpdateProviderRequest,
    if_match: str | Unset = UNSET,
) -> Response[ApiError | ProviderResponse]:
    """Update provider

     Updates a provider in place: its display name, description, settings, credentials or sync frequency.
    A field left out keeps its value; clearDescription and clearSettings remove theirs. An update that
    another write to the provider overtook, or whose credentials or settings changed while the new
    credentials or export location were verified, answers 409 concurrency_conflict and changes nothing.

    Needs an organization token with `manageProviders`.

    Args:
        provider_id (str):
        if_match (str | Unset):
        body (UpdateProviderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | ProviderResponse]
    """

    kwargs = _get_kwargs(
        provider_id=provider_id,
        body=body,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateProviderRequest,
    if_match: str | Unset = UNSET,
) -> ApiError | ProviderResponse | None:
    """Update provider

     Updates a provider in place: its display name, description, settings, credentials or sync frequency.
    A field left out keeps its value; clearDescription and clearSettings remove theirs. An update that
    another write to the provider overtook, or whose credentials or settings changed while the new
    credentials or export location were verified, answers 409 concurrency_conflict and changes nothing.

    Needs an organization token with `manageProviders`.

    Args:
        provider_id (str):
        if_match (str | Unset):
        body (UpdateProviderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | ProviderResponse
    """

    return sync_detailed(
        provider_id=provider_id,
        client=client,
        body=body,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    provider_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateProviderRequest,
    if_match: str | Unset = UNSET,
) -> Response[ApiError | ProviderResponse]:
    """Update provider

     Updates a provider in place: its display name, description, settings, credentials or sync frequency.
    A field left out keeps its value; clearDescription and clearSettings remove theirs. An update that
    another write to the provider overtook, or whose credentials or settings changed while the new
    credentials or export location were verified, answers 409 concurrency_conflict and changes nothing.

    Needs an organization token with `manageProviders`.

    Args:
        provider_id (str):
        if_match (str | Unset):
        body (UpdateProviderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | ProviderResponse]
    """

    kwargs = _get_kwargs(
        provider_id=provider_id,
        body=body,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateProviderRequest,
    if_match: str | Unset = UNSET,
) -> ApiError | ProviderResponse | None:
    """Update provider

     Updates a provider in place: its display name, description, settings, credentials or sync frequency.
    A field left out keeps its value; clearDescription and clearSettings remove theirs. An update that
    another write to the provider overtook, or whose credentials or settings changed while the new
    credentials or export location were verified, answers 409 concurrency_conflict and changes nothing.

    Needs an organization token with `manageProviders`.

    Args:
        provider_id (str):
        if_match (str | Unset):
        body (UpdateProviderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | ProviderResponse
    """

    return (
        await asyncio_detailed(
            provider_id=provider_id,
            client=client,
            body=body,
            if_match=if_match,
        )
    ).parsed
