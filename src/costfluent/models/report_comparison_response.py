from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.report_comparison_point_response import ReportComparisonPointResponse


T = TypeVar("T", bound="ReportComparisonResponse")


@_attrs_define
class ReportComparisonResponse:
    """
    Attributes:
        start_date (datetime.date):
        end_date (datetime.date):
        series (list[ReportComparisonPointResponse]):
    """

    start_date: datetime.date
    end_date: datetime.date
    series: list[ReportComparisonPointResponse]

    def to_dict(self) -> dict[str, Any]:
        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        series = []
        for series_item_data in self.series:
            series_item = series_item_data.to_dict()
            series.append(series_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "startDate": start_date,
                "endDate": end_date,
                "series": series,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.report_comparison_point_response import (
            ReportComparisonPointResponse,
        )

        d = dict(src_dict)
        start_date = datetime.date.fromisoformat(d.pop("startDate"))

        end_date = datetime.date.fromisoformat(d.pop("endDate"))

        series = []
        _series = d.pop("series")
        for series_item_data in _series:
            series_item = ReportComparisonPointResponse.from_dict(series_item_data)

            series.append(series_item)

        report_comparison_response = cls(
            start_date=start_date,
            end_date=end_date,
            series=series,
        )

        return report_comparison_response
