from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostEstimateResourceResponse")


@_attrs_define
class CostEstimateResourceResponse:
    """
    Attributes:
        address (str):
        type_ (str):
        change (str):
        resource_ids (list[str]):
        applied_resource_ids (list[str]):
        monthly_cost_before (None | str | Unset):
        monthly_cost_after (None | str | Unset):
        planned_change (None | str | Unset):
        match (None | str | Unset):
        actual_monthly_cost_before (None | str | Unset):
        actual_monthly_cost_after (None | str | Unset):
        actual_change (None | str | Unset):
    """

    address: str
    type_: str
    change: str
    resource_ids: list[str]
    applied_resource_ids: list[str]
    monthly_cost_before: None | str | Unset = UNSET
    monthly_cost_after: None | str | Unset = UNSET
    planned_change: None | str | Unset = UNSET
    match: None | str | Unset = UNSET
    actual_monthly_cost_before: None | str | Unset = UNSET
    actual_monthly_cost_after: None | str | Unset = UNSET
    actual_change: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        type_ = self.type_

        change = self.change

        resource_ids = self.resource_ids

        applied_resource_ids = self.applied_resource_ids

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

        planned_change: None | str | Unset
        if isinstance(self.planned_change, Unset):
            planned_change = UNSET
        else:
            planned_change = self.planned_change

        match: None | str | Unset
        if isinstance(self.match, Unset):
            match = UNSET
        else:
            match = self.match

        actual_monthly_cost_before: None | str | Unset
        if isinstance(self.actual_monthly_cost_before, Unset):
            actual_monthly_cost_before = UNSET
        else:
            actual_monthly_cost_before = self.actual_monthly_cost_before

        actual_monthly_cost_after: None | str | Unset
        if isinstance(self.actual_monthly_cost_after, Unset):
            actual_monthly_cost_after = UNSET
        else:
            actual_monthly_cost_after = self.actual_monthly_cost_after

        actual_change: None | str | Unset
        if isinstance(self.actual_change, Unset):
            actual_change = UNSET
        else:
            actual_change = self.actual_change

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "address": address,
                "type": type_,
                "change": change,
                "resourceIds": resource_ids,
                "appliedResourceIds": applied_resource_ids,
            }
        )
        if monthly_cost_before is not UNSET:
            field_dict["monthlyCostBefore"] = monthly_cost_before
        if monthly_cost_after is not UNSET:
            field_dict["monthlyCostAfter"] = monthly_cost_after
        if planned_change is not UNSET:
            field_dict["plannedChange"] = planned_change
        if match is not UNSET:
            field_dict["match"] = match
        if actual_monthly_cost_before is not UNSET:
            field_dict["actualMonthlyCostBefore"] = actual_monthly_cost_before
        if actual_monthly_cost_after is not UNSET:
            field_dict["actualMonthlyCostAfter"] = actual_monthly_cost_after
        if actual_change is not UNSET:
            field_dict["actualChange"] = actual_change

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        address = d.pop("address")

        type_ = d.pop("type")

        change = d.pop("change")

        resource_ids = cast(list[str], d.pop("resourceIds"))

        applied_resource_ids = cast(list[str], d.pop("appliedResourceIds"))

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

        def _parse_planned_change(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        planned_change = _parse_planned_change(d.pop("plannedChange", UNSET))

        def _parse_match(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        match = _parse_match(d.pop("match", UNSET))

        def _parse_actual_monthly_cost_before(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        actual_monthly_cost_before = _parse_actual_monthly_cost_before(
            d.pop("actualMonthlyCostBefore", UNSET)
        )

        def _parse_actual_monthly_cost_after(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        actual_monthly_cost_after = _parse_actual_monthly_cost_after(
            d.pop("actualMonthlyCostAfter", UNSET)
        )

        def _parse_actual_change(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        actual_change = _parse_actual_change(d.pop("actualChange", UNSET))

        cost_estimate_resource_response = cls(
            address=address,
            type_=type_,
            change=change,
            resource_ids=resource_ids,
            applied_resource_ids=applied_resource_ids,
            monthly_cost_before=monthly_cost_before,
            monthly_cost_after=monthly_cost_after,
            planned_change=planned_change,
            match=match,
            actual_monthly_cost_before=actual_monthly_cost_before,
            actual_monthly_cost_after=actual_monthly_cost_after,
            actual_change=actual_change,
        )

        return cost_estimate_resource_response
