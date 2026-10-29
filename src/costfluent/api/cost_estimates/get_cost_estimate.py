from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.cost_estimate_response import CostEstimateResponse
from ...types import Response


def _get_kwargs(
    estimate_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/cost-estimates/{estimate_id}".format(
            estimate_id=quote(str(estimate_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | CostEstimateResponse | None:
    if response.status_code == 200:
        response_200 = CostEstimateResponse.from_dict(response.json())

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
) -> Response[ApiError | CostEstimateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    estimate_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | CostEstimateResponse]:
    """Get cost estimate

     Returns one estimate with each resource's planned and, once reconciled, measured monthly cost and
    whether the reconciliation found it.

    Needs a token with `viewCosts` on the workspace.

    Args:
        estimate_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | CostEstimateResponse]
    """

    kwargs = _get_kwargs(
        estimate_id=estimate_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    estimate_id: str,
    *,
    client: AuthenticatedClient,
) -> ApiError | CostEstimateResponse | None:
    """Get cost estimate

     Returns one estimate with each resource's planned and, once reconciled, measured monthly cost and
    whether the reconciliation found it.

    Needs a token with `viewCosts` on the workspace.

    Args:
        estimate_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | CostEstimateResponse
    """

    return sync_detailed(
        estimate_id=estimate_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    estimate_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiError | CostEstimateResponse]:
    """Get cost estimate

     Returns one estimate with each resource's planned and, once reconciled, measured monthly cost and
    whether the reconciliation found it.

    Needs a token with `viewCosts` on the workspace.

    Args:
        estimate_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | CostEstimateResponse]
    """

    kwargs = _get_kwargs(
        estimate_id=estimate_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    estimate_id: str,
    *,
    client: AuthenticatedClient,
) -> ApiError | CostEstimateResponse | None:
    """Get cost estimate

     Returns one estimate with each resource's planned and, once reconciled, measured monthly cost and
    whether the reconciliation found it.

    Needs a token with `viewCosts` on the workspace.

    Args:
        estimate_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | CostEstimateResponse
    """

    return (
        await asyncio_detailed(
            estimate_id=estimate_id,
            client=client,
        )
    ).parsed
