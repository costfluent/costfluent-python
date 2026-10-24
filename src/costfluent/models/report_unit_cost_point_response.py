from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportUnitCostPointResponse")


@_attrs_define
class ReportUnitCostPointResponse:
    """
    Attributes:
        date (datetime.date):
        metric_amount (None | str | Unset):
        unit_cost (None | str | Unset):
    """

    date: datetime.date
    metric_amount: None | str | Unset = UNSET
    unit_cost: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        metric_amount: None | str | Unset
        if isinstance(self.metric_amount, Unset):
            metric_amount = UNSET
        else:
            metric_amount = self.metric_amount

        unit_cost: None | str | Unset
        if isinstance(self.unit_cost, Unset):
            unit_cost = UNSET
        else:
            unit_cost = self.unit_cost

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "date": date,
            }
        )
        if metric_amount is not UNSET:
            field_dict["metricAmount"] = metric_amount
        if unit_cost is not UNSET:
            field_dict["unitCost"] = unit_cost

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        date = datetime.date.fromisoformat(d.pop("date"))

        def _parse_metric_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metric_amount = _parse_metric_amount(d.pop("metricAmount", UNSET))

        def _parse_unit_cost(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit_cost = _parse_unit_cost(d.pop("unitCost", UNSET))

        report_unit_cost_point_response = cls(
            date=date,
            metric_amount=metric_amount,
            unit_cost=unit_cost,
        )

        return report_unit_cost_point_response
