from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportGroupResponse")


@_attrs_define
class ReportGroupResponse:
    """
    Attributes:
        keys (list[str]):
        is_other (bool):
        cost (str):
        currency (None | str | Unset):
        unit (None | str | Unset):
    """

    keys: list[str]
    is_other: bool
    cost: str
    currency: None | str | Unset = UNSET
    unit: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        keys = self.keys

        is_other = self.is_other

        cost = self.cost

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

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "keys": keys,
                "isOther": is_other,
                "cost": cost,
            }
        )
        if currency is not UNSET:
            field_dict["currency"] = currency
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        keys = cast(list[str], d.pop("keys"))

        is_other = d.pop("isOther")

        cost = d.pop("cost")

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

        report_group_response = cls(
            keys=keys,
            is_other=is_other,
            cost=cost,
            currency=currency,
            unit=unit,
        )

        return report_group_response
