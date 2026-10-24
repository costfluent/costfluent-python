from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.budget_alert_response import BudgetAlertResponse
    from ..models.budget_period_response import BudgetPeriodResponse
    from ..models.currency_amount import CurrencyAmount


T = TypeVar("T", bound="BudgetResponse")


@_attrs_define
class BudgetResponse:
    """
    Attributes:
        id (str):
        name (str):
        currency (str):
        measure (str):
        start_date (datetime.date):
        interval_count (int):
        interval_unit (str):
        periods (list[BudgetPeriodResponse]):
        status (str):
        state (str):
        spend_availability (str):
        unconverted (list[CurrencyAmount]):
        alerts (list[BudgetAlertResponse]):
        created_at (datetime.datetime):
        amount (None | str | Unset):
        usage_unit (None | str | Unset):
        current_period (BudgetPeriodResponse | None | Unset):
        segment_id (None | str | Unset):
        cost_report_id (None | str | Unset):
        current_spend (None | str | Unset):
        budgeted_to_date (None | str | Unset):
        projected_spend (None | str | Unset):
        percent_used (float | None | Unset):
        history_floor (datetime.date | None | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    id: str
    name: str
    currency: str
    measure: str
    start_date: datetime.date
    interval_count: int
    interval_unit: str
    periods: list[BudgetPeriodResponse]
    status: str
    state: str
    spend_availability: str
    unconverted: list[CurrencyAmount]
    alerts: list[BudgetAlertResponse]
    created_at: datetime.datetime
    amount: None | str | Unset = UNSET
    usage_unit: None | str | Unset = UNSET
    current_period: BudgetPeriodResponse | None | Unset = UNSET
    segment_id: None | str | Unset = UNSET
    cost_report_id: None | str | Unset = UNSET
    current_spend: None | str | Unset = UNSET
    budgeted_to_date: None | str | Unset = UNSET
    projected_spend: None | str | Unset = UNSET
    percent_used: float | None | Unset = UNSET
    history_floor: datetime.date | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.budget_period_response import BudgetPeriodResponse

        id = self.id

        name = self.name

        currency = self.currency

        measure = self.measure

        start_date = self.start_date.isoformat()

        interval_count = self.interval_count

        interval_unit = self.interval_unit

        periods = []
        for periods_item_data in self.periods:
            periods_item = periods_item_data.to_dict()
            periods.append(periods_item)

        status = self.status

        state = self.state

        spend_availability = self.spend_availability

        unconverted = []
        for unconverted_item_data in self.unconverted:
            unconverted_item = unconverted_item_data.to_dict()
            unconverted.append(unconverted_item)

        alerts = []
        for alerts_item_data in self.alerts:
            alerts_item = alerts_item_data.to_dict()
            alerts.append(alerts_item)

        created_at = self.created_at.isoformat()

        amount: None | str | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        usage_unit: None | str | Unset
        if isinstance(self.usage_unit, Unset):
            usage_unit = UNSET
        else:
            usage_unit = self.usage_unit

        current_period: dict[str, Any] | None | Unset
        if isinstance(self.current_period, Unset):
            current_period = UNSET
        elif isinstance(self.current_period, BudgetPeriodResponse):
            current_period = self.current_period.to_dict()
        else:
            current_period = self.current_period

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

        current_spend: None | str | Unset
        if isinstance(self.current_spend, Unset):
            current_spend = UNSET
        else:
            current_spend = self.current_spend

        budgeted_to_date: None | str | Unset
        if isinstance(self.budgeted_to_date, Unset):
            budgeted_to_date = UNSET
        else:
            budgeted_to_date = self.budgeted_to_date

        projected_spend: None | str | Unset
        if isinstance(self.projected_spend, Unset):
            projected_spend = UNSET
        else:
            projected_spend = self.projected_spend

        percent_used: float | None | Unset
        if isinstance(self.percent_used, Unset):
            percent_used = UNSET
        else:
            percent_used = self.percent_used

        history_floor: None | str | Unset
        if isinstance(self.history_floor, Unset):
            history_floor = UNSET
        elif isinstance(self.history_floor, datetime.date):
            history_floor = self.history_floor.isoformat()
        else:
            history_floor = self.history_floor

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "currency": currency,
                "measure": measure,
                "startDate": start_date,
                "intervalCount": interval_count,
                "intervalUnit": interval_unit,
                "periods": periods,
                "status": status,
                "state": state,
                "spendAvailability": spend_availability,
                "unconverted": unconverted,
                "alerts": alerts,
                "createdAt": created_at,
            }
        )
        if amount is not UNSET:
            field_dict["amount"] = amount
        if usage_unit is not UNSET:
            field_dict["usageUnit"] = usage_unit
        if current_period is not UNSET:
            field_dict["currentPeriod"] = current_period
        if segment_id is not UNSET:
            field_dict["segmentId"] = segment_id
        if cost_report_id is not UNSET:
            field_dict["costReportId"] = cost_report_id
        if current_spend is not UNSET:
            field_dict["currentSpend"] = current_spend
        if budgeted_to_date is not UNSET:
            field_dict["budgetedToDate"] = budgeted_to_date
        if projected_spend is not UNSET:
            field_dict["projectedSpend"] = projected_spend
        if percent_used is not UNSET:
            field_dict["percentUsed"] = percent_used
        if history_floor is not UNSET:
            field_dict["historyFloor"] = history_floor
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.budget_alert_response import BudgetAlertResponse
        from ..models.budget_period_response import BudgetPeriodResponse
        from ..models.currency_amount import CurrencyAmount

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        currency = d.pop("currency")

        measure = d.pop("measure")

        start_date = datetime.date.fromisoformat(d.pop("startDate"))

        interval_count = d.pop("intervalCount")

        interval_unit = d.pop("intervalUnit")

        periods = []
        _periods = d.pop("periods")
        for periods_item_data in _periods:
            periods_item = BudgetPeriodResponse.from_dict(periods_item_data)

            periods.append(periods_item)

        status = d.pop("status")

        state = d.pop("state")

        spend_availability = d.pop("spendAvailability")

        unconverted = []
        _unconverted = d.pop("unconverted")
        for unconverted_item_data in _unconverted:
            unconverted_item = CurrencyAmount.from_dict(unconverted_item_data)

            unconverted.append(unconverted_item)

        alerts = []
        _alerts = d.pop("alerts")
        for alerts_item_data in _alerts:
            alerts_item = BudgetAlertResponse.from_dict(alerts_item_data)

            alerts.append(alerts_item)

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        def _parse_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))

        def _parse_usage_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        usage_unit = _parse_usage_unit(d.pop("usageUnit", UNSET))

        def _parse_current_period(data: object) -> BudgetPeriodResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_period_type_0 = BudgetPeriodResponse.from_dict(data)

                return current_period_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BudgetPeriodResponse | None | Unset, data)

        current_period = _parse_current_period(d.pop("currentPeriod", UNSET))

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

        def _parse_current_spend(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_spend = _parse_current_spend(d.pop("currentSpend", UNSET))

        def _parse_budgeted_to_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        budgeted_to_date = _parse_budgeted_to_date(d.pop("budgetedToDate", UNSET))

        def _parse_projected_spend(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        projected_spend = _parse_projected_spend(d.pop("projectedSpend", UNSET))

        def _parse_percent_used(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        percent_used = _parse_percent_used(d.pop("percentUsed", UNSET))

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

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))

        budget_response = cls(
            id=id,
            name=name,
            currency=currency,
            measure=measure,
            start_date=start_date,
            interval_count=interval_count,
            interval_unit=interval_unit,
            periods=periods,
            status=status,
            state=state,
            spend_availability=spend_availability,
            unconverted=unconverted,
            alerts=alerts,
            created_at=created_at,
            amount=amount,
            usage_unit=usage_unit,
            current_period=current_period,
            segment_id=segment_id,
            cost_report_id=cost_report_id,
            current_spend=current_spend,
            budgeted_to_date=budgeted_to_date,
            projected_spend=projected_spend,
            percent_used=percent_used,
            history_floor=history_floor,
            updated_at=updated_at,
        )

        return budget_response
