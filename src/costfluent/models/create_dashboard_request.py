from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateDashboardRequest")


@_attrs_define
class CreateDashboardRequest:
    """
    Attributes:
        workspace_id (str):
        title (str):
        is_default (bool | Unset):
        date_interval (str | Unset):
        date_bin (str | Unset):
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
    """

    workspace_id: str
    title: str
    is_default: bool | Unset = UNSET
    date_interval: str | Unset = UNSET
    date_bin: str | Unset = UNSET
    start_date: datetime.date | None | Unset = UNSET
    end_date: datetime.date | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        title = self.title

        is_default = self.is_default

        date_interval = self.date_interval

        date_bin = self.date_bin

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

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workspaceId": workspace_id,
                "title": title,
            }
        )
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if date_interval is not UNSET:
            field_dict["dateInterval"] = date_interval
        if date_bin is not UNSET:
            field_dict["dateBin"] = date_bin
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        title = d.pop("title")

        is_default = d.pop("isDefault", UNSET)

        date_interval = d.pop("dateInterval", UNSET)

        date_bin = d.pop("dateBin", UNSET)

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

        create_dashboard_request = cls(
            workspace_id=workspace_id,
            title=title,
            is_default=is_default,
            date_interval=date_interval,
            date_bin=date_bin,
            start_date=start_date,
            end_date=end_date,
        )

        return create_dashboard_request
