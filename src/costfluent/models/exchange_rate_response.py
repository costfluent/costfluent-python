from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ExchangeRateResponse")


@_attrs_define
class ExchangeRateResponse:
    """
    Attributes:
        base_currency (str):
        target_currency (str):
        rate (float):
        effective_date (datetime.date):
        source (str):
    """

    base_currency: str
    target_currency: str
    rate: float
    effective_date: datetime.date
    source: str

    def to_dict(self) -> dict[str, Any]:
        base_currency = self.base_currency

        target_currency = self.target_currency

        rate = self.rate

        effective_date = self.effective_date.isoformat()

        source = self.source

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "baseCurrency": base_currency,
                "targetCurrency": target_currency,
                "rate": rate,
                "effectiveDate": effective_date,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        base_currency = d.pop("baseCurrency")

        target_currency = d.pop("targetCurrency")

        rate = d.pop("rate")

        effective_date = datetime.date.fromisoformat(d.pop("effectiveDate"))

        source = d.pop("source")

        exchange_rate_response = cls(
            base_currency=base_currency,
            target_currency=target_currency,
            rate=rate,
            effective_date=effective_date,
            source=source,
        )

        return exchange_rate_response
