from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.budget_period_request import BudgetPeriodRequest


T = TypeVar("T", bound="UpdateBudgetRequest")


@_attrs_define
class UpdateBudgetRequest:
    """
    Attributes:
        name (None | str | Unset):
        amount (None | str | Unset):
        periods (list[BudgetPeriodRequest] | None | Unset):
        segment_id (None | str | Unset):
        clear_segment (bool | Unset):
        cost_report_id (None | str | Unset):
        clear_cost_report (bool | Unset):
        app_ids (list[str] | None | Unset):
        usage_unit (None | str | Unset):
    """

    name: None | str | Unset = UNSET
    amount: None | str | Unset = UNSET
    periods: list[BudgetPeriodRequest] | None | Unset = UNSET
    segment_id: None | str | Unset = UNSET
    clear_segment: bool | Unset = UNSET
    cost_report_id: None | str | Unset = UNSET
    clear_cost_report: bool | Unset = UNSET
    app_ids: list[str] | None | Unset = UNSET
    usage_unit: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        amount: None | str | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        periods: list[dict[str, Any]] | None | Unset
        if isinstance(self.periods, Unset):
            periods = UNSET
        elif isinstance(self.periods, list):
            periods = []
            for periods_type_0_item_data in self.periods:
                periods_type_0_item = periods_type_0_item_data.to_dict()
                periods.append(periods_type_0_item)

        else:
            periods = self.periods

        segment_id: None | str | Unset
        if isinstance(self.segment_id, Unset):
            segment_id = UNSET
        else:
            segment_id = self.segment_id

        clear_segment = self.clear_segment

        cost_report_id: None | str | Unset
        if isinstance(self.cost_report_id, Unset):
            cost_report_id = UNSET
        else:
            cost_report_id = self.cost_report_id

        clear_cost_report = self.clear_cost_report

        app_ids: list[str] | None | Unset
        if isinstance(self.app_ids, Unset):
            app_ids = UNSET
        elif isinstance(self.app_ids, list):
            app_ids = self.app_ids

        else:
            app_ids = self.app_ids

        usage_unit: None | str | Unset
        if isinstance(self.usage_unit, Unset):
            usage_unit = UNSET
        else:
            usage_unit = self.usage_unit

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if amount is not UNSET:
            field_dict["amount"] = amount
        if periods is not UNSET:
            field_dict["periods"] = periods
        if segment_id is not UNSET:
            field_dict["segmentId"] = segment_id
        if clear_segment is not UNSET:
            field_dict["clearSegment"] = clear_segment
        if cost_report_id is not UNSET:
            field_dict["costReportId"] = cost_report_id
        if clear_cost_report is not UNSET:
            field_dict["clearCostReport"] = clear_cost_report
        if app_ids is not UNSET:
            field_dict["appIds"] = app_ids
        if usage_unit is not UNSET:
            field_dict["usageUnit"] = usage_unit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.budget_period_request import BudgetPeriodRequest

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))

        def _parse_periods(data: object) -> list[BudgetPeriodRequest] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                periods_type_0 = []
                _periods_type_0 = data
                for periods_type_0_item_data in _periods_type_0:
                    periods_type_0_item = BudgetPeriodRequest.from_dict(
                        periods_type_0_item_data
                    )

                    periods_type_0.append(periods_type_0_item)

                return periods_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BudgetPeriodRequest] | None | Unset, data)

        periods = _parse_periods(d.pop("periods", UNSET))

        def _parse_segment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        segment_id = _parse_segment_id(d.pop("segmentId", UNSET))

        clear_segment = d.pop("clearSegment", UNSET)

        def _parse_cost_report_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cost_report_id = _parse_cost_report_id(d.pop("costReportId", UNSET))

        clear_cost_report = d.pop("clearCostReport", UNSET)

        def _parse_app_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                app_ids_type_0 = cast(list[str], data)

                return app_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        app_ids = _parse_app_ids(d.pop("appIds", UNSET))

        def _parse_usage_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        usage_unit = _parse_usage_unit(d.pop("usageUnit", UNSET))

        update_budget_request = cls(
            name=name,
            amount=amount,
            periods=periods,
            segment_id=segment_id,
            clear_segment=clear_segment,
            cost_report_id=cost_report_id,
            clear_cost_report=clear_cost_report,
            app_ids=app_ids,
            usage_unit=usage_unit,
        )

        return update_budget_request
