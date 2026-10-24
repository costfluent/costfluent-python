from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ForecastMonthResponse")


@_attrs_define
class ForecastMonthResponse:
    """
    Attributes:
        month (str):
        amount (str):
        lower_bound (str):
        upper_bound (str):
    """

    month: str
    amount: str
    lower_bound: str
    upper_bound: str

    def to_dict(self) -> dict[str, Any]:
        month = self.month

        amount = self.amount

        lower_bound = self.lower_bound

        upper_bound = self.upper_bound

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "month": month,
                "amount": amount,
                "lowerBound": lower_bound,
                "upperBound": upper_bound,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        month = d.pop("month")

        amount = d.pop("amount")

        lower_bound = d.pop("lowerBound")

        upper_bound = d.pop("upperBound")

        forecast_month_response = cls(
            month=month,
            amount=amount,
            lower_bound=lower_bound,
            upper_bound=upper_bound,
        )

        return forecast_month_response
