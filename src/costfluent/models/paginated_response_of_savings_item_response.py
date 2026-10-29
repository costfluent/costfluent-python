from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.pagination_links import PaginationLinks
    from ..models.savings_item_response import SavingsItemResponse


T = TypeVar("T", bound="PaginatedResponseOfSavingsItemResponse")


@_attrs_define
class PaginatedResponseOfSavingsItemResponse:
    """
    Attributes:
        links (PaginationLinks):
        data (list[SavingsItemResponse]):
    """

    links: PaginationLinks
    data: list[SavingsItemResponse]

    def to_dict(self) -> dict[str, Any]:
        links = self.links.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

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
        from ..models.savings_item_response import SavingsItemResponse

        d = dict(src_dict)
        links = PaginationLinks.from_dict(d.pop("links"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = SavingsItemResponse.from_dict(data_item_data)

            data.append(data_item)

        paginated_response_of_savings_item_response = cls(
            links=links,
            data=data,
        )

        return paginated_response_of_savings_item_response
