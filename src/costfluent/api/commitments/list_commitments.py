from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.paginated_response_of_commitment_response import (
    PaginatedResponseOfCommitmentResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    workspace_id: str,
    provider: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    type_: None | str | Unset = UNSET,
    service: None | str | Unset = UNSET,
    account: None | str | Unset = UNSET,
    region: None | str | Unset = UNSET,
    term_years: int | None | Unset = UNSET,
    payment_option: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["workspaceId"] = workspace_id

    json_provider: None | str | Unset
    if isinstance(provider, Unset):
        json_provider = UNSET
    else:
        json_provider = provider
    params["provider"] = json_provider

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    json_type_: None | str | Unset
    if isinstance(type_, Unset):
        json_type_ = UNSET
    else:
        json_type_ = type_
    params["type"] = json_type_

    json_service: None | str | Unset
    if isinstance(service, Unset):
        json_service = UNSET
    else:
        json_service = service
    params["service"] = json_service

    json_account: None | str | Unset
    if isinstance(account, Unset):
        json_account = UNSET
    else:
        json_account = account
    params["account"] = json_account

    json_region: None | str | Unset
    if isinstance(region, Unset):
        json_region = UNSET
    else:
        json_region = region
    params["region"] = json_region

    json_term_years: int | None | Unset
    if isinstance(term_years, Unset):
        json_term_years = UNSET
    else:
        json_term_years = term_years
    params["termYears"] = json_term_years

    json_payment_option: None | str | Unset
    if isinstance(payment_option, Unset):
        json_payment_option = UNSET
    else:
        json_payment_option = payment_option
    params["paymentOption"] = json_payment_option

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/commitments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PaginatedResponseOfCommitmentResponse | None:
    if response.status_code == 200:
        response_200 = PaginatedResponseOfCommitmentResponse.from_dict(response.json())

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
) -> Response[ApiError | PaginatedResponseOfCommitmentResponse]:
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
    provider: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    type_: None | str | Unset = UNSET,
    service: None | str | Unset = UNSET,
    account: None | str | Unset = UNSET,
    region: None | str | Unset = UNSET,
    term_years: int | None | Unset = UNSET,
    payment_option: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> Response[ApiError | PaginatedResponseOfCommitmentResponse]:
    """List commitments

     Returns the reservations, savings plans and committed use discounts held through the workspace's
    connections, narrowed to the accounts the workspace reads of each, by end date, earliest first and
    those without an end last. It holds at most 5,000: those still running, soonest end first, before
    those that have ended.

    Needs a token with `viewCosts` on the workspace.

    Args:
        workspace_id (str):
        provider (None | str | Unset):
        status (None | str | Unset):
        type_ (None | str | Unset):
        service (None | str | Unset):
        account (None | str | Unset):
        region (None | str | Unset):
        term_years (int | None | Unset):
        payment_option (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PaginatedResponseOfCommitmentResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        provider=provider,
        status=status,
        type_=type_,
        service=service,
        account=account,
        region=region,
        term_years=term_years,
        payment_option=payment_option,
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
    provider: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    type_: None | str | Unset = UNSET,
    service: None | str | Unset = UNSET,
    account: None | str | Unset = UNSET,
    region: None | str | Unset = UNSET,
    term_years: int | None | Unset = UNSET,
    payment_option: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> ApiError | PaginatedResponseOfCommitmentResponse | None:
    """List commitments

     Returns the reservations, savings plans and committed use discounts held through the workspace's
    connections, narrowed to the accounts the workspace reads of each, by end date, earliest first and
    those without an end last. It holds at most 5,000: those still running, soonest end first, before
    those that have ended.

    Needs a token with `viewCosts` on the workspace.

    Args:
        workspace_id (str):
        provider (None | str | Unset):
        status (None | str | Unset):
        type_ (None | str | Unset):
        service (None | str | Unset):
        account (None | str | Unset):
        region (None | str | Unset):
        term_years (int | None | Unset):
        payment_option (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PaginatedResponseOfCommitmentResponse
    """

    return sync_detailed(
        client=client,
        workspace_id=workspace_id,
        provider=provider,
        status=status,
        type_=type_,
        service=service,
        account=account,
        region=region,
        term_years=term_years,
        payment_option=payment_option,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    workspace_id: str,
    provider: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    type_: None | str | Unset = UNSET,
    service: None | str | Unset = UNSET,
    account: None | str | Unset = UNSET,
    region: None | str | Unset = UNSET,
    term_years: int | None | Unset = UNSET,
    payment_option: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> Response[ApiError | PaginatedResponseOfCommitmentResponse]:
    """List commitments

     Returns the reservations, savings plans and committed use discounts held through the workspace's
    connections, narrowed to the accounts the workspace reads of each, by end date, earliest first and
    those without an end last. It holds at most 5,000: those still running, soonest end first, before
    those that have ended.

    Needs a token with `viewCosts` on the workspace.

    Args:
        workspace_id (str):
        provider (None | str | Unset):
        status (None | str | Unset):
        type_ (None | str | Unset):
        service (None | str | Unset):
        account (None | str | Unset):
        region (None | str | Unset):
        term_years (int | None | Unset):
        payment_option (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PaginatedResponseOfCommitmentResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        provider=provider,
        status=status,
        type_=type_,
        service=service,
        account=account,
        region=region,
        term_years=term_years,
        payment_option=payment_option,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    workspace_id: str,
    provider: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    type_: None | str | Unset = UNSET,
    service: None | str | Unset = UNSET,
    account: None | str | Unset = UNSET,
    region: None | str | Unset = UNSET,
    term_years: int | None | Unset = UNSET,
    payment_option: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> ApiError | PaginatedResponseOfCommitmentResponse | None:
    """List commitments

     Returns the reservations, savings plans and committed use discounts held through the workspace's
    connections, narrowed to the accounts the workspace reads of each, by end date, earliest first and
    those without an end last. It holds at most 5,000: those still running, soonest end first, before
    those that have ended.

    Needs a token with `viewCosts` on the workspace.

    Args:
        workspace_id (str):
        provider (None | str | Unset):
        status (None | str | Unset):
        type_ (None | str | Unset):
        service (None | str | Unset):
        account (None | str | Unset):
        region (None | str | Unset):
        term_years (int | None | Unset):
        payment_option (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PaginatedResponseOfCommitmentResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            workspace_id=workspace_id,
            provider=provider,
            status=status,
            type_=type_,
            service=service,
            account=account,
            region=region,
            term_years=term_years,
            payment_option=payment_option,
            page=page,
            limit=limit,
        )
    ).parsed
