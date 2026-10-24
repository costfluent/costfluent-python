from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..models.chart_type import ChartType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_report_settings_request import CostReportSettingsRequest
    from ..models.report_grouping_request import ReportGroupingRequest


T = TypeVar("T", bound="CreateCostReportRequest")


@_attrs_define
class CreateCostReportRequest:
    """
    Attributes:
        workspace_id (str):
        title (str):
        folder_id (None | str | Unset):
        filter_ (None | str | Unset):
        group_by (list[ReportGroupingRequest] | None | Unset):
        date_interval (None | str | Unset):
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        chart_type (ChartType | Unset):
        date_bin (None | str | Unset):
        settings (CostReportSettingsRequest | None | Unset):
    """

    workspace_id: str
    title: str
    folder_id: None | str | Unset = UNSET
    filter_: None | str | Unset = UNSET
    group_by: list[ReportGroupingRequest] | None | Unset = UNSET
    date_interval: None | str | Unset = UNSET
    start_date: datetime.date | None | Unset = UNSET
    end_date: datetime.date | None | Unset = UNSET
    chart_type: ChartType | Unset = UNSET
    date_bin: None | str | Unset = UNSET
    settings: CostReportSettingsRequest | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.cost_report_settings_request import CostReportSettingsRequest

        workspace_id = self.workspace_id

        title = self.title

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

        group_by: list[dict[str, Any]] | None | Unset
        if isinstance(self.group_by, Unset):
            group_by = UNSET
        elif isinstance(self.group_by, list):
            group_by = []
            for group_by_type_0_item_data in self.group_by:
                group_by_type_0_item = group_by_type_0_item_data.to_dict()
                group_by.append(group_by_type_0_item)

        else:
            group_by = self.group_by

        date_interval: None | str | Unset
        if isinstance(self.date_interval, Unset):
            date_interval = UNSET
        else:
            date_interval = self.date_interval

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

        chart_type: str | Unset = UNSET
        if not isinstance(self.chart_type, Unset):
            chart_type = self.chart_type.value

        date_bin: None | str | Unset
        if isinstance(self.date_bin, Unset):
            date_bin = UNSET
        else:
            date_bin = self.date_bin

        settings: dict[str, Any] | None | Unset
        if isinstance(self.settings, Unset):
            settings = UNSET
        elif isinstance(self.settings, CostReportSettingsRequest):
            settings = self.settings.to_dict()
        else:
            settings = self.settings

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workspaceId": workspace_id,
                "title": title,
            }
        )
        if folder_id is not UNSET:
            field_dict["folderId"] = folder_id
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if group_by is not UNSET:
            field_dict["groupBy"] = group_by
        if date_interval is not UNSET:
            field_dict["dateInterval"] = date_interval
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if chart_type is not UNSET:
            field_dict["chartType"] = chart_type
        if date_bin is not UNSET:
            field_dict["dateBin"] = date_bin
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.cost_report_settings_request import CostReportSettingsRequest
        from ..models.report_grouping_request import ReportGroupingRequest

        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        title = d.pop("title")

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

        def _parse_group_by(data: object) -> list[ReportGroupingRequest] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                group_by_type_0 = []
                _group_by_type_0 = data
                for group_by_type_0_item_data in _group_by_type_0:
                    group_by_type_0_item = ReportGroupingRequest.from_dict(
                        group_by_type_0_item_data
                    )

                    group_by_type_0.append(group_by_type_0_item)

                return group_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ReportGroupingRequest] | None | Unset, data)

        group_by = _parse_group_by(d.pop("groupBy", UNSET))

        def _parse_date_interval(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_interval = _parse_date_interval(d.pop("dateInterval", UNSET))

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

        _chart_type = d.pop("chartType", UNSET)
        chart_type: ChartType | Unset
        if isinstance(_chart_type, Unset):
            chart_type = UNSET
        else:
            chart_type = ChartType(_chart_type)

        def _parse_date_bin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_bin = _parse_date_bin(d.pop("dateBin", UNSET))

        def _parse_settings(data: object) -> CostReportSettingsRequest | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                settings_type_0 = CostReportSettingsRequest.from_dict(data)

                return settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CostReportSettingsRequest | None | Unset, data)

        settings = _parse_settings(d.pop("settings", UNSET))

        create_cost_report_request = cls(
            workspace_id=workspace_id,
            title=title,
            folder_id=folder_id,
            filter_=filter_,
            group_by=group_by,
            date_interval=date_interval,
            start_date=start_date,
            end_date=end_date,
            chart_type=chart_type,
            date_bin=date_bin,
            settings=settings,
        )

        return create_cost_report_request
