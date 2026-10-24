from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateFolderRequest")


@_attrs_define
class UpdateFolderRequest:
    """
    Attributes:
        workspace_id (str):
        title (None | str | Unset):
        parent_id (None | str | Unset):
        clear_parent (bool | Unset):
    """

    workspace_id: str
    title: None | str | Unset = UNSET
    parent_id: None | str | Unset = UNSET
    clear_parent: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        clear_parent = self.clear_parent

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workspaceId": workspace_id,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if clear_parent is not UNSET:
            field_dict["clearParent"] = clear_parent

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_parent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))

        clear_parent = d.pop("clearParent", UNSET)

        update_folder_request = cls(
            workspace_id=workspace_id,
            title=title,
            parent_id=parent_id,
            clear_parent=clear_parent,
        )

        return update_folder_request
