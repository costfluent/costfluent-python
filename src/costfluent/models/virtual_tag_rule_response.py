from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="VirtualTagRuleResponse")


@_attrs_define
class VirtualTagRuleResponse:
    """
    Attributes:
        value (str):
        filter_ (str):
    """

    value: str
    filter_: str

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        filter_ = self.filter_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "value": value,
                "filter": filter_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        value = d.pop("value")

        filter_ = d.pop("filter")

        virtual_tag_rule_response = cls(
            value=value,
            filter_=filter_,
        )

        return virtual_tag_rule_response
