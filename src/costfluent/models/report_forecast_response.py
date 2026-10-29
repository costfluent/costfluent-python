from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.report_forecast_point_response import ReportForecastPointResponse


T = TypeVar("T", bound="ReportForecastResponse")


@_attrs_define
class ReportForecastResponse:
    """
    Attributes:
        series (list[ReportForecastPointResponse]):
    """

    series: list[ReportForecastPointResponse]

    def to_dict(self) -> dict[str, Any]:
        series = []
        for series_item_data in self.series:
            series_item = series_item_data.to_dict()
            series.append(series_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "series": series,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.report_forecast_point_response import ReportForecastPointResponse

        d = dict(src_dict)
        series = []
        _series = d.pop("series")
        for series_item_data in _series:
            series_item = ReportForecastPointResponse.from_dict(series_item_data)

            series.append(series_item)

        report_forecast_response = cls(
            series=series,
        )

        return report_forecast_response
