from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="BudgetPeriodResponse")


@_attrs_define
class BudgetPeriodResponse:
    """
    Attributes:
        start_date (datetime.date):
        end_date (datetime.date):
        amount (str):
    """

    start_date: datetime.date
    end_date: datetime.date
    amount: str

    def to_dict(self) -> dict[str, Any]:
        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        amount = self.amount

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "startDate": start_date,
                "endDate": end_date,
                "amount": amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        start_date = datetime.date.fromisoformat(d.pop("startDate"))

        end_date = datetime.date.fromisoformat(d.pop("endDate"))

        amount = d.pop("amount")

        budget_period_response = cls(
            start_date=start_date,
            end_date=end_date,
            amount=amount,
        )

        return budget_period_response
