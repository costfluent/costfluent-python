from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    virtual_tag_id: str,
    *,
    workspace_id: str,
    if_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    params: dict[str, Any] = {}

    params["workspaceId"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/virtual-tags/{virtual_tag_id}".format(
            virtual_tag_id=quote(str(virtual_tag_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiError | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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

    if response.status_code == 409:
        response_409 = ApiError.from_dict(response.json())

        return response_409

    if response.status_code == 412:
        response_412 = ApiError.from_dict(response.json())

        return response_412

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
) -> Response[Any | ApiError]:
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
    workspace_id: str,
    if_match: str | Unset = UNSET,
) -> Response[Any | ApiError]:
    """Delete virtual tag

     Deletes a virtual tag. Refused with 409 in_use, naming them, while cost reports, cost alerts or
    saved filters filter or group by it.

    Needs a token with `manageTags` on the workspace.

    Args:
        virtual_tag_id (str):
        workspace_id (str):
        if_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiError]
    """

    kwargs = _get_kwargs(
        virtual_tag_id=virtual_tag_id,
        workspace_id=workspace_id,
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
    workspace_id: str,
    if_match: str | Unset = UNSET,
) -> Any | ApiError | None:
    """Delete virtual tag

     Deletes a virtual tag. Refused with 409 in_use, naming them, while cost reports, cost alerts or
    saved filters filter or group by it.

    Needs a token with `manageTags` on the workspace.

    Args:
        virtual_tag_id (str):
        workspace_id (str):
        if_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiError
    """

    return sync_detailed(
        virtual_tag_id=virtual_tag_id,
        client=client,
        workspace_id=workspace_id,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    virtual_tag_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: str,
    if_match: str | Unset = UNSET,
) -> Response[Any | ApiError]:
    """Delete virtual tag

     Deletes a virtual tag. Refused with 409 in_use, naming them, while cost reports, cost alerts or
    saved filters filter or group by it.

    Needs a token with `manageTags` on the workspace.

    Args:
        virtual_tag_id (str):
        workspace_id (str):
        if_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiError]
    """

    kwargs = _get_kwargs(
        virtual_tag_id=virtual_tag_id,
        workspace_id=workspace_id,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    virtual_tag_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: str,
    if_match: str | Unset = UNSET,
) -> Any | ApiError | None:
    """Delete virtual tag

     Deletes a virtual tag. Refused with 409 in_use, naming them, while cost reports, cost alerts or
    saved filters filter or group by it.

    Needs a token with `manageTags` on the workspace.

    Args:
        virtual_tag_id (str):
        workspace_id (str):
        if_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiError
    """

    return (
        await asyncio_detailed(
            virtual_tag_id=virtual_tag_id,
            client=client,
            workspace_id=workspace_id,
            if_match=if_match,
        )
    ).parsed
