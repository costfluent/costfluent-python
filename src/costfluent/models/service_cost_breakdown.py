from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ServiceCostBreakdown")


@_attrs_define
class ServiceCostBreakdown:
    """
    Attributes:
        service_name (str):
        cost (str):
        percentage (float):
    """

    service_name: str
    cost: str
    percentage: float

    def to_dict(self) -> dict[str, Any]:
        service_name = self.service_name

        cost = self.cost

        percentage = self.percentage

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "serviceName": service_name,
                "cost": cost,
                "percentage": percentage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        service_name = d.pop("serviceName")

        cost = d.pop("cost")

        percentage = d.pop("percentage")

        service_cost_breakdown = cls(
            service_name=service_name,
            cost=cost,
            percentage=percentage,
        )

        return service_cost_breakdown
