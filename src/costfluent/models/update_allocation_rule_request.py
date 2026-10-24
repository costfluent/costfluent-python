from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAllocationRuleRequest")


@_attrs_define
class UpdateAllocationRuleRequest:
    """
    Attributes:
        name (str):
        filter_ (str):
        segment_id (str):
        priority (int | None | Unset):
        is_enabled (bool | None | Unset):
    """

    name: str
    filter_: str
    segment_id: str
    priority: int | None | Unset = UNSET
    is_enabled: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        filter_ = self.filter_

        segment_id = self.segment_id

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        is_enabled: bool | None | Unset
        if isinstance(self.is_enabled, Unset):
            is_enabled = UNSET
        else:
            is_enabled = self.is_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
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
        name = d.pop("name")

        filter_ = d.pop("filter")

        segment_id = d.pop("segmentId")

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_is_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_enabled = _parse_is_enabled(d.pop("isEnabled", UNSET))

        update_allocation_rule_request = cls(
            name=name,
            filter_=filter_,
            segment_id=segment_id,
            priority=priority,
            is_enabled=is_enabled,
        )

        return update_allocation_rule_request
