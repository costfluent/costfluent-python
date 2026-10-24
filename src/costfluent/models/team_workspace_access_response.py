from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="TeamWorkspaceAccessResponse")


@_attrs_define
class TeamWorkspaceAccessResponse:
    """
    Attributes:
        workspace_id (str):
        workspace_name (str):
        access_level (str):
    """

    workspace_id: str
    workspace_name: str
    access_level: str

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        workspace_name = self.workspace_name

        access_level = self.access_level

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workspaceId": workspace_id,
                "workspaceName": workspace_name,
                "accessLevel": access_level,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        workspace_name = d.pop("workspaceName")

        access_level = d.pop("accessLevel")

        team_workspace_access_response = cls(
            workspace_id=workspace_id,
            workspace_name=workspace_name,
            access_level=access_level,
        )

        return team_workspace_access_response
