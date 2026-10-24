from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.allocation_dry_run_segment_change_response import (
        AllocationDryRunSegmentChangeResponse,
    )


T = TypeVar("T", bound="AllocationDryRunResponse")


@_attrs_define
class AllocationDryRunResponse:
    """
    Attributes:
        billing_currency (str):
        moved_cost (str):
        moved_record_count (int):
        coverage_before (float):
        coverage_after (float):
        segment_changes (list[AllocationDryRunSegmentChangeResponse]):
    """

    billing_currency: str
    moved_cost: str
    moved_record_count: int
    coverage_before: float
    coverage_after: float
    segment_changes: list[AllocationDryRunSegmentChangeResponse]

    def to_dict(self) -> dict[str, Any]:
        billing_currency = self.billing_currency

        moved_cost = self.moved_cost

        moved_record_count = self.moved_record_count

        coverage_before = self.coverage_before

        coverage_after = self.coverage_after

        segment_changes = []
        for segment_changes_item_data in self.segment_changes:
            segment_changes_item = segment_changes_item_data.to_dict()
            segment_changes.append(segment_changes_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "billingCurrency": billing_currency,
                "movedCost": moved_cost,
                "movedRecordCount": moved_record_count,
                "coverageBefore": coverage_before,
                "coverageAfter": coverage_after,
                "segmentChanges": segment_changes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.allocation_dry_run_segment_change_response import (
            AllocationDryRunSegmentChangeResponse,
        )

        d = dict(src_dict)
        billing_currency = d.pop("billingCurrency")

        moved_cost = d.pop("movedCost")

        moved_record_count = d.pop("movedRecordCount")

        coverage_before = d.pop("coverageBefore")

        coverage_after = d.pop("coverageAfter")

        segment_changes = []
        _segment_changes = d.pop("segmentChanges")
        for segment_changes_item_data in _segment_changes:
            segment_changes_item = AllocationDryRunSegmentChangeResponse.from_dict(
                segment_changes_item_data
            )

            segment_changes.append(segment_changes_item)

        allocation_dry_run_response = cls(
            billing_currency=billing_currency,
            moved_cost=moved_cost,
            moved_record_count=moved_record_count,
            coverage_before=coverage_before,
            coverage_after=coverage_after,
            segment_changes=segment_changes,
        )

        return allocation_dry_run_response
