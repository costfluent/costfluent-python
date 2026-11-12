from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="UsageHistoryEntryResponse")


@_attrs_define
class UsageHistoryEntryResponse:
    """
    Attributes:
        period_start (datetime.date):
        rows_ingested (int):
        bytes_stored (int):
        tracked_spend (None | str):
    """

    period_start: datetime.date
    rows_ingested: int
    bytes_stored: int
    tracked_spend: None | str

    def to_dict(self) -> dict[str, Any]:
        period_start = self.period_start.isoformat()

        rows_ingested = self.rows_ingested

        bytes_stored = self.bytes_stored

        tracked_spend: None | str
        tracked_spend = self.tracked_spend

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "periodStart": period_start,
                "rowsIngested": rows_ingested,
                "bytesStored": bytes_stored,
                "trackedSpend": tracked_spend,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        period_start = datetime.date.fromisoformat(d.pop("periodStart"))

        rows_ingested = d.pop("rowsIngested")

        bytes_stored = d.pop("bytesStored")

        def _parse_tracked_spend(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tracked_spend = _parse_tracked_spend(d.pop("trackedSpend"))

        usage_history_entry_response = cls(
            period_start=period_start,
            rows_ingested=rows_ingested,
            bytes_stored=bytes_stored,
            tracked_spend=tracked_spend,
        )

        return usage_history_entry_response
