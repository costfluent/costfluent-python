from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetTeamDefaultDashboardRequest")


@_attrs_define
class SetTeamDefaultDashboardRequest:
    """
    Attributes:
        dashboard_id (None | str | Unset):
    """

    dashboard_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        dashboard_id: None | str | Unset
        if isinstance(self.dashboard_id, Unset):
            dashboard_id = UNSET
        else:
            dashboard_id = self.dashboard_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if dashboard_id is not UNSET:
            field_dict["dashboardId"] = dashboard_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_dashboard_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dashboard_id = _parse_dashboard_id(d.pop("dashboardId", UNSET))

        set_team_default_dashboard_request = cls(
            dashboard_id=dashboard_id,
        )

        return set_team_default_dashboard_request
