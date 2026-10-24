from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SetTeamWorkspaceAccessRequest")


@_attrs_define
class SetTeamWorkspaceAccessRequest:
    """
    Attributes:
        access_level (str):
    """

    access_level: str

    def to_dict(self) -> dict[str, Any]:
        access_level = self.access_level

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "accessLevel": access_level,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        access_level = d.pop("accessLevel")

        set_team_workspace_access_request = cls(
            access_level=access_level,
        )

        return set_team_workspace_access_request
