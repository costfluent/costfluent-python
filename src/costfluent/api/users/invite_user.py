from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.invite_user_request import InviteUserRequest
from ...models.user_invited_response import UserInvitedResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: InviteUserRequest,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/users",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | UserInvitedResponse | None:
    if response.status_code == 201:
        response_201 = UserInvitedResponse.from_dict(response.json())

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
) -> Response[ApiError | UserInvitedResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: InviteUserRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[ApiError | UserInvitedResponse]:
    """Invite user

     Invites a person to the organization by email as a viewer, editor or integration owner; the
    invitation stands for seven days. Owner is granted in the product, not by invitation. A person who
    is already a member, or suspended, is a conflict. An organization sends at most 100 invitations in
    24 hours, and one address at most 3; past either the call is refused with 429 and Retry-After.

    Needs an organization token with `inviteUser`.

    Args:
        idempotency_key (str | Unset):
        body (InviteUserRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | UserInvitedResponse]
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
    body: InviteUserRequest,
    idempotency_key: str | Unset = UNSET,
) -> ApiError | UserInvitedResponse | None:
    """Invite user

     Invites a person to the organization by email as a viewer, editor or integration owner; the
    invitation stands for seven days. Owner is granted in the product, not by invitation. A person who
    is already a member, or suspended, is a conflict. An organization sends at most 100 invitations in
    24 hours, and one address at most 3; past either the call is refused with 429 and Retry-After.

    Needs an organization token with `inviteUser`.

    Args:
        idempotency_key (str | Unset):
        body (InviteUserRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | UserInvitedResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: InviteUserRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[ApiError | UserInvitedResponse]:
    """Invite user

     Invites a person to the organization by email as a viewer, editor or integration owner; the
    invitation stands for seven days. Owner is granted in the product, not by invitation. A person who
    is already a member, or suspended, is a conflict. An organization sends at most 100 invitations in
    24 hours, and one address at most 3; past either the call is refused with 429 and Retry-After.

    Needs an organization token with `inviteUser`.

    Args:
        idempotency_key (str | Unset):
        body (InviteUserRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | UserInvitedResponse]
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
    body: InviteUserRequest,
    idempotency_key: str | Unset = UNSET,
) -> ApiError | UserInvitedResponse | None:
    """Invite user

     Invites a person to the organization by email as a viewer, editor or integration owner; the
    invitation stands for seven days. Owner is granted in the product, not by invitation. A person who
    is already a member, or suspended, is a conflict. An organization sends at most 100 invitations in
    24 hours, and one address at most 3; past either the call is refused with 429 and Retry-After.

    Needs an organization token with `inviteUser`.

    Args:
        idempotency_key (str | Unset):
        body (InviteUserRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | UserInvitedResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
