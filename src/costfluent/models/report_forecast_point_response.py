from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ReportForecastPointResponse")


@_attrs_define
class ReportForecastPointResponse:
    """
    Attributes:
        date (datetime.date):
        amount (str):
        lower_bound (str):
        upper_bound (str):
    """

    date: datetime.date
    amount: str
    lower_bound: str
    upper_bound: str

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        amount = self.amount

        lower_bound = self.lower_bound

        upper_bound = self.upper_bound

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "date": date,
                "amount": amount,
                "lowerBound": lower_bound,
                "upperBound": upper_bound,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        date = datetime.date.fromisoformat(d.pop("date"))

        amount = d.pop("amount")

        lower_bound = d.pop("lowerBound")

        upper_bound = d.pop("upperBound")

        report_forecast_point_response = cls(
            date=date,
            amount=amount,
            lower_bound=lower_bound,
            upper_bound=upper_bound,
        )

        return report_forecast_point_response
