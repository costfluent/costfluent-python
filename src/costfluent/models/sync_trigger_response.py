from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SyncTriggerResponse")


@_attrs_define
class SyncTriggerResponse:
    """
    Attributes:
        triggered (bool):
        message (None | str | Unset):
    """

    triggered: bool
    message: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        triggered = self.triggered

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "triggered": triggered,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        triggered = d.pop("triggered")

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        sync_trigger_response = cls(
            triggered=triggered,
            message=message,
        )

        return sync_trigger_response
