from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AddTeamMemberRequest")


@_attrs_define
class AddTeamMemberRequest:
    """
    Attributes:
        user_id (str):
        role (str):
    """

    user_id: str
    role: str

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        role = self.role

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "userId": user_id,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        user_id = d.pop("userId")

        role = d.pop("role")

        add_team_member_request = cls(
            user_id=user_id,
            role=role,
        )

        return add_team_member_request
