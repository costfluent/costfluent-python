from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.segment_split_method_value import SegmentSplitMethodValue
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.segment_split_target_request import SegmentSplitTargetRequest


T = TypeVar("T", bound="SegmentSplitRequest")


@_attrs_define
class SegmentSplitRequest:
    """
    Attributes:
        method (SegmentSplitMethodValue | Unset):
        targets (list[SegmentSplitTargetRequest] | Unset):
    """

    method: SegmentSplitMethodValue | Unset = UNSET
    targets: list[SegmentSplitTargetRequest] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        targets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()
                targets.append(targets_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if method is not UNSET:
            field_dict["method"] = method
        if targets is not UNSET:
            field_dict["targets"] = targets

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.segment_split_target_request import SegmentSplitTargetRequest

        d = dict(src_dict)
        _method = d.pop("method", UNSET)
        method: SegmentSplitMethodValue | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = SegmentSplitMethodValue(_method)

        _targets = d.pop("targets", UNSET)
        targets: list[SegmentSplitTargetRequest] | Unset = UNSET
        if _targets is not UNSET:
            targets = []
            for targets_item_data in _targets:
                targets_item = SegmentSplitTargetRequest.from_dict(targets_item_data)

                targets.append(targets_item)

        segment_split_request = cls(
            method=method,
            targets=targets,
        )

        return segment_split_request
