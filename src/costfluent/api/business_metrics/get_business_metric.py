from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.business_metric_response import BusinessMetricResponse
from ...types import UNSET, Response


def _get_kwargs(
    metric_id: str,
    *,
    workspace_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["workspaceId"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/business-metrics/{metric_id}".format(
            metric_id=quote(str(metric_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | BusinessMetricResponse | None:
    if response.status_code == 200:
        response_200 = BusinessMetricResponse.from_dict(response.json())

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
) -> Response[ApiError | BusinessMetricResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    metric_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: str,
) -> Response[ApiError | BusinessMetricResponse]:
    """Get business metric

     Returns one business metric.

    Needs a token with `viewCostReports` on the workspace.

    Args:
        metric_id (str):
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | BusinessMetricResponse]
    """

    kwargs = _get_kwargs(
        metric_id=metric_id,
        workspace_id=workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    metric_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: str,
) -> ApiError | BusinessMetricResponse | None:
    """Get business metric

     Returns one business metric.

    Needs a token with `viewCostReports` on the workspace.

    Args:
        metric_id (str):
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | BusinessMetricResponse
    """

    return sync_detailed(
        metric_id=metric_id,
        client=client,
        workspace_id=workspace_id,
    ).parsed


async def asyncio_detailed(
    metric_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: str,
) -> Response[ApiError | BusinessMetricResponse]:
    """Get business metric

     Returns one business metric.

    Needs a token with `viewCostReports` on the workspace.

    Args:
        metric_id (str):
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | BusinessMetricResponse]
    """

    kwargs = _get_kwargs(
        metric_id=metric_id,
        workspace_id=workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    metric_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: str,
) -> ApiError | BusinessMetricResponse | None:
    """Get business metric

     Returns one business metric.

    Needs a token with `viewCostReports` on the workspace.

    Args:
        metric_id (str):
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | BusinessMetricResponse
    """

    return (
        await asyncio_detailed(
            metric_id=metric_id,
            client=client,
            workspace_id=workspace_id,
        )
    ).parsed
