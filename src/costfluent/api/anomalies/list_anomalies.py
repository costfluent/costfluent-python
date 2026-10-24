import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.paginated_response_of_anomaly_response import (
    PaginatedResponseOfAnomalyResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cloud_account_id: None | str | Unset = UNSET,
    severity: None | str | Unset = UNSET,
    unacknowledged_only: bool | Unset = False,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_cloud_account_id: None | str | Unset
    if isinstance(cloud_account_id, Unset):
        json_cloud_account_id = UNSET
    else:
        json_cloud_account_id = cloud_account_id
    params["cloudAccountId"] = json_cloud_account_id

    json_severity: None | str | Unset
    if isinstance(severity, Unset):
        json_severity = UNSET
    else:
        json_severity = severity
    params["severity"] = json_severity

    params["unacknowledgedOnly"] = unacknowledged_only

    json_start_date: None | str | Unset
    if isinstance(start_date, Unset):
        json_start_date = UNSET
    elif isinstance(start_date, datetime.date):
        json_start_date = start_date.isoformat()
    else:
        json_start_date = start_date
    params["startDate"] = json_start_date

    json_end_date: None | str | Unset
    if isinstance(end_date, Unset):
        json_end_date = UNSET
    elif isinstance(end_date, datetime.date):
        json_end_date = end_date.isoformat()
    else:
        json_end_date = end_date
    params["endDate"] = json_end_date

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/anomalies",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PaginatedResponseOfAnomalyResponse | None:
    if response.status_code == 200:
        response_200 = PaginatedResponseOfAnomalyResponse.from_dict(response.json())

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
) -> Response[ApiError | PaginatedResponseOfAnomalyResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cloud_account_id: None | str | Unset = UNSET,
    severity: None | str | Unset = UNSET,
    unacknowledged_only: bool | Unset = False,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> Response[ApiError | PaginatedResponseOfAnomalyResponse]:
    """List anomalies

     Returns detected cost anomalies, newest charge date first. An unknown cloudAccountId answers 404.

    Needs a token with `viewAnomalies`; a workspace token lists its own workspace only.

    Args:
        cloud_account_id (None | str | Unset):
        severity (None | str | Unset):
        unacknowledged_only (bool | Unset):  Default: False.
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PaginatedResponseOfAnomalyResponse]
    """

    kwargs = _get_kwargs(
        cloud_account_id=cloud_account_id,
        severity=severity,
        unacknowledged_only=unacknowledged_only,
        start_date=start_date,
        end_date=end_date,
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
    cloud_account_id: None | str | Unset = UNSET,
    severity: None | str | Unset = UNSET,
    unacknowledged_only: bool | Unset = False,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> ApiError | PaginatedResponseOfAnomalyResponse | None:
    """List anomalies

     Returns detected cost anomalies, newest charge date first. An unknown cloudAccountId answers 404.

    Needs a token with `viewAnomalies`; a workspace token lists its own workspace only.

    Args:
        cloud_account_id (None | str | Unset):
        severity (None | str | Unset):
        unacknowledged_only (bool | Unset):  Default: False.
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PaginatedResponseOfAnomalyResponse
    """

    return sync_detailed(
        client=client,
        cloud_account_id=cloud_account_id,
        severity=severity,
        unacknowledged_only=unacknowledged_only,
        start_date=start_date,
        end_date=end_date,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cloud_account_id: None | str | Unset = UNSET,
    severity: None | str | Unset = UNSET,
    unacknowledged_only: bool | Unset = False,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> Response[ApiError | PaginatedResponseOfAnomalyResponse]:
    """List anomalies

     Returns detected cost anomalies, newest charge date first. An unknown cloudAccountId answers 404.

    Needs a token with `viewAnomalies`; a workspace token lists its own workspace only.

    Args:
        cloud_account_id (None | str | Unset):
        severity (None | str | Unset):
        unacknowledged_only (bool | Unset):  Default: False.
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PaginatedResponseOfAnomalyResponse]
    """

    kwargs = _get_kwargs(
        cloud_account_id=cloud_account_id,
        severity=severity,
        unacknowledged_only=unacknowledged_only,
        start_date=start_date,
        end_date=end_date,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cloud_account_id: None | str | Unset = UNSET,
    severity: None | str | Unset = UNSET,
    unacknowledged_only: bool | Unset = False,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> ApiError | PaginatedResponseOfAnomalyResponse | None:
    """List anomalies

     Returns detected cost anomalies, newest charge date first. An unknown cloudAccountId answers 404.

    Needs a token with `viewAnomalies`; a workspace token lists its own workspace only.

    Args:
        cloud_account_id (None | str | Unset):
        severity (None | str | Unset):
        unacknowledged_only (bool | Unset):  Default: False.
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PaginatedResponseOfAnomalyResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            cloud_account_id=cloud_account_id,
            severity=severity,
            unacknowledged_only=unacknowledged_only,
            start_date=start_date,
            end_date=end_date,
            page=page,
            limit=limit,
        )
    ).parsed
