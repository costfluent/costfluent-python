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
        same_period_last_year (bool):
    """

    start_date: datetime.date
    end_date: datetime.date
    series: list[ReportComparisonPointResponse]
    same_period_last_year: bool

    def to_dict(self) -> dict[str, Any]:
        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        series = []
        for series_item_data in self.series:
            series_item = series_item_data.to_dict()
            series.append(series_item)

        same_period_last_year = self.same_period_last_year

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "startDate": start_date,
                "endDate": end_date,
                "series": series,
                "samePeriodLastYear": same_period_last_year,
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

        same_period_last_year = d.pop("samePeriodLastYear")

        report_comparison_response = cls(
            start_date=start_date,
            end_date=end_date,
            series=series,
            same_period_last_year=same_period_last_year,
        )

        return report_comparison_response
