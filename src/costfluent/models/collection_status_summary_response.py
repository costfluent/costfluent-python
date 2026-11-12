from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.next_delivery_response import NextDeliveryResponse


T = TypeVar("T", bound="CollectionStatusSummaryResponse")


@_attrs_define
class CollectionStatusSummaryResponse:
    """
    Attributes:
        provider_id (str):
        name (str):
        key (str):
        status (str):
        cadence (str):
        period (str):
        has_provider_total (bool):
        is_late (bool):
        awaiting_first_import (bool):
        last_imported_at (datetime.datetime | None | Unset):
        data_through (datetime.date | None | Unset):
        next_delivery (NextDeliveryResponse | None | Unset):
        days_overdue (int | None | Unset):
        last_sync_status (None | str | Unset):
    """

    provider_id: str
    name: str
    key: str
    status: str
    cadence: str
    period: str
    has_provider_total: bool
    is_late: bool
    awaiting_first_import: bool
    last_imported_at: datetime.datetime | None | Unset = UNSET
    data_through: datetime.date | None | Unset = UNSET
    next_delivery: NextDeliveryResponse | None | Unset = UNSET
    days_overdue: int | None | Unset = UNSET
    last_sync_status: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.next_delivery_response import NextDeliveryResponse

        provider_id = self.provider_id

        name = self.name

        key = self.key

        status = self.status

        cadence = self.cadence

        period = self.period

        has_provider_total = self.has_provider_total

        is_late = self.is_late

        awaiting_first_import = self.awaiting_first_import

        last_imported_at: None | str | Unset
        if isinstance(self.last_imported_at, Unset):
            last_imported_at = UNSET
        elif isinstance(self.last_imported_at, datetime.datetime):
            last_imported_at = self.last_imported_at.isoformat()
        else:
            last_imported_at = self.last_imported_at

        data_through: None | str | Unset
        if isinstance(self.data_through, Unset):
            data_through = UNSET
        elif isinstance(self.data_through, datetime.date):
            data_through = self.data_through.isoformat()
        else:
            data_through = self.data_through

        next_delivery: dict[str, Any] | None | Unset
        if isinstance(self.next_delivery, Unset):
            next_delivery = UNSET
        elif isinstance(self.next_delivery, NextDeliveryResponse):
            next_delivery = self.next_delivery.to_dict()
        else:
            next_delivery = self.next_delivery

        days_overdue: int | None | Unset
        if isinstance(self.days_overdue, Unset):
            days_overdue = UNSET
        else:
            days_overdue = self.days_overdue

        last_sync_status: None | str | Unset
        if isinstance(self.last_sync_status, Unset):
            last_sync_status = UNSET
        else:
            last_sync_status = self.last_sync_status

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "providerId": provider_id,
                "name": name,
                "key": key,
                "status": status,
                "cadence": cadence,
                "period": period,
                "hasProviderTotal": has_provider_total,
                "isLate": is_late,
                "awaitingFirstImport": awaiting_first_import,
            }
        )
        if last_imported_at is not UNSET:
            field_dict["lastImportedAt"] = last_imported_at
        if data_through is not UNSET:
            field_dict["dataThrough"] = data_through
        if next_delivery is not UNSET:
            field_dict["nextDelivery"] = next_delivery
        if days_overdue is not UNSET:
            field_dict["daysOverdue"] = days_overdue
        if last_sync_status is not UNSET:
            field_dict["lastSyncStatus"] = last_sync_status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.next_delivery_response import NextDeliveryResponse

        d = dict(src_dict)
        provider_id = d.pop("providerId")

        name = d.pop("name")

        key = d.pop("key")

        status = d.pop("status")

        cadence = d.pop("cadence")

        period = d.pop("period")

        has_provider_total = d.pop("hasProviderTotal")

        is_late = d.pop("isLate")

        awaiting_first_import = d.pop("awaitingFirstImport")

        def _parse_last_imported_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_imported_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_imported_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_imported_at = _parse_last_imported_at(d.pop("lastImportedAt", UNSET))

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

        def _parse_next_delivery(data: object) -> NextDeliveryResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                next_delivery_type_0 = NextDeliveryResponse.from_dict(data)

                return next_delivery_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NextDeliveryResponse | None | Unset, data)

        next_delivery = _parse_next_delivery(d.pop("nextDelivery", UNSET))

        def _parse_days_overdue(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        days_overdue = _parse_days_overdue(d.pop("daysOverdue", UNSET))

        def _parse_last_sync_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_sync_status = _parse_last_sync_status(d.pop("lastSyncStatus", UNSET))

        collection_status_summary_response = cls(
            provider_id=provider_id,
            name=name,
            key=key,
            status=status,
            cadence=cadence,
            period=period,
            has_provider_total=has_provider_total,
            is_late=is_late,
            awaiting_first_import=awaiting_first_import,
            last_imported_at=last_imported_at,
            data_through=data_through,
            next_delivery=next_delivery,
            days_overdue=days_overdue,
            last_sync_status=last_sync_status,
        )

        return collection_status_summary_response
