from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usage_history_entry_response import UsageHistoryEntryResponse


T = TypeVar("T", bound="UsageResponse")


@_attrs_define
class UsageResponse:
    """
    Attributes:
        period_start (datetime.date):
        currency (str):
        tracked_spend (str):
        is_spend_complete (bool):
        unconverted_currencies (list[str]):
        rows_ingested (int):
        bytes_stored (int):
        connection_count (int):
        active_user_count (int):
        history (list[UsageHistoryEntryResponse]):
        computed_at (datetime.datetime | None | Unset):
        average_tracked_spend (None | str | Unset):
        band_plan_code (None | str | Unset):
    """

    period_start: datetime.date
    currency: str
    tracked_spend: str
    is_spend_complete: bool
    unconverted_currencies: list[str]
    rows_ingested: int
    bytes_stored: int
    connection_count: int
    active_user_count: int
    history: list[UsageHistoryEntryResponse]
    computed_at: datetime.datetime | None | Unset = UNSET
    average_tracked_spend: None | str | Unset = UNSET
    band_plan_code: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        period_start = self.period_start.isoformat()

        currency = self.currency

        tracked_spend = self.tracked_spend

        is_spend_complete = self.is_spend_complete

        unconverted_currencies = self.unconverted_currencies

        rows_ingested = self.rows_ingested

        bytes_stored = self.bytes_stored

        connection_count = self.connection_count

        active_user_count = self.active_user_count

        history = []
        for history_item_data in self.history:
            history_item = history_item_data.to_dict()
            history.append(history_item)

        computed_at: None | str | Unset
        if isinstance(self.computed_at, Unset):
            computed_at = UNSET
        elif isinstance(self.computed_at, datetime.datetime):
            computed_at = self.computed_at.isoformat()
        else:
            computed_at = self.computed_at

        average_tracked_spend: None | str | Unset
        if isinstance(self.average_tracked_spend, Unset):
            average_tracked_spend = UNSET
        else:
            average_tracked_spend = self.average_tracked_spend

        band_plan_code: None | str | Unset
        if isinstance(self.band_plan_code, Unset):
            band_plan_code = UNSET
        else:
            band_plan_code = self.band_plan_code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "periodStart": period_start,
                "currency": currency,
                "trackedSpend": tracked_spend,
                "isSpendComplete": is_spend_complete,
                "unconvertedCurrencies": unconverted_currencies,
                "rowsIngested": rows_ingested,
                "bytesStored": bytes_stored,
                "connectionCount": connection_count,
                "activeUserCount": active_user_count,
                "history": history,
            }
        )
        if computed_at is not UNSET:
            field_dict["computedAt"] = computed_at
        if average_tracked_spend is not UNSET:
            field_dict["averageTrackedSpend"] = average_tracked_spend
        if band_plan_code is not UNSET:
            field_dict["bandPlanCode"] = band_plan_code

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.usage_history_entry_response import UsageHistoryEntryResponse

        d = dict(src_dict)
        period_start = datetime.date.fromisoformat(d.pop("periodStart"))

        currency = d.pop("currency")

        tracked_spend = d.pop("trackedSpend")

        is_spend_complete = d.pop("isSpendComplete")

        unconverted_currencies = cast(list[str], d.pop("unconvertedCurrencies"))

        rows_ingested = d.pop("rowsIngested")

        bytes_stored = d.pop("bytesStored")

        connection_count = d.pop("connectionCount")

        active_user_count = d.pop("activeUserCount")

        history = []
        _history = d.pop("history")
        for history_item_data in _history:
            history_item = UsageHistoryEntryResponse.from_dict(history_item_data)

            history.append(history_item)

        def _parse_computed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                computed_at_type_0 = datetime.datetime.fromisoformat(data)

                return computed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        computed_at = _parse_computed_at(d.pop("computedAt", UNSET))

        def _parse_average_tracked_spend(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        average_tracked_spend = _parse_average_tracked_spend(
            d.pop("averageTrackedSpend", UNSET)
        )

        def _parse_band_plan_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        band_plan_code = _parse_band_plan_code(d.pop("bandPlanCode", UNSET))

        usage_response = cls(
            period_start=period_start,
            currency=currency,
            tracked_spend=tracked_spend,
            is_spend_complete=is_spend_complete,
            unconverted_currencies=unconverted_currencies,
            rows_ingested=rows_ingested,
            bytes_stored=bytes_stored,
            connection_count=connection_count,
            active_user_count=active_user_count,
            history=history,
            computed_at=computed_at,
            average_tracked_spend=average_tracked_spend,
            band_plan_code=band_plan_code,
        )

        return usage_response
