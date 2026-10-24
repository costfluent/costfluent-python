from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AllocationCoverageShare")


@_attrs_define
class AllocationCoverageShare:
    """
    Attributes:
        segment_id (str):
        share (str):
    """

    segment_id: str
    share: str

    def to_dict(self) -> dict[str, Any]:
        segment_id = self.segment_id

        share = self.share

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "segmentId": segment_id,
                "share": share,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        segment_id = d.pop("segmentId")

        share = d.pop("share")

        allocation_coverage_share = cls(
            segment_id=segment_id,
            share=share,
        )

        return allocation_coverage_share
