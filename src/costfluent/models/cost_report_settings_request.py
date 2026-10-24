from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unit_cost_label_condition_request import UnitCostLabelConditionRequest


T = TypeVar("T", bound="CostReportSettingsRequest")


@_attrs_define
class CostReportSettingsRequest:
    """
    Attributes:
        include_credits (bool | None | Unset):
        include_refunds (bool | None | Unset):
        include_tax (bool | None | Unset):
        amortize (bool | None | Unset):
        show_forecast (bool | None | Unset):
        compare_to_last_period (bool | None | Unset):
        comparison_start_date (datetime.date | None | Unset):
        comparison_end_date (datetime.date | None | Unset):
        measure (None | str | Unset):
        unit_cost_metric_id (None | str | Unset):
        unit_cost_label_filter (list[UnitCostLabelConditionRequest] | None | Unset):
    """

    include_credits: bool | None | Unset = UNSET
    include_refunds: bool | None | Unset = UNSET
    include_tax: bool | None | Unset = UNSET
    amortize: bool | None | Unset = UNSET
    show_forecast: bool | None | Unset = UNSET
    compare_to_last_period: bool | None | Unset = UNSET
    comparison_start_date: datetime.date | None | Unset = UNSET
    comparison_end_date: datetime.date | None | Unset = UNSET
    measure: None | str | Unset = UNSET
    unit_cost_metric_id: None | str | Unset = UNSET
    unit_cost_label_filter: list[UnitCostLabelConditionRequest] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        include_credits: bool | None | Unset
        if isinstance(self.include_credits, Unset):
            include_credits = UNSET
        else:
            include_credits = self.include_credits

        include_refunds: bool | None | Unset
        if isinstance(self.include_refunds, Unset):
            include_refunds = UNSET
        else:
            include_refunds = self.include_refunds

        include_tax: bool | None | Unset
        if isinstance(self.include_tax, Unset):
            include_tax = UNSET
        else:
            include_tax = self.include_tax

        amortize: bool | None | Unset
        if isinstance(self.amortize, Unset):
            amortize = UNSET
        else:
            amortize = self.amortize

        show_forecast: bool | None | Unset
        if isinstance(self.show_forecast, Unset):
            show_forecast = UNSET
        else:
            show_forecast = self.show_forecast

        compare_to_last_period: bool | None | Unset
        if isinstance(self.compare_to_last_period, Unset):
            compare_to_last_period = UNSET
        else:
            compare_to_last_period = self.compare_to_last_period

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

        measure: None | str | Unset
        if isinstance(self.measure, Unset):
            measure = UNSET
        else:
            measure = self.measure

        unit_cost_metric_id: None | str | Unset
        if isinstance(self.unit_cost_metric_id, Unset):
            unit_cost_metric_id = UNSET
        else:
            unit_cost_metric_id = self.unit_cost_metric_id

        unit_cost_label_filter: list[dict[str, Any]] | None | Unset
        if isinstance(self.unit_cost_label_filter, Unset):
            unit_cost_label_filter = UNSET
        elif isinstance(self.unit_cost_label_filter, list):
            unit_cost_label_filter = []
            for unit_cost_label_filter_type_0_item_data in self.unit_cost_label_filter:
                unit_cost_label_filter_type_0_item = (
                    unit_cost_label_filter_type_0_item_data.to_dict()
                )
                unit_cost_label_filter.append(unit_cost_label_filter_type_0_item)

        else:
            unit_cost_label_filter = self.unit_cost_label_filter

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if include_credits is not UNSET:
            field_dict["includeCredits"] = include_credits
        if include_refunds is not UNSET:
            field_dict["includeRefunds"] = include_refunds
        if include_tax is not UNSET:
            field_dict["includeTax"] = include_tax
        if amortize is not UNSET:
            field_dict["amortize"] = amortize
        if show_forecast is not UNSET:
            field_dict["showForecast"] = show_forecast
        if compare_to_last_period is not UNSET:
            field_dict["compareToLastPeriod"] = compare_to_last_period
        if comparison_start_date is not UNSET:
            field_dict["comparisonStartDate"] = comparison_start_date
        if comparison_end_date is not UNSET:
            field_dict["comparisonEndDate"] = comparison_end_date
        if measure is not UNSET:
            field_dict["measure"] = measure
        if unit_cost_metric_id is not UNSET:
            field_dict["unitCostMetricId"] = unit_cost_metric_id
        if unit_cost_label_filter is not UNSET:
            field_dict["unitCostLabelFilter"] = unit_cost_label_filter

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.unit_cost_label_condition_request import (
            UnitCostLabelConditionRequest,
        )

        d = dict(src_dict)

        def _parse_include_credits(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_credits = _parse_include_credits(d.pop("includeCredits", UNSET))

        def _parse_include_refunds(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_refunds = _parse_include_refunds(d.pop("includeRefunds", UNSET))

        def _parse_include_tax(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_tax = _parse_include_tax(d.pop("includeTax", UNSET))

        def _parse_amortize(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        amortize = _parse_amortize(d.pop("amortize", UNSET))

        def _parse_show_forecast(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_forecast = _parse_show_forecast(d.pop("showForecast", UNSET))

        def _parse_compare_to_last_period(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        compare_to_last_period = _parse_compare_to_last_period(
            d.pop("compareToLastPeriod", UNSET)
        )

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

        def _parse_measure(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        measure = _parse_measure(d.pop("measure", UNSET))

        def _parse_unit_cost_metric_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit_cost_metric_id = _parse_unit_cost_metric_id(
            d.pop("unitCostMetricId", UNSET)
        )

        def _parse_unit_cost_label_filter(
            data: object,
        ) -> list[UnitCostLabelConditionRequest] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                unit_cost_label_filter_type_0 = []
                _unit_cost_label_filter_type_0 = data
                for (
                    unit_cost_label_filter_type_0_item_data
                ) in _unit_cost_label_filter_type_0:
                    unit_cost_label_filter_type_0_item = (
                        UnitCostLabelConditionRequest.from_dict(
                            unit_cost_label_filter_type_0_item_data
                        )
                    )

                    unit_cost_label_filter_type_0.append(
                        unit_cost_label_filter_type_0_item
                    )

                return unit_cost_label_filter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UnitCostLabelConditionRequest] | None | Unset, data)

        unit_cost_label_filter = _parse_unit_cost_label_filter(
            d.pop("unitCostLabelFilter", UNSET)
        )

        cost_report_settings_request = cls(
            include_credits=include_credits,
            include_refunds=include_refunds,
            include_tax=include_tax,
            amortize=amortize,
            show_forecast=show_forecast,
            compare_to_last_period=compare_to_last_period,
            comparison_start_date=comparison_start_date,
            comparison_end_date=comparison_end_date,
            measure=measure,
            unit_cost_metric_id=unit_cost_metric_id,
            unit_cost_label_filter=unit_cost_label_filter,
        )

        return cost_report_settings_request
