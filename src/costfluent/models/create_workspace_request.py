from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWorkspaceRequest")


@_attrs_define
class CreateWorkspaceRequest:
    """
    Attributes:
        name (str):
        currency (str):
        time_zone (None | str | Unset):
    """

    name: str
    currency: str
    time_zone: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        currency = self.currency

        time_zone: None | str | Unset
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = self.time_zone

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "currency": currency,
            }
        )
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        currency = d.pop("currency")

        def _parse_time_zone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_zone = _parse_time_zone(d.pop("timeZone", UNSET))

        create_workspace_request = cls(
            name=name,
            currency=currency,
            time_zone=time_zone,
        )

        return create_workspace_request
