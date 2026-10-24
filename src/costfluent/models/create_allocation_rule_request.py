from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAllocationRuleRequest")


@_attrs_define
class CreateAllocationRuleRequest:
    """
    Attributes:
        workspace_id (str):
        name (str):
        filter_ (str):
        segment_id (str):
        priority (int | Unset):
        is_enabled (bool | Unset):
    """

    workspace_id: str
    name: str
    filter_: str
    segment_id: str
    priority: int | Unset = UNSET
    is_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        name = self.name

        filter_ = self.filter_

        segment_id = self.segment_id

        priority = self.priority

        is_enabled = self.is_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workspaceId": workspace_id,
                "name": name,
                "filter": filter_,
                "segmentId": segment_id,
            }
        )
        if priority is not UNSET:
            field_dict["priority"] = priority
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        name = d.pop("name")

        filter_ = d.pop("filter")

        segment_id = d.pop("segmentId")

        priority = d.pop("priority", UNSET)

        is_enabled = d.pop("isEnabled", UNSET)

        create_allocation_rule_request = cls(
            workspace_id=workspace_id,
            name=name,
            filter_=filter_,
            segment_id=segment_id,
            priority=priority,
            is_enabled=is_enabled,
        )

        return create_allocation_rule_request
