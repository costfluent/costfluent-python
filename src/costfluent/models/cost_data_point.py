from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_data_point_dimensions import CostDataPointDimensions


T = TypeVar("T", bound="CostDataPoint")


@_attrs_define
class CostDataPoint:
    """
    Attributes:
        date (datetime.date):
        cost (str):
        list_cost (str):
        amortized_cost (str):
        currency (str):
        dimensions (CostDataPointDimensions):
        quantity (float | None | Unset):
        unit (None | str | Unset):
    """

    date: datetime.date
    cost: str
    list_cost: str
    amortized_cost: str
    currency: str
    dimensions: CostDataPointDimensions
    quantity: float | None | Unset = UNSET
    unit: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        cost = self.cost

        list_cost = self.list_cost

        amortized_cost = self.amortized_cost

        currency = self.currency

        dimensions = self.dimensions.to_dict()

        quantity: float | None | Unset
        if isinstance(self.quantity, Unset):
            quantity = UNSET
        else:
            quantity = self.quantity

        unit: None | str | Unset
        if isinstance(self.unit, Unset):
            unit = UNSET
        else:
            unit = self.unit

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "date": date,
                "cost": cost,
                "listCost": list_cost,
                "amortizedCost": amortized_cost,
                "currency": currency,
                "dimensions": dimensions,
            }
        )
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.cost_data_point_dimensions import CostDataPointDimensions

        d = dict(src_dict)
        date = datetime.date.fromisoformat(d.pop("date"))

        cost = d.pop("cost")

        list_cost = d.pop("listCost")

        amortized_cost = d.pop("amortizedCost")

        currency = d.pop("currency")

        dimensions = CostDataPointDimensions.from_dict(d.pop("dimensions"))

        def _parse_quantity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        quantity = _parse_quantity(d.pop("quantity", UNSET))

        def _parse_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit = _parse_unit(d.pop("unit", UNSET))

        cost_data_point = cls(
            date=date,
            cost=cost,
            list_cost=list_cost,
            amortized_cost=amortized_cost,
            currency=currency,
            dimensions=dimensions,
            quantity=quantity,
            unit=unit,
        )

        return cost_data_point
