from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SavedFilterResponse")


@_attrs_define
class SavedFilterResponse:
    """
    Attributes:
        id (str):
        title (str):
        filter_ (str):
        is_default (bool):
        created_at (datetime.datetime):
    """

    id: str
    title: str
    filter_: str
    is_default: bool
    created_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        filter_ = self.filter_

        is_default = self.is_default

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "title": title,
                "filter": filter_,
                "isDefault": is_default,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        filter_ = d.pop("filter")

        is_default = d.pop("isDefault")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        saved_filter_response = cls(
            id=id,
            title=title,
            filter_=filter_,
            is_default=is_default,
            created_at=created_at,
        )

        return saved_filter_response
