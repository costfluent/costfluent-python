from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CurrencyAmount")


@_attrs_define
class CurrencyAmount:
    """
    Attributes:
        currency (str):
        amount (str):
    """

    currency: str
    amount: str

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        amount = self.amount

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "currency": currency,
                "amount": amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        currency = d.pop("currency")

        amount = d.pop("amount")

        currency_amount = cls(
            currency=currency,
            amount=amount,
        )

        return currency_amount
