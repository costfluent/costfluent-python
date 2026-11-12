from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProviderCostBreakdown")


@_attrs_define
class ProviderCostBreakdown:
    """
    Attributes:
        provider_id (str):
        provider_name (str):
        provider_key (str):
        cost (str):
        currency (None | str | Unset):
    """

    provider_id: str
    provider_name: str
    provider_key: str
    cost: str
    currency: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        provider_id = self.provider_id

        provider_name = self.provider_name

        provider_key = self.provider_key

        cost = self.cost

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "providerId": provider_id,
                "providerName": provider_name,
                "providerKey": provider_key,
                "cost": cost,
            }
        )
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        provider_id = d.pop("providerId")

        provider_name = d.pop("providerName")

        provider_key = d.pop("providerKey")

        cost = d.pop("cost")

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        provider_cost_breakdown = cls(
            provider_id=provider_id,
            provider_name=provider_name,
            provider_key=provider_key,
            cost=cost,
            currency=currency,
        )

        return provider_cost_breakdown
