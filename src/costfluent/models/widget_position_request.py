from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WidgetPositionRequest")


@_attrs_define
class WidgetPositionRequest:
    """
    Attributes:
        x (int | Unset):
        y (int | Unset):
        w (int | Unset):
        h (int | Unset):
    """

    x: int | Unset = UNSET
    y: int | Unset = UNSET
    w: int | Unset = UNSET
    h: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        x = self.x

        y = self.y

        w = self.w

        h = self.h

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y
        if w is not UNSET:
            field_dict["w"] = w
        if h is not UNSET:
            field_dict["h"] = h

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        x = d.pop("x", UNSET)

        y = d.pop("y", UNSET)

        w = d.pop("w", UNSET)

        h = d.pop("h", UNSET)

        widget_position_request = cls(
            x=x,
            y=y,
            w=w,
            h=h,
        )

        return widget_position_request
