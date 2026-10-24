from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report_unit_cost_point_response import ReportUnitCostPointResponse


T = TypeVar("T", bound="ReportUnitCostResponse")


@_attrs_define
class ReportUnitCostResponse:
    """
    Attributes:
        metric_id (str):
        name (str):
        unit (str):
        series (list[ReportUnitCostPointResponse]):
        currency (None | str | Unset):
        average (None | str | Unset):
    """

    metric_id: str
    name: str
    unit: str
    series: list[ReportUnitCostPointResponse]
    currency: None | str | Unset = UNSET
    average: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        metric_id = self.metric_id

        name = self.name

        unit = self.unit

        series = []
        for series_item_data in self.series:
            series_item = series_item_data.to_dict()
            series.append(series_item)

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        average: None | str | Unset
        if isinstance(self.average, Unset):
            average = UNSET
        else:
            average = self.average

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "metricId": metric_id,
                "name": name,
                "unit": unit,
                "series": series,
            }
        )
        if currency is not UNSET:
            field_dict["currency"] = currency
        if average is not UNSET:
            field_dict["average"] = average

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.report_unit_cost_point_response import ReportUnitCostPointResponse

        d = dict(src_dict)
        metric_id = d.pop("metricId")

        name = d.pop("name")

        unit = d.pop("unit")

        series = []
        _series = d.pop("series")
        for series_item_data in _series:
            series_item = ReportUnitCostPointResponse.from_dict(series_item_data)

            series.append(series_item)

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_average(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        average = _parse_average(d.pop("average", UNSET))

        report_unit_cost_response = cls(
            metric_id=metric_id,
            name=name,
            unit=unit,
            series=series,
            currency=currency,
            average=average,
        )

        return report_unit_cost_response
