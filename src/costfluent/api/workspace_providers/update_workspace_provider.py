from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.update_workspace_provider_request import UpdateWorkspaceProviderRequest
from ...models.workspace_provider_response import WorkspaceProviderResponse
from ...types import Response


def _get_kwargs(
    workspace_provider_id: str,
    *,
    body: UpdateWorkspaceProviderRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/workspace-providers/{workspace_provider_id}".format(
            workspace_provider_id=quote(str(workspace_provider_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | WorkspaceProviderResponse | None:
    if response.status_code == 200:
        response_200 = WorkspaceProviderResponse.from_dict(response.json())

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
) -> Response[ApiError | WorkspaceProviderResponse]:
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
    body: UpdateWorkspaceProviderRequest,
) -> Response[ApiError | WorkspaceProviderResponse]:
    """Update workspace provider

     Turns a connection on or off in a workspace, or replaces the accounts it reads. Which accounts a
    workspace reads is the organization's to decide, so a workspace token can only turn the link on or
    off.

    Needs a token with `addWorkspaceProvider` on the workspace unless the request only turns the link
    off, and `removeWorkspaceProvider` to turn it off. It also needs an organization token with
    `manageProviders` to send `accountIds`.

    Args:
        workspace_provider_id (str):
        body (UpdateWorkspaceProviderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | WorkspaceProviderResponse]
    """

    kwargs = _get_kwargs(
        workspace_provider_id=workspace_provider_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_provider_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateWorkspaceProviderRequest,
) -> ApiError | WorkspaceProviderResponse | None:
    """Update workspace provider

     Turns a connection on or off in a workspace, or replaces the accounts it reads. Which accounts a
    workspace reads is the organization's to decide, so a workspace token can only turn the link on or
    off.

    Needs a token with `addWorkspaceProvider` on the workspace unless the request only turns the link
    off, and `removeWorkspaceProvider` to turn it off. It also needs an organization token with
    `manageProviders` to send `accountIds`.

    Args:
        workspace_provider_id (str):
        body (UpdateWorkspaceProviderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | WorkspaceProviderResponse
    """

    return sync_detailed(
        workspace_provider_id=workspace_provider_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace_provider_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateWorkspaceProviderRequest,
) -> Response[ApiError | WorkspaceProviderResponse]:
    """Update workspace provider

     Turns a connection on or off in a workspace, or replaces the accounts it reads. Which accounts a
    workspace reads is the organization's to decide, so a workspace token can only turn the link on or
    off.

    Needs a token with `addWorkspaceProvider` on the workspace unless the request only turns the link
    off, and `removeWorkspaceProvider` to turn it off. It also needs an organization token with
    `manageProviders` to send `accountIds`.

    Args:
        workspace_provider_id (str):
        body (UpdateWorkspaceProviderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | WorkspaceProviderResponse]
    """

    kwargs = _get_kwargs(
        workspace_provider_id=workspace_provider_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_provider_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateWorkspaceProviderRequest,
) -> ApiError | WorkspaceProviderResponse | None:
    """Update workspace provider

     Turns a connection on or off in a workspace, or replaces the accounts it reads. Which accounts a
    workspace reads is the organization's to decide, so a workspace token can only turn the link on or
    off.

    Needs a token with `addWorkspaceProvider` on the workspace unless the request only turns the link
    off, and `removeWorkspaceProvider` to turn it off. It also needs an organization token with
    `manageProviders` to send `accountIds`.

    Args:
        workspace_provider_id (str):
        body (UpdateWorkspaceProviderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | WorkspaceProviderResponse
    """

    return (
        await asyncio_detailed(
            workspace_provider_id=workspace_provider_id,
            client=client,
            body=body,
        )
    ).parsed
