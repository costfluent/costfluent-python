from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ProviderCreatedResponse")


@_attrs_define
class ProviderCreatedResponse:
    """
    Attributes:
        id (str):
        type_ (str):
        key (str):
        name (str):
    """

    id: str
    type_: str
    key: str
    name: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        key = self.key

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "type": type_,
                "key": key,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = d.pop("type")

        key = d.pop("key")

        name = d.pop("name")

        provider_created_response = cls(
            id=id,
            type_=type_,
            key=key,
            name=name,
        )

        return provider_created_response
