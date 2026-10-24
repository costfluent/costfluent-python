import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.cost_summary_response import CostSummaryResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_date: datetime.date,
    end_date: datetime.date,
    workspace_id: None | str | Unset = UNSET,
    cloud_account_ids: list[str] | None | Unset = UNSET,
    filter_: None | str | Unset = UNSET,
    include_credits: bool | Unset = False,
    include_refunds: bool | Unset = True,
    include_tax: bool | Unset = True,
    amortize: bool | Unset = True,
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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/costs/summary",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | CostSummaryResponse | None:
    if response.status_code == 200:
        response_200 = CostSummaryResponse.from_dict(response.json())

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
) -> Response[ApiError | CostSummaryResponse]:
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
    cloud_account_ids: list[str] | None | Unset = UNSET,
    filter_: None | str | Unset = UNSET,
    include_credits: bool | Unset = False,
    include_refunds: bool | Unset = True,
    include_tax: bool | Unset = True,
    amortize: bool | Unset = True,
) -> Response[ApiError | CostSummaryResponse]:
    """Get cost summary

     Returns aggregated cost summary with comparisons. A service's `percentage` is its share of the
    window's total cost; with conversion off over several currencies, of the total in its own currency.

    Needs a token with `viewCosts`; a workspace token lists its own workspace only.

    Args:
        start_date (datetime.date):
        end_date (datetime.date):
        workspace_id (None | str | Unset):
        cloud_account_ids (list[str] | None | Unset):
        filter_ (None | str | Unset):
        include_credits (bool | Unset):  Default: False.
        include_refunds (bool | Unset):  Default: True.
        include_tax (bool | Unset):  Default: True.
        amortize (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | CostSummaryResponse]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        workspace_id=workspace_id,
        cloud_account_ids=cloud_account_ids,
        filter_=filter_,
        include_credits=include_credits,
        include_refunds=include_refunds,
        include_tax=include_tax,
        amortize=amortize,
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
    cloud_account_ids: list[str] | None | Unset = UNSET,
    filter_: None | str | Unset = UNSET,
    include_credits: bool | Unset = False,
    include_refunds: bool | Unset = True,
    include_tax: bool | Unset = True,
    amortize: bool | Unset = True,
) -> ApiError | CostSummaryResponse | None:
    """Get cost summary

     Returns aggregated cost summary with comparisons. A service's `percentage` is its share of the
    window's total cost; with conversion off over several currencies, of the total in its own currency.

    Needs a token with `viewCosts`; a workspace token lists its own workspace only.

    Args:
        start_date (datetime.date):
        end_date (datetime.date):
        workspace_id (None | str | Unset):
        cloud_account_ids (list[str] | None | Unset):
        filter_ (None | str | Unset):
        include_credits (bool | Unset):  Default: False.
        include_refunds (bool | Unset):  Default: True.
        include_tax (bool | Unset):  Default: True.
        amortize (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | CostSummaryResponse
    """

    return sync_detailed(
        client=client,
        start_date=start_date,
        end_date=end_date,
        workspace_id=workspace_id,
        cloud_account_ids=cloud_account_ids,
        filter_=filter_,
        include_credits=include_credits,
        include_refunds=include_refunds,
        include_tax=include_tax,
        amortize=amortize,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_date: datetime.date,
    end_date: datetime.date,
    workspace_id: None | str | Unset = UNSET,
    cloud_account_ids: list[str] | None | Unset = UNSET,
    filter_: None | str | Unset = UNSET,
    include_credits: bool | Unset = False,
    include_refunds: bool | Unset = True,
    include_tax: bool | Unset = True,
    amortize: bool | Unset = True,
) -> Response[ApiError | CostSummaryResponse]:
    """Get cost summary

     Returns aggregated cost summary with comparisons. A service's `percentage` is its share of the
    window's total cost; with conversion off over several currencies, of the total in its own currency.

    Needs a token with `viewCosts`; a workspace token lists its own workspace only.

    Args:
        start_date (datetime.date):
        end_date (datetime.date):
        workspace_id (None | str | Unset):
        cloud_account_ids (list[str] | None | Unset):
        filter_ (None | str | Unset):
        include_credits (bool | Unset):  Default: False.
        include_refunds (bool | Unset):  Default: True.
        include_tax (bool | Unset):  Default: True.
        amortize (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | CostSummaryResponse]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        workspace_id=workspace_id,
        cloud_account_ids=cloud_account_ids,
        filter_=filter_,
        include_credits=include_credits,
        include_refunds=include_refunds,
        include_tax=include_tax,
        amortize=amortize,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start_date: datetime.date,
    end_date: datetime.date,
    workspace_id: None | str | Unset = UNSET,
    cloud_account_ids: list[str] | None | Unset = UNSET,
    filter_: None | str | Unset = UNSET,
    include_credits: bool | Unset = False,
    include_refunds: bool | Unset = True,
    include_tax: bool | Unset = True,
    amortize: bool | Unset = True,
) -> ApiError | CostSummaryResponse | None:
    """Get cost summary

     Returns aggregated cost summary with comparisons. A service's `percentage` is its share of the
    window's total cost; with conversion off over several currencies, of the total in its own currency.

    Needs a token with `viewCosts`; a workspace token lists its own workspace only.

    Args:
        start_date (datetime.date):
        end_date (datetime.date):
        workspace_id (None | str | Unset):
        cloud_account_ids (list[str] | None | Unset):
        filter_ (None | str | Unset):
        include_credits (bool | Unset):  Default: False.
        include_refunds (bool | Unset):  Default: True.
        include_tax (bool | Unset):  Default: True.
        amortize (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | CostSummaryResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            start_date=start_date,
            end_date=end_date,
            workspace_id=workspace_id,
            cloud_account_ids=cloud_account_ids,
            filter_=filter_,
            include_credits=include_credits,
            include_refunds=include_refunds,
            include_tax=include_tax,
            amortize=amortize,
        )
    ).parsed
