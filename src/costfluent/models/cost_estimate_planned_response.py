from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CostEstimatePlannedResponse")


@_attrs_define
class CostEstimatePlannedResponse:
    """
    Attributes:
        monthly_cost_before (str):
        monthly_cost_after (str):
        monthly_change (str):
        unpriced_resources (int):
    """

    monthly_cost_before: str
    monthly_cost_after: str
    monthly_change: str
    unpriced_resources: int

    def to_dict(self) -> dict[str, Any]:
        monthly_cost_before = self.monthly_cost_before

        monthly_cost_after = self.monthly_cost_after

        monthly_change = self.monthly_change

        unpriced_resources = self.unpriced_resources

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "monthlyCostBefore": monthly_cost_before,
                "monthlyCostAfter": monthly_cost_after,
                "monthlyChange": monthly_change,
                "unpricedResources": unpriced_resources,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        monthly_cost_before = d.pop("monthlyCostBefore")

        monthly_cost_after = d.pop("monthlyCostAfter")

        monthly_change = d.pop("monthlyChange")

        unpriced_resources = d.pop("unpricedResources")

        cost_estimate_planned_response = cls(
            monthly_cost_before=monthly_cost_before,
            monthly_cost_after=monthly_cost_after,
            monthly_change=monthly_change,
            unpriced_resources=unpriced_resources,
        )

        return cost_estimate_planned_response
