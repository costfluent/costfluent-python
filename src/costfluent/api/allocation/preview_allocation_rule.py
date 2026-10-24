from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.allocation_dry_run_response import AllocationDryRunResponse
from ...models.api_error import ApiError
from ...models.preview_allocation_rule_request import PreviewAllocationRuleRequest
from ...types import Response


def _get_kwargs(
    *,
    body: PreviewAllocationRuleRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/allocation/rules/preview",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | list[AllocationDryRunResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AllocationDryRunResponse.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

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
) -> Response[ApiError | list[AllocationDryRunResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PreviewAllocationRuleRequest,
) -> Response[ApiError | list[AllocationDryRunResponse]]:
    """Preview an allocation rule

     Computes what the rule would move without creating it. Allocation is evaluated at query time, so
    enabling a rule restates history immediately.

    Needs a token with `viewCostAllocation` on the workspace.

    Args:
        body (PreviewAllocationRuleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | list[AllocationDryRunResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PreviewAllocationRuleRequest,
) -> ApiError | list[AllocationDryRunResponse] | None:
    """Preview an allocation rule

     Computes what the rule would move without creating it. Allocation is evaluated at query time, so
    enabling a rule restates history immediately.

    Needs a token with `viewCostAllocation` on the workspace.

    Args:
        body (PreviewAllocationRuleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | list[AllocationDryRunResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PreviewAllocationRuleRequest,
) -> Response[ApiError | list[AllocationDryRunResponse]]:
    """Preview an allocation rule

     Computes what the rule would move without creating it. Allocation is evaluated at query time, so
    enabling a rule restates history immediately.

    Needs a token with `viewCostAllocation` on the workspace.

    Args:
        body (PreviewAllocationRuleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | list[AllocationDryRunResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PreviewAllocationRuleRequest,
) -> ApiError | list[AllocationDryRunResponse] | None:
    """Preview an allocation rule

     Computes what the rule would move without creating it. Allocation is evaluated at query time, so
    enabling a rule restates history immediately.

    Needs a token with `viewCostAllocation` on the workspace.

    Args:
        body (PreviewAllocationRuleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | list[AllocationDryRunResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
