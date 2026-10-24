from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.allocation_coverage_pool import AllocationCoveragePool
    from ..models.allocation_coverage_segment import AllocationCoverageSegment


T = TypeVar("T", bound="AllocationCoverageCurrency")


@_attrs_define
class AllocationCoverageCurrency:
    """
    Attributes:
        billing_currency (str):
        total_cost (str):
        direct_cost (str):
        shared_cost (str):
        undistributed_shared_cost (str):
        unallocated_cost (str):
        unallocated_record_count (int):
        record_count (int):
        segments (list[AllocationCoverageSegment]):
        pools (list[AllocationCoveragePool]):
        coverage (float | None | Unset):
    """

    billing_currency: str
    total_cost: str
    direct_cost: str
    shared_cost: str
    undistributed_shared_cost: str
    unallocated_cost: str
    unallocated_record_count: int
    record_count: int
    segments: list[AllocationCoverageSegment]
    pools: list[AllocationCoveragePool]
    coverage: float | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        billing_currency = self.billing_currency

        total_cost = self.total_cost

        direct_cost = self.direct_cost

        shared_cost = self.shared_cost

        undistributed_shared_cost = self.undistributed_shared_cost

        unallocated_cost = self.unallocated_cost

        unallocated_record_count = self.unallocated_record_count

        record_count = self.record_count

        segments = []
        for segments_item_data in self.segments:
            segments_item = segments_item_data.to_dict()
            segments.append(segments_item)

        pools = []
        for pools_item_data in self.pools:
            pools_item = pools_item_data.to_dict()
            pools.append(pools_item)

        coverage: float | None | Unset
        if isinstance(self.coverage, Unset):
            coverage = UNSET
        else:
            coverage = self.coverage

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "billingCurrency": billing_currency,
                "totalCost": total_cost,
                "directCost": direct_cost,
                "sharedCost": shared_cost,
                "undistributedSharedCost": undistributed_shared_cost,
                "unallocatedCost": unallocated_cost,
                "unallocatedRecordCount": unallocated_record_count,
                "recordCount": record_count,
                "segments": segments,
                "pools": pools,
            }
        )
        if coverage is not UNSET:
            field_dict["coverage"] = coverage

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.allocation_coverage_pool import AllocationCoveragePool
        from ..models.allocation_coverage_segment import AllocationCoverageSegment

        d = dict(src_dict)
        billing_currency = d.pop("billingCurrency")

        total_cost = d.pop("totalCost")

        direct_cost = d.pop("directCost")

        shared_cost = d.pop("sharedCost")

        undistributed_shared_cost = d.pop("undistributedSharedCost")

        unallocated_cost = d.pop("unallocatedCost")

        unallocated_record_count = d.pop("unallocatedRecordCount")

        record_count = d.pop("recordCount")

        segments = []
        _segments = d.pop("segments")
        for segments_item_data in _segments:
            segments_item = AllocationCoverageSegment.from_dict(segments_item_data)

            segments.append(segments_item)

        pools = []
        _pools = d.pop("pools")
        for pools_item_data in _pools:
            pools_item = AllocationCoveragePool.from_dict(pools_item_data)

            pools.append(pools_item)

        def _parse_coverage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        coverage = _parse_coverage(d.pop("coverage", UNSET))

        allocation_coverage_currency = cls(
            billing_currency=billing_currency,
            total_cost=total_cost,
            direct_cost=direct_cost,
            shared_cost=shared_cost,
            undistributed_shared_cost=undistributed_shared_cost,
            unallocated_cost=unallocated_cost,
            unallocated_record_count=unallocated_record_count,
            record_count=record_count,
            segments=segments,
            pools=pools,
            coverage=coverage,
        )

        return allocation_coverage_currency
