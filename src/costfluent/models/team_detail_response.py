from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.team_member_response import TeamMemberResponse
    from ..models.team_workspace_access_response import TeamWorkspaceAccessResponse


T = TypeVar("T", bound="TeamDetailResponse")


@_attrs_define
class TeamDetailResponse:
    """
    Attributes:
        id (str):
        name (str):
        is_system_team (bool):
        members (list[TeamMemberResponse]):
        workspace_access (list[TeamWorkspaceAccessResponse]):
        created_at (datetime.datetime):
    """

    id: str
    name: str
    is_system_team: bool
    members: list[TeamMemberResponse]
    workspace_access: list[TeamWorkspaceAccessResponse]
    created_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        is_system_team = self.is_system_team

        members = []
        for members_item_data in self.members:
            members_item = members_item_data.to_dict()
            members.append(members_item)

        workspace_access = []
        for workspace_access_item_data in self.workspace_access:
            workspace_access_item = workspace_access_item_data.to_dict()
            workspace_access.append(workspace_access_item)

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "isSystemTeam": is_system_team,
                "members": members,
                "workspaceAccess": workspace_access,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.team_member_response import TeamMemberResponse
        from ..models.team_workspace_access_response import TeamWorkspaceAccessResponse

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        is_system_team = d.pop("isSystemTeam")

        members = []
        _members = d.pop("members")
        for members_item_data in _members:
            members_item = TeamMemberResponse.from_dict(members_item_data)

            members.append(members_item)

        workspace_access = []
        _workspace_access = d.pop("workspaceAccess")
        for workspace_access_item_data in _workspace_access:
            workspace_access_item = TeamWorkspaceAccessResponse.from_dict(
                workspace_access_item_data
            )

            workspace_access.append(workspace_access_item)

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        team_detail_response = cls(
            id=id,
            name=name,
            is_system_team=is_system_team,
            members=members,
            workspace_access=workspace_access,
            created_at=created_at,
        )

        return team_detail_response
