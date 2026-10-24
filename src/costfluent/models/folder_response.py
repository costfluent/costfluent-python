from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FolderResponse")


@_attrs_define
class FolderResponse:
    """
    Attributes:
        id (str):
        title (str):
        report_count (int):
        parent_id (None | str | Unset):
        children (list[FolderResponse] | None | Unset):
        saved_filter_id (None | str | Unset):
    """

    id: str
    title: str
    report_count: int
    parent_id: None | str | Unset = UNSET
    children: list[FolderResponse] | None | Unset = UNSET
    saved_filter_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        report_count = self.report_count

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        children: list[dict[str, Any]] | None | Unset
        if isinstance(self.children, Unset):
            children = UNSET
        elif isinstance(self.children, list):
            children = []
            for children_type_0_item_data in self.children:
                children_type_0_item = children_type_0_item_data.to_dict()
                children.append(children_type_0_item)

        else:
            children = self.children

        saved_filter_id: None | str | Unset
        if isinstance(self.saved_filter_id, Unset):
            saved_filter_id = UNSET
        else:
            saved_filter_id = self.saved_filter_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "title": title,
                "reportCount": report_count,
            }
        )
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if children is not UNSET:
            field_dict["children"] = children
        if saved_filter_id is not UNSET:
            field_dict["savedFilterId"] = saved_filter_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        report_count = d.pop("reportCount")

        def _parse_parent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))

        def _parse_children(data: object) -> list[FolderResponse] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                children_type_0 = []
                _children_type_0 = data
                for children_type_0_item_data in _children_type_0:
                    children_type_0_item = FolderResponse.from_dict(
                        children_type_0_item_data
                    )

                    children_type_0.append(children_type_0_item)

                return children_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FolderResponse] | None | Unset, data)

        children = _parse_children(d.pop("children", UNSET))

        def _parse_saved_filter_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        saved_filter_id = _parse_saved_filter_id(d.pop("savedFilterId", UNSET))

        folder_response = cls(
            id=id,
            title=title,
            report_count=report_count,
            parent_id=parent_id,
            children=children,
            saved_filter_id=saved_filter_id,
        )

        return folder_response
