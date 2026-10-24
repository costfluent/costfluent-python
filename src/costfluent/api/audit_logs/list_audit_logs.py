import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.paginated_response_of_audit_log_entry_response import (
    PaginatedResponseOfAuditLogEntryResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    event_name: None | str | Unset = UNSET,
    object_type: None | str | Unset = UNSET,
    actor_id: None | str | Unset = UNSET,
    target_user_id: None | str | Unset = UNSET,
    from_: datetime.datetime | None | Unset = UNSET,
    to: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_event_name: None | str | Unset
    if isinstance(event_name, Unset):
        json_event_name = UNSET
    else:
        json_event_name = event_name
    params["eventName"] = json_event_name

    json_object_type: None | str | Unset
    if isinstance(object_type, Unset):
        json_object_type = UNSET
    else:
        json_object_type = object_type
    params["objectType"] = json_object_type

    json_actor_id: None | str | Unset
    if isinstance(actor_id, Unset):
        json_actor_id = UNSET
    else:
        json_actor_id = actor_id
    params["actorId"] = json_actor_id

    json_target_user_id: None | str | Unset
    if isinstance(target_user_id, Unset):
        json_target_user_id = UNSET
    else:
        json_target_user_id = target_user_id
    params["targetUserId"] = json_target_user_id

    json_from_: None | str | Unset
    if isinstance(from_, Unset):
        json_from_ = UNSET
    elif isinstance(from_, datetime.datetime):
        json_from_ = from_.isoformat()
    else:
        json_from_ = from_
    params["from"] = json_from_

    json_to: None | str | Unset
    if isinstance(to, Unset):
        json_to = UNSET
    elif isinstance(to, datetime.datetime):
        json_to = to.isoformat()
    else:
        json_to = to
    params["to"] = json_to

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/audit-logs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | PaginatedResponseOfAuditLogEntryResponse | None:
    if response.status_code == 200:
        response_200 = PaginatedResponseOfAuditLogEntryResponse.from_dict(
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
) -> Response[ApiError | PaginatedResponseOfAuditLogEntryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    event_name: None | str | Unset = UNSET,
    object_type: None | str | Unset = UNSET,
    actor_id: None | str | Unset = UNSET,
    target_user_id: None | str | Unset = UNSET,
    from_: datetime.datetime | None | Unset = UNSET,
    to: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> Response[ApiError | PaginatedResponseOfAuditLogEntryResponse]:
    """List audit log

     Returns the organization's audit log, newest first: what members, API tokens and the system changed.

    Needs an organization token with `viewAuditLog`.

    Args:
        event_name (None | str | Unset):
        object_type (None | str | Unset):
        actor_id (None | str | Unset):
        target_user_id (None | str | Unset):
        from_ (datetime.datetime | None | Unset):
        to (datetime.datetime | None | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PaginatedResponseOfAuditLogEntryResponse]
    """

    kwargs = _get_kwargs(
        event_name=event_name,
        object_type=object_type,
        actor_id=actor_id,
        target_user_id=target_user_id,
        from_=from_,
        to=to,
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
    event_name: None | str | Unset = UNSET,
    object_type: None | str | Unset = UNSET,
    actor_id: None | str | Unset = UNSET,
    target_user_id: None | str | Unset = UNSET,
    from_: datetime.datetime | None | Unset = UNSET,
    to: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> ApiError | PaginatedResponseOfAuditLogEntryResponse | None:
    """List audit log

     Returns the organization's audit log, newest first: what members, API tokens and the system changed.

    Needs an organization token with `viewAuditLog`.

    Args:
        event_name (None | str | Unset):
        object_type (None | str | Unset):
        actor_id (None | str | Unset):
        target_user_id (None | str | Unset):
        from_ (datetime.datetime | None | Unset):
        to (datetime.datetime | None | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PaginatedResponseOfAuditLogEntryResponse
    """

    return sync_detailed(
        client=client,
        event_name=event_name,
        object_type=object_type,
        actor_id=actor_id,
        target_user_id=target_user_id,
        from_=from_,
        to=to,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    event_name: None | str | Unset = UNSET,
    object_type: None | str | Unset = UNSET,
    actor_id: None | str | Unset = UNSET,
    target_user_id: None | str | Unset = UNSET,
    from_: datetime.datetime | None | Unset = UNSET,
    to: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> Response[ApiError | PaginatedResponseOfAuditLogEntryResponse]:
    """List audit log

     Returns the organization's audit log, newest first: what members, API tokens and the system changed.

    Needs an organization token with `viewAuditLog`.

    Args:
        event_name (None | str | Unset):
        object_type (None | str | Unset):
        actor_id (None | str | Unset):
        target_user_id (None | str | Unset):
        from_ (datetime.datetime | None | Unset):
        to (datetime.datetime | None | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | PaginatedResponseOfAuditLogEntryResponse]
    """

    kwargs = _get_kwargs(
        event_name=event_name,
        object_type=object_type,
        actor_id=actor_id,
        target_user_id=target_user_id,
        from_=from_,
        to=to,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    event_name: None | str | Unset = UNSET,
    object_type: None | str | Unset = UNSET,
    actor_id: None | str | Unset = UNSET,
    target_user_id: None | str | Unset = UNSET,
    from_: datetime.datetime | None | Unset = UNSET,
    to: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> ApiError | PaginatedResponseOfAuditLogEntryResponse | None:
    """List audit log

     Returns the organization's audit log, newest first: what members, API tokens and the system changed.

    Needs an organization token with `viewAuditLog`.

    Args:
        event_name (None | str | Unset):
        object_type (None | str | Unset):
        actor_id (None | str | Unset):
        target_user_id (None | str | Unset):
        from_ (datetime.datetime | None | Unset):
        to (datetime.datetime | None | Unset):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | PaginatedResponseOfAuditLogEntryResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            event_name=event_name,
            object_type=object_type,
            actor_id=actor_id,
            target_user_id=target_user_id,
            from_=from_,
            to=to,
            page=page,
            limit=limit,
        )
    ).parsed
