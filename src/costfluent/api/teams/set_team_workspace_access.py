from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.set_team_workspace_access_request import SetTeamWorkspaceAccessRequest
from ...types import Response


def _get_kwargs(
    team_id: str,
    workspace_id: str,
    *,
    body: SetTeamWorkspaceAccessRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/teams/{team_id}/workspaces/{workspace_id}".format(
            team_id=quote(str(team_id), safe=""),
            workspace_id=quote(str(workspace_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

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
) -> Response[Any | ApiError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    team_id: str,
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    body: SetTeamWorkspaceAccessRequest,
) -> Response[Any | ApiError]:
    """Set team workspace access

     Sets the access level a team's members have on a workspace, replacing any level it had.

    Needs an organization token with `manageWorkspaceAccess`.

    Args:
        team_id (str):
        workspace_id (str):
        body (SetTeamWorkspaceAccessRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiError]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        workspace_id=workspace_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    team_id: str,
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    body: SetTeamWorkspaceAccessRequest,
) -> Any | ApiError | None:
    """Set team workspace access

     Sets the access level a team's members have on a workspace, replacing any level it had.

    Needs an organization token with `manageWorkspaceAccess`.

    Args:
        team_id (str):
        workspace_id (str):
        body (SetTeamWorkspaceAccessRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiError
    """

    return sync_detailed(
        team_id=team_id,
        workspace_id=workspace_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    team_id: str,
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    body: SetTeamWorkspaceAccessRequest,
) -> Response[Any | ApiError]:
    """Set team workspace access

     Sets the access level a team's members have on a workspace, replacing any level it had.

    Needs an organization token with `manageWorkspaceAccess`.

    Args:
        team_id (str):
        workspace_id (str):
        body (SetTeamWorkspaceAccessRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiError]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        workspace_id=workspace_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_id: str,
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    body: SetTeamWorkspaceAccessRequest,
) -> Any | ApiError | None:
    """Set team workspace access

     Sets the access level a team's members have on a workspace, replacing any level it had.

    Needs an organization token with `manageWorkspaceAccess`.

    Args:
        team_id (str):
        workspace_id (str):
        body (SetTeamWorkspaceAccessRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiError
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            workspace_id=workspace_id,
            client=client,
            body=body,
        )
    ).parsed
