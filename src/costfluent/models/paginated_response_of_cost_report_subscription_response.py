from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.cost_report_subscription_response import (
        CostReportSubscriptionResponse,
    )
    from ..models.pagination_links import PaginationLinks


T = TypeVar("T", bound="PaginatedResponseOfCostReportSubscriptionResponse")


@_attrs_define
class PaginatedResponseOfCostReportSubscriptionResponse:
    """
    Attributes:
        links (PaginationLinks):
        data (list[CostReportSubscriptionResponse]):
    """

    links: PaginationLinks
    data: list[CostReportSubscriptionResponse]

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
        from ..models.cost_report_subscription_response import (
            CostReportSubscriptionResponse,
        )
        from ..models.pagination_links import PaginationLinks

        d = dict(src_dict)
        links = PaginationLinks.from_dict(d.pop("links"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = CostReportSubscriptionResponse.from_dict(data_item_data)

            data.append(data_item)

        paginated_response_of_cost_report_subscription_response = cls(
            links=links,
            data=data,
        )

        return paginated_response_of_cost_report_subscription_response
