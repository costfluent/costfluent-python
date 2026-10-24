from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.widget_position_request import WidgetPositionRequest


T = TypeVar("T", bound="CreateDashboardWidgetRequest")


@_attrs_define
class CreateDashboardWidgetRequest:
    """
    Attributes:
        title (str):
        position (WidgetPositionRequest):
        type_ (str | Unset):
        cost_report_id (None | str | Unset):
        display (None | str | Unset):
        content (None | str | Unset):
    """

    title: str
    position: WidgetPositionRequest
    type_: str | Unset = UNSET
    cost_report_id: None | str | Unset = UNSET
    display: None | str | Unset = UNSET
    content: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        position = self.position.to_dict()

        type_ = self.type_

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

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "title": title,
                "position": position,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if cost_report_id is not UNSET:
            field_dict["costReportId"] = cost_report_id
        if display is not UNSET:
            field_dict["display"] = display
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.widget_position_request import WidgetPositionRequest

        d = dict(src_dict)
        title = d.pop("title")

        position = WidgetPositionRequest.from_dict(d.pop("position"))

        type_ = d.pop("type", UNSET)

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

        create_dashboard_widget_request = cls(
            title=title,
            position=position,
            type_=type_,
            cost_report_id=cost_report_id,
            display=display,
            content=content,
        )

        return create_dashboard_widget_request
