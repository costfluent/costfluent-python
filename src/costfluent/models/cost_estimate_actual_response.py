from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostEstimateActualResponse")


@_attrs_define
class CostEstimateActualResponse:
    """
    Attributes:
        monthly_cost_before (str):
        monthly_cost_after (str):
        monthly_change (str):
        monthly_variance (str):
        billing_currency (None | str | Unset):
        exchange_rate (None | str | Unset):
    """

    monthly_cost_before: str
    monthly_cost_after: str
    monthly_change: str
    monthly_variance: str
    billing_currency: None | str | Unset = UNSET
    exchange_rate: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        monthly_cost_before = self.monthly_cost_before

        monthly_cost_after = self.monthly_cost_after

        monthly_change = self.monthly_change

        monthly_variance = self.monthly_variance

        billing_currency: None | str | Unset
        if isinstance(self.billing_currency, Unset):
            billing_currency = UNSET
        else:
            billing_currency = self.billing_currency

        exchange_rate: None | str | Unset
        if isinstance(self.exchange_rate, Unset):
            exchange_rate = UNSET
        else:
            exchange_rate = self.exchange_rate

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "monthlyCostBefore": monthly_cost_before,
                "monthlyCostAfter": monthly_cost_after,
                "monthlyChange": monthly_change,
                "monthlyVariance": monthly_variance,
            }
        )
        if billing_currency is not UNSET:
            field_dict["billingCurrency"] = billing_currency
        if exchange_rate is not UNSET:
            field_dict["exchangeRate"] = exchange_rate

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        monthly_cost_before = d.pop("monthlyCostBefore")

        monthly_cost_after = d.pop("monthlyCostAfter")

        monthly_change = d.pop("monthlyChange")

        monthly_variance = d.pop("monthlyVariance")

        def _parse_billing_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        billing_currency = _parse_billing_currency(d.pop("billingCurrency", UNSET))

        def _parse_exchange_rate(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exchange_rate = _parse_exchange_rate(d.pop("exchangeRate", UNSET))

        cost_estimate_actual_response = cls(
            monthly_cost_before=monthly_cost_before,
            monthly_cost_after=monthly_cost_after,
            monthly_change=monthly_change,
            monthly_variance=monthly_variance,
            billing_currency=billing_currency,
            exchange_rate=exchange_rate,
        )

        return cost_estimate_actual_response
