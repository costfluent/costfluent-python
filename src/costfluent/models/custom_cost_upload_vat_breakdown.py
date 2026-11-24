from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomCostUploadVatBreakdown")


@_attrs_define
class CustomCostUploadVatBreakdown:
    """
    Attributes:
        category_code (str):
        taxable_amount (str):
        tax_amount (str):
        rate (None | str | Unset):
        exemption_reason_code (None | str | Unset):
    """

    category_code: str
    taxable_amount: str
    tax_amount: str
    rate: None | str | Unset = UNSET
    exemption_reason_code: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        category_code = self.category_code

        taxable_amount = self.taxable_amount

        tax_amount = self.tax_amount

        rate: None | str | Unset
        if isinstance(self.rate, Unset):
            rate = UNSET
        else:
            rate = self.rate

        exemption_reason_code: None | str | Unset
        if isinstance(self.exemption_reason_code, Unset):
            exemption_reason_code = UNSET
        else:
            exemption_reason_code = self.exemption_reason_code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "categoryCode": category_code,
                "taxableAmount": taxable_amount,
                "taxAmount": tax_amount,
            }
        )
        if rate is not UNSET:
            field_dict["rate"] = rate
        if exemption_reason_code is not UNSET:
            field_dict["exemptionReasonCode"] = exemption_reason_code

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        category_code = d.pop("categoryCode")

        taxable_amount = d.pop("taxableAmount")

        tax_amount = d.pop("taxAmount")

        def _parse_rate(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rate = _parse_rate(d.pop("rate", UNSET))

        def _parse_exemption_reason_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exemption_reason_code = _parse_exemption_reason_code(
            d.pop("exemptionReasonCode", UNSET)
        )

        custom_cost_upload_vat_breakdown = cls(
            category_code=category_code,
            taxable_amount=taxable_amount,
            tax_amount=tax_amount,
            rate=rate,
            exemption_reason_code=exemption_reason_code,
        )

        return custom_cost_upload_vat_breakdown
