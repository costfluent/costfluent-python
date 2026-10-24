from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="UnitCostLabelConditionResponse")


@_attrs_define
class UnitCostLabelConditionResponse:
    """
    Attributes:
        key (str):
        values (list[str]):
    """

    key: str
    values: list[str]

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        values = self.values

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = d.pop("key")

        values = cast(list[str], d.pop("values"))

        unit_cost_label_condition_response = cls(
            key=key,
            values=values,
        )

        return unit_cost_label_condition_response
