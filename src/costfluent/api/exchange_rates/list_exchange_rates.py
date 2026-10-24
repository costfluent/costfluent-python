import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.paginated_response_of_exchange_rate_response import (
    PaginatedResponseOfExchangeRateResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    base_currency: None | str | Unset = UNSET,
    target_currency: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

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

    json_base_currency: None | str | Unset
    if isinstance(base_currency, Unset):
        json_base_currency = UNSET
    else:
        json_base_currency = base_currency
    params["baseCurrency"] = json_base_currency

    json_target_currency: None | str | Unset
    if isinstance(target_currency, Unset):
        json_target_currency = UNSET
    else:
        json_target_currency = target_currency
    params["targetCurrency"] = json_target_currency

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/exchange-rates",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PaginatedResponseOfExchangeRateResponse | None:
    if response.status_code == 200:
        response_200 = PaginatedResponseOfExchangeRateResponse.from_dict(
            response.json()
        )

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
) -> Response[ApiError | PaginatedResponseOfExchangeRateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    base_currency: None | str | Unset = UNSET,
    target_currency: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> Response[ApiError | PaginatedResponseOfExchangeRateResponse]:
    """List exchange rates

     Returns the published exchange rates over a window of publication days, paged; the window defaults
    to the latest publication day.

    Needs any valid token.

    Args:
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        base_currency (None | str | Unset):
        target_currency (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PaginatedResponseOfExchangeRateResponse]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        base_currency=base_currency,
        target_currency=target_currency,
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
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    base_currency: None | str | Unset = UNSET,
    target_currency: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> ApiError | PaginatedResponseOfExchangeRateResponse | None:
    """List exchange rates

     Returns the published exchange rates over a window of publication days, paged; the window defaults
    to the latest publication day.

    Needs any valid token.

    Args:
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        base_currency (None | str | Unset):
        target_currency (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PaginatedResponseOfExchangeRateResponse
    """

    return sync_detailed(
        client=client,
        start_date=start_date,
        end_date=end_date,
        base_currency=base_currency,
        target_currency=target_currency,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    base_currency: None | str | Unset = UNSET,
    target_currency: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> Response[ApiError | PaginatedResponseOfExchangeRateResponse]:
    """List exchange rates

     Returns the published exchange rates over a window of publication days, paged; the window defaults
    to the latest publication day.

    Needs any valid token.

    Args:
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        base_currency (None | str | Unset):
        target_currency (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PaginatedResponseOfExchangeRateResponse]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        base_currency=base_currency,
        target_currency=target_currency,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    base_currency: None | str | Unset = UNSET,
    target_currency: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> ApiError | PaginatedResponseOfExchangeRateResponse | None:
    """List exchange rates

     Returns the published exchange rates over a window of publication days, paged; the window defaults
    to the latest publication day.

    Needs any valid token.

    Args:
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        base_currency (None | str | Unset):
        target_currency (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PaginatedResponseOfExchangeRateResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            start_date=start_date,
            end_date=end_date,
            base_currency=base_currency,
            target_currency=target_currency,
            page=page,
            limit=limit,
        )
    ).parsed
