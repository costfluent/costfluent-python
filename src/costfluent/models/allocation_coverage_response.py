from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.allocation_coverage_currency import AllocationCoverageCurrency


T = TypeVar("T", bound="AllocationCoverageResponse")


@_attrs_define
class AllocationCoverageResponse:
    """
    Attributes:
        start_date (datetime.date):
        end_date (datetime.date):
        cost_basis (str):
        currencies (list[AllocationCoverageCurrency]):
    """

    start_date: datetime.date
    end_date: datetime.date
    cost_basis: str
    currencies: list[AllocationCoverageCurrency]

    def to_dict(self) -> dict[str, Any]:
        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        cost_basis = self.cost_basis

        currencies = []
        for currencies_item_data in self.currencies:
            currencies_item = currencies_item_data.to_dict()
            currencies.append(currencies_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "startDate": start_date,
                "endDate": end_date,
                "costBasis": cost_basis,
                "currencies": currencies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.allocation_coverage_currency import AllocationCoverageCurrency

        d = dict(src_dict)
        start_date = datetime.date.fromisoformat(d.pop("startDate"))

        end_date = datetime.date.fromisoformat(d.pop("endDate"))

        cost_basis = d.pop("costBasis")

        currencies = []
        _currencies = d.pop("currencies")
        for currencies_item_data in _currencies:
            currencies_item = AllocationCoverageCurrency.from_dict(currencies_item_data)

            currencies.append(currencies_item)

        allocation_coverage_response = cls(
            start_date=start_date,
            end_date=end_date,
            cost_basis=cost_basis,
            currencies=currencies,
        )

        return allocation_coverage_response
