from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSavedFilterRequest")


@_attrs_define
class CreateSavedFilterRequest:
    """
    Attributes:
        workspace_id (str):
        title (str):
        filter_ (str):
        is_default (bool | Unset):
    """

    workspace_id: str
    title: str
    filter_: str
    is_default: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        title = self.title

        filter_ = self.filter_

        is_default = self.is_default

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workspaceId": workspace_id,
                "title": title,
                "filter": filter_,
            }
        )
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        title = d.pop("title")

        filter_ = d.pop("filter")

        is_default = d.pop("isDefault", UNSET)

        create_saved_filter_request = cls(
            workspace_id=workspace_id,
            title=title,
            filter_=filter_,
            is_default=is_default,
        )

        return create_saved_filter_request
