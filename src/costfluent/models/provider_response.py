from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProviderResponse")


@_attrs_define
class ProviderResponse:
    """
    Attributes:
        id (str):
        type_ (str):
        key (str):
        display_name (str):
        status (str):
        sync_frequency_minutes (int):
        created_at (datetime.datetime):
        description (None | str | Unset):
        parent_provider_id (None | str | Unset):
        external_id (None | str | Unset):
        last_sync_at (datetime.datetime | None | Unset):
        last_sync_status (None | str | Unset):
        last_sync_error (None | str | Unset):
        next_sync_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    id: str
    type_: str
    key: str
    display_name: str
    status: str
    sync_frequency_minutes: int
    created_at: datetime.datetime
    description: None | str | Unset = UNSET
    parent_provider_id: None | str | Unset = UNSET
    external_id: None | str | Unset = UNSET
    last_sync_at: datetime.datetime | None | Unset = UNSET
    last_sync_status: None | str | Unset = UNSET
    last_sync_error: None | str | Unset = UNSET
    next_sync_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        key = self.key

        display_name = self.display_name

        status = self.status

        sync_frequency_minutes = self.sync_frequency_minutes

        created_at = self.created_at.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        parent_provider_id: None | str | Unset
        if isinstance(self.parent_provider_id, Unset):
            parent_provider_id = UNSET
        else:
            parent_provider_id = self.parent_provider_id

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        last_sync_at: None | str | Unset
        if isinstance(self.last_sync_at, Unset):
            last_sync_at = UNSET
        elif isinstance(self.last_sync_at, datetime.datetime):
            last_sync_at = self.last_sync_at.isoformat()
        else:
            last_sync_at = self.last_sync_at

        last_sync_status: None | str | Unset
        if isinstance(self.last_sync_status, Unset):
            last_sync_status = UNSET
        else:
            last_sync_status = self.last_sync_status

        last_sync_error: None | str | Unset
        if isinstance(self.last_sync_error, Unset):
            last_sync_error = UNSET
        else:
            last_sync_error = self.last_sync_error

        next_sync_at: None | str | Unset
        if isinstance(self.next_sync_at, Unset):
            next_sync_at = UNSET
        elif isinstance(self.next_sync_at, datetime.datetime):
            next_sync_at = self.next_sync_at.isoformat()
        else:
            next_sync_at = self.next_sync_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "type": type_,
                "key": key,
                "displayName": display_name,
                "status": status,
                "syncFrequencyMinutes": sync_frequency_minutes,
                "createdAt": created_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if parent_provider_id is not UNSET:
            field_dict["parentProviderId"] = parent_provider_id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if last_sync_at is not UNSET:
            field_dict["lastSyncAt"] = last_sync_at
        if last_sync_status is not UNSET:
            field_dict["lastSyncStatus"] = last_sync_status
        if last_sync_error is not UNSET:
            field_dict["lastSyncError"] = last_sync_error
        if next_sync_at is not UNSET:
            field_dict["nextSyncAt"] = next_sync_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = d.pop("type")

        key = d.pop("key")

        display_name = d.pop("displayName")

        status = d.pop("status")

        sync_frequency_minutes = d.pop("syncFrequencyMinutes")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_parent_provider_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_provider_id = _parse_parent_provider_id(d.pop("parentProviderId", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_last_sync_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_sync_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_sync_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_sync_at = _parse_last_sync_at(d.pop("lastSyncAt", UNSET))

        def _parse_last_sync_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_sync_status = _parse_last_sync_status(d.pop("lastSyncStatus", UNSET))

        def _parse_last_sync_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_sync_error = _parse_last_sync_error(d.pop("lastSyncError", UNSET))

        def _parse_next_sync_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_sync_at_type_0 = datetime.datetime.fromisoformat(data)

                return next_sync_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_sync_at = _parse_next_sync_at(d.pop("nextSyncAt", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))

        provider_response = cls(
            id=id,
            type_=type_,
            key=key,
            display_name=display_name,
            status=status,
            sync_frequency_minutes=sync_frequency_minutes,
            created_at=created_at,
            description=description,
            parent_provider_id=parent_provider_id,
            external_id=external_id,
            last_sync_at=last_sync_at,
            last_sync_status=last_sync_status,
            last_sync_error=last_sync_error,
            next_sync_at=next_sync_at,
            updated_at=updated_at,
        )

        return provider_response
