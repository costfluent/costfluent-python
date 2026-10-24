from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetFolderSavedFilterRequest")


@_attrs_define
class SetFolderSavedFilterRequest:
    """
    Attributes:
        workspace_id (str):
        saved_filter_id (None | str | Unset):
    """

    workspace_id: str
    saved_filter_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        saved_filter_id: None | str | Unset
        if isinstance(self.saved_filter_id, Unset):
            saved_filter_id = UNSET
        else:
            saved_filter_id = self.saved_filter_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workspaceId": workspace_id,
            }
        )
        if saved_filter_id is not UNSET:
            field_dict["savedFilterId"] = saved_filter_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        def _parse_saved_filter_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        saved_filter_id = _parse_saved_filter_id(d.pop("savedFilterId", UNSET))

        set_folder_saved_filter_request = cls(
            workspace_id=workspace_id,
            saved_filter_id=saved_filter_id,
        )

        return set_folder_saved_filter_request
