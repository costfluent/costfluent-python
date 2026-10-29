from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.set_team_default_dashboard_request import SetTeamDefaultDashboardRequest
from ...models.team_workspace_access_response import TeamWorkspaceAccessResponse
from ...types import Response


def _get_kwargs(
    team_id: str,
    workspace_id: str,
    *,
    body: SetTeamDefaultDashboardRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/teams/{team_id}/workspaces/{workspace_id}/default-dashboard".format(
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
) -> ApiError | TeamWorkspaceAccessResponse | None:
    if response.status_code == 200:
        response_200 = TeamWorkspaceAccessResponse.from_dict(response.json())

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
) -> Response[ApiError | TeamWorkspaceAccessResponse]:
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
    body: SetTeamDefaultDashboardRequest,
) -> Response[ApiError | TeamWorkspaceAccessResponse]:
    """Set team default dashboard

     Sets the dashboard of the workspace that the team's members open after signing in, unless they chose
    their own, or clears it with a null dashboardId. The team needs access to the workspace, and the
    Everyone team has none. Removing the team's access to the workspace ends its default there; changing
    the level keeps it.

    Needs an organization token with `manageWorkspaceAccess` and `viewDashboards`.

    Args:
        team_id (str):
        workspace_id (str):
        body (SetTeamDefaultDashboardRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | TeamWorkspaceAccessResponse]
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
    body: SetTeamDefaultDashboardRequest,
) -> ApiError | TeamWorkspaceAccessResponse | None:
    """Set team default dashboard

     Sets the dashboard of the workspace that the team's members open after signing in, unless they chose
    their own, or clears it with a null dashboardId. The team needs access to the workspace, and the
    Everyone team has none. Removing the team's access to the workspace ends its default there; changing
    the level keeps it.

    Needs an organization token with `manageWorkspaceAccess` and `viewDashboards`.

    Args:
        team_id (str):
        workspace_id (str):
        body (SetTeamDefaultDashboardRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | TeamWorkspaceAccessResponse
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
    body: SetTeamDefaultDashboardRequest,
) -> Response[ApiError | TeamWorkspaceAccessResponse]:
    """Set team default dashboard

     Sets the dashboard of the workspace that the team's members open after signing in, unless they chose
    their own, or clears it with a null dashboardId. The team needs access to the workspace, and the
    Everyone team has none. Removing the team's access to the workspace ends its default there; changing
    the level keeps it.

    Needs an organization token with `manageWorkspaceAccess` and `viewDashboards`.

    Args:
        team_id (str):
        workspace_id (str):
        body (SetTeamDefaultDashboardRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | TeamWorkspaceAccessResponse]
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
    body: SetTeamDefaultDashboardRequest,
) -> ApiError | TeamWorkspaceAccessResponse | None:
    """Set team default dashboard

     Sets the dashboard of the workspace that the team's members open after signing in, unless they chose
    their own, or clears it with a null dashboardId. The team needs access to the workspace, and the
    Everyone team has none. Removing the team's access to the workspace ends its default there; changing
    the level keeps it.

    Needs an organization token with `manageWorkspaceAccess` and `viewDashboards`.

    Args:
        team_id (str):
        workspace_id (str):
        body (SetTeamDefaultDashboardRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | TeamWorkspaceAccessResponse
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            workspace_id=workspace_id,
            client=client,
            body=body,
        )
    ).parsed
