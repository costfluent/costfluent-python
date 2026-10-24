from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.update_virtual_tag_route_request import UpdateVirtualTagRouteRequest
from ...models.virtual_tag_response import VirtualTagResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    virtual_tag_id: str,
    *,
    body: UpdateVirtualTagRouteRequest,
    if_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/virtual-tags/{virtual_tag_id}".format(
            virtual_tag_id=quote(str(virtual_tag_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | VirtualTagResponse | None:
    if response.status_code == 200:
        response_200 = VirtualTagResponse.from_dict(response.json())

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
) -> Response[ApiError | VirtualTagResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    virtual_tag_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateVirtualTagRouteRequest,
    if_match: str | Unset = UNSET,
) -> Response[ApiError | VirtualTagResponse]:
    """Update virtual tag

     Updates a virtual tag and returns it as stored.

    Needs a token with `manageTags` on the workspace.

    Args:
        virtual_tag_id (str):
        if_match (str | Unset):
        body (UpdateVirtualTagRouteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | VirtualTagResponse]
    """

    kwargs = _get_kwargs(
        virtual_tag_id=virtual_tag_id,
        body=body,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    virtual_tag_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateVirtualTagRouteRequest,
    if_match: str | Unset = UNSET,
) -> ApiError | VirtualTagResponse | None:
    """Update virtual tag

     Updates a virtual tag and returns it as stored.

    Needs a token with `manageTags` on the workspace.

    Args:
        virtual_tag_id (str):
        if_match (str | Unset):
        body (UpdateVirtualTagRouteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | VirtualTagResponse
    """

    return sync_detailed(
        virtual_tag_id=virtual_tag_id,
        client=client,
        body=body,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    virtual_tag_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateVirtualTagRouteRequest,
    if_match: str | Unset = UNSET,
) -> Response[ApiError | VirtualTagResponse]:
    """Update virtual tag

     Updates a virtual tag and returns it as stored.

    Needs a token with `manageTags` on the workspace.

    Args:
        virtual_tag_id (str):
        if_match (str | Unset):
        body (UpdateVirtualTagRouteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | VirtualTagResponse]
    """

    kwargs = _get_kwargs(
        virtual_tag_id=virtual_tag_id,
        body=body,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    virtual_tag_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateVirtualTagRouteRequest,
    if_match: str | Unset = UNSET,
) -> ApiError | VirtualTagResponse | None:
    """Update virtual tag

     Updates a virtual tag and returns it as stored.

    Needs a token with `manageTags` on the workspace.

    Args:
        virtual_tag_id (str):
        if_match (str | Unset):
        body (UpdateVirtualTagRouteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | VirtualTagResponse
    """

    return (
        await asyncio_detailed(
            virtual_tag_id=virtual_tag_id,
            client=client,
            body=body,
            if_match=if_match,
        )
    ).parsed
