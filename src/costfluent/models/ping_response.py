from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PingResponse")


@_attrs_define
class PingResponse:
    """
    Attributes:
        status (str):
        timestamp (datetime.datetime):
        version (str):
    """

    status: str
    timestamp: datetime.datetime
    version: str

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        timestamp = self.timestamp.isoformat()

        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
                "timestamp": timestamp,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = d.pop("status")

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        version = d.pop("version")

        ping_response = cls(
            status=status,
            timestamp=timestamp,
            version=version,
        )

        return ping_response
