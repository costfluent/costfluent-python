from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.budget_response import BudgetResponse
from ...models.update_budget_request import UpdateBudgetRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    budget_id: str,
    *,
    body: UpdateBudgetRequest,
    if_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/budgets/{budget_id}".format(
            budget_id=quote(str(budget_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | BudgetResponse | None:
    if response.status_code == 200:
        response_200 = BudgetResponse.from_dict(response.json())

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

    if response.status_code == 408:
        response_408 = ApiError.from_dict(response.json())

        return response_408

    if response.status_code == 412:
        response_412 = ApiError.from_dict(response.json())

        return response_412

    if response.status_code == 413:
        response_413 = ApiError.from_dict(response.json())

        return response_413

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
) -> Response[ApiError | BudgetResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    budget_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBudgetRequest,
    if_match: str | Unset = UNSET,
) -> Response[ApiError | BudgetResponse]:
    """Update budget

     Updates the name, the amounts, the scope (a segment, a cost report or the whole workspace), a usage
    budget's unit, the alert thresholds or the notification channels of a budget in place; the start
    date, cadence and measure are fixed once created, and a usage budget keeps a cost report. A field
    left out keeps its value; clearSegment and clearCostReport return the budget to the whole workspace.
    Alerts replace the thresholds: one kept at the same percent and basis keeps whether it fired this
    period.

    Needs a token with `updateBudget` on the workspace.

    Args:
        budget_id (str):
        if_match (str | Unset):
        body (UpdateBudgetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | BudgetResponse]
    """

    kwargs = _get_kwargs(
        budget_id=budget_id,
        body=body,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    budget_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBudgetRequest,
    if_match: str | Unset = UNSET,
) -> ApiError | BudgetResponse | None:
    """Update budget

     Updates the name, the amounts, the scope (a segment, a cost report or the whole workspace), a usage
    budget's unit, the alert thresholds or the notification channels of a budget in place; the start
    date, cadence and measure are fixed once created, and a usage budget keeps a cost report. A field
    left out keeps its value; clearSegment and clearCostReport return the budget to the whole workspace.
    Alerts replace the thresholds: one kept at the same percent and basis keeps whether it fired this
    period.

    Needs a token with `updateBudget` on the workspace.

    Args:
        budget_id (str):
        if_match (str | Unset):
        body (UpdateBudgetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | BudgetResponse
    """

    return sync_detailed(
        budget_id=budget_id,
        client=client,
        body=body,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    budget_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBudgetRequest,
    if_match: str | Unset = UNSET,
) -> Response[ApiError | BudgetResponse]:
    """Update budget

     Updates the name, the amounts, the scope (a segment, a cost report or the whole workspace), a usage
    budget's unit, the alert thresholds or the notification channels of a budget in place; the start
    date, cadence and measure are fixed once created, and a usage budget keeps a cost report. A field
    left out keeps its value; clearSegment and clearCostReport return the budget to the whole workspace.
    Alerts replace the thresholds: one kept at the same percent and basis keeps whether it fired this
    period.

    Needs a token with `updateBudget` on the workspace.

    Args:
        budget_id (str):
        if_match (str | Unset):
        body (UpdateBudgetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | BudgetResponse]
    """

    kwargs = _get_kwargs(
        budget_id=budget_id,
        body=body,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    budget_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateBudgetRequest,
    if_match: str | Unset = UNSET,
) -> ApiError | BudgetResponse | None:
    """Update budget

     Updates the name, the amounts, the scope (a segment, a cost report or the whole workspace), a usage
    budget's unit, the alert thresholds or the notification channels of a budget in place; the start
    date, cadence and measure are fixed once created, and a usage budget keeps a cost report. A field
    left out keeps its value; clearSegment and clearCostReport return the budget to the whole workspace.
    Alerts replace the thresholds: one kept at the same percent and basis keeps whether it fired this
    period.

    Needs a token with `updateBudget` on the workspace.

    Args:
        budget_id (str):
        if_match (str | Unset):
        body (UpdateBudgetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | BudgetResponse
    """

    return (
        await asyncio_detailed(
            budget_id=budget_id,
            client=client,
            body=body,
            if_match=if_match,
        )
    ).parsed
