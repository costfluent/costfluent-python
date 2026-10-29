from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="AppliedResourceRequest")


@_attrs_define
class AppliedResourceRequest:
    """
    Attributes:
        address (str):
        resource_ids (list[str]):
    """

    address: str
    resource_ids: list[str]

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        resource_ids = self.resource_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "address": address,
                "resourceIds": resource_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        address = d.pop("address")

        resource_ids = cast(list[str], d.pop("resourceIds"))

        applied_resource_request = cls(
            address=address,
            resource_ids=resource_ids,
        )

        return applied_resource_request
