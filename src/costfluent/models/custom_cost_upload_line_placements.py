from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CustomCostUploadLinePlacements")


@_attrs_define
class CustomCostUploadLinePlacements:
    """
    Attributes:
        line_period (int):
        invoice_period (int):
        delivery_date (int):
        issue_date (int):
    """

    line_period: int
    invoice_period: int
    delivery_date: int
    issue_date: int

    def to_dict(self) -> dict[str, Any]:
        line_period = self.line_period

        invoice_period = self.invoice_period

        delivery_date = self.delivery_date

        issue_date = self.issue_date

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "linePeriod": line_period,
                "invoicePeriod": invoice_period,
                "deliveryDate": delivery_date,
                "issueDate": issue_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        line_period = d.pop("linePeriod")

        invoice_period = d.pop("invoicePeriod")

        delivery_date = d.pop("deliveryDate")

        issue_date = d.pop("issueDate")

        custom_cost_upload_line_placements = cls(
            line_period=line_period,
            invoice_period=invoice_period,
            delivery_date=delivery_date,
            issue_date=issue_date,
        )

        return custom_cost_upload_line_placements
