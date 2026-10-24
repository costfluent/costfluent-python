from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.report_group_response import ReportGroupResponse


T = TypeVar("T", bound="ReportTimeSeriesResponse")


@_attrs_define
class ReportTimeSeriesResponse:
    """
    Attributes:
        date (datetime.date):
        groups (list[ReportGroupResponse]):
    """

    date: datetime.date
    groups: list[ReportGroupResponse]

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        groups = []
        for groups_item_data in self.groups:
            groups_item = groups_item_data.to_dict()
            groups.append(groups_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "date": date,
                "groups": groups,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.report_group_response import ReportGroupResponse

        d = dict(src_dict)
        date = datetime.date.fromisoformat(d.pop("date"))

        groups = []
        _groups = d.pop("groups")
        for groups_item_data in _groups:
            groups_item = ReportGroupResponse.from_dict(groups_item_data)

            groups.append(groups_item)

        report_time_series_response = cls(
            date=date,
            groups=groups,
        )

        return report_time_series_response
