from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ProviderCostBreakdown")


@_attrs_define
class ProviderCostBreakdown:
    """
    Attributes:
        provider_id (str):
        provider_name (str):
        provider_key (str):
        cost (str):
    """

    provider_id: str
    provider_name: str
    provider_key: str
    cost: str

    def to_dict(self) -> dict[str, Any]:
        provider_id = self.provider_id

        provider_name = self.provider_name

        provider_key = self.provider_key

        cost = self.cost

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "providerId": provider_id,
                "providerName": provider_name,
                "providerKey": provider_key,
                "cost": cost,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        provider_id = d.pop("providerId")

        provider_name = d.pop("providerName")

        provider_key = d.pop("providerKey")

        cost = d.pop("cost")

        provider_cost_breakdown = cls(
            provider_id=provider_id,
            provider_name=provider_name,
            provider_key=provider_key,
            cost=cost,
        )

        return provider_cost_breakdown
