import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.exchange_rate_response import ExchangeRateResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    base_currency: str,
    target_currency: str,
    date: datetime.date | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["baseCurrency"] = base_currency

    params["targetCurrency"] = target_currency

    json_date: None | str | Unset
    if isinstance(date, Unset):
        json_date = UNSET
    elif isinstance(date, datetime.date):
        json_date = date.isoformat()
    else:
        json_date = date
    params["date"] = json_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/exchange-rates/rate",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | ExchangeRateResponse | None:
    if response.status_code == 200:
        response_200 = ExchangeRateResponse.from_dict(response.json())

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
) -> Response[ApiError | ExchangeRateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    base_currency: str,
    target_currency: str,
    date: datetime.date | None | Unset = UNSET,
) -> Response[ApiError | ExchangeRateResponse]:
    """Get exchange rate

     Returns the rate for a currency pair from the last ECB publication on or before date, named in
    effectiveDate; the latest publication when date is omitted or later. Every pair derives through the
    euro, so inverse and cross pairs are computed from the euro rates.

    Needs any valid token.

    Args:
        base_currency (str):
        target_currency (str):
        date (datetime.date | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | ExchangeRateResponse]
    """

    kwargs = _get_kwargs(
        base_currency=base_currency,
        target_currency=target_currency,
        date=date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    base_currency: str,
    target_currency: str,
    date: datetime.date | None | Unset = UNSET,
) -> ApiError | ExchangeRateResponse | None:
    """Get exchange rate

     Returns the rate for a currency pair from the last ECB publication on or before date, named in
    effectiveDate; the latest publication when date is omitted or later. Every pair derives through the
    euro, so inverse and cross pairs are computed from the euro rates.

    Needs any valid token.

    Args:
        base_currency (str):
        target_currency (str):
        date (datetime.date | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | ExchangeRateResponse
    """

    return sync_detailed(
        client=client,
        base_currency=base_currency,
        target_currency=target_currency,
        date=date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    base_currency: str,
    target_currency: str,
    date: datetime.date | None | Unset = UNSET,
) -> Response[ApiError | ExchangeRateResponse]:
    """Get exchange rate

     Returns the rate for a currency pair from the last ECB publication on or before date, named in
    effectiveDate; the latest publication when date is omitted or later. Every pair derives through the
    euro, so inverse and cross pairs are computed from the euro rates.

    Needs any valid token.

    Args:
        base_currency (str):
        target_currency (str):
        date (datetime.date | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | ExchangeRateResponse]
    """

    kwargs = _get_kwargs(
        base_currency=base_currency,
        target_currency=target_currency,
        date=date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    base_currency: str,
    target_currency: str,
    date: datetime.date | None | Unset = UNSET,
) -> ApiError | ExchangeRateResponse | None:
    """Get exchange rate

     Returns the rate for a currency pair from the last ECB publication on or before date, named in
    effectiveDate; the latest publication when date is omitted or later. Every pair derives through the
    euro, so inverse and cross pairs are computed from the euro rates.

    Needs any valid token.

    Args:
        base_currency (str):
        target_currency (str):
        date (datetime.date | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | ExchangeRateResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            base_currency=base_currency,
            target_currency=target_currency,
            date=date,
        )
    ).parsed
