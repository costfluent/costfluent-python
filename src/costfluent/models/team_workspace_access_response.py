from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamWorkspaceAccessResponse")


@_attrs_define
class TeamWorkspaceAccessResponse:
    """
    Attributes:
        workspace_id (str):
        workspace_name (str):
        access_level (str):
        default_dashboard_id (None | str | Unset):
    """

    workspace_id: str
    workspace_name: str
    access_level: str
    default_dashboard_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        workspace_name = self.workspace_name

        access_level = self.access_level

        default_dashboard_id: None | str | Unset
        if isinstance(self.default_dashboard_id, Unset):
            default_dashboard_id = UNSET
        else:
            default_dashboard_id = self.default_dashboard_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workspaceId": workspace_id,
                "workspaceName": workspace_name,
                "accessLevel": access_level,
            }
        )
        if default_dashboard_id is not UNSET:
            field_dict["defaultDashboardId"] = default_dashboard_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        workspace_name = d.pop("workspaceName")

        access_level = d.pop("accessLevel")

        def _parse_default_dashboard_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_dashboard_id = _parse_default_dashboard_id(
            d.pop("defaultDashboardId", UNSET)
        )

        team_workspace_access_response = cls(
            workspace_id=workspace_id,
            workspace_name=workspace_name,
            access_level=access_level,
            default_dashboard_id=default_dashboard_id,
        )

        return team_workspace_access_response
