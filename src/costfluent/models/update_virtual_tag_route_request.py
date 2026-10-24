from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.virtual_tag_rule_request import VirtualTagRuleRequest


T = TypeVar("T", bound="UpdateVirtualTagRouteRequest")


@_attrs_define
class UpdateVirtualTagRouteRequest:
    """
    Attributes:
        workspace_id (str):
        key (None | str | Unset):
        description (None | str | Unset):
        clear_description (bool | Unset):
        default_value (None | str | Unset):
        clear_default_value (bool | Unset):
        collapsed_tag_keys (list[str] | None | Unset):
        rules (list[VirtualTagRuleRequest] | None | Unset):
    """

    workspace_id: str
    key: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    clear_description: bool | Unset = UNSET
    default_value: None | str | Unset = UNSET
    clear_default_value: bool | Unset = UNSET
    collapsed_tag_keys: list[str] | None | Unset = UNSET
    rules: list[VirtualTagRuleRequest] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        clear_description = self.clear_description

        default_value: None | str | Unset
        if isinstance(self.default_value, Unset):
            default_value = UNSET
        else:
            default_value = self.default_value

        clear_default_value = self.clear_default_value

        collapsed_tag_keys: list[str] | None | Unset
        if isinstance(self.collapsed_tag_keys, Unset):
            collapsed_tag_keys = UNSET
        elif isinstance(self.collapsed_tag_keys, list):
            collapsed_tag_keys = self.collapsed_tag_keys

        else:
            collapsed_tag_keys = self.collapsed_tag_keys

        rules: list[dict[str, Any]] | None | Unset
        if isinstance(self.rules, Unset):
            rules = UNSET
        elif isinstance(self.rules, list):
            rules = []
            for rules_type_0_item_data in self.rules:
                rules_type_0_item = rules_type_0_item_data.to_dict()
                rules.append(rules_type_0_item)

        else:
            rules = self.rules

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workspaceId": workspace_id,
            }
        )
        if key is not UNSET:
            field_dict["key"] = key
        if description is not UNSET:
            field_dict["description"] = description
        if clear_description is not UNSET:
            field_dict["clearDescription"] = clear_description
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if clear_default_value is not UNSET:
            field_dict["clearDefaultValue"] = clear_default_value
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

        def _parse_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key = _parse_key(d.pop("key", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        clear_description = d.pop("clearDescription", UNSET)

        def _parse_default_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_value = _parse_default_value(d.pop("defaultValue", UNSET))

        clear_default_value = d.pop("clearDefaultValue", UNSET)

        def _parse_collapsed_tag_keys(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                collapsed_tag_keys_type_0 = cast(list[str], data)

                return collapsed_tag_keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        collapsed_tag_keys = _parse_collapsed_tag_keys(d.pop("collapsedTagKeys", UNSET))

        def _parse_rules(data: object) -> list[VirtualTagRuleRequest] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rules_type_0 = []
                _rules_type_0 = data
                for rules_type_0_item_data in _rules_type_0:
                    rules_type_0_item = VirtualTagRuleRequest.from_dict(
                        rules_type_0_item_data
                    )

                    rules_type_0.append(rules_type_0_item)

                return rules_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VirtualTagRuleRequest] | None | Unset, data)

        rules = _parse_rules(d.pop("rules", UNSET))

        update_virtual_tag_route_request = cls(
            workspace_id=workspace_id,
            key=key,
            description=description,
            clear_description=clear_description,
            default_value=default_value,
            clear_default_value=clear_default_value,
            collapsed_tag_keys=collapsed_tag_keys,
            rules=rules,
        )

        return update_virtual_tag_route_request
