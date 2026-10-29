from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CostEstimateTagRequest")


@_attrs_define
class CostEstimateTagRequest:
    """
    Attributes:
        key (str):
        value (str):
    """

    key: str
    value: str

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = d.pop("key")

        value = d.pop("value")

        cost_estimate_tag_request = cls(
            key=key,
            value=value,
        )

        return cost_estimate_tag_request
