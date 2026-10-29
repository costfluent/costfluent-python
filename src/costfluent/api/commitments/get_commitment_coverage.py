import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.commitment_coverage_response import CommitmentCoverageResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    workspace_id: str,
    start_date: datetime.date,
    end_date: datetime.date,
    granularity: str | Unset = "day",
    filter_: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["workspaceId"] = workspace_id

    json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date

    params["granularity"] = granularity

    json_filter_: None | str | Unset
    if isinstance(filter_, Unset):
        json_filter_ = UNSET
    else:
        json_filter_ = filter_
    params["filter"] = json_filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/commitments/coverage",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | CommitmentCoverageResponse | None:
    if response.status_code == 200:
        response_200 = CommitmentCoverageResponse.from_dict(response.json())

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
) -> Response[ApiError | CommitmentCoverageResponse]:
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
    start_date: datetime.date,
    end_date: datetime.date,
    granularity: str | Unset = "day",
    filter_: None | str | Unset = UNSET,
) -> Response[ApiError | CommitmentCoverageResponse]:
    """Get commitment coverage

     Returns how much of the workspace's eligible usage commitments covered, the effective savings rate
    and the commitment left unused over a window, per bin and provider and in total, at amortized cost
    in the workspace's presentation currency.

    Needs a token with `viewCosts` on the workspace.

    Args:
        workspace_id (str):
        start_date (datetime.date):
        end_date (datetime.date):
        granularity (str | Unset):  Default: 'day'.
        filter_ (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | CommitmentCoverageResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        start_date=start_date,
        end_date=end_date,
        granularity=granularity,
        filter_=filter_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    workspace_id: str,
    start_date: datetime.date,
    end_date: datetime.date,
    granularity: str | Unset = "day",
    filter_: None | str | Unset = UNSET,
) -> ApiError | CommitmentCoverageResponse | None:
    """Get commitment coverage

     Returns how much of the workspace's eligible usage commitments covered, the effective savings rate
    and the commitment left unused over a window, per bin and provider and in total, at amortized cost
    in the workspace's presentation currency.

    Needs a token with `viewCosts` on the workspace.

    Args:
        workspace_id (str):
        start_date (datetime.date):
        end_date (datetime.date):
        granularity (str | Unset):  Default: 'day'.
        filter_ (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | CommitmentCoverageResponse
    """

    return sync_detailed(
        client=client,
        workspace_id=workspace_id,
        start_date=start_date,
        end_date=end_date,
        granularity=granularity,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    workspace_id: str,
    start_date: datetime.date,
    end_date: datetime.date,
    granularity: str | Unset = "day",
    filter_: None | str | Unset = UNSET,
) -> Response[ApiError | CommitmentCoverageResponse]:
    """Get commitment coverage

     Returns how much of the workspace's eligible usage commitments covered, the effective savings rate
    and the commitment left unused over a window, per bin and provider and in total, at amortized cost
    in the workspace's presentation currency.

    Needs a token with `viewCosts` on the workspace.

    Args:
        workspace_id (str):
        start_date (datetime.date):
        end_date (datetime.date):
        granularity (str | Unset):  Default: 'day'.
        filter_ (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | CommitmentCoverageResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        start_date=start_date,
        end_date=end_date,
        granularity=granularity,
        filter_=filter_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    workspace_id: str,
    start_date: datetime.date,
    end_date: datetime.date,
    granularity: str | Unset = "day",
    filter_: None | str | Unset = UNSET,
) -> ApiError | CommitmentCoverageResponse | None:
    """Get commitment coverage

     Returns how much of the workspace's eligible usage commitments covered, the effective savings rate
    and the commitment left unused over a window, per bin and provider and in total, at amortized cost
    in the workspace's presentation currency.

    Needs a token with `viewCosts` on the workspace.

    Args:
        workspace_id (str):
        start_date (datetime.date):
        end_date (datetime.date):
        granularity (str | Unset):  Default: 'day'.
        filter_ (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | CommitmentCoverageResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            workspace_id=workspace_id,
            start_date=start_date,
            end_date=end_date,
            granularity=granularity,
            filter_=filter_,
        )
    ).parsed
