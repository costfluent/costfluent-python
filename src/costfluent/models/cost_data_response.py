from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.cost_data_meta import CostDataMeta
    from ..models.cost_data_point import CostDataPoint
    from ..models.pagination_links import PaginationLinks


T = TypeVar("T", bound="CostDataResponse")


@_attrs_define
class CostDataResponse:
    """
    Attributes:
        links (PaginationLinks):
        data (list[CostDataPoint]):
        meta (CostDataMeta):
    """

    links: PaginationLinks
    data: list[CostDataPoint]
    meta: CostDataMeta

    def to_dict(self) -> dict[str, Any]:
        links = self.links.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "links": links,
                "data": data,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.cost_data_meta import CostDataMeta
        from ..models.cost_data_point import CostDataPoint
        from ..models.pagination_links import PaginationLinks

        d = dict(src_dict)
        links = PaginationLinks.from_dict(d.pop("links"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = CostDataPoint.from_dict(data_item_data)

            data.append(data_item)

        meta = CostDataMeta.from_dict(d.pop("meta"))

        cost_data_response = cls(
            links=links,
            data=data,
            meta=meta,
        )

        return cost_data_response
