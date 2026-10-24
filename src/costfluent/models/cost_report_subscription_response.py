from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostReportSubscriptionResponse")


@_attrs_define
class CostReportSubscriptionResponse:
    """
    Attributes:
        id (str):
        cost_report_id (str):
        name (str):
        schedule_type (str):
        delivery_hour (int):
        time_zone (str):
        app_ids (list[str]):
        is_active (bool):
        created_at (datetime.datetime):
        last_sent_at (datetime.datetime | None | Unset):
        next_scheduled_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    id: str
    cost_report_id: str
    name: str
    schedule_type: str
    delivery_hour: int
    time_zone: str
    app_ids: list[str]
    is_active: bool
    created_at: datetime.datetime
    last_sent_at: datetime.datetime | None | Unset = UNSET
    next_scheduled_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        cost_report_id = self.cost_report_id

        name = self.name

        schedule_type = self.schedule_type

        delivery_hour = self.delivery_hour

        time_zone = self.time_zone

        app_ids = self.app_ids

        is_active = self.is_active

        created_at = self.created_at.isoformat()

        last_sent_at: None | str | Unset
        if isinstance(self.last_sent_at, Unset):
            last_sent_at = UNSET
        elif isinstance(self.last_sent_at, datetime.datetime):
            last_sent_at = self.last_sent_at.isoformat()
        else:
            last_sent_at = self.last_sent_at

        next_scheduled_at: None | str | Unset
        if isinstance(self.next_scheduled_at, Unset):
            next_scheduled_at = UNSET
        elif isinstance(self.next_scheduled_at, datetime.datetime):
            next_scheduled_at = self.next_scheduled_at.isoformat()
        else:
            next_scheduled_at = self.next_scheduled_at

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
                "costReportId": cost_report_id,
                "name": name,
                "scheduleType": schedule_type,
                "deliveryHour": delivery_hour,
                "timeZone": time_zone,
                "appIds": app_ids,
                "isActive": is_active,
                "createdAt": created_at,
            }
        )
        if last_sent_at is not UNSET:
            field_dict["lastSentAt"] = last_sent_at
        if next_scheduled_at is not UNSET:
            field_dict["nextScheduledAt"] = next_scheduled_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        cost_report_id = d.pop("costReportId")

        name = d.pop("name")

        schedule_type = d.pop("scheduleType")

        delivery_hour = d.pop("deliveryHour")

        time_zone = d.pop("timeZone")

        app_ids = cast(list[str], d.pop("appIds"))

        is_active = d.pop("isActive")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        def _parse_last_sent_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_sent_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_sent_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_sent_at = _parse_last_sent_at(d.pop("lastSentAt", UNSET))

        def _parse_next_scheduled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_scheduled_at_type_0 = datetime.datetime.fromisoformat(data)

                return next_scheduled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_scheduled_at = _parse_next_scheduled_at(d.pop("nextScheduledAt", UNSET))

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

        cost_report_subscription_response = cls(
            id=id,
            cost_report_id=cost_report_id,
            name=name,
            schedule_type=schedule_type,
            delivery_hour=delivery_hour,
            time_zone=time_zone,
            app_ids=app_ids,
            is_active=is_active,
            created_at=created_at,
            last_sent_at=last_sent_at,
            next_scheduled_at=next_scheduled_at,
            updated_at=updated_at,
        )

        return cost_report_subscription_response
