from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.virtual_tag_rule_request import VirtualTagRuleRequest


T = TypeVar("T", bound="CreateVirtualTagRequest")


@_attrs_define
class CreateVirtualTagRequest:
    """
    Attributes:
        workspace_id (str):
        key (str):
        description (None | str | Unset):
        default_value (None | str | Unset):
        collapsed_tag_keys (list[str] | Unset):
        rules (list[VirtualTagRuleRequest] | Unset):
    """

    workspace_id: str
    key: str
    description: None | str | Unset = UNSET
    default_value: None | str | Unset = UNSET
    collapsed_tag_keys: list[str] | Unset = UNSET
    rules: list[VirtualTagRuleRequest] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        key = self.key

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

        collapsed_tag_keys: list[str] | Unset = UNSET
        if not isinstance(self.collapsed_tag_keys, Unset):
            collapsed_tag_keys = self.collapsed_tag_keys

        rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()
                rules.append(rules_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workspaceId": workspace_id,
                "key": key,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if collapsed_tag_keys is not UNSET:
            field_dict["collapsedTagKeys"] = collapsed_tag_keys
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.virtual_tag_rule_request import VirtualTagRuleRequest

        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        key = d.pop("key")

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

        collapsed_tag_keys = cast(list[str], d.pop("collapsedTagKeys", UNSET))

        _rules = d.pop("rules", UNSET)
        rules: list[VirtualTagRuleRequest] | Unset = UNSET
        if _rules is not UNSET:
            rules = []
            for rules_item_data in _rules:
                rules_item = VirtualTagRuleRequest.from_dict(rules_item_data)

                rules.append(rules_item)

        create_virtual_tag_request = cls(
            workspace_id=workspace_id,
            key=key,
            description=description,
            default_value=default_value,
            collapsed_tag_keys=collapsed_tag_keys,
            rules=rules,
        )

        return create_virtual_tag_request
