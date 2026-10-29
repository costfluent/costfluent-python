from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.paginated_response_of_cost_estimate_response import (
    PaginatedResponseOfCostEstimateResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    workspace_id: str,
    state: None | str | Unset = UNSET,
    repository: None | str | Unset = UNSET,
    pull_request: int | None | Unset = UNSET,
    plan: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["workspaceId"] = workspace_id

    json_state: None | str | Unset
    if isinstance(state, Unset):
        json_state = UNSET
    else:
        json_state = state
    params["state"] = json_state

    json_repository: None | str | Unset
    if isinstance(repository, Unset):
        json_repository = UNSET
    else:
        json_repository = repository
    params["repository"] = json_repository

    json_pull_request: int | None | Unset
    if isinstance(pull_request, Unset):
        json_pull_request = UNSET
    else:
        json_pull_request = pull_request
    params["pullRequest"] = json_pull_request

    json_plan: None | str | Unset
    if isinstance(plan, Unset):
        json_plan = UNSET
    else:
        json_plan = plan
    params["plan"] = json_plan

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/cost-estimates",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PaginatedResponseOfCostEstimateResponse | None:
    if response.status_code == 200:
        response_200 = PaginatedResponseOfCostEstimateResponse.from_dict(
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
) -> Response[ApiError | PaginatedResponseOfCostEstimateResponse]:
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
    state: None | str | Unset = UNSET,
    repository: None | str | Unset = UNSET,
    pull_request: int | None | Unset = UNSET,
    plan: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> Response[ApiError | PaginatedResponseOfCostEstimateResponse]:
    """List cost estimates

     Returns the workspace's estimates newest first, each with its planned and measured totals and
    without its resources.

    Needs a token with `viewCosts` on the workspace.

    Args:
        workspace_id (str):
        state (None | str | Unset):
        repository (None | str | Unset):
        pull_request (int | None | Unset):
        plan (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PaginatedResponseOfCostEstimateResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        state=state,
        repository=repository,
        pull_request=pull_request,
        plan=plan,
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
    state: None | str | Unset = UNSET,
    repository: None | str | Unset = UNSET,
    pull_request: int | None | Unset = UNSET,
    plan: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> ApiError | PaginatedResponseOfCostEstimateResponse | None:
    """List cost estimates

     Returns the workspace's estimates newest first, each with its planned and measured totals and
    without its resources.

    Needs a token with `viewCosts` on the workspace.

    Args:
        workspace_id (str):
        state (None | str | Unset):
        repository (None | str | Unset):
        pull_request (int | None | Unset):
        plan (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PaginatedResponseOfCostEstimateResponse
    """

    return sync_detailed(
        client=client,
        workspace_id=workspace_id,
        state=state,
        repository=repository,
        pull_request=pull_request,
        plan=plan,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    workspace_id: str,
    state: None | str | Unset = UNSET,
    repository: None | str | Unset = UNSET,
    pull_request: int | None | Unset = UNSET,
    plan: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> Response[ApiError | PaginatedResponseOfCostEstimateResponse]:
    """List cost estimates

     Returns the workspace's estimates newest first, each with its planned and measured totals and
    without its resources.

    Needs a token with `viewCosts` on the workspace.

    Args:
        workspace_id (str):
        state (None | str | Unset):
        repository (None | str | Unset):
        pull_request (int | None | Unset):
        plan (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PaginatedResponseOfCostEstimateResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        state=state,
        repository=repository,
        pull_request=pull_request,
        plan=plan,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    workspace_id: str,
    state: None | str | Unset = UNSET,
    repository: None | str | Unset = UNSET,
    pull_request: int | None | Unset = UNSET,
    plan: None | str | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> ApiError | PaginatedResponseOfCostEstimateResponse | None:
    """List cost estimates

     Returns the workspace's estimates newest first, each with its planned and measured totals and
    without its resources.

    Needs a token with `viewCosts` on the workspace.

    Args:
        workspace_id (str):
        state (None | str | Unset):
        repository (None | str | Unset):
        pull_request (int | None | Unset):
        plan (None | str | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PaginatedResponseOfCostEstimateResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            workspace_id=workspace_id,
            state=state,
            repository=repository,
            pull_request=pull_request,
            plan=plan,
            page=page,
            limit=limit,
        )
    ).parsed
