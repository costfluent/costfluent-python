from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SegmentSplitTargetRequest")


@_attrs_define
class SegmentSplitTargetRequest:
    """
    Attributes:
        segment_id (str):
        percent (float | None | Unset):
    """

    segment_id: str
    percent: float | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        segment_id = self.segment_id

        percent: float | None | Unset
        if isinstance(self.percent, Unset):
            percent = UNSET
        else:
            percent = self.percent

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "segmentId": segment_id,
            }
        )
        if percent is not UNSET:
            field_dict["percent"] = percent

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        segment_id = d.pop("segmentId")

        def _parse_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        percent = _parse_percent(d.pop("percent", UNSET))

        segment_split_target_request = cls(
            segment_id=segment_id,
            percent=percent,
        )

        return segment_split_target_request
