from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_entry import CostEntry


T = TypeVar("T", bound="SubmitCostsRequest")


@_attrs_define
class SubmitCostsRequest:
    """
    Attributes:
        costs (list[CostEntry]):
        replace_lines (bool | Unset):
    """

    costs: list[CostEntry]
    replace_lines: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        costs = []
        for costs_item_data in self.costs:
            costs_item = costs_item_data.to_dict()
            costs.append(costs_item)

        replace_lines = self.replace_lines

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "costs": costs,
            }
        )
        if replace_lines is not UNSET:
            field_dict["replaceLines"] = replace_lines

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.cost_entry import CostEntry

        d = dict(src_dict)
        costs = []
        _costs = d.pop("costs")
        for costs_item_data in _costs:
            costs_item = CostEntry.from_dict(costs_item_data)

            costs.append(costs_item)

        replace_lines = d.pop("replaceLines", UNSET)

        submit_costs_request = cls(
            costs=costs,
            replace_lines=replace_lines,
        )

        return submit_costs_request
