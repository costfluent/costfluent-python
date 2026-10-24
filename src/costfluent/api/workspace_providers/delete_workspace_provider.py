from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...types import UNSET, Response


def _get_kwargs(
    workspace_provider_id: str,
    *,
    workspace_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["workspaceId"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/workspace-providers/{workspace_provider_id}".format(
            workspace_provider_id=quote(str(workspace_provider_id), safe=""),
        ),
        "params": params,
    }

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
    workspace_provider_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: str,
) -> Response[Any | ApiError]:
    """Delete workspace provider

     Stops a workspace reading a connection. The connection and its cost stay; other workspaces that
    enable it are unaffected.

    Needs a token with `removeWorkspaceProvider` on the workspace.

    Args:
        workspace_provider_id (str):
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiError]
    """

    kwargs = _get_kwargs(
        workspace_provider_id=workspace_provider_id,
        workspace_id=workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_provider_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: str,
) -> Any | ApiError | None:
    """Delete workspace provider

     Stops a workspace reading a connection. The connection and its cost stay; other workspaces that
    enable it are unaffected.

    Needs a token with `removeWorkspaceProvider` on the workspace.

    Args:
        workspace_provider_id (str):
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiError
    """

    return sync_detailed(
        workspace_provider_id=workspace_provider_id,
        client=client,
        workspace_id=workspace_id,
    ).parsed


async def asyncio_detailed(
    workspace_provider_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: str,
) -> Response[Any | ApiError]:
    """Delete workspace provider

     Stops a workspace reading a connection. The connection and its cost stay; other workspaces that
    enable it are unaffected.

    Needs a token with `removeWorkspaceProvider` on the workspace.

    Args:
        workspace_provider_id (str):
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiError]
    """

    kwargs = _get_kwargs(
        workspace_provider_id=workspace_provider_id,
        workspace_id=workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_provider_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: str,
) -> Any | ApiError | None:
    """Delete workspace provider

     Stops a workspace reading a connection. The connection and its cost stay; other workspaces that
    enable it are unaffected.

    Needs a token with `removeWorkspaceProvider` on the workspace.

    Args:
        workspace_provider_id (str):
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiError
    """

    return (
        await asyncio_detailed(
            workspace_provider_id=workspace_provider_id,
            client=client,
            workspace_id=workspace_id,
        )
    ).parsed
