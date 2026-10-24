from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plan_ladder_entry_response import PlanLadderEntryResponse


T = TypeVar("T", bound="EntitlementResponse")


@_attrs_define
class EntitlementResponse:
    """
    Attributes:
        plan_code (str):
        plan_name (str):
        status (str):
        currency (str):
        features (list[str]):
        overridden_limits (list[str]):
        ingestion_halted (bool):
        ingestion_halted_reason (str):
        current_period_start (datetime.date):
        current_period_end (datetime.date):
        ladder (list[PlanLadderEntryResponse]):
        spend_ceiling (None | str | Unset):
        history_days (int | None | Unset):
        max_connections (int | None | Unset):
        max_allocation_rules (int | None | Unset):
        max_backfill_months (int | None | Unset):
        max_rows_per_month (int | None | Unset):
        max_bytes_stored (int | None | Unset):
        band_plan_code (None | str | Unset):
    """

    plan_code: str
    plan_name: str
    status: str
    currency: str
    features: list[str]
    overridden_limits: list[str]
    ingestion_halted: bool
    ingestion_halted_reason: str
    current_period_start: datetime.date
    current_period_end: datetime.date
    ladder: list[PlanLadderEntryResponse]
    spend_ceiling: None | str | Unset = UNSET
    history_days: int | None | Unset = UNSET
    max_connections: int | None | Unset = UNSET
    max_allocation_rules: int | None | Unset = UNSET
    max_backfill_months: int | None | Unset = UNSET
    max_rows_per_month: int | None | Unset = UNSET
    max_bytes_stored: int | None | Unset = UNSET
    band_plan_code: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        plan_code = self.plan_code

        plan_name = self.plan_name

        status = self.status

        currency = self.currency

        features = self.features

        overridden_limits = self.overridden_limits

        ingestion_halted = self.ingestion_halted

        ingestion_halted_reason = self.ingestion_halted_reason

        current_period_start = self.current_period_start.isoformat()

        current_period_end = self.current_period_end.isoformat()

        ladder = []
        for ladder_item_data in self.ladder:
            ladder_item = ladder_item_data.to_dict()
            ladder.append(ladder_item)

        spend_ceiling: None | str | Unset
        if isinstance(self.spend_ceiling, Unset):
            spend_ceiling = UNSET
        else:
            spend_ceiling = self.spend_ceiling

        history_days: int | None | Unset
        if isinstance(self.history_days, Unset):
            history_days = UNSET
        else:
            history_days = self.history_days

        max_connections: int | None | Unset
        if isinstance(self.max_connections, Unset):
            max_connections = UNSET
        else:
            max_connections = self.max_connections

        max_allocation_rules: int | None | Unset
        if isinstance(self.max_allocation_rules, Unset):
            max_allocation_rules = UNSET
        else:
            max_allocation_rules = self.max_allocation_rules

        max_backfill_months: int | None | Unset
        if isinstance(self.max_backfill_months, Unset):
            max_backfill_months = UNSET
        else:
            max_backfill_months = self.max_backfill_months

        max_rows_per_month: int | None | Unset
        if isinstance(self.max_rows_per_month, Unset):
            max_rows_per_month = UNSET
        else:
            max_rows_per_month = self.max_rows_per_month

        max_bytes_stored: int | None | Unset
        if isinstance(self.max_bytes_stored, Unset):
            max_bytes_stored = UNSET
        else:
            max_bytes_stored = self.max_bytes_stored

        band_plan_code: None | str | Unset
        if isinstance(self.band_plan_code, Unset):
            band_plan_code = UNSET
        else:
            band_plan_code = self.band_plan_code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "planCode": plan_code,
                "planName": plan_name,
                "status": status,
                "currency": currency,
                "features": features,
                "overriddenLimits": overridden_limits,
                "ingestionHalted": ingestion_halted,
                "ingestionHaltedReason": ingestion_halted_reason,
                "currentPeriodStart": current_period_start,
                "currentPeriodEnd": current_period_end,
                "ladder": ladder,
            }
        )
        if spend_ceiling is not UNSET:
            field_dict["spendCeiling"] = spend_ceiling
        if history_days is not UNSET:
            field_dict["historyDays"] = history_days
        if max_connections is not UNSET:
            field_dict["maxConnections"] = max_connections
        if max_allocation_rules is not UNSET:
            field_dict["maxAllocationRules"] = max_allocation_rules
        if max_backfill_months is not UNSET:
            field_dict["maxBackfillMonths"] = max_backfill_months
        if max_rows_per_month is not UNSET:
            field_dict["maxRowsPerMonth"] = max_rows_per_month
        if max_bytes_stored is not UNSET:
            field_dict["maxBytesStored"] = max_bytes_stored
        if band_plan_code is not UNSET:
            field_dict["bandPlanCode"] = band_plan_code

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.plan_ladder_entry_response import PlanLadderEntryResponse

        d = dict(src_dict)
        plan_code = d.pop("planCode")

        plan_name = d.pop("planName")

        status = d.pop("status")

        currency = d.pop("currency")

        features = cast(list[str], d.pop("features"))

        overridden_limits = cast(list[str], d.pop("overriddenLimits"))

        ingestion_halted = d.pop("ingestionHalted")

        ingestion_halted_reason = d.pop("ingestionHaltedReason")

        current_period_start = datetime.date.fromisoformat(d.pop("currentPeriodStart"))

        current_period_end = datetime.date.fromisoformat(d.pop("currentPeriodEnd"))

        ladder = []
        _ladder = d.pop("ladder")
        for ladder_item_data in _ladder:
            ladder_item = PlanLadderEntryResponse.from_dict(ladder_item_data)

            ladder.append(ladder_item)

        def _parse_spend_ceiling(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        spend_ceiling = _parse_spend_ceiling(d.pop("spendCeiling", UNSET))

        def _parse_history_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        history_days = _parse_history_days(d.pop("historyDays", UNSET))

        def _parse_max_connections(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_connections = _parse_max_connections(d.pop("maxConnections", UNSET))

        def _parse_max_allocation_rules(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_allocation_rules = _parse_max_allocation_rules(
            d.pop("maxAllocationRules", UNSET)
        )

        def _parse_max_backfill_months(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_backfill_months = _parse_max_backfill_months(
            d.pop("maxBackfillMonths", UNSET)
        )

        def _parse_max_rows_per_month(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_rows_per_month = _parse_max_rows_per_month(d.pop("maxRowsPerMonth", UNSET))

        def _parse_max_bytes_stored(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_bytes_stored = _parse_max_bytes_stored(d.pop("maxBytesStored", UNSET))

        def _parse_band_plan_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        band_plan_code = _parse_band_plan_code(d.pop("bandPlanCode", UNSET))

        entitlement_response = cls(
            plan_code=plan_code,
            plan_name=plan_name,
            status=status,
            currency=currency,
            features=features,
            overridden_limits=overridden_limits,
            ingestion_halted=ingestion_halted,
            ingestion_halted_reason=ingestion_halted_reason,
            current_period_start=current_period_start,
            current_period_end=current_period_end,
            ladder=ladder,
            spend_ceiling=spend_ceiling,
            history_days=history_days,
            max_connections=max_connections,
            max_allocation_rules=max_allocation_rules,
            max_backfill_months=max_backfill_months,
            max_rows_per_month=max_rows_per_month,
            max_bytes_stored=max_bytes_stored,
            band_plan_code=band_plan_code,
        )

        return entitlement_response
