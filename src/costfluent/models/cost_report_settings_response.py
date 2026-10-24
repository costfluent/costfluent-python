from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unit_cost_label_condition_response import (
        UnitCostLabelConditionResponse,
    )


T = TypeVar("T", bound="CostReportSettingsResponse")


@_attrs_define
class CostReportSettingsResponse:
    """
    Attributes:
        include_credits (bool):
        include_refunds (bool):
        include_tax (bool):
        amortize (bool):
        show_forecast (bool):
        compare_to_last_period (bool):
        measure (str):
        unit_cost_label_filter (list[UnitCostLabelConditionResponse]):
        comparison_start_date (datetime.date | None | Unset):
        comparison_end_date (datetime.date | None | Unset):
        unit_cost_metric_id (None | str | Unset):
    """

    include_credits: bool
    include_refunds: bool
    include_tax: bool
    amortize: bool
    show_forecast: bool
    compare_to_last_period: bool
    measure: str
    unit_cost_label_filter: list[UnitCostLabelConditionResponse]
    comparison_start_date: datetime.date | None | Unset = UNSET
    comparison_end_date: datetime.date | None | Unset = UNSET
    unit_cost_metric_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        include_credits = self.include_credits

        include_refunds = self.include_refunds

        include_tax = self.include_tax

        amortize = self.amortize

        show_forecast = self.show_forecast

        compare_to_last_period = self.compare_to_last_period

        measure = self.measure

        unit_cost_label_filter = []
        for unit_cost_label_filter_item_data in self.unit_cost_label_filter:
            unit_cost_label_filter_item = unit_cost_label_filter_item_data.to_dict()
            unit_cost_label_filter.append(unit_cost_label_filter_item)

        comparison_start_date: None | str | Unset
        if isinstance(self.comparison_start_date, Unset):
            comparison_start_date = UNSET
        elif isinstance(self.comparison_start_date, datetime.date):
            comparison_start_date = self.comparison_start_date.isoformat()
        else:
            comparison_start_date = self.comparison_start_date

        comparison_end_date: None | str | Unset
        if isinstance(self.comparison_end_date, Unset):
            comparison_end_date = UNSET
        elif isinstance(self.comparison_end_date, datetime.date):
            comparison_end_date = self.comparison_end_date.isoformat()
        else:
            comparison_end_date = self.comparison_end_date

        unit_cost_metric_id: None | str | Unset
        if isinstance(self.unit_cost_metric_id, Unset):
            unit_cost_metric_id = UNSET
        else:
            unit_cost_metric_id = self.unit_cost_metric_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "includeCredits": include_credits,
                "includeRefunds": include_refunds,
                "includeTax": include_tax,
                "amortize": amortize,
                "showForecast": show_forecast,
                "compareToLastPeriod": compare_to_last_period,
                "measure": measure,
                "unitCostLabelFilter": unit_cost_label_filter,
            }
        )
        if comparison_start_date is not UNSET:
            field_dict["comparisonStartDate"] = comparison_start_date
        if comparison_end_date is not UNSET:
            field_dict["comparisonEndDate"] = comparison_end_date
        if unit_cost_metric_id is not UNSET:
            field_dict["unitCostMetricId"] = unit_cost_metric_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.unit_cost_label_condition_response import (
            UnitCostLabelConditionResponse,
        )

        d = dict(src_dict)
        include_credits = d.pop("includeCredits")

        include_refunds = d.pop("includeRefunds")

        include_tax = d.pop("includeTax")

        amortize = d.pop("amortize")

        show_forecast = d.pop("showForecast")

        compare_to_last_period = d.pop("compareToLastPeriod")

        measure = d.pop("measure")

        unit_cost_label_filter = []
        _unit_cost_label_filter = d.pop("unitCostLabelFilter")
        for unit_cost_label_filter_item_data in _unit_cost_label_filter:
            unit_cost_label_filter_item = UnitCostLabelConditionResponse.from_dict(
                unit_cost_label_filter_item_data
            )

            unit_cost_label_filter.append(unit_cost_label_filter_item)

        def _parse_comparison_start_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                comparison_start_date_type_0 = datetime.date.fromisoformat(data)

                return comparison_start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        comparison_start_date = _parse_comparison_start_date(
            d.pop("comparisonStartDate", UNSET)
        )

        def _parse_comparison_end_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                comparison_end_date_type_0 = datetime.date.fromisoformat(data)

                return comparison_end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        comparison_end_date = _parse_comparison_end_date(
            d.pop("comparisonEndDate", UNSET)
        )

        def _parse_unit_cost_metric_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit_cost_metric_id = _parse_unit_cost_metric_id(
            d.pop("unitCostMetricId", UNSET)
        )

        cost_report_settings_response = cls(
            include_credits=include_credits,
            include_refunds=include_refunds,
            include_tax=include_tax,
            amortize=amortize,
            show_forecast=show_forecast,
            compare_to_last_period=compare_to_last_period,
            measure=measure,
            unit_cost_label_filter=unit_cost_label_filter,
            comparison_start_date=comparison_start_date,
            comparison_end_date=comparison_end_date,
            unit_cost_metric_id=unit_cost_metric_id,
        )

        return cost_report_settings_response
