from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostEstimateResourceRequest")


@_attrs_define
class CostEstimateResourceRequest:
    """
    Attributes:
        address (str):
        type_ (str):
        change (str):
        monthly_cost_before (None | str | Unset):
        monthly_cost_after (None | str | Unset):
        resource_ids (list[str] | None | Unset):
    """

    address: str
    type_: str
    change: str
    monthly_cost_before: None | str | Unset = UNSET
    monthly_cost_after: None | str | Unset = UNSET
    resource_ids: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        type_ = self.type_

        change = self.change

        monthly_cost_before: None | str | Unset
        if isinstance(self.monthly_cost_before, Unset):
            monthly_cost_before = UNSET
        else:
            monthly_cost_before = self.monthly_cost_before

        monthly_cost_after: None | str | Unset
        if isinstance(self.monthly_cost_after, Unset):
            monthly_cost_after = UNSET
        else:
            monthly_cost_after = self.monthly_cost_after

        resource_ids: list[str] | None | Unset
        if isinstance(self.resource_ids, Unset):
            resource_ids = UNSET
        elif isinstance(self.resource_ids, list):
            resource_ids = self.resource_ids

        else:
            resource_ids = self.resource_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "address": address,
                "type": type_,
                "change": change,
            }
        )
        if monthly_cost_before is not UNSET:
            field_dict["monthlyCostBefore"] = monthly_cost_before
        if monthly_cost_after is not UNSET:
            field_dict["monthlyCostAfter"] = monthly_cost_after
        if resource_ids is not UNSET:
            field_dict["resourceIds"] = resource_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        address = d.pop("address")

        type_ = d.pop("type")

        change = d.pop("change")

        def _parse_monthly_cost_before(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        monthly_cost_before = _parse_monthly_cost_before(
            d.pop("monthlyCostBefore", UNSET)
        )

        def _parse_monthly_cost_after(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        monthly_cost_after = _parse_monthly_cost_after(d.pop("monthlyCostAfter", UNSET))

        def _parse_resource_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                resource_ids_type_0 = cast(list[str], data)

                return resource_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        resource_ids = _parse_resource_ids(d.pop("resourceIds", UNSET))

        cost_estimate_resource_request = cls(
            address=address,
            type_=type_,
            change=change,
            monthly_cost_before=monthly_cost_before,
            monthly_cost_after=monthly_cost_after,
            resource_ids=resource_ids,
        )

        return cost_estimate_resource_request
