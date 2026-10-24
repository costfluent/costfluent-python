from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogEntryResponse")


@_attrs_define
class AuditLogEntryResponse:
    """
    Attributes:
        id (str):
        event_name (str):
        created_at (datetime.datetime):
        object_type (None | str | Unset):
        actor_id (None | str | Unset):
        actor_name (None | str | Unset):
        target_user_id (None | str | Unset):
        managed_by (None | str | Unset):
        managed_organization (None | str | Unset):
        ip_address (None | str | Unset):
        user_agent (None | str | Unset):
        metadata (Any | Unset):
    """

    id: str
    event_name: str
    created_at: datetime.datetime
    object_type: None | str | Unset = UNSET
    actor_id: None | str | Unset = UNSET
    actor_name: None | str | Unset = UNSET
    target_user_id: None | str | Unset = UNSET
    managed_by: None | str | Unset = UNSET
    managed_organization: None | str | Unset = UNSET
    ip_address: None | str | Unset = UNSET
    user_agent: None | str | Unset = UNSET
    metadata: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        event_name = self.event_name

        created_at = self.created_at.isoformat()

        object_type: None | str | Unset
        if isinstance(self.object_type, Unset):
            object_type = UNSET
        else:
            object_type = self.object_type

        actor_id: None | str | Unset
        if isinstance(self.actor_id, Unset):
            actor_id = UNSET
        else:
            actor_id = self.actor_id

        actor_name: None | str | Unset
        if isinstance(self.actor_name, Unset):
            actor_name = UNSET
        else:
            actor_name = self.actor_name

        target_user_id: None | str | Unset
        if isinstance(self.target_user_id, Unset):
            target_user_id = UNSET
        else:
            target_user_id = self.target_user_id

        managed_by: None | str | Unset
        if isinstance(self.managed_by, Unset):
            managed_by = UNSET
        else:
            managed_by = self.managed_by

        managed_organization: None | str | Unset
        if isinstance(self.managed_organization, Unset):
            managed_organization = UNSET
        else:
            managed_organization = self.managed_organization

        ip_address: None | str | Unset
        if isinstance(self.ip_address, Unset):
            ip_address = UNSET
        else:
            ip_address = self.ip_address

        user_agent: None | str | Unset
        if isinstance(self.user_agent, Unset):
            user_agent = UNSET
        else:
            user_agent = self.user_agent

        metadata = self.metadata

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "eventName": event_name,
                "createdAt": created_at,
            }
        )
        if object_type is not UNSET:
            field_dict["objectType"] = object_type
        if actor_id is not UNSET:
            field_dict["actorId"] = actor_id
        if actor_name is not UNSET:
            field_dict["actorName"] = actor_name
        if target_user_id is not UNSET:
            field_dict["targetUserId"] = target_user_id
        if managed_by is not UNSET:
            field_dict["managedBy"] = managed_by
        if managed_organization is not UNSET:
            field_dict["managedOrganization"] = managed_organization
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if user_agent is not UNSET:
            field_dict["userAgent"] = user_agent
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        event_name = d.pop("eventName")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        def _parse_object_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_type = _parse_object_type(d.pop("objectType", UNSET))

        def _parse_actor_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        actor_id = _parse_actor_id(d.pop("actorId", UNSET))

        def _parse_actor_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        actor_name = _parse_actor_name(d.pop("actorName", UNSET))

        def _parse_target_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_user_id = _parse_target_user_id(d.pop("targetUserId", UNSET))

        def _parse_managed_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        managed_by = _parse_managed_by(d.pop("managedBy", UNSET))

        def _parse_managed_organization(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        managed_organization = _parse_managed_organization(
            d.pop("managedOrganization", UNSET)
        )

        def _parse_ip_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip_address = _parse_ip_address(d.pop("ipAddress", UNSET))

        def _parse_user_agent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_agent = _parse_user_agent(d.pop("userAgent", UNSET))

        metadata = d.pop("metadata", UNSET)

        audit_log_entry_response = cls(
            id=id,
            event_name=event_name,
            created_at=created_at,
            object_type=object_type,
            actor_id=actor_id,
            actor_name=actor_name,
            target_user_id=target_user_id,
            managed_by=managed_by,
            managed_organization=managed_organization,
            ip_address=ip_address,
            user_agent=user_agent,
            metadata=metadata,
        )

        return audit_log_entry_response
