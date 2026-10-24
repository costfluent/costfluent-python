from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.budget_response import BudgetResponse
from ...types import Response


def _get_kwargs(
    budget_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/budgets/{budget_id}".format(
            budget_id=quote(str(budget_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | BudgetResponse | None:
    if response.status_code == 200:
        response_200 = BudgetResponse.from_dict(response.json())

        return response_200

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
) -> Response[ApiError | BudgetResponse]:
    """Get budget

     Returns a specific budget with current spend.

    Needs a token with `viewBudgets` on the workspace.

    Args:
        budget_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | BudgetResponse]
    """

    kwargs = _get_kwargs(
        budget_id=budget_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    budget_id: str,
    *,
    client: AuthenticatedClient,
) -> ApiError | BudgetResponse | None:
    """Get budget

     Returns a specific budget with current spend.

    Needs a token with `viewBudgets` on the workspace.

    Args:
        budget_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | BudgetResponse
    """

    return sync_detailed(
        budget_id=budget_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    budget_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | BudgetResponse]:
    """Get budget

     Returns a specific budget with current spend.

    Needs a token with `viewBudgets` on the workspace.

    Args:
        budget_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | BudgetResponse]
    """

    kwargs = _get_kwargs(
        budget_id=budget_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    budget_id: str,
    *,
    client: AuthenticatedClient,
) -> ApiError | BudgetResponse | None:
    """Get budget

     Returns a specific budget with current spend.

    Needs a token with `viewBudgets` on the workspace.

    Args:
        budget_id (str):

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
        )
    ).parsed
