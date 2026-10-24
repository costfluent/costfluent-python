from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.invitation_role import InvitationRole

T = TypeVar("T", bound="InviteUserRequest")


@_attrs_define
class InviteUserRequest:
    """
    Attributes:
        email (str):
        first_name (str):
        last_name (str):
        role (InvitationRole):
    """

    email: str
    first_name: str
    last_name: str
    role: InvitationRole

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        role = self.role.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "email": email,
                "firstName": first_name,
                "lastName": last_name,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        email = d.pop("email")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        role = InvitationRole(d.pop("role"))

        invite_user_request = cls(
            email=email,
            first_name=first_name,
            last_name=last_name,
            role=role,
        )

        return invite_user_request
