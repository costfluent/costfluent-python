from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportBreakdownResponse")


@_attrs_define
class ReportBreakdownResponse:
    """
    Attributes:
        keys (list[str]):
        is_other (bool):
        cost (str):
        percent (float):
        currency (None | str | Unset):
        unit (None | str | Unset):
        previous_cost (None | str | Unset):
        compared_cost (None | str | Unset):
        change_percent (float | None | Unset):
    """

    keys: list[str]
    is_other: bool
    cost: str
    percent: float
    currency: None | str | Unset = UNSET
    unit: None | str | Unset = UNSET
    previous_cost: None | str | Unset = UNSET
    compared_cost: None | str | Unset = UNSET
    change_percent: float | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        keys = self.keys

        is_other = self.is_other

        cost = self.cost

        percent = self.percent

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        unit: None | str | Unset
        if isinstance(self.unit, Unset):
            unit = UNSET
        else:
            unit = self.unit

        previous_cost: None | str | Unset
        if isinstance(self.previous_cost, Unset):
            previous_cost = UNSET
        else:
            previous_cost = self.previous_cost

        compared_cost: None | str | Unset
        if isinstance(self.compared_cost, Unset):
            compared_cost = UNSET
        else:
            compared_cost = self.compared_cost

        change_percent: float | None | Unset
        if isinstance(self.change_percent, Unset):
            change_percent = UNSET
        else:
            change_percent = self.change_percent

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "keys": keys,
                "isOther": is_other,
                "cost": cost,
                "percent": percent,
            }
        )
        if currency is not UNSET:
            field_dict["currency"] = currency
        if unit is not UNSET:
            field_dict["unit"] = unit
        if previous_cost is not UNSET:
            field_dict["previousCost"] = previous_cost
        if compared_cost is not UNSET:
            field_dict["comparedCost"] = compared_cost
        if change_percent is not UNSET:
            field_dict["changePercent"] = change_percent

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        keys = cast(list[str], d.pop("keys"))

        is_other = d.pop("isOther")

        cost = d.pop("cost")

        percent = d.pop("percent")

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit = _parse_unit(d.pop("unit", UNSET))

        def _parse_previous_cost(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_cost = _parse_previous_cost(d.pop("previousCost", UNSET))

        def _parse_compared_cost(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        compared_cost = _parse_compared_cost(d.pop("comparedCost", UNSET))

        def _parse_change_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        change_percent = _parse_change_percent(d.pop("changePercent", UNSET))

        report_breakdown_response = cls(
            keys=keys,
            is_other=is_other,
            cost=cost,
            percent=percent,
            currency=currency,
            unit=unit,
            previous_cost=previous_cost,
            compared_cost=compared_cost,
            change_percent=change_percent,
        )

        return report_breakdown_response
