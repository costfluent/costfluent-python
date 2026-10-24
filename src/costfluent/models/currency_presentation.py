from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.currency_amount import CurrencyAmount
    from ..models.currency_conversion import CurrencyConversion


T = TypeVar("T", bound="CurrencyPresentation")


@_attrs_define
class CurrencyPresentation:
    """
    Attributes:
        conversions (list[CurrencyConversion]):
        unconverted (list[CurrencyAmount]):
        totals_by_currency (list[CurrencyAmount]):
    """

    conversions: list[CurrencyConversion]
    unconverted: list[CurrencyAmount]
    totals_by_currency: list[CurrencyAmount]

    def to_dict(self) -> dict[str, Any]:
        conversions = []
        for conversions_item_data in self.conversions:
            conversions_item = conversions_item_data.to_dict()
            conversions.append(conversions_item)

        unconverted = []
        for unconverted_item_data in self.unconverted:
            unconverted_item = unconverted_item_data.to_dict()
            unconverted.append(unconverted_item)

        totals_by_currency = []
        for totals_by_currency_item_data in self.totals_by_currency:
            totals_by_currency_item = totals_by_currency_item_data.to_dict()
            totals_by_currency.append(totals_by_currency_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "conversions": conversions,
                "unconverted": unconverted,
                "totalsByCurrency": totals_by_currency,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.currency_amount import CurrencyAmount
        from ..models.currency_conversion import CurrencyConversion

        d = dict(src_dict)
        conversions = []
        _conversions = d.pop("conversions")
        for conversions_item_data in _conversions:
            conversions_item = CurrencyConversion.from_dict(conversions_item_data)

            conversions.append(conversions_item)

        unconverted = []
        _unconverted = d.pop("unconverted")
        for unconverted_item_data in _unconverted:
            unconverted_item = CurrencyAmount.from_dict(unconverted_item_data)

            unconverted.append(unconverted_item)

        totals_by_currency = []
        _totals_by_currency = d.pop("totalsByCurrency")
        for totals_by_currency_item_data in _totals_by_currency:
            totals_by_currency_item = CurrencyAmount.from_dict(
                totals_by_currency_item_data
            )

            totals_by_currency.append(totals_by_currency_item)

        currency_presentation = cls(
            conversions=conversions,
            unconverted=unconverted,
            totals_by_currency=totals_by_currency,
        )

        return currency_presentation
