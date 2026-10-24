from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="UsageHistoryEntryResponse")


@_attrs_define
class UsageHistoryEntryResponse:
    """
    Attributes:
        period_start (datetime.date):
        tracked_spend (str):
        rows_ingested (int):
        bytes_stored (int):
    """

    period_start: datetime.date
    tracked_spend: str
    rows_ingested: int
    bytes_stored: int

    def to_dict(self) -> dict[str, Any]:
        period_start = self.period_start.isoformat()

        tracked_spend = self.tracked_spend

        rows_ingested = self.rows_ingested

        bytes_stored = self.bytes_stored

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "periodStart": period_start,
                "trackedSpend": tracked_spend,
                "rowsIngested": rows_ingested,
                "bytesStored": bytes_stored,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        period_start = datetime.date.fromisoformat(d.pop("periodStart"))

        tracked_spend = d.pop("trackedSpend")

        rows_ingested = d.pop("rowsIngested")

        bytes_stored = d.pop("bytesStored")

        usage_history_entry_response = cls(
            period_start=period_start,
            tracked_spend=tracked_spend,
            rows_ingested=rows_ingested,
            bytes_stored=bytes_stored,
        )

        return usage_history_entry_response
