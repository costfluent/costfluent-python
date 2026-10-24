from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WidgetPositionResponse")


@_attrs_define
class WidgetPositionResponse:
    """
    Attributes:
        x (int):
        y (int):
        w (int):
        h (int):
    """

    x: int
    y: int
    w: int
    h: int

    def to_dict(self) -> dict[str, Any]:
        x = self.x

        y = self.y

        w = self.w

        h = self.h

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "x": x,
                "y": y,
                "w": w,
                "h": h,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        x = d.pop("x")

        y = d.pop("y")

        w = d.pop("w")

        h = d.pop("h")

        widget_position_response = cls(
            x=x,
            y=y,
            w=w,
            h=h,
        )

        return widget_position_response
