from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AnomalySkuContributorResponse")


@_attrs_define
class AnomalySkuContributorResponse:
    """
    Attributes:
        sku (str):
        increase (str):
    """

    sku: str
    increase: str

    def to_dict(self) -> dict[str, Any]:
        sku = self.sku

        increase = self.increase

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sku": sku,
                "increase": increase,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        sku = d.pop("sku")

        increase = d.pop("increase")

        anomaly_sku_contributor_response = cls(
            sku=sku,
            increase=increase,
        )

        return anomaly_sku_contributor_response
