import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.cost_data_response import CostDataResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_date: datetime.date,
    end_date: datetime.date,
    workspace_id: None | str | Unset = UNSET,
    granularity: str | Unset = "day",
    group_by: list[str] | None | Unset = UNSET,
    cloud_account_ids: list[str] | None | Unset = UNSET,
    filter_: None | str | Unset = UNSET,
    include_credits: bool | Unset = False,
    include_refunds: bool | Unset = True,
    include_tax: bool | Unset = True,
    amortize: bool | Unset = True,
    measure: None | str | Unset = UNSET,
    data_version: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date

    json_workspace_id: None | str | Unset
    if isinstance(workspace_id, Unset):
        json_workspace_id = UNSET
    else:
        json_workspace_id = workspace_id
    params["workspaceId"] = json_workspace_id

    params["granularity"] = granularity

    json_group_by: list[str] | None | Unset
    if isinstance(group_by, Unset):
        json_group_by = UNSET
    elif isinstance(group_by, list):
        json_group_by = group_by

    else:
        json_group_by = group_by
    params["groupBy"] = json_group_by

    json_cloud_account_ids: list[str] | None | Unset
    if isinstance(cloud_account_ids, Unset):
        json_cloud_account_ids = UNSET
    elif isinstance(cloud_account_ids, list):
        json_cloud_account_ids = cloud_account_ids

    else:
        json_cloud_account_ids = cloud_account_ids
    params["cloudAccountIds"] = json_cloud_account_ids

    json_filter_: None | str | Unset
    if isinstance(filter_, Unset):
        json_filter_ = UNSET
    else:
        json_filter_ = filter_
    params["filter"] = json_filter_

    params["includeCredits"] = include_credits

    params["includeRefunds"] = include_refunds

    params["includeTax"] = include_tax

    params["amortize"] = amortize

    json_measure: None | str | Unset
    if isinstance(measure, Unset):
        json_measure = UNSET
    else:
        json_measure = measure
    params["measure"] = json_measure

    json_data_version: None | str | Unset
    if isinstance(data_version, Unset):
        json_data_version = UNSET
    else:
        json_data_version = data_version
    params["dataVersion"] = json_data_version

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/costs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | CostDataResponse | None:
    if response.status_code == 200:
        response_200 = CostDataResponse.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = ApiError.from_dict(response.json())

        return response_409

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
) -> Response[ApiError | CostDataResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_date: datetime.date,
    end_date: datetime.date,
    workspace_id: None | str | Unset = UNSET,
    granularity: str | Unset = "day",
    group_by: list[str] | None | Unset = UNSET,
    cloud_account_ids: list[str] | None | Unset = UNSET,
    filter_: None | str | Unset = UNSET,
    include_credits: bool | Unset = False,
    include_refunds: bool | Unset = True,
    include_tax: bool | Unset = True,
    amortize: bool | Unset = True,
    measure: None | str | Unset = UNSET,
    data_version: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> Response[ApiError | CostDataResponse]:
    """Get cost data

     Returns cost data grouped by up to three ordered dimensions, filtered by the supplied cost filter. A
    page holds up to 5,000 rows, and paging reaches 100,000 rows (page × limit): a larger read splits
    its date window into shorter ranges. Each row's `dimensions` object holds one value per `groupBy`
    slot, keyed by the slot: the dimension's name with a capital first letter (`ServiceName` for
    `groupBy=serviceName`), followed by a colon and the key for a tag or virtual tag (`Tag:team`,
    `VirtualTag:vtag_...`). An ungrouped read has an empty `dimensions`.

    Needs a token with `viewCosts`; a workspace token lists its own workspace only.

    Args:
        start_date (datetime.date):
        end_date (datetime.date):
        workspace_id (None | str | Unset):
        granularity (str | Unset):  Default: 'day'.
        group_by (list[str] | None | Unset):
        cloud_account_ids (list[str] | None | Unset):
        filter_ (None | str | Unset):
        include_credits (bool | Unset):  Default: False.
        include_refunds (bool | Unset):  Default: True.
        include_tax (bool | Unset):  Default: True.
        amortize (bool | Unset):  Default: True.
        measure (None | str | Unset):
        data_version (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | CostDataResponse]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        workspace_id=workspace_id,
        granularity=granularity,
        group_by=group_by,
        cloud_account_ids=cloud_account_ids,
        filter_=filter_,
        include_credits=include_credits,
        include_refunds=include_refunds,
        include_tax=include_tax,
        amortize=amortize,
        measure=measure,
        data_version=data_version,
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
    start_date: datetime.date,
    end_date: datetime.date,
    workspace_id: None | str | Unset = UNSET,
    granularity: str | Unset = "day",
    group_by: list[str] | None | Unset = UNSET,
    cloud_account_ids: list[str] | None | Unset = UNSET,
    filter_: None | str | Unset = UNSET,
    include_credits: bool | Unset = False,
    include_refunds: bool | Unset = True,
    include_tax: bool | Unset = True,
    amortize: bool | Unset = True,
    measure: None | str | Unset = UNSET,
    data_version: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> ApiError | CostDataResponse | None:
    """Get cost data

     Returns cost data grouped by up to three ordered dimensions, filtered by the supplied cost filter. A
    page holds up to 5,000 rows, and paging reaches 100,000 rows (page × limit): a larger read splits
    its date window into shorter ranges. Each row's `dimensions` object holds one value per `groupBy`
    slot, keyed by the slot: the dimension's name with a capital first letter (`ServiceName` for
    `groupBy=serviceName`), followed by a colon and the key for a tag or virtual tag (`Tag:team`,
    `VirtualTag:vtag_...`). An ungrouped read has an empty `dimensions`.

    Needs a token with `viewCosts`; a workspace token lists its own workspace only.

    Args:
        start_date (datetime.date):
        end_date (datetime.date):
        workspace_id (None | str | Unset):
        granularity (str | Unset):  Default: 'day'.
        group_by (list[str] | None | Unset):
        cloud_account_ids (list[str] | None | Unset):
        filter_ (None | str | Unset):
        include_credits (bool | Unset):  Default: False.
        include_refunds (bool | Unset):  Default: True.
        include_tax (bool | Unset):  Default: True.
        amortize (bool | Unset):  Default: True.
        measure (None | str | Unset):
        data_version (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | CostDataResponse
    """

    return sync_detailed(
        client=client,
        start_date=start_date,
        end_date=end_date,
        workspace_id=workspace_id,
        granularity=granularity,
        group_by=group_by,
        cloud_account_ids=cloud_account_ids,
        filter_=filter_,
        include_credits=include_credits,
        include_refunds=include_refunds,
        include_tax=include_tax,
        amortize=amortize,
        measure=measure,
        data_version=data_version,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_date: datetime.date,
    end_date: datetime.date,
    workspace_id: None | str | Unset = UNSET,
    granularity: str | Unset = "day",
    group_by: list[str] | None | Unset = UNSET,
    cloud_account_ids: list[str] | None | Unset = UNSET,
    filter_: None | str | Unset = UNSET,
    include_credits: bool | Unset = False,
    include_refunds: bool | Unset = True,
    include_tax: bool | Unset = True,
    amortize: bool | Unset = True,
    measure: None | str | Unset = UNSET,
    data_version: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> Response[ApiError | CostDataResponse]:
    """Get cost data

     Returns cost data grouped by up to three ordered dimensions, filtered by the supplied cost filter. A
    page holds up to 5,000 rows, and paging reaches 100,000 rows (page × limit): a larger read splits
    its date window into shorter ranges. Each row's `dimensions` object holds one value per `groupBy`
    slot, keyed by the slot: the dimension's name with a capital first letter (`ServiceName` for
    `groupBy=serviceName`), followed by a colon and the key for a tag or virtual tag (`Tag:team`,
    `VirtualTag:vtag_...`). An ungrouped read has an empty `dimensions`.

    Needs a token with `viewCosts`; a workspace token lists its own workspace only.

    Args:
        start_date (datetime.date):
        end_date (datetime.date):
        workspace_id (None | str | Unset):
        granularity (str | Unset):  Default: 'day'.
        group_by (list[str] | None | Unset):
        cloud_account_ids (list[str] | None | Unset):
        filter_ (None | str | Unset):
        include_credits (bool | Unset):  Default: False.
        include_refunds (bool | Unset):  Default: True.
        include_tax (bool | Unset):  Default: True.
        amortize (bool | Unset):  Default: True.
        measure (None | str | Unset):
        data_version (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | CostDataResponse]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        workspace_id=workspace_id,
        granularity=granularity,
        group_by=group_by,
        cloud_account_ids=cloud_account_ids,
        filter_=filter_,
        include_credits=include_credits,
        include_refunds=include_refunds,
        include_tax=include_tax,
        amortize=amortize,
        measure=measure,
        data_version=data_version,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start_date: datetime.date,
    end_date: datetime.date,
    workspace_id: None | str | Unset = UNSET,
    granularity: str | Unset = "day",
    group_by: list[str] | None | Unset = UNSET,
    cloud_account_ids: list[str] | None | Unset = UNSET,
    filter_: None | str | Unset = UNSET,
    include_credits: bool | Unset = False,
    include_refunds: bool | Unset = True,
    include_tax: bool | Unset = True,
    amortize: bool | Unset = True,
    measure: None | str | Unset = UNSET,
    data_version: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> ApiError | CostDataResponse | None:
    """Get cost data

     Returns cost data grouped by up to three ordered dimensions, filtered by the supplied cost filter. A
    page holds up to 5,000 rows, and paging reaches 100,000 rows (page × limit): a larger read splits
    its date window into shorter ranges. Each row's `dimensions` object holds one value per `groupBy`
    slot, keyed by the slot: the dimension's name with a capital first letter (`ServiceName` for
    `groupBy=serviceName`), followed by a colon and the key for a tag or virtual tag (`Tag:team`,
    `VirtualTag:vtag_...`). An ungrouped read has an empty `dimensions`.

    Needs a token with `viewCosts`; a workspace token lists its own workspace only.

    Args:
        start_date (datetime.date):
        end_date (datetime.date):
        workspace_id (None | str | Unset):
        granularity (str | Unset):  Default: 'day'.
        group_by (list[str] | None | Unset):
        cloud_account_ids (list[str] | None | Unset):
        filter_ (None | str | Unset):
        include_credits (bool | Unset):  Default: False.
        include_refunds (bool | Unset):  Default: True.
        include_tax (bool | Unset):  Default: True.
        amortize (bool | Unset):  Default: True.
        measure (None | str | Unset):
        data_version (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | CostDataResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            start_date=start_date,
            end_date=end_date,
            workspace_id=workspace_id,
            granularity=granularity,
            group_by=group_by,
            cloud_account_ids=cloud_account_ids,
            filter_=filter_,
            include_credits=include_credits,
            include_refunds=include_refunds,
            include_tax=include_tax,
            amortize=amortize,
            measure=measure,
            data_version=data_version,
            page=page,
            limit=limit,
        )
    ).parsed
