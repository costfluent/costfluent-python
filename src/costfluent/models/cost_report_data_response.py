from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_report_data_response_account_names_type_0 import (
        CostReportDataResponseAccountNamesType0,
    )
    from ..models.cost_report_data_response_cluster_names_type_0 import (
        CostReportDataResponseClusterNamesType0,
    )
    from ..models.cost_report_data_response_resource_names_type_0 import (
        CostReportDataResponseResourceNamesType0,
    )
    from ..models.report_breakdown_response import ReportBreakdownResponse
    from ..models.report_comparison_response import ReportComparisonResponse
    from ..models.report_forecast_response import ReportForecastResponse
    from ..models.report_summary_response import ReportSummaryResponse
    from ..models.report_time_series_response import ReportTimeSeriesResponse
    from ..models.report_unit_cost_response import ReportUnitCostResponse


T = TypeVar("T", bound="CostReportDataResponse")


@_attrs_define
class CostReportDataResponse:
    """
    Attributes:
        summary (ReportSummaryResponse):
        series (list[ReportTimeSeriesResponse]):
        breakdown (list[ReportBreakdownResponse]):
        start_date (datetime.date):
        end_date (datetime.date):
        history_floor (datetime.date | None | Unset):
        comparison (None | ReportComparisonResponse | Unset):
        comparison_history_floor (datetime.date | None | Unset):
        forecast (None | ReportForecastResponse | Unset):
        data_through (datetime.date | None | Unset):
        unit_cost (None | ReportUnitCostResponse | Unset):
        resource_names (CostReportDataResponseResourceNamesType0 | None | Unset):
        account_names (CostReportDataResponseAccountNamesType0 | None | Unset):
        cluster_names (CostReportDataResponseClusterNamesType0 | None | Unset):
    """

    summary: ReportSummaryResponse
    series: list[ReportTimeSeriesResponse]
    breakdown: list[ReportBreakdownResponse]
    start_date: datetime.date
    end_date: datetime.date
    history_floor: datetime.date | None | Unset = UNSET
    comparison: None | ReportComparisonResponse | Unset = UNSET
    comparison_history_floor: datetime.date | None | Unset = UNSET
    forecast: None | ReportForecastResponse | Unset = UNSET
    data_through: datetime.date | None | Unset = UNSET
    unit_cost: None | ReportUnitCostResponse | Unset = UNSET
    resource_names: CostReportDataResponseResourceNamesType0 | None | Unset = UNSET
    account_names: CostReportDataResponseAccountNamesType0 | None | Unset = UNSET
    cluster_names: CostReportDataResponseClusterNamesType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.cost_report_data_response_account_names_type_0 import (
            CostReportDataResponseAccountNamesType0,
        )
        from ..models.cost_report_data_response_cluster_names_type_0 import (
            CostReportDataResponseClusterNamesType0,
        )
        from ..models.cost_report_data_response_resource_names_type_0 import (
            CostReportDataResponseResourceNamesType0,
        )
        from ..models.report_comparison_response import ReportComparisonResponse
        from ..models.report_forecast_response import ReportForecastResponse
        from ..models.report_unit_cost_response import ReportUnitCostResponse

        summary = self.summary.to_dict()

        series = []
        for series_item_data in self.series:
            series_item = series_item_data.to_dict()
            series.append(series_item)

        breakdown = []
        for breakdown_item_data in self.breakdown:
            breakdown_item = breakdown_item_data.to_dict()
            breakdown.append(breakdown_item)

        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        history_floor: None | str | Unset
        if isinstance(self.history_floor, Unset):
            history_floor = UNSET
        elif isinstance(self.history_floor, datetime.date):
            history_floor = self.history_floor.isoformat()
        else:
            history_floor = self.history_floor

        comparison: dict[str, Any] | None | Unset
        if isinstance(self.comparison, Unset):
            comparison = UNSET
        elif isinstance(self.comparison, ReportComparisonResponse):
            comparison = self.comparison.to_dict()
        else:
            comparison = self.comparison

        comparison_history_floor: None | str | Unset
        if isinstance(self.comparison_history_floor, Unset):
            comparison_history_floor = UNSET
        elif isinstance(self.comparison_history_floor, datetime.date):
            comparison_history_floor = self.comparison_history_floor.isoformat()
        else:
            comparison_history_floor = self.comparison_history_floor

        forecast: dict[str, Any] | None | Unset
        if isinstance(self.forecast, Unset):
            forecast = UNSET
        elif isinstance(self.forecast, ReportForecastResponse):
            forecast = self.forecast.to_dict()
        else:
            forecast = self.forecast

        data_through: None | str | Unset
        if isinstance(self.data_through, Unset):
            data_through = UNSET
        elif isinstance(self.data_through, datetime.date):
            data_through = self.data_through.isoformat()
        else:
            data_through = self.data_through

        unit_cost: dict[str, Any] | None | Unset
        if isinstance(self.unit_cost, Unset):
            unit_cost = UNSET
        elif isinstance(self.unit_cost, ReportUnitCostResponse):
            unit_cost = self.unit_cost.to_dict()
        else:
            unit_cost = self.unit_cost

        resource_names: dict[str, Any] | None | Unset
        if isinstance(self.resource_names, Unset):
            resource_names = UNSET
        elif isinstance(self.resource_names, CostReportDataResponseResourceNamesType0):
            resource_names = self.resource_names.to_dict()
        else:
            resource_names = self.resource_names

        account_names: dict[str, Any] | None | Unset
        if isinstance(self.account_names, Unset):
            account_names = UNSET
        elif isinstance(self.account_names, CostReportDataResponseAccountNamesType0):
            account_names = self.account_names.to_dict()
        else:
            account_names = self.account_names

        cluster_names: dict[str, Any] | None | Unset
        if isinstance(self.cluster_names, Unset):
            cluster_names = UNSET
        elif isinstance(self.cluster_names, CostReportDataResponseClusterNamesType0):
            cluster_names = self.cluster_names.to_dict()
        else:
            cluster_names = self.cluster_names

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "summary": summary,
                "series": series,
                "breakdown": breakdown,
                "startDate": start_date,
                "endDate": end_date,
            }
        )
        if history_floor is not UNSET:
            field_dict["historyFloor"] = history_floor
        if comparison is not UNSET:
            field_dict["comparison"] = comparison
        if comparison_history_floor is not UNSET:
            field_dict["comparisonHistoryFloor"] = comparison_history_floor
        if forecast is not UNSET:
            field_dict["forecast"] = forecast
        if data_through is not UNSET:
            field_dict["dataThrough"] = data_through
        if unit_cost is not UNSET:
            field_dict["unitCost"] = unit_cost
        if resource_names is not UNSET:
            field_dict["resourceNames"] = resource_names
        if account_names is not UNSET:
            field_dict["accountNames"] = account_names
        if cluster_names is not UNSET:
            field_dict["clusterNames"] = cluster_names

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.cost_report_data_response_account_names_type_0 import (
            CostReportDataResponseAccountNamesType0,
        )
        from ..models.cost_report_data_response_cluster_names_type_0 import (
            CostReportDataResponseClusterNamesType0,
        )
        from ..models.cost_report_data_response_resource_names_type_0 import (
            CostReportDataResponseResourceNamesType0,
        )
        from ..models.report_breakdown_response import ReportBreakdownResponse
        from ..models.report_comparison_response import ReportComparisonResponse
        from ..models.report_forecast_response import ReportForecastResponse
        from ..models.report_summary_response import ReportSummaryResponse
        from ..models.report_time_series_response import ReportTimeSeriesResponse
        from ..models.report_unit_cost_response import ReportUnitCostResponse

        d = dict(src_dict)
        summary = ReportSummaryResponse.from_dict(d.pop("summary"))

        series = []
        _series = d.pop("series")
        for series_item_data in _series:
            series_item = ReportTimeSeriesResponse.from_dict(series_item_data)

            series.append(series_item)

        breakdown = []
        _breakdown = d.pop("breakdown")
        for breakdown_item_data in _breakdown:
            breakdown_item = ReportBreakdownResponse.from_dict(breakdown_item_data)

            breakdown.append(breakdown_item)

        start_date = datetime.date.fromisoformat(d.pop("startDate"))

        end_date = datetime.date.fromisoformat(d.pop("endDate"))

        def _parse_history_floor(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                history_floor_type_0 = datetime.date.fromisoformat(data)

                return history_floor_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        history_floor = _parse_history_floor(d.pop("historyFloor", UNSET))

        def _parse_comparison(data: object) -> None | ReportComparisonResponse | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                comparison_type_0 = ReportComparisonResponse.from_dict(data)

                return comparison_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReportComparisonResponse | Unset, data)

        comparison = _parse_comparison(d.pop("comparison", UNSET))

        def _parse_comparison_history_floor(
            data: object,
        ) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                comparison_history_floor_type_0 = datetime.date.fromisoformat(data)

                return comparison_history_floor_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        comparison_history_floor = _parse_comparison_history_floor(
            d.pop("comparisonHistoryFloor", UNSET)
        )

        def _parse_forecast(data: object) -> None | ReportForecastResponse | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                forecast_type_0 = ReportForecastResponse.from_dict(data)

                return forecast_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReportForecastResponse | Unset, data)

        forecast = _parse_forecast(d.pop("forecast", UNSET))

        def _parse_data_through(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                data_through_type_0 = datetime.date.fromisoformat(data)

                return data_through_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        data_through = _parse_data_through(d.pop("dataThrough", UNSET))

        def _parse_unit_cost(data: object) -> None | ReportUnitCostResponse | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                unit_cost_type_0 = ReportUnitCostResponse.from_dict(data)

                return unit_cost_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReportUnitCostResponse | Unset, data)

        unit_cost = _parse_unit_cost(d.pop("unitCost", UNSET))

        def _parse_resource_names(
            data: object,
        ) -> CostReportDataResponseResourceNamesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                resource_names_type_0 = (
                    CostReportDataResponseResourceNamesType0.from_dict(data)
                )

                return resource_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CostReportDataResponseResourceNamesType0 | None | Unset, data)

        resource_names = _parse_resource_names(d.pop("resourceNames", UNSET))

        def _parse_account_names(
            data: object,
        ) -> CostReportDataResponseAccountNamesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                account_names_type_0 = (
                    CostReportDataResponseAccountNamesType0.from_dict(data)
                )

                return account_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CostReportDataResponseAccountNamesType0 | None | Unset, data)

        account_names = _parse_account_names(d.pop("accountNames", UNSET))

        def _parse_cluster_names(
            data: object,
        ) -> CostReportDataResponseClusterNamesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cluster_names_type_0 = (
                    CostReportDataResponseClusterNamesType0.from_dict(data)
                )

                return cluster_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CostReportDataResponseClusterNamesType0 | None | Unset, data)

        cluster_names = _parse_cluster_names(d.pop("clusterNames", UNSET))

        cost_report_data_response = cls(
            summary=summary,
            series=series,
            breakdown=breakdown,
            start_date=start_date,
            end_date=end_date,
            history_floor=history_floor,
            comparison=comparison,
            comparison_history_floor=comparison_history_floor,
            forecast=forecast,
            data_through=data_through,
            unit_cost=unit_cost,
            resource_names=resource_names,
            account_names=account_names,
            cluster_names=cluster_names,
        )

        return cost_report_data_response
