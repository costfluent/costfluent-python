from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="UnitQuantity")


@_attrs_define
class UnitQuantity:
    """
    Attributes:
        unit (str):
        quantity (float):
    """

    unit: str
    quantity: float

    def to_dict(self) -> dict[str, Any]:
        unit = self.unit

        quantity = self.quantity

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "unit": unit,
                "quantity": quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        unit = d.pop("unit")

        quantity = d.pop("quantity")

        unit_quantity = cls(
            unit=unit,
            quantity=quantity,
        )

        return unit_quantity
