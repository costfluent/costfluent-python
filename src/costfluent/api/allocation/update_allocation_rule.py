from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.allocation_rule_response import AllocationRuleResponse
from ...models.api_error import ApiError
from ...models.update_allocation_rule_request import UpdateAllocationRuleRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    rule_id: str,
    *,
    body: UpdateAllocationRuleRequest,
    workspace_id: str,
    if_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    params: dict[str, Any] = {}

    params["workspaceId"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/allocation/rules/{rule_id}".format(
            rule_id=quote(str(rule_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AllocationRuleResponse | ApiError | None:
    if response.status_code == 200:
        response_200 = AllocationRuleResponse.from_dict(response.json())

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
) -> Response[AllocationRuleResponse | ApiError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    rule_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAllocationRuleRequest,
    workspace_id: str,
    if_match: str | Unset = UNSET,
) -> Response[AllocationRuleResponse | ApiError]:
    """Update an allocation rule

     Needs a token with `manageCostAllocation` on the workspace.

    Args:
        rule_id (str):
        workspace_id (str):
        if_match (str | Unset):
        body (UpdateAllocationRuleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AllocationRuleResponse | ApiError]
    """

    kwargs = _get_kwargs(
        rule_id=rule_id,
        body=body,
        workspace_id=workspace_id,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    rule_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAllocationRuleRequest,
    workspace_id: str,
    if_match: str | Unset = UNSET,
) -> AllocationRuleResponse | ApiError | None:
    """Update an allocation rule

     Needs a token with `manageCostAllocation` on the workspace.

    Args:
        rule_id (str):
        workspace_id (str):
        if_match (str | Unset):
        body (UpdateAllocationRuleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AllocationRuleResponse | ApiError
    """

    return sync_detailed(
        rule_id=rule_id,
        client=client,
        body=body,
        workspace_id=workspace_id,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    rule_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAllocationRuleRequest,
    workspace_id: str,
    if_match: str | Unset = UNSET,
) -> Response[AllocationRuleResponse | ApiError]:
    """Update an allocation rule

     Needs a token with `manageCostAllocation` on the workspace.

    Args:
        rule_id (str):
        workspace_id (str):
        if_match (str | Unset):
        body (UpdateAllocationRuleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AllocationRuleResponse | ApiError]
    """

    kwargs = _get_kwargs(
        rule_id=rule_id,
        body=body,
        workspace_id=workspace_id,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    rule_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAllocationRuleRequest,
    workspace_id: str,
    if_match: str | Unset = UNSET,
) -> AllocationRuleResponse | ApiError | None:
    """Update an allocation rule

     Needs a token with `manageCostAllocation` on the workspace.

    Args:
        rule_id (str):
        workspace_id (str):
        if_match (str | Unset):
        body (UpdateAllocationRuleRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AllocationRuleResponse | ApiError
    """

    return (
        await asyncio_detailed(
            rule_id=rule_id,
            client=client,
            body=body,
            workspace_id=workspace_id,
            if_match=if_match,
        )
    ).parsed
