from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.saved_filter_response import SavedFilterResponse
from ...models.update_saved_filter_request import UpdateSavedFilterRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    filter_id: str,
    *,
    body: UpdateSavedFilterRequest,
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
        "method": "put",
        "url": "/v1/saved-filters/{filter_id}".format(
            filter_id=quote(str(filter_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | SavedFilterResponse | None:
    if response.status_code == 200:
        response_200 = SavedFilterResponse.from_dict(response.json())

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
) -> Response[ApiError | SavedFilterResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    filter_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateSavedFilterRequest,
    workspace_id: str,
    if_match: str | Unset = UNSET,
) -> Response[ApiError | SavedFilterResponse]:
    """Update saved filter

     Updates a saved filter.

    Needs a token with `updateSavedFilter` on the workspace.

    Args:
        filter_id (str):
        workspace_id (str):
        if_match (str | Unset):
        body (UpdateSavedFilterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | SavedFilterResponse]
    """

    kwargs = _get_kwargs(
        filter_id=filter_id,
        body=body,
        workspace_id=workspace_id,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    filter_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateSavedFilterRequest,
    workspace_id: str,
    if_match: str | Unset = UNSET,
) -> ApiError | SavedFilterResponse | None:
    """Update saved filter

     Updates a saved filter.

    Needs a token with `updateSavedFilter` on the workspace.

    Args:
        filter_id (str):
        workspace_id (str):
        if_match (str | Unset):
        body (UpdateSavedFilterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | SavedFilterResponse
    """

    return sync_detailed(
        filter_id=filter_id,
        client=client,
        body=body,
        workspace_id=workspace_id,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    filter_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateSavedFilterRequest,
    workspace_id: str,
    if_match: str | Unset = UNSET,
) -> Response[ApiError | SavedFilterResponse]:
    """Update saved filter

     Updates a saved filter.

    Needs a token with `updateSavedFilter` on the workspace.

    Args:
        filter_id (str):
        workspace_id (str):
        if_match (str | Unset):
        body (UpdateSavedFilterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | SavedFilterResponse]
    """

    kwargs = _get_kwargs(
        filter_id=filter_id,
        body=body,
        workspace_id=workspace_id,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    filter_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateSavedFilterRequest,
    workspace_id: str,
    if_match: str | Unset = UNSET,
) -> ApiError | SavedFilterResponse | None:
    """Update saved filter

     Updates a saved filter.

    Needs a token with `updateSavedFilter` on the workspace.

    Args:
        filter_id (str):
        workspace_id (str):
        if_match (str | Unset):
        body (UpdateSavedFilterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | SavedFilterResponse
    """

    return (
        await asyncio_detailed(
            filter_id=filter_id,
            client=client,
            body=body,
            workspace_id=workspace_id,
            if_match=if_match,
        )
    ).parsed
