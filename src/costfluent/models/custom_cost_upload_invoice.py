from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_cost_upload_line_placements import (
        CustomCostUploadLinePlacements,
    )
    from ..models.custom_cost_upload_vat_breakdown import CustomCostUploadVatBreakdown


T = TypeVar("T", bound="CustomCostUploadInvoice")


@_attrs_define
class CustomCostUploadInvoice:
    """
    Attributes:
        number (str):
        type_code (str):
        kind (str):
        issue_date (datetime.date):
        seller_name (str):
        currency (str):
        net_total (str):
        vat_total (str):
        gross_total (str):
        vat_breakdown (list[CustomCostUploadVatBreakdown]):
        reverse_charge (bool):
        line_count (int):
        placements (CustomCostUploadLinePlacements):
        preceding_invoice_number (None | str | Unset):
        vat_currency (None | str | Unset):
        vat_total_in_vat_currency (None | str | Unset):
    """

    number: str
    type_code: str
    kind: str
    issue_date: datetime.date
    seller_name: str
    currency: str
    net_total: str
    vat_total: str
    gross_total: str
    vat_breakdown: list[CustomCostUploadVatBreakdown]
    reverse_charge: bool
    line_count: int
    placements: CustomCostUploadLinePlacements
    preceding_invoice_number: None | str | Unset = UNSET
    vat_currency: None | str | Unset = UNSET
    vat_total_in_vat_currency: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        number = self.number

        type_code = self.type_code

        kind = self.kind

        issue_date = self.issue_date.isoformat()

        seller_name = self.seller_name

        currency = self.currency

        net_total = self.net_total

        vat_total = self.vat_total

        gross_total = self.gross_total

        vat_breakdown = []
        for vat_breakdown_item_data in self.vat_breakdown:
            vat_breakdown_item = vat_breakdown_item_data.to_dict()
            vat_breakdown.append(vat_breakdown_item)

        reverse_charge = self.reverse_charge

        line_count = self.line_count

        placements = self.placements.to_dict()

        preceding_invoice_number: None | str | Unset
        if isinstance(self.preceding_invoice_number, Unset):
            preceding_invoice_number = UNSET
        else:
            preceding_invoice_number = self.preceding_invoice_number

        vat_currency: None | str | Unset
        if isinstance(self.vat_currency, Unset):
            vat_currency = UNSET
        else:
            vat_currency = self.vat_currency

        vat_total_in_vat_currency: None | str | Unset
        if isinstance(self.vat_total_in_vat_currency, Unset):
            vat_total_in_vat_currency = UNSET
        else:
            vat_total_in_vat_currency = self.vat_total_in_vat_currency

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "number": number,
                "typeCode": type_code,
                "kind": kind,
                "issueDate": issue_date,
                "sellerName": seller_name,
                "currency": currency,
                "netTotal": net_total,
                "vatTotal": vat_total,
                "grossTotal": gross_total,
                "vatBreakdown": vat_breakdown,
                "reverseCharge": reverse_charge,
                "lineCount": line_count,
                "placements": placements,
            }
        )
        if preceding_invoice_number is not UNSET:
            field_dict["precedingInvoiceNumber"] = preceding_invoice_number
        if vat_currency is not UNSET:
            field_dict["vatCurrency"] = vat_currency
        if vat_total_in_vat_currency is not UNSET:
            field_dict["vatTotalInVatCurrency"] = vat_total_in_vat_currency

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.custom_cost_upload_line_placements import (
            CustomCostUploadLinePlacements,
        )
        from ..models.custom_cost_upload_vat_breakdown import (
            CustomCostUploadVatBreakdown,
        )

        d = dict(src_dict)
        number = d.pop("number")

        type_code = d.pop("typeCode")

        kind = d.pop("kind")

        issue_date = datetime.date.fromisoformat(d.pop("issueDate"))

        seller_name = d.pop("sellerName")

        currency = d.pop("currency")

        net_total = d.pop("netTotal")

        vat_total = d.pop("vatTotal")

        gross_total = d.pop("grossTotal")

        vat_breakdown = []
        _vat_breakdown = d.pop("vatBreakdown")
        for vat_breakdown_item_data in _vat_breakdown:
            vat_breakdown_item = CustomCostUploadVatBreakdown.from_dict(
                vat_breakdown_item_data
            )

            vat_breakdown.append(vat_breakdown_item)

        reverse_charge = d.pop("reverseCharge")

        line_count = d.pop("lineCount")

        placements = CustomCostUploadLinePlacements.from_dict(d.pop("placements"))

        def _parse_preceding_invoice_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preceding_invoice_number = _parse_preceding_invoice_number(
            d.pop("precedingInvoiceNumber", UNSET)
        )

        def _parse_vat_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vat_currency = _parse_vat_currency(d.pop("vatCurrency", UNSET))

        def _parse_vat_total_in_vat_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vat_total_in_vat_currency = _parse_vat_total_in_vat_currency(
            d.pop("vatTotalInVatCurrency", UNSET)
        )

        custom_cost_upload_invoice = cls(
            number=number,
            type_code=type_code,
            kind=kind,
            issue_date=issue_date,
            seller_name=seller_name,
            currency=currency,
            net_total=net_total,
            vat_total=vat_total,
            gross_total=gross_total,
            vat_breakdown=vat_breakdown,
            reverse_charge=reverse_charge,
            line_count=line_count,
            placements=placements,
            preceding_invoice_number=preceding_invoice_number,
            vat_currency=vat_currency,
            vat_total_in_vat_currency=vat_total_in_vat_currency,
        )

        return custom_cost_upload_invoice
