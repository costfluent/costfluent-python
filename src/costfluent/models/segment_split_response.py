from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.segment_split_target_response import SegmentSplitTargetResponse


T = TypeVar("T", bound="SegmentSplitResponse")


@_attrs_define
class SegmentSplitResponse:
    """
    Attributes:
        method (str):
        targets (list[SegmentSplitTargetResponse]):
    """

    method: str
    targets: list[SegmentSplitTargetResponse]

    def to_dict(self) -> dict[str, Any]:
        method = self.method

        targets = []
        for targets_item_data in self.targets:
            targets_item = targets_item_data.to_dict()
            targets.append(targets_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "method": method,
                "targets": targets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.segment_split_target_response import SegmentSplitTargetResponse

        d = dict(src_dict)
        method = d.pop("method")

        targets = []
        _targets = d.pop("targets")
        for targets_item_data in _targets:
            targets_item = SegmentSplitTargetResponse.from_dict(targets_item_data)

            targets.append(targets_item)

        segment_split_response = cls(
            method=method,
            targets=targets,
        )

        return segment_split_response
