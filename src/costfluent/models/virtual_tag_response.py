from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.virtual_tag_rule_response import VirtualTagRuleResponse


T = TypeVar("T", bound="VirtualTagResponse")


@_attrs_define
class VirtualTagResponse:
    """
    Attributes:
        id (str):
        key (str):
        collapsed_tag_keys (list[str]):
        rules (list[VirtualTagRuleResponse]):
        created_at (datetime.datetime):
        description (None | str | Unset):
        default_value (None | str | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    id: str
    key: str
    collapsed_tag_keys: list[str]
    rules: list[VirtualTagRuleResponse]
    created_at: datetime.datetime
    description: None | str | Unset = UNSET
    default_value: None | str | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        key = self.key

        collapsed_tag_keys = self.collapsed_tag_keys

        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()
            rules.append(rules_item)

        created_at = self.created_at.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        default_value: None | str | Unset
        if isinstance(self.default_value, Unset):
            default_value = UNSET
        else:
            default_value = self.default_value

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "key": key,
                "collapsedTagKeys": collapsed_tag_keys,
                "rules": rules,
                "createdAt": created_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.virtual_tag_rule_response import VirtualTagRuleResponse

        d = dict(src_dict)
        id = d.pop("id")

        key = d.pop("key")

        collapsed_tag_keys = cast(list[str], d.pop("collapsedTagKeys"))

        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = VirtualTagRuleResponse.from_dict(rules_item_data)

            rules.append(rules_item)

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_default_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_value = _parse_default_value(d.pop("defaultValue", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))

        virtual_tag_response = cls(
            id=id,
            key=key,
            collapsed_tag_keys=collapsed_tag_keys,
            rules=rules,
            created_at=created_at,
            description=description,
            default_value=default_value,
            updated_at=updated_at,
        )

        return virtual_tag_response
