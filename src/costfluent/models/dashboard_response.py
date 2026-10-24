from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.widget_response import WidgetResponse


T = TypeVar("T", bound="DashboardResponse")


@_attrs_define
class DashboardResponse:
    """
    Attributes:
        id (str):
        title (str):
        is_default (bool):
        date_interval (str):
        date_bin (str):
        widgets (list[WidgetResponse]):
        created_at (datetime.datetime):
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        saved_filter_id (None | str | Unset):
    """

    id: str
    title: str
    is_default: bool
    date_interval: str
    date_bin: str
    widgets: list[WidgetResponse]
    created_at: datetime.datetime
    start_date: datetime.date | None | Unset = UNSET
    end_date: datetime.date | None | Unset = UNSET
    saved_filter_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        is_default = self.is_default

        date_interval = self.date_interval

        date_bin = self.date_bin

        widgets = []
        for widgets_item_data in self.widgets:
            widgets_item = widgets_item_data.to_dict()
            widgets.append(widgets_item)

        created_at = self.created_at.isoformat()

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.date):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.date):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        saved_filter_id: None | str | Unset
        if isinstance(self.saved_filter_id, Unset):
            saved_filter_id = UNSET
        else:
            saved_filter_id = self.saved_filter_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "title": title,
                "isDefault": is_default,
                "dateInterval": date_interval,
                "dateBin": date_bin,
                "widgets": widgets,
                "createdAt": created_at,
            }
        )
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if saved_filter_id is not UNSET:
            field_dict["savedFilterId"] = saved_filter_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.widget_response import WidgetResponse

        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        is_default = d.pop("isDefault")

        date_interval = d.pop("dateInterval")

        date_bin = d.pop("dateBin")

        widgets = []
        _widgets = d.pop("widgets")
        for widgets_item_data in _widgets:
            widgets_item = WidgetResponse.from_dict(widgets_item_data)

            widgets.append(widgets_item)

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

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

        def _parse_end_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = datetime.date.fromisoformat(data)

                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        end_date = _parse_end_date(d.pop("endDate", UNSET))

        def _parse_saved_filter_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        saved_filter_id = _parse_saved_filter_id(d.pop("savedFilterId", UNSET))

        dashboard_response = cls(
            id=id,
            title=title,
            is_default=is_default,
            date_interval=date_interval,
            date_bin=date_bin,
            widgets=widgets,
            created_at=created_at,
            start_date=start_date,
            end_date=end_date,
            saved_filter_id=saved_filter_id,
        )

        return dashboard_response
