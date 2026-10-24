from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="UserInvitedResponse")


@_attrs_define
class UserInvitedResponse:
    """
    Attributes:
        id (str):
        email (str):
    """

    id: str
    email: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "email": email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        user_invited_response = cls(
            id=id,
            email=email,
        )

        return user_invited_response
