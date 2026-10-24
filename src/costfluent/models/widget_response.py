from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.widget_position_response import WidgetPositionResponse
    from ..models.widget_response_config_type_0 import WidgetResponseConfigType0


T = TypeVar("T", bound="WidgetResponse")


@_attrs_define
class WidgetResponse:
    """
    Attributes:
        id (str):
        type_ (str):
        title (str):
        position (WidgetPositionResponse):
        cost_report_id (None | str | Unset):
        display (None | str | Unset):
        content (None | str | Unset):
        config (None | Unset | WidgetResponseConfigType0):
    """

    id: str
    type_: str
    title: str
    position: WidgetPositionResponse
    cost_report_id: None | str | Unset = UNSET
    display: None | str | Unset = UNSET
    content: None | str | Unset = UNSET
    config: None | Unset | WidgetResponseConfigType0 = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.widget_response_config_type_0 import WidgetResponseConfigType0

        id = self.id

        type_ = self.type_

        title = self.title

        position = self.position.to_dict()

        cost_report_id: None | str | Unset
        if isinstance(self.cost_report_id, Unset):
            cost_report_id = UNSET
        else:
            cost_report_id = self.cost_report_id

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

        config: dict[str, Any] | None | Unset
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, WidgetResponseConfigType0):
            config = self.config.to_dict()
        else:
            config = self.config

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "type": type_,
                "title": title,
                "position": position,
            }
        )
        if cost_report_id is not UNSET:
            field_dict["costReportId"] = cost_report_id
        if display is not UNSET:
            field_dict["display"] = display
        if content is not UNSET:
            field_dict["content"] = content
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.widget_position_response import WidgetPositionResponse
        from ..models.widget_response_config_type_0 import WidgetResponseConfigType0

        d = dict(src_dict)
        id = d.pop("id")

        type_ = d.pop("type")

        title = d.pop("title")

        position = WidgetPositionResponse.from_dict(d.pop("position"))

        def _parse_cost_report_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cost_report_id = _parse_cost_report_id(d.pop("costReportId", UNSET))

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

        def _parse_config(data: object) -> None | Unset | WidgetResponseConfigType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = WidgetResponseConfigType0.from_dict(data)

                return config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WidgetResponseConfigType0, data)

        config = _parse_config(d.pop("config", UNSET))

        widget_response = cls(
            id=id,
            type_=type_,
            title=title,
            position=position,
            cost_report_id=cost_report_id,
            display=display,
            content=content,
            config=config,
        )

        return widget_response
