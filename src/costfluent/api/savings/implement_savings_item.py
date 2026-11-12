from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...types import UNSET, Response


def _get_kwargs(
    savings_item_id: str,
    *,
    workspace_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["workspaceId"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/savings-items/{savings_item_id}/implement".format(
            savings_item_id=quote(str(savings_item_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiError | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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

    if response.status_code == 409:
        response_409 = ApiError.from_dict(response.json())

        return response_409

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
) -> Response[Any | ApiError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    savings_item_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: str,
) -> Response[Any | ApiError]:
    """Mark savings finding implemented

     Records that the change an accepted finding recommends was made, which moves it to implemented.
    Changes nothing in the cloud.

    Needs a token with `respondToSavingsItem` on the workspace.

    Args:
        savings_item_id (str):
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiError]
    """

    kwargs = _get_kwargs(
        savings_item_id=savings_item_id,
        workspace_id=workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    savings_item_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: str,
) -> Any | ApiError | None:
    """Mark savings finding implemented

     Records that the change an accepted finding recommends was made, which moves it to implemented.
    Changes nothing in the cloud.

    Needs a token with `respondToSavingsItem` on the workspace.

    Args:
        savings_item_id (str):
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiError
    """

    return sync_detailed(
        savings_item_id=savings_item_id,
        client=client,
        workspace_id=workspace_id,
    ).parsed


async def asyncio_detailed(
    savings_item_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: str,
) -> Response[Any | ApiError]:
    """Mark savings finding implemented

     Records that the change an accepted finding recommends was made, which moves it to implemented.
    Changes nothing in the cloud.

    Needs a token with `respondToSavingsItem` on the workspace.

    Args:
        savings_item_id (str):
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiError]
    """

    kwargs = _get_kwargs(
        savings_item_id=savings_item_id,
        workspace_id=workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    savings_item_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: str,
) -> Any | ApiError | None:
    """Mark savings finding implemented

     Records that the change an accepted finding recommends was made, which moves it to implemented.
    Changes nothing in the cloud.

    Needs a token with `respondToSavingsItem` on the workspace.

    Args:
        savings_item_id (str):
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiError
    """

    return (
        await asyncio_detailed(
            savings_item_id=savings_item_id,
            client=client,
            workspace_id=workspace_id,
        )
    ).parsed
