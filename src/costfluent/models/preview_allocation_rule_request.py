from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PreviewAllocationRuleRequest")


@_attrs_define
class PreviewAllocationRuleRequest:
    """
    Attributes:
        workspace_id (str):
        start_date (datetime.date):
        end_date (datetime.date):
        filter_ (str):
        segment_id (str):
        priority (int | Unset):
    """

    workspace_id: str
    start_date: datetime.date
    end_date: datetime.date
    filter_: str
    segment_id: str
    priority: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        filter_ = self.filter_

        segment_id = self.segment_id

        priority = self.priority

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workspaceId": workspace_id,
                "startDate": start_date,
                "endDate": end_date,
                "filter": filter_,
                "segmentId": segment_id,
            }
        )
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        start_date = datetime.date.fromisoformat(d.pop("startDate"))

        end_date = datetime.date.fromisoformat(d.pop("endDate"))

        filter_ = d.pop("filter")

        segment_id = d.pop("segmentId")

        priority = d.pop("priority", UNSET)

        preview_allocation_rule_request = cls(
            workspace_id=workspace_id,
            start_date=start_date,
            end_date=end_date,
            filter_=filter_,
            segment_id=segment_id,
            priority=priority,
        )

        return preview_allocation_rule_request
