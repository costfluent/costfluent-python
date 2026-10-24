from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserResponse")


@_attrs_define
class UserResponse:
    """
    Attributes:
        id (str):
        email (str):
        first_name (str):
        last_name (str):
        role (str):
        status (str):
        joined_at (datetime.datetime):
        last_login_at (datetime.datetime | None | Unset):
        invite_expires_at (datetime.datetime | None | Unset):
    """

    id: str
    email: str
    first_name: str
    last_name: str
    role: str
    status: str
    joined_at: datetime.datetime
    last_login_at: datetime.datetime | None | Unset = UNSET
    invite_expires_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        role = self.role

        status = self.status

        joined_at = self.joined_at.isoformat()

        last_login_at: None | str | Unset
        if isinstance(self.last_login_at, Unset):
            last_login_at = UNSET
        elif isinstance(self.last_login_at, datetime.datetime):
            last_login_at = self.last_login_at.isoformat()
        else:
            last_login_at = self.last_login_at

        invite_expires_at: None | str | Unset
        if isinstance(self.invite_expires_at, Unset):
            invite_expires_at = UNSET
        elif isinstance(self.invite_expires_at, datetime.datetime):
            invite_expires_at = self.invite_expires_at.isoformat()
        else:
            invite_expires_at = self.invite_expires_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "email": email,
                "firstName": first_name,
                "lastName": last_name,
                "role": role,
                "status": status,
                "joinedAt": joined_at,
            }
        )
        if last_login_at is not UNSET:
            field_dict["lastLoginAt"] = last_login_at
        if invite_expires_at is not UNSET:
            field_dict["inviteExpiresAt"] = invite_expires_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        role = d.pop("role")

        status = d.pop("status")

        joined_at = datetime.datetime.fromisoformat(d.pop("joinedAt"))

        def _parse_last_login_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_login_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_login_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_login_at = _parse_last_login_at(d.pop("lastLoginAt", UNSET))

        def _parse_invite_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                invite_expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return invite_expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        invite_expires_at = _parse_invite_expires_at(d.pop("inviteExpiresAt", UNSET))

        user_response = cls(
            id=id,
            email=email,
            first_name=first_name,
            last_name=last_name,
            role=role,
            status=status,
            joined_at=joined_at,
            last_login_at=last_login_at,
            invite_expires_at=invite_expires_at,
        )

        return user_response
