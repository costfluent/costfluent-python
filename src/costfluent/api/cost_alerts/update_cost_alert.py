from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.cost_alert_response import CostAlertResponse
from ...models.update_cost_alert_route_request import UpdateCostAlertRouteRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    alert_id: str,
    *,
    body: UpdateCostAlertRouteRequest,
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
        "url": "/v1/cost-alerts/{alert_id}".format(
            alert_id=quote(str(alert_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | CostAlertResponse | None:
    if response.status_code == 200:
        response_200 = CostAlertResponse.from_dict(response.json())

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
) -> Response[ApiError | CostAlertResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    alert_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCostAlertRouteRequest,
    workspace_id: str,
    if_match: str | Unset = UNSET,
) -> Response[ApiError | CostAlertResponse]:
    """Update cost alert

     Updates a cost alert and returns it as stored. `thresholdType` sets what `thresholdValue` measures:
    `absolute`, the increase in cost against `comparisonPeriod`, in the alert's currency;
    `percentageIncrease`, that increase as a percentage; `budgetPercentage`, the month-to-date spend,
    from the 1st of the month through the last settled day, reaching `thresholdValue` in the alert's
    currency; `tagCoverageBelow`, the workspace's tag coverage falling below `thresholdValue` percent.
    `budgetPercentage` references no budget; its name is kept for compatibility.

    Needs a token with `manageAlerts` on the workspace.

    Args:
        alert_id (str):
        workspace_id (str):
        if_match (str | Unset):
        body (UpdateCostAlertRouteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | CostAlertResponse]
    """

    kwargs = _get_kwargs(
        alert_id=alert_id,
        body=body,
        workspace_id=workspace_id,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    alert_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCostAlertRouteRequest,
    workspace_id: str,
    if_match: str | Unset = UNSET,
) -> ApiError | CostAlertResponse | None:
    """Update cost alert

     Updates a cost alert and returns it as stored. `thresholdType` sets what `thresholdValue` measures:
    `absolute`, the increase in cost against `comparisonPeriod`, in the alert's currency;
    `percentageIncrease`, that increase as a percentage; `budgetPercentage`, the month-to-date spend,
    from the 1st of the month through the last settled day, reaching `thresholdValue` in the alert's
    currency; `tagCoverageBelow`, the workspace's tag coverage falling below `thresholdValue` percent.
    `budgetPercentage` references no budget; its name is kept for compatibility.

    Needs a token with `manageAlerts` on the workspace.

    Args:
        alert_id (str):
        workspace_id (str):
        if_match (str | Unset):
        body (UpdateCostAlertRouteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | CostAlertResponse
    """

    return sync_detailed(
        alert_id=alert_id,
        client=client,
        body=body,
        workspace_id=workspace_id,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    alert_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCostAlertRouteRequest,
    workspace_id: str,
    if_match: str | Unset = UNSET,
) -> Response[ApiError | CostAlertResponse]:
    """Update cost alert

     Updates a cost alert and returns it as stored. `thresholdType` sets what `thresholdValue` measures:
    `absolute`, the increase in cost against `comparisonPeriod`, in the alert's currency;
    `percentageIncrease`, that increase as a percentage; `budgetPercentage`, the month-to-date spend,
    from the 1st of the month through the last settled day, reaching `thresholdValue` in the alert's
    currency; `tagCoverageBelow`, the workspace's tag coverage falling below `thresholdValue` percent.
    `budgetPercentage` references no budget; its name is kept for compatibility.

    Needs a token with `manageAlerts` on the workspace.

    Args:
        alert_id (str):
        workspace_id (str):
        if_match (str | Unset):
        body (UpdateCostAlertRouteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | CostAlertResponse]
    """

    kwargs = _get_kwargs(
        alert_id=alert_id,
        body=body,
        workspace_id=workspace_id,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alert_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCostAlertRouteRequest,
    workspace_id: str,
    if_match: str | Unset = UNSET,
) -> ApiError | CostAlertResponse | None:
    """Update cost alert

     Updates a cost alert and returns it as stored. `thresholdType` sets what `thresholdValue` measures:
    `absolute`, the increase in cost against `comparisonPeriod`, in the alert's currency;
    `percentageIncrease`, that increase as a percentage; `budgetPercentage`, the month-to-date spend,
    from the 1st of the month through the last settled day, reaching `thresholdValue` in the alert's
    currency; `tagCoverageBelow`, the workspace's tag coverage falling below `thresholdValue` percent.
    `budgetPercentage` references no budget; its name is kept for compatibility.

    Needs a token with `manageAlerts` on the workspace.

    Args:
        alert_id (str):
        workspace_id (str):
        if_match (str | Unset):
        body (UpdateCostAlertRouteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | CostAlertResponse
    """

    return (
        await asyncio_detailed(
            alert_id=alert_id,
            client=client,
            body=body,
            workspace_id=workspace_id,
            if_match=if_match,
        )
    ).parsed
