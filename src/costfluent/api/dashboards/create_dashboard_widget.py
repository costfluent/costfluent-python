from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.create_dashboard_widget_request import CreateDashboardWidgetRequest
from ...models.dashboard_widget_created_response import DashboardWidgetCreatedResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dashboard_id: str,
    *,
    body: CreateDashboardWidgetRequest,
    workspace_id: str,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    params: dict[str, Any] = {}

    params["workspaceId"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/dashboards/{dashboard_id}/widgets".format(
            dashboard_id=quote(str(dashboard_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | DashboardWidgetCreatedResponse | None:
    if response.status_code == 201:
        response_201 = DashboardWidgetCreatedResponse.from_dict(response.json())

        return response_201

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

    if response.status_code == 413:
        response_413 = ApiError.from_dict(response.json())

        return response_413

    if response.status_code == 422:
        response_422 = ApiError.from_dict(response.json())

        return response_422

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
) -> Response[ApiError | DashboardWidgetCreatedResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dashboard_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateDashboardWidgetRequest,
    workspace_id: str,
    idempotency_key: str | Unset = UNSET,
) -> Response[ApiError | DashboardWidgetCreatedResponse]:
    """Create dashboard widget

     Adds a widget to a dashboard: a saved cost report drawn as a chart, a table or a KPI, or a text
    widget whose words are rendered as markdown emphasis without HTML. At most 50 per dashboard.

    Needs a token with `viewCostReports` and `updateDashboard` on the workspace.

    Args:
        dashboard_id (str):
        workspace_id (str):
        idempotency_key (str | Unset):
        body (CreateDashboardWidgetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DashboardWidgetCreatedResponse]
    """

    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
        body=body,
        workspace_id=workspace_id,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dashboard_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateDashboardWidgetRequest,
    workspace_id: str,
    idempotency_key: str | Unset = UNSET,
) -> ApiError | DashboardWidgetCreatedResponse | None:
    """Create dashboard widget

     Adds a widget to a dashboard: a saved cost report drawn as a chart, a table or a KPI, or a text
    widget whose words are rendered as markdown emphasis without HTML. At most 50 per dashboard.

    Needs a token with `viewCostReports` and `updateDashboard` on the workspace.

    Args:
        dashboard_id (str):
        workspace_id (str):
        idempotency_key (str | Unset):
        body (CreateDashboardWidgetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DashboardWidgetCreatedResponse
    """

    return sync_detailed(
        dashboard_id=dashboard_id,
        client=client,
        body=body,
        workspace_id=workspace_id,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    dashboard_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateDashboardWidgetRequest,
    workspace_id: str,
    idempotency_key: str | Unset = UNSET,
) -> Response[ApiError | DashboardWidgetCreatedResponse]:
    """Create dashboard widget

     Adds a widget to a dashboard: a saved cost report drawn as a chart, a table or a KPI, or a text
    widget whose words are rendered as markdown emphasis without HTML. At most 50 per dashboard.

    Needs a token with `viewCostReports` and `updateDashboard` on the workspace.

    Args:
        dashboard_id (str):
        workspace_id (str):
        idempotency_key (str | Unset):
        body (CreateDashboardWidgetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DashboardWidgetCreatedResponse]
    """

    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
        body=body,
        workspace_id=workspace_id,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dashboard_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateDashboardWidgetRequest,
    workspace_id: str,
    idempotency_key: str | Unset = UNSET,
) -> ApiError | DashboardWidgetCreatedResponse | None:
    """Create dashboard widget

     Adds a widget to a dashboard: a saved cost report drawn as a chart, a table or a KPI, or a text
    widget whose words are rendered as markdown emphasis without HTML. At most 50 per dashboard.

    Needs a token with `viewCostReports` and `updateDashboard` on the workspace.

    Args:
        dashboard_id (str):
        workspace_id (str):
        idempotency_key (str | Unset):
        body (CreateDashboardWidgetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DashboardWidgetCreatedResponse
    """

    return (
        await asyncio_detailed(
            dashboard_id=dashboard_id,
            client=client,
            body=body,
            workspace_id=workspace_id,
            idempotency_key=idempotency_key,
        )
    ).parsed
