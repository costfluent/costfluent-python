from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateAnnotationRequest")


@_attrs_define
class CreateAnnotationRequest:
    """
    Attributes:
        workspace_id (str):
        date (datetime.date):
        text (str):
        cost_report_ids (list[str]):
    """

    workspace_id: str
    date: datetime.date
    text: str
    cost_report_ids: list[str]

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        date = self.date.isoformat()

        text = self.text

        cost_report_ids = self.cost_report_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workspaceId": workspace_id,
                "date": date,
                "text": text,
                "costReportIds": cost_report_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        date = datetime.date.fromisoformat(d.pop("date"))

        text = d.pop("text")

        cost_report_ids = cast(list[str], d.pop("costReportIds"))

        create_annotation_request = cls(
            workspace_id=workspace_id,
            date=date,
            text=text,
            cost_report_ids=cost_report_ids,
        )

        return create_annotation_request
