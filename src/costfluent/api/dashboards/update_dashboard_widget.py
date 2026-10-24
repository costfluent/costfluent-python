from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.update_dashboard_widget_request import UpdateDashboardWidgetRequest
from ...models.widget_response import WidgetResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dashboard_id: str,
    widget_id: str,
    *,
    body: UpdateDashboardWidgetRequest,
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
        "url": "/v1/dashboards/{dashboard_id}/widgets/{widget_id}".format(
            dashboard_id=quote(str(dashboard_id), safe=""),
            widget_id=quote(str(widget_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | WidgetResponse | None:
    if response.status_code == 200:
        response_200 = WidgetResponse.from_dict(response.json())

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
) -> Response[ApiError | WidgetResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dashboard_id: str,
    widget_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateDashboardWidgetRequest,
    workspace_id: str,
    if_match: str | Unset = UNSET,
) -> Response[ApiError | WidgetResponse]:
    """Update dashboard widget

     Changes the fields given. A report widget's display and a text widget's words are its own; the type
    and the report stay, so a different report is a new widget. An update that another request's change
    or delete of the widget overtook answers 409 concurrency_conflict and changes nothing.

    Needs a token with `updateDashboard` on the workspace.

    Args:
        dashboard_id (str):
        widget_id (str):
        workspace_id (str):
        if_match (str | Unset):
        body (UpdateDashboardWidgetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | WidgetResponse]
    """

    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
        widget_id=widget_id,
        body=body,
        workspace_id=workspace_id,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dashboard_id: str,
    widget_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateDashboardWidgetRequest,
    workspace_id: str,
    if_match: str | Unset = UNSET,
) -> ApiError | WidgetResponse | None:
    """Update dashboard widget

     Changes the fields given. A report widget's display and a text widget's words are its own; the type
    and the report stay, so a different report is a new widget. An update that another request's change
    or delete of the widget overtook answers 409 concurrency_conflict and changes nothing.

    Needs a token with `updateDashboard` on the workspace.

    Args:
        dashboard_id (str):
        widget_id (str):
        workspace_id (str):
        if_match (str | Unset):
        body (UpdateDashboardWidgetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | WidgetResponse
    """

    return sync_detailed(
        dashboard_id=dashboard_id,
        widget_id=widget_id,
        client=client,
        body=body,
        workspace_id=workspace_id,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    dashboard_id: str,
    widget_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateDashboardWidgetRequest,
    workspace_id: str,
    if_match: str | Unset = UNSET,
) -> Response[ApiError | WidgetResponse]:
    """Update dashboard widget

     Changes the fields given. A report widget's display and a text widget's words are its own; the type
    and the report stay, so a different report is a new widget. An update that another request's change
    or delete of the widget overtook answers 409 concurrency_conflict and changes nothing.

    Needs a token with `updateDashboard` on the workspace.

    Args:
        dashboard_id (str):
        widget_id (str):
        workspace_id (str):
        if_match (str | Unset):
        body (UpdateDashboardWidgetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | WidgetResponse]
    """

    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
        widget_id=widget_id,
        body=body,
        workspace_id=workspace_id,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dashboard_id: str,
    widget_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateDashboardWidgetRequest,
    workspace_id: str,
    if_match: str | Unset = UNSET,
) -> ApiError | WidgetResponse | None:
    """Update dashboard widget

     Changes the fields given. A report widget's display and a text widget's words are its own; the type
    and the report stay, so a different report is a new widget. An update that another request's change
    or delete of the widget overtook answers 409 concurrency_conflict and changes nothing.

    Needs a token with `updateDashboard` on the workspace.

    Args:
        dashboard_id (str):
        widget_id (str):
        workspace_id (str):
        if_match (str | Unset):
        body (UpdateDashboardWidgetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | WidgetResponse
    """

    return (
        await asyncio_detailed(
            dashboard_id=dashboard_id,
            widget_id=widget_id,
            client=client,
            body=body,
            workspace_id=workspace_id,
            if_match=if_match,
        )
    ).parsed
