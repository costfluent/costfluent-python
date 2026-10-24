from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.allocation_coverage_share import AllocationCoverageShare


T = TypeVar("T", bound="AllocationCoveragePool")


@_attrs_define
class AllocationCoveragePool:
    """
    Attributes:
        segment_id (str):
        label (str):
        method (str):
        cost (str):
        distributed_cost (str):
        residual (str):
        record_count (int):
        shares (list[AllocationCoverageShare]):
    """

    segment_id: str
    label: str
    method: str
    cost: str
    distributed_cost: str
    residual: str
    record_count: int
    shares: list[AllocationCoverageShare]

    def to_dict(self) -> dict[str, Any]:
        segment_id = self.segment_id

        label = self.label

        method = self.method

        cost = self.cost

        distributed_cost = self.distributed_cost

        residual = self.residual

        record_count = self.record_count

        shares = []
        for shares_item_data in self.shares:
            shares_item = shares_item_data.to_dict()
            shares.append(shares_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "segmentId": segment_id,
                "label": label,
                "method": method,
                "cost": cost,
                "distributedCost": distributed_cost,
                "residual": residual,
                "recordCount": record_count,
                "shares": shares,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.allocation_coverage_share import AllocationCoverageShare

        d = dict(src_dict)
        segment_id = d.pop("segmentId")

        label = d.pop("label")

        method = d.pop("method")

        cost = d.pop("cost")

        distributed_cost = d.pop("distributedCost")

        residual = d.pop("residual")

        record_count = d.pop("recordCount")

        shares = []
        _shares = d.pop("shares")
        for shares_item_data in _shares:
            shares_item = AllocationCoverageShare.from_dict(shares_item_data)

            shares.append(shares_item)

        allocation_coverage_pool = cls(
            segment_id=segment_id,
            label=label,
            method=method,
            cost=cost,
            distributed_cost=distributed_cost,
            residual=residual,
            record_count=record_count,
            shares=shares,
        )

        return allocation_coverage_pool
