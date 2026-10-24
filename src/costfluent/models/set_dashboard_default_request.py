from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SetDashboardDefaultRequest")


@_attrs_define
class SetDashboardDefaultRequest:
    """
    Attributes:
        workspace_id (str):
        is_default (bool):
    """

    workspace_id: str
    is_default: bool

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        is_default = self.is_default

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workspaceId": workspace_id,
                "isDefault": is_default,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        is_default = d.pop("isDefault")

        set_dashboard_default_request = cls(
            workspace_id=workspace_id,
            is_default=is_default,
        )

        return set_dashboard_default_request
