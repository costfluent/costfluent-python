from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.anomaly_response import AnomalyResponse
    from ..models.pagination_links import PaginationLinks


T = TypeVar("T", bound="PaginatedResponseOfAnomalyResponse")


@_attrs_define
class PaginatedResponseOfAnomalyResponse:
    """
    Attributes:
        links (PaginationLinks):
        data (list[AnomalyResponse]):
    """

    links: PaginationLinks
    data: list[AnomalyResponse]

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
        from ..models.anomaly_response import AnomalyResponse
        from ..models.pagination_links import PaginationLinks

        d = dict(src_dict)
        links = PaginationLinks.from_dict(d.pop("links"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = AnomalyResponse.from_dict(data_item_data)

            data.append(data_item)

        paginated_response_of_anomaly_response = cls(
            links=links,
            data=data,
        )

        return paginated_response_of_anomaly_response
