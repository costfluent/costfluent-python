from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="TeamMemberResponse")


@_attrs_define
class TeamMemberResponse:
    """
    Attributes:
        user_id (str):
        email (str):
        first_name (str):
        last_name (str):
        role (str):
        joined_at (datetime.datetime):
    """

    user_id: str
    email: str
    first_name: str
    last_name: str
    role: str
    joined_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        role = self.role

        joined_at = self.joined_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "userId": user_id,
                "email": email,
                "firstName": first_name,
                "lastName": last_name,
                "role": role,
                "joinedAt": joined_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        user_id = d.pop("userId")

        email = d.pop("email")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        role = d.pop("role")

        joined_at = datetime.datetime.fromisoformat(d.pop("joinedAt"))

        team_member_response = cls(
            user_id=user_id,
            email=email,
            first_name=first_name,
            last_name=last_name,
            role=role,
            joined_at=joined_at,
        )

        return team_member_response
