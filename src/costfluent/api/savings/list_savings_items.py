from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.paginated_response_of_savings_item_response import (
    PaginatedResponseOfSavingsItemResponse,
)
from ...models.savings_queue_sort import SavingsQueueSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    workspace_id: str,
    tab: None | str | Unset = UNSET,
    source: None | str | Unset = UNSET,
    kind: None | str | Unset = UNSET,
    cloud_account_id: None | str | Unset = UNSET,
    minimum_monthly_saving: None | str | Unset = UNSET,
    sort: SavingsQueueSort | Unset = SavingsQueueSort.NEWEST,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["workspaceId"] = workspace_id

    json_tab: None | str | Unset
    if isinstance(tab, Unset):
        json_tab = UNSET
    else:
        json_tab = tab
    params["tab"] = json_tab

    json_source: None | str | Unset
    if isinstance(source, Unset):
        json_source = UNSET
    else:
        json_source = source
    params["source"] = json_source

    json_kind: None | str | Unset
    if isinstance(kind, Unset):
        json_kind = UNSET
    else:
        json_kind = kind
    params["kind"] = json_kind

    json_cloud_account_id: None | str | Unset
    if isinstance(cloud_account_id, Unset):
        json_cloud_account_id = UNSET
    else:
        json_cloud_account_id = cloud_account_id
    params["cloudAccountId"] = json_cloud_account_id

    json_minimum_monthly_saving: None | str | Unset
    if isinstance(minimum_monthly_saving, Unset):
        json_minimum_monthly_saving = UNSET
    else:
        json_minimum_monthly_saving = minimum_monthly_saving
    params["minimumMonthlySaving"] = json_minimum_monthly_saving

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/savings-items",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PaginatedResponseOfSavingsItemResponse | None:
    if response.status_code == 200:
        response_200 = PaginatedResponseOfSavingsItemResponse.from_dict(response.json())

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
) -> Response[ApiError | PaginatedResponseOfSavingsItemResponse]:
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
    tab: None | str | Unset = UNSET,
    source: None | str | Unset = UNSET,
    kind: None | str | Unset = UNSET,
    cloud_account_id: None | str | Unset = UNSET,
    minimum_monthly_saving: None | str | Unset = UNSET,
    sort: SavingsQueueSort | Unset = SavingsQueueSort.NEWEST,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> Response[ApiError | PaginatedResponseOfSavingsItemResponse]:
    """List savings findings

     Returns the workspace's savings queue: one tab's findings, or every status without one, narrowed by
    source, kind, the connection that generated them and a minimum monthly saving, newest first or
    largest saving first. Costfluent's curated findings are listed only on a plan that includes them. An
    unknown cloudAccountId matches no finding.

    Needs a token with `viewSavingsItems` on the workspace.

    Args:
        workspace_id (str):
        tab (None | str | Unset):
        source (None | str | Unset):
        kind (None | str | Unset):
        cloud_account_id (None | str | Unset):
        minimum_monthly_saving (None | str | Unset):
        sort (SavingsQueueSort | Unset):  Default: SavingsQueueSort.NEWEST.
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PaginatedResponseOfSavingsItemResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        tab=tab,
        source=source,
        kind=kind,
        cloud_account_id=cloud_account_id,
        minimum_monthly_saving=minimum_monthly_saving,
        sort=sort,
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
    tab: None | str | Unset = UNSET,
    source: None | str | Unset = UNSET,
    kind: None | str | Unset = UNSET,
    cloud_account_id: None | str | Unset = UNSET,
    minimum_monthly_saving: None | str | Unset = UNSET,
    sort: SavingsQueueSort | Unset = SavingsQueueSort.NEWEST,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> ApiError | PaginatedResponseOfSavingsItemResponse | None:
    """List savings findings

     Returns the workspace's savings queue: one tab's findings, or every status without one, narrowed by
    source, kind, the connection that generated them and a minimum monthly saving, newest first or
    largest saving first. Costfluent's curated findings are listed only on a plan that includes them. An
    unknown cloudAccountId matches no finding.

    Needs a token with `viewSavingsItems` on the workspace.

    Args:
        workspace_id (str):
        tab (None | str | Unset):
        source (None | str | Unset):
        kind (None | str | Unset):
        cloud_account_id (None | str | Unset):
        minimum_monthly_saving (None | str | Unset):
        sort (SavingsQueueSort | Unset):  Default: SavingsQueueSort.NEWEST.
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PaginatedResponseOfSavingsItemResponse
    """

    return sync_detailed(
        client=client,
        workspace_id=workspace_id,
        tab=tab,
        source=source,
        kind=kind,
        cloud_account_id=cloud_account_id,
        minimum_monthly_saving=minimum_monthly_saving,
        sort=sort,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    workspace_id: str,
    tab: None | str | Unset = UNSET,
    source: None | str | Unset = UNSET,
    kind: None | str | Unset = UNSET,
    cloud_account_id: None | str | Unset = UNSET,
    minimum_monthly_saving: None | str | Unset = UNSET,
    sort: SavingsQueueSort | Unset = SavingsQueueSort.NEWEST,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> Response[ApiError | PaginatedResponseOfSavingsItemResponse]:
    """List savings findings

     Returns the workspace's savings queue: one tab's findings, or every status without one, narrowed by
    source, kind, the connection that generated them and a minimum monthly saving, newest first or
    largest saving first. Costfluent's curated findings are listed only on a plan that includes them. An
    unknown cloudAccountId matches no finding.

    Needs a token with `viewSavingsItems` on the workspace.

    Args:
        workspace_id (str):
        tab (None | str | Unset):
        source (None | str | Unset):
        kind (None | str | Unset):
        cloud_account_id (None | str | Unset):
        minimum_monthly_saving (None | str | Unset):
        sort (SavingsQueueSort | Unset):  Default: SavingsQueueSort.NEWEST.
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PaginatedResponseOfSavingsItemResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        tab=tab,
        source=source,
        kind=kind,
        cloud_account_id=cloud_account_id,
        minimum_monthly_saving=minimum_monthly_saving,
        sort=sort,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    workspace_id: str,
    tab: None | str | Unset = UNSET,
    source: None | str | Unset = UNSET,
    kind: None | str | Unset = UNSET,
    cloud_account_id: None | str | Unset = UNSET,
    minimum_monthly_saving: None | str | Unset = UNSET,
    sort: SavingsQueueSort | Unset = SavingsQueueSort.NEWEST,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> ApiError | PaginatedResponseOfSavingsItemResponse | None:
    """List savings findings

     Returns the workspace's savings queue: one tab's findings, or every status without one, narrowed by
    source, kind, the connection that generated them and a minimum monthly saving, newest first or
    largest saving first. Costfluent's curated findings are listed only on a plan that includes them. An
    unknown cloudAccountId matches no finding.

    Needs a token with `viewSavingsItems` on the workspace.

    Args:
        workspace_id (str):
        tab (None | str | Unset):
        source (None | str | Unset):
        kind (None | str | Unset):
        cloud_account_id (None | str | Unset):
        minimum_monthly_saving (None | str | Unset):
        sort (SavingsQueueSort | Unset):  Default: SavingsQueueSort.NEWEST.
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PaginatedResponseOfSavingsItemResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            workspace_id=workspace_id,
            tab=tab,
            source=source,
            kind=kind,
            cloud_account_id=cloud_account_id,
            minimum_monthly_saving=minimum_monthly_saving,
            sort=sort,
            page=page,
            limit=limit,
        )
    ).parsed
