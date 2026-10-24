from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AllocationRuleResponse")


@_attrs_define
class AllocationRuleResponse:
    """
    Attributes:
        id (str):
        name (str):
        priority (int):
        filter_ (str):
        cost_kind (str):
        segment_id (str):
        is_enabled (bool):
        created_at (datetime.datetime):
        segment_name (None | str | Unset):
        cost_centre (None | str | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    id: str
    name: str
    priority: int
    filter_: str
    cost_kind: str
    segment_id: str
    is_enabled: bool
    created_at: datetime.datetime
    segment_name: None | str | Unset = UNSET
    cost_centre: None | str | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        priority = self.priority

        filter_ = self.filter_

        cost_kind = self.cost_kind

        segment_id = self.segment_id

        is_enabled = self.is_enabled

        created_at = self.created_at.isoformat()

        segment_name: None | str | Unset
        if isinstance(self.segment_name, Unset):
            segment_name = UNSET
        else:
            segment_name = self.segment_name

        cost_centre: None | str | Unset
        if isinstance(self.cost_centre, Unset):
            cost_centre = UNSET
        else:
            cost_centre = self.cost_centre

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
                "name": name,
                "priority": priority,
                "filter": filter_,
                "costKind": cost_kind,
                "segmentId": segment_id,
                "isEnabled": is_enabled,
                "createdAt": created_at,
            }
        )
        if segment_name is not UNSET:
            field_dict["segmentName"] = segment_name
        if cost_centre is not UNSET:
            field_dict["costCentre"] = cost_centre
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        priority = d.pop("priority")

        filter_ = d.pop("filter")

        cost_kind = d.pop("costKind")

        segment_id = d.pop("segmentId")

        is_enabled = d.pop("isEnabled")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        def _parse_segment_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        segment_name = _parse_segment_name(d.pop("segmentName", UNSET))

        def _parse_cost_centre(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cost_centre = _parse_cost_centre(d.pop("costCentre", UNSET))

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

        allocation_rule_response = cls(
            id=id,
            name=name,
            priority=priority,
            filter_=filter_,
            cost_kind=cost_kind,
            segment_id=segment_id,
            is_enabled=is_enabled,
            created_at=created_at,
            segment_name=segment_name,
            cost_centre=cost_centre,
            updated_at=updated_at,
        )

        return allocation_rule_response
