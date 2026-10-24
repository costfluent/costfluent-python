from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.paginated_response_of_cost_report_response import (
    PaginatedResponseOfCostReportResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    workspace_id: str,
    folder_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["workspaceId"] = workspace_id

    json_folder_id: None | str | Unset
    if isinstance(folder_id, Unset):
        json_folder_id = UNSET
    else:
        json_folder_id = folder_id
    params["folderId"] = json_folder_id

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/cost-reports",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PaginatedResponseOfCostReportResponse | None:
    if response.status_code == 200:
        response_200 = PaginatedResponseOfCostReportResponse.from_dict(response.json())

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
) -> Response[ApiError | PaginatedResponseOfCostReportResponse]:
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
    folder_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> Response[ApiError | PaginatedResponseOfCostReportResponse]:
    """List cost reports

     Returns all cost reports for a workspace, optionally filtered by folder.

    Needs a token with `viewCostReports` on the workspace.

    Args:
        workspace_id (str):
        folder_id (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PaginatedResponseOfCostReportResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        folder_id=folder_id,
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
    folder_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> ApiError | PaginatedResponseOfCostReportResponse | None:
    """List cost reports

     Returns all cost reports for a workspace, optionally filtered by folder.

    Needs a token with `viewCostReports` on the workspace.

    Args:
        workspace_id (str):
        folder_id (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PaginatedResponseOfCostReportResponse
    """

    return sync_detailed(
        client=client,
        workspace_id=workspace_id,
        folder_id=folder_id,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    workspace_id: str,
    folder_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> Response[ApiError | PaginatedResponseOfCostReportResponse]:
    """List cost reports

     Returns all cost reports for a workspace, optionally filtered by folder.

    Needs a token with `viewCostReports` on the workspace.

    Args:
        workspace_id (str):
        folder_id (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PaginatedResponseOfCostReportResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        folder_id=folder_id,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    workspace_id: str,
    folder_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> ApiError | PaginatedResponseOfCostReportResponse | None:
    """List cost reports

     Returns all cost reports for a workspace, optionally filtered by folder.

    Needs a token with `viewCostReports` on the workspace.

    Args:
        workspace_id (str):
        folder_id (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PaginatedResponseOfCostReportResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            workspace_id=workspace_id,
            folder_id=folder_id,
            page=page,
            limit=limit,
        )
    ).parsed
