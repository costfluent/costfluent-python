from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AllocationCoverageSegment")


@_attrs_define
class AllocationCoverageSegment:
    """
    Attributes:
        segment_id (str):
        name (str):
        cost_centre (str):
        direct_cost (str):
        shared_cost (str):
        allocated_cost (str):
        record_count (int):
    """

    segment_id: str
    name: str
    cost_centre: str
    direct_cost: str
    shared_cost: str
    allocated_cost: str
    record_count: int

    def to_dict(self) -> dict[str, Any]:
        segment_id = self.segment_id

        name = self.name

        cost_centre = self.cost_centre

        direct_cost = self.direct_cost

        shared_cost = self.shared_cost

        allocated_cost = self.allocated_cost

        record_count = self.record_count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "segmentId": segment_id,
                "name": name,
                "costCentre": cost_centre,
                "directCost": direct_cost,
                "sharedCost": shared_cost,
                "allocatedCost": allocated_cost,
                "recordCount": record_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        segment_id = d.pop("segmentId")

        name = d.pop("name")

        cost_centre = d.pop("costCentre")

        direct_cost = d.pop("directCost")

        shared_cost = d.pop("sharedCost")

        allocated_cost = d.pop("allocatedCost")

        record_count = d.pop("recordCount")

        allocation_coverage_segment = cls(
            segment_id=segment_id,
            name=name,
            cost_centre=cost_centre,
            direct_cost=direct_cost,
            shared_cost=shared_cost,
            allocated_cost=allocated_cost,
            record_count=record_count,
        )

        return allocation_coverage_segment
