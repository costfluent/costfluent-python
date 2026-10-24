from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="UpdateTeamMemberRequest")


@_attrs_define
class UpdateTeamMemberRequest:
    """
    Attributes:
        role (str):
    """

    role: str

    def to_dict(self) -> dict[str, Any]:
        role = self.role

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        role = d.pop("role")

        update_team_member_request = cls(
            role=role,
        )

        return update_team_member_request
