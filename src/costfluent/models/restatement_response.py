from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="RestatementResponse")


@_attrs_define
class RestatementResponse:
    """
    Attributes:
        last_committed_at (datetime.datetime):
        records (int):
    """

    last_committed_at: datetime.datetime
    records: int

    def to_dict(self) -> dict[str, Any]:
        last_committed_at = self.last_committed_at.isoformat()

        records = self.records

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "lastCommittedAt": last_committed_at,
                "records": records,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        last_committed_at = datetime.datetime.fromisoformat(d.pop("lastCommittedAt"))

        records = d.pop("records")

        restatement_response = cls(
            last_committed_at=last_committed_at,
            records=records,
        )

        return restatement_response
