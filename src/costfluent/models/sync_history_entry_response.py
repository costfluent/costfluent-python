from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SyncHistoryEntryResponse")


@_attrs_define
class SyncHistoryEntryResponse:
    """
    Attributes:
        started_at (datetime.datetime):
        status (str):
        quarantined_count (int):
        completed_at (datetime.datetime | None | Unset):
        records_ingested (int | None | Unset):
        error_message (None | str | Unset):
    """

    started_at: datetime.datetime
    status: str
    quarantined_count: int
    completed_at: datetime.datetime | None | Unset = UNSET
    records_ingested: int | None | Unset = UNSET
    error_message: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        started_at = self.started_at.isoformat()

        status = self.status

        quarantined_count = self.quarantined_count

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        records_ingested: int | None | Unset
        if isinstance(self.records_ingested, Unset):
            records_ingested = UNSET
        else:
            records_ingested = self.records_ingested

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "startedAt": started_at,
                "status": status,
                "quarantinedCount": quarantined_count,
            }
        )
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if records_ingested is not UNSET:
            field_dict["recordsIngested"] = records_ingested
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        started_at = datetime.datetime.fromisoformat(d.pop("startedAt"))

        status = d.pop("status")

        quarantined_count = d.pop("quarantinedCount")

        def _parse_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = datetime.datetime.fromisoformat(data)

                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_at = _parse_completed_at(d.pop("completedAt", UNSET))

        def _parse_records_ingested(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        records_ingested = _parse_records_ingested(d.pop("recordsIngested", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("errorMessage", UNSET))

        sync_history_entry_response = cls(
            started_at=started_at,
            status=status,
            quarantined_count=quarantined_count,
            completed_at=completed_at,
            records_ingested=records_ingested,
            error_message=error_message,
        )

        return sync_history_entry_response
