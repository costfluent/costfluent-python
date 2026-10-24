from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="TeamResponse")


@_attrs_define
class TeamResponse:
    """
    Attributes:
        id (str):
        name (str):
        is_system_team (bool):
        member_count (int):
        created_at (datetime.datetime):
    """

    id: str
    name: str
    is_system_team: bool
    member_count: int
    created_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        is_system_team = self.is_system_team

        member_count = self.member_count

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "isSystemTeam": is_system_team,
                "memberCount": member_count,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        is_system_team = d.pop("isSystemTeam")

        member_count = d.pop("memberCount")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        team_response = cls(
            id=id,
            name=name,
            is_system_team=is_system_team,
            member_count=member_count,
            created_at=created_at,
        )

        return team_response
