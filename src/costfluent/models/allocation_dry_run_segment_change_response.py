from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AllocationDryRunSegmentChangeResponse")


@_attrs_define
class AllocationDryRunSegmentChangeResponse:
    """
    Attributes:
        name (str):
        cost_centre (str):
        allocated_before (str):
        allocated_after (str):
        delta (str):
    """

    name: str
    cost_centre: str
    allocated_before: str
    allocated_after: str
    delta: str

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        cost_centre = self.cost_centre

        allocated_before = self.allocated_before

        allocated_after = self.allocated_after

        delta = self.delta

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "costCentre": cost_centre,
                "allocatedBefore": allocated_before,
                "allocatedAfter": allocated_after,
                "delta": delta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        cost_centre = d.pop("costCentre")

        allocated_before = d.pop("allocatedBefore")

        allocated_after = d.pop("allocatedAfter")

        delta = d.pop("delta")

        allocation_dry_run_segment_change_response = cls(
            name=name,
            cost_centre=cost_centre,
            allocated_before=allocated_before,
            allocated_after=allocated_after,
            delta=delta,
        )

        return allocation_dry_run_segment_change_response
