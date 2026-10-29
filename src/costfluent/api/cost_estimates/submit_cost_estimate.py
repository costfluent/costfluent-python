from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.cost_estimate_receipt_response import CostEstimateReceiptResponse
from ...models.submit_cost_estimate_request import SubmitCostEstimateRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SubmitCostEstimateRequest,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/cost-estimates",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | CostEstimateReceiptResponse | None:
    if response.status_code == 200:
        response_200 = CostEstimateReceiptResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = CostEstimateReceiptResponse.from_dict(response.json())

        return response_201

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

    if response.status_code == 409:
        response_409 = ApiError.from_dict(response.json())

        return response_409

    if response.status_code == 413:
        response_413 = ApiError.from_dict(response.json())

        return response_413

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
) -> Response[ApiError | CostEstimateReceiptResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SubmitCostEstimateRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[ApiError | CostEstimateReceiptResponse]:
    """Post cost estimate

     Posts a planned change's monthly cost estimate for a pull request of a repository, or a named plan,
    as CI does on every push. The first post for a reference creates the estimate (201); a later one
    replaces it whole (200) until the change is applied, after which a post answers 409. Costfluent
    stores the figures as posted and prices nothing itself; a null monthly cost is one the estimator
    could not price, never zero. The answer names the estimate and its state only: the token CI posts
    with may hold submitCostEstimates alone and read no cost, and a token that may view costs reads the
    estimate by its id. A workspace holds at most 1,000 proposed or applied estimates. The body is at
    most 5 MiB.

    Needs a token with `submitCostEstimates` on the workspace.

    Args:
        idempotency_key (str | Unset):
        body (SubmitCostEstimateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | CostEstimateReceiptResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: SubmitCostEstimateRequest,
    idempotency_key: str | Unset = UNSET,
) -> ApiError | CostEstimateReceiptResponse | None:
    """Post cost estimate

     Posts a planned change's monthly cost estimate for a pull request of a repository, or a named plan,
    as CI does on every push. The first post for a reference creates the estimate (201); a later one
    replaces it whole (200) until the change is applied, after which a post answers 409. Costfluent
    stores the figures as posted and prices nothing itself; a null monthly cost is one the estimator
    could not price, never zero. The answer names the estimate and its state only: the token CI posts
    with may hold submitCostEstimates alone and read no cost, and a token that may view costs reads the
    estimate by its id. A workspace holds at most 1,000 proposed or applied estimates. The body is at
    most 5 MiB.

    Needs a token with `submitCostEstimates` on the workspace.

    Args:
        idempotency_key (str | Unset):
        body (SubmitCostEstimateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | CostEstimateReceiptResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SubmitCostEstimateRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[ApiError | CostEstimateReceiptResponse]:
    """Post cost estimate

     Posts a planned change's monthly cost estimate for a pull request of a repository, or a named plan,
    as CI does on every push. The first post for a reference creates the estimate (201); a later one
    replaces it whole (200) until the change is applied, after which a post answers 409. Costfluent
    stores the figures as posted and prices nothing itself; a null monthly cost is one the estimator
    could not price, never zero. The answer names the estimate and its state only: the token CI posts
    with may hold submitCostEstimates alone and read no cost, and a token that may view costs reads the
    estimate by its id. A workspace holds at most 1,000 proposed or applied estimates. The body is at
    most 5 MiB.

    Needs a token with `submitCostEstimates` on the workspace.

    Args:
        idempotency_key (str | Unset):
        body (SubmitCostEstimateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | CostEstimateReceiptResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SubmitCostEstimateRequest,
    idempotency_key: str | Unset = UNSET,
) -> ApiError | CostEstimateReceiptResponse | None:
    """Post cost estimate

     Posts a planned change's monthly cost estimate for a pull request of a repository, or a named plan,
    as CI does on every push. The first post for a reference creates the estimate (201); a later one
    replaces it whole (200) until the change is applied, after which a post answers 409. Costfluent
    stores the figures as posted and prices nothing itself; a null monthly cost is one the estimator
    could not price, never zero. The answer names the estimate and its state only: the token CI posts
    with may hold submitCostEstimates alone and read no cost, and a token that may view costs reads the
    estimate by its id. A workspace holds at most 1,000 proposed or applied estimates. The body is at
    most 5 MiB.

    Needs a token with `submitCostEstimates` on the workspace.

    Args:
        idempotency_key (str | Unset):
        body (SubmitCostEstimateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | CostEstimateReceiptResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
