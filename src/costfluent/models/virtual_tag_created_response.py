from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="VirtualTagCreatedResponse")


@_attrs_define
class VirtualTagCreatedResponse:
    """
    Attributes:
        id (str):
        key (str):
    """

    id: str
    key: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        key = self.key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "key": key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        key = d.pop("key")

        virtual_tag_created_response = cls(
            id=id,
            key=key,
        )

        return virtual_tag_created_response
