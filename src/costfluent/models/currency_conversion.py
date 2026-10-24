from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CurrencyConversion")


@_attrs_define
class CurrencyConversion:
    """
    Attributes:
        source_currency (str):
        source_amount (str):
        converted_amount (str):
        method (str):
        source (str):
        description (str):
    """

    source_currency: str
    source_amount: str
    converted_amount: str
    method: str
    source: str
    description: str

    def to_dict(self) -> dict[str, Any]:
        source_currency = self.source_currency

        source_amount = self.source_amount

        converted_amount = self.converted_amount

        method = self.method

        source = self.source

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sourceCurrency": source_currency,
                "sourceAmount": source_amount,
                "convertedAmount": converted_amount,
                "method": method,
                "source": source,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        source_currency = d.pop("sourceCurrency")

        source_amount = d.pop("sourceAmount")

        converted_amount = d.pop("convertedAmount")

        method = d.pop("method")

        source = d.pop("source")

        description = d.pop("description")

        currency_conversion = cls(
            source_currency=source_currency,
            source_amount=source_amount,
            converted_amount=converted_amount,
            method=method,
            source=source,
            description=description,
        )

        return currency_conversion
