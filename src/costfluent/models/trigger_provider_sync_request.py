from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TriggerProviderSyncRequest")


@_attrs_define
class TriggerProviderSyncRequest:
    """
    Attributes:
        full_sync (bool | Unset):
    """

    full_sync: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        full_sync = self.full_sync

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if full_sync is not UNSET:
            field_dict["fullSync"] = full_sync

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        full_sync = d.pop("fullSync", UNSET)

        trigger_provider_sync_request = cls(
            full_sync=full_sync,
        )

        return trigger_provider_sync_request
