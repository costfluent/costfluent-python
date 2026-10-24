from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.pagination_links import PaginationLinks


T = TypeVar("T", bound="PaginatedResponseOfString")


@_attrs_define
class PaginatedResponseOfString:
    """
    Attributes:
        links (PaginationLinks):
        data (list[str]):
    """

    links: PaginationLinks
    data: list[str]

    def to_dict(self) -> dict[str, Any]:
        links = self.links.to_dict()

        data = self.data

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "links": links,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pagination_links import PaginationLinks

        d = dict(src_dict)
        links = PaginationLinks.from_dict(d.pop("links"))

        data = cast(list[str], d.pop("data"))

        paginated_response_of_string = cls(
            links=links,
            data=data,
        )

        return paginated_response_of_string
