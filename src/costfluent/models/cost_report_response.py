from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_report_settings_response import CostReportSettingsResponse
    from ..models.report_grouping_response import ReportGroupingResponse


T = TypeVar("T", bound="CostReportResponse")


@_attrs_define
class CostReportResponse:
    """
    Attributes:
        id (str):
        title (str):
        group_by (list[ReportGroupingResponse]):
        date_interval (str):
        chart_type (str):
        date_bin (str):
        settings (CostReportSettingsResponse):
        created_at (datetime.datetime):
        is_default (bool):
        folder_id (None | str | Unset):
        filter_ (None | str | Unset):
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    id: str
    title: str
    group_by: list[ReportGroupingResponse]
    date_interval: str
    chart_type: str
    date_bin: str
    settings: CostReportSettingsResponse
    created_at: datetime.datetime
    is_default: bool
    folder_id: None | str | Unset = UNSET
    filter_: None | str | Unset = UNSET
    start_date: datetime.date | None | Unset = UNSET
    end_date: datetime.date | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        group_by = []
        for group_by_item_data in self.group_by:
            group_by_item = group_by_item_data.to_dict()
            group_by.append(group_by_item)

        date_interval = self.date_interval

        chart_type = self.chart_type

        date_bin = self.date_bin

        settings = self.settings.to_dict()

        created_at = self.created_at.isoformat()

        is_default = self.is_default

        folder_id: None | str | Unset
        if isinstance(self.folder_id, Unset):
            folder_id = UNSET
        else:
            folder_id = self.folder_id

        filter_: None | str | Unset
        if isinstance(self.filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = self.filter_

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
                "title": title,
                "groupBy": group_by,
                "dateInterval": date_interval,
                "chartType": chart_type,
                "dateBin": date_bin,
                "settings": settings,
                "createdAt": created_at,
                "isDefault": is_default,
            }
        )
        if folder_id is not UNSET:
            field_dict["folderId"] = folder_id
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.cost_report_settings_response import CostReportSettingsResponse
        from ..models.report_grouping_response import ReportGroupingResponse

        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        group_by = []
        _group_by = d.pop("groupBy")
        for group_by_item_data in _group_by:
            group_by_item = ReportGroupingResponse.from_dict(group_by_item_data)

            group_by.append(group_by_item)

        date_interval = d.pop("dateInterval")

        chart_type = d.pop("chartType")

        date_bin = d.pop("dateBin")

        settings = CostReportSettingsResponse.from_dict(d.pop("settings"))

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        is_default = d.pop("isDefault")

        def _parse_folder_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        folder_id = _parse_folder_id(d.pop("folderId", UNSET))

        def _parse_filter_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filter_ = _parse_filter_(d.pop("filter", UNSET))

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

        cost_report_response = cls(
            id=id,
            title=title,
            group_by=group_by,
            date_interval=date_interval,
            chart_type=chart_type,
            date_bin=date_bin,
            settings=settings,
            created_at=created_at,
            is_default=is_default,
            folder_id=folder_id,
            filter_=filter_,
            start_date=start_date,
            end_date=end_date,
            updated_at=updated_at,
        )

        return cost_report_response
