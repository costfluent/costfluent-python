from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..models.budget_interval_unit_value import BudgetIntervalUnitValue
from ..models.budget_measure_value import BudgetMeasureValue
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.budget_alert_request import BudgetAlertRequest
    from ..models.budget_period_request import BudgetPeriodRequest


T = TypeVar("T", bound="CreateBudgetRequest")


@_attrs_define
class CreateBudgetRequest:
    """
    Attributes:
        workspace_id (str):
        name (str):
        currency (str):
        measure (BudgetMeasureValue | Unset):
        usage_unit (None | str | Unset):
        start_date (datetime.date | None | Unset):
        interval_count (int | Unset):
        interval_unit (BudgetIntervalUnitValue | Unset):
        amount (None | str | Unset):
        periods (list[BudgetPeriodRequest] | None | Unset):
        alerts (list[BudgetAlertRequest] | None | Unset):
        segment_id (None | str | Unset):
        cost_report_id (None | str | Unset):
        app_ids (list[str] | None | Unset):
    """

    workspace_id: str
    name: str
    currency: str
    measure: BudgetMeasureValue | Unset = UNSET
    usage_unit: None | str | Unset = UNSET
    start_date: datetime.date | None | Unset = UNSET
    interval_count: int | Unset = UNSET
    interval_unit: BudgetIntervalUnitValue | Unset = UNSET
    amount: None | str | Unset = UNSET
    periods: list[BudgetPeriodRequest] | None | Unset = UNSET
    alerts: list[BudgetAlertRequest] | None | Unset = UNSET
    segment_id: None | str | Unset = UNSET
    cost_report_id: None | str | Unset = UNSET
    app_ids: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        name = self.name

        currency = self.currency

        measure: str | Unset = UNSET
        if not isinstance(self.measure, Unset):
            measure = self.measure.value

        usage_unit: None | str | Unset
        if isinstance(self.usage_unit, Unset):
            usage_unit = UNSET
        else:
            usage_unit = self.usage_unit

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.date):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        interval_count = self.interval_count

        interval_unit: str | Unset = UNSET
        if not isinstance(self.interval_unit, Unset):
            interval_unit = self.interval_unit.value

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

        alerts: list[dict[str, Any]] | None | Unset
        if isinstance(self.alerts, Unset):
            alerts = UNSET
        elif isinstance(self.alerts, list):
            alerts = []
            for alerts_type_0_item_data in self.alerts:
                alerts_type_0_item = alerts_type_0_item_data.to_dict()
                alerts.append(alerts_type_0_item)

        else:
            alerts = self.alerts

        segment_id: None | str | Unset
        if isinstance(self.segment_id, Unset):
            segment_id = UNSET
        else:
            segment_id = self.segment_id

        cost_report_id: None | str | Unset
        if isinstance(self.cost_report_id, Unset):
            cost_report_id = UNSET
        else:
            cost_report_id = self.cost_report_id

        app_ids: list[str] | None | Unset
        if isinstance(self.app_ids, Unset):
            app_ids = UNSET
        elif isinstance(self.app_ids, list):
            app_ids = self.app_ids

        else:
            app_ids = self.app_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workspaceId": workspace_id,
                "name": name,
                "currency": currency,
            }
        )
        if measure is not UNSET:
            field_dict["measure"] = measure
        if usage_unit is not UNSET:
            field_dict["usageUnit"] = usage_unit
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if interval_count is not UNSET:
            field_dict["intervalCount"] = interval_count
        if interval_unit is not UNSET:
            field_dict["intervalUnit"] = interval_unit
        if amount is not UNSET:
            field_dict["amount"] = amount
        if periods is not UNSET:
            field_dict["periods"] = periods
        if alerts is not UNSET:
            field_dict["alerts"] = alerts
        if segment_id is not UNSET:
            field_dict["segmentId"] = segment_id
        if cost_report_id is not UNSET:
            field_dict["costReportId"] = cost_report_id
        if app_ids is not UNSET:
            field_dict["appIds"] = app_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.budget_alert_request import BudgetAlertRequest
        from ..models.budget_period_request import BudgetPeriodRequest

        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        name = d.pop("name")

        currency = d.pop("currency")

        _measure = d.pop("measure", UNSET)
        measure: BudgetMeasureValue | Unset
        if isinstance(_measure, Unset):
            measure = UNSET
        else:
            measure = BudgetMeasureValue(_measure)

        def _parse_usage_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        usage_unit = _parse_usage_unit(d.pop("usageUnit", UNSET))

        def _parse_start_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = datetime.date.fromisoformat(data)

                return start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        start_date = _parse_start_date(d.pop("startDate", UNSET))

        interval_count = d.pop("intervalCount", UNSET)

        _interval_unit = d.pop("intervalUnit", UNSET)
        interval_unit: BudgetIntervalUnitValue | Unset
        if isinstance(_interval_unit, Unset):
            interval_unit = UNSET
        else:
            interval_unit = BudgetIntervalUnitValue(_interval_unit)

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

        def _parse_alerts(data: object) -> list[BudgetAlertRequest] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                alerts_type_0 = []
                _alerts_type_0 = data
                for alerts_type_0_item_data in _alerts_type_0:
                    alerts_type_0_item = BudgetAlertRequest.from_dict(
                        alerts_type_0_item_data
                    )

                    alerts_type_0.append(alerts_type_0_item)

                return alerts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BudgetAlertRequest] | None | Unset, data)

        alerts = _parse_alerts(d.pop("alerts", UNSET))

        def _parse_segment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        segment_id = _parse_segment_id(d.pop("segmentId", UNSET))

        def _parse_cost_report_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cost_report_id = _parse_cost_report_id(d.pop("costReportId", UNSET))

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

        create_budget_request = cls(
            workspace_id=workspace_id,
            name=name,
            currency=currency,
            measure=measure,
            usage_unit=usage_unit,
            start_date=start_date,
            interval_count=interval_count,
            interval_unit=interval_unit,
            amount=amount,
            periods=periods,
            alerts=alerts,
            segment_id=segment_id,
            cost_report_id=cost_report_id,
            app_ids=app_ids,
        )

        return create_budget_request
