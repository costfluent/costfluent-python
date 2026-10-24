from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..models.cost_group_dimension import CostGroupDimension
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportGroupingRequest")


@_attrs_define
class ReportGroupingRequest:
    """
    Attributes:
        dimension (CostGroupDimension):
        key (None | str | Unset):
    """

    dimension: CostGroupDimension
    key: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        dimension = self.dimension.value

        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dimension": dimension,
            }
        )
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        dimension = CostGroupDimension(d.pop("dimension"))

        def _parse_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key = _parse_key(d.pop("key", UNSET))

        report_grouping_request = cls(
            dimension=dimension,
            key=key,
        )

        return report_grouping_request
