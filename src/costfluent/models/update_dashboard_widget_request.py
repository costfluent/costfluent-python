from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.widget_position_request import WidgetPositionRequest


T = TypeVar("T", bound="UpdateDashboardWidgetRequest")


@_attrs_define
class UpdateDashboardWidgetRequest:
    """
    Attributes:
        title (None | str | Unset):
        display (None | str | Unset):
        content (None | str | Unset):
        position (None | Unset | WidgetPositionRequest):
    """

    title: None | str | Unset = UNSET
    display: None | str | Unset = UNSET
    content: None | str | Unset = UNSET
    position: None | Unset | WidgetPositionRequest = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.widget_position_request import WidgetPositionRequest

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        display: None | str | Unset
        if isinstance(self.display, Unset):
            display = UNSET
        else:
            display = self.display

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        position: dict[str, Any] | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        elif isinstance(self.position, WidgetPositionRequest):
            position = self.position.to_dict()
        else:
            position = self.position

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if display is not UNSET:
            field_dict["display"] = display
        if content is not UNSET:
            field_dict["content"] = content
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.widget_position_request import WidgetPositionRequest

        d = dict(src_dict)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_display(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display = _parse_display(d.pop("display", UNSET))

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        def _parse_position(data: object) -> None | Unset | WidgetPositionRequest:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                position_type_0 = WidgetPositionRequest.from_dict(data)

                return position_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WidgetPositionRequest, data)

        position = _parse_position(d.pop("position", UNSET))

        update_dashboard_widget_request = cls(
            title=title,
            display=display,
            content=content,
            position=position,
        )

        return update_dashboard_widget_request
