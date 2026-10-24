from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCostReportSubscriptionRouteRequest")


@_attrs_define
class UpdateCostReportSubscriptionRouteRequest:
    """
    Attributes:
        workspace_id (str):
        name (None | str | Unset):
        schedule_type (None | str | Unset):
        delivery_hour (int | None | Unset):
        time_zone (None | str | Unset):
        app_ids (list[str] | None | Unset):
    """

    workspace_id: str
    name: None | str | Unset = UNSET
    schedule_type: None | str | Unset = UNSET
    delivery_hour: int | None | Unset = UNSET
    time_zone: None | str | Unset = UNSET
    app_ids: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        schedule_type: None | str | Unset
        if isinstance(self.schedule_type, Unset):
            schedule_type = UNSET
        else:
            schedule_type = self.schedule_type

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
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if schedule_type is not UNSET:
            field_dict["scheduleType"] = schedule_type
        if delivery_hour is not UNSET:
            field_dict["deliveryHour"] = delivery_hour
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if app_ids is not UNSET:
            field_dict["appIds"] = app_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_schedule_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schedule_type = _parse_schedule_type(d.pop("scheduleType", UNSET))

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

        update_cost_report_subscription_route_request = cls(
            workspace_id=workspace_id,
            name=name,
            schedule_type=schedule_type,
            delivery_hour=delivery_hour,
            time_zone=time_zone,
            app_ids=app_ids,
        )

        return update_cost_report_subscription_route_request
