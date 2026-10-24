from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.cost_report_data_response import CostReportDataResponse
from ...types import UNSET, Response


def _get_kwargs(
    cost_report_id: str,
    *,
    workspace_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["workspaceId"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/cost-reports/{cost_report_id}/data".format(
            cost_report_id=quote(str(cost_report_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | CostReportDataResponse | None:
    if response.status_code == 200:
        response_200 = CostReportDataResponse.from_dict(response.json())

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
) -> Response[ApiError | CostReportDataResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cost_report_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: str,
) -> Response[ApiError | CostReportDataResponse]:
    """Get cost report data

     Returns the computed cost data for a report. A breakdown row's `percent` is its share of the
    window's total cost; with conversion off over several currencies, of the total in its own currency.

    Needs a token with `viewCosts` on the workspace.

    Args:
        cost_report_id (str):
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | CostReportDataResponse]
    """

    kwargs = _get_kwargs(
        cost_report_id=cost_report_id,
        workspace_id=workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cost_report_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: str,
) -> ApiError | CostReportDataResponse | None:
    """Get cost report data

     Returns the computed cost data for a report. A breakdown row's `percent` is its share of the
    window's total cost; with conversion off over several currencies, of the total in its own currency.

    Needs a token with `viewCosts` on the workspace.

    Args:
        cost_report_id (str):
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | CostReportDataResponse
    """

    return sync_detailed(
        cost_report_id=cost_report_id,
        client=client,
        workspace_id=workspace_id,
    ).parsed


async def asyncio_detailed(
    cost_report_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: str,
) -> Response[ApiError | CostReportDataResponse]:
    """Get cost report data

     Returns the computed cost data for a report. A breakdown row's `percent` is its share of the
    window's total cost; with conversion off over several currencies, of the total in its own currency.

    Needs a token with `viewCosts` on the workspace.

    Args:
        cost_report_id (str):
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | CostReportDataResponse]
    """

    kwargs = _get_kwargs(
        cost_report_id=cost_report_id,
        workspace_id=workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cost_report_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: str,
) -> ApiError | CostReportDataResponse | None:
    """Get cost report data

     Returns the computed cost data for a report. A breakdown row's `percent` is its share of the
    window's total cost; with conversion off over several currencies, of the total in its own currency.

    Needs a token with `viewCosts` on the workspace.

    Args:
        cost_report_id (str):
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | CostReportDataResponse
    """

    return (
        await asyncio_detailed(
            cost_report_id=cost_report_id,
            client=client,
            workspace_id=workspace_id,
        )
    ).parsed
