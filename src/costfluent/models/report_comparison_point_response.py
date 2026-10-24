from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ReportComparisonPointResponse")


@_attrs_define
class ReportComparisonPointResponse:
    """
    Attributes:
        date (datetime.date):
        previous_date (datetime.date):
        cost (str):
    """

    date: datetime.date
    previous_date: datetime.date
    cost: str

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        previous_date = self.previous_date.isoformat()

        cost = self.cost

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "date": date,
                "previousDate": previous_date,
                "cost": cost,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        date = datetime.date.fromisoformat(d.pop("date"))

        previous_date = datetime.date.fromisoformat(d.pop("previousDate"))

        cost = d.pop("cost")

        report_comparison_point_response = cls(
            date=date,
            previous_date=previous_date,
            cost=cost,
        )

        return report_comparison_point_response
