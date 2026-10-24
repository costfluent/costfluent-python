from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="BusinessMetricImportResponse")


@_attrs_define
class BusinessMetricImportResponse:
    """
    Attributes:
        created (int):
        updated (int):
        unchanged (int):
    """

    created: int
    updated: int
    unchanged: int

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        updated = self.updated

        unchanged = self.unchanged

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "created": created,
                "updated": updated,
                "unchanged": unchanged,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created = d.pop("created")

        updated = d.pop("updated")

        unchanged = d.pop("unchanged")

        business_metric_import_response = cls(
            created=created,
            updated=updated,
            unchanged=unchanged,
        )

        return business_metric_import_response
