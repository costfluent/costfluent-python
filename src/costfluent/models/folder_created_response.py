from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="FolderCreatedResponse")


@_attrs_define
class FolderCreatedResponse:
    """
    Attributes:
        id (str):
        title (str):
    """

    id: str
    title: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        folder_created_response = cls(
            id=id,
            title=title,
        )

        return folder_created_response
