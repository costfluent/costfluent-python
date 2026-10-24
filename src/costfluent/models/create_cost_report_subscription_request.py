from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCostReportSubscriptionRequest")


@_attrs_define
class CreateCostReportSubscriptionRequest:
    """
    Attributes:
        workspace_id (str):
        cost_report_id (str):
        name (str):
        schedule_type (str):
        app_ids (list[str]):
        delivery_hour (int | None | Unset):
        time_zone (None | str | Unset):
    """

    workspace_id: str
    cost_report_id: str
    name: str
    schedule_type: str
    app_ids: list[str]
    delivery_hour: int | None | Unset = UNSET
    time_zone: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        cost_report_id = self.cost_report_id

        name = self.name

        schedule_type = self.schedule_type

        app_ids = self.app_ids

        delivery_hour: int | None | Unset
        if isinstance(self.delivery_hour, Unset):
            delivery_hour = UNSET
        else:
            delivery_hour = self.delivery_hour

        time_zone: None | str | Unset
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = self.time_zone

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workspaceId": workspace_id,
                "costReportId": cost_report_id,
                "name": name,
                "scheduleType": schedule_type,
                "appIds": app_ids,
            }
        )
        if delivery_hour is not UNSET:
            field_dict["deliveryHour"] = delivery_hour
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        cost_report_id = d.pop("costReportId")

        name = d.pop("name")

        schedule_type = d.pop("scheduleType")

        app_ids = cast(list[str], d.pop("appIds"))

        def _parse_delivery_hour(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        delivery_hour = _parse_delivery_hour(d.pop("deliveryHour", UNSET))

        def _parse_time_zone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_zone = _parse_time_zone(d.pop("timeZone", UNSET))

        create_cost_report_subscription_request = cls(
            workspace_id=workspace_id,
            cost_report_id=cost_report_id,
            name=name,
            schedule_type=schedule_type,
            app_ids=app_ids,
            delivery_hour=delivery_hour,
            time_zone=time_zone,
        )

        return create_cost_report_subscription_request
