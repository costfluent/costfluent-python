from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.paginated_response_of_cost_alert_response import (
    PaginatedResponseOfCostAlertResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    workspace_id: str,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["workspaceId"] = workspace_id

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/cost-alerts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PaginatedResponseOfCostAlertResponse | None:
    if response.status_code == 200:
        response_200 = PaginatedResponseOfCostAlertResponse.from_dict(response.json())

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
) -> Response[ApiError | PaginatedResponseOfCostAlertResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    workspace_id: str,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> Response[ApiError | PaginatedResponseOfCostAlertResponse]:
    """List cost alerts

     Returns all cost alerts for a workspace.

    Needs a token with `viewCosts` on the workspace.

    Args:
        workspace_id (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PaginatedResponseOfCostAlertResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    workspace_id: str,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> ApiError | PaginatedResponseOfCostAlertResponse | None:
    """List cost alerts

     Returns all cost alerts for a workspace.

    Needs a token with `viewCosts` on the workspace.

    Args:
        workspace_id (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PaginatedResponseOfCostAlertResponse
    """

    return sync_detailed(
        client=client,
        workspace_id=workspace_id,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    workspace_id: str,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> Response[ApiError | PaginatedResponseOfCostAlertResponse]:
    """List cost alerts

     Returns all cost alerts for a workspace.

    Needs a token with `viewCosts` on the workspace.

    Args:
        workspace_id (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PaginatedResponseOfCostAlertResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    workspace_id: str,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> ApiError | PaginatedResponseOfCostAlertResponse | None:
    """List cost alerts

     Returns all cost alerts for a workspace.

    Needs a token with `viewCosts` on the workspace.

    Args:
        workspace_id (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PaginatedResponseOfCostAlertResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            workspace_id=workspace_id,
            page=page,
            limit=limit,
        )
    ).parsed
