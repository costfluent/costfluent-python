from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SavingsItemActionRequest")


@_attrs_define
class SavingsItemActionRequest:
    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        savings_item_action_request = cls()

        return savings_item_action_request
