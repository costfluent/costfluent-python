from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.tag_policy_rule_request import TagPolicyRuleRequest


T = TypeVar("T", bound="UpdateTagPolicyRequest")


@_attrs_define
class UpdateTagPolicyRequest:
    """
    Attributes:
        rules (list[TagPolicyRuleRequest]):
    """

    rules: list[TagPolicyRuleRequest]

    def to_dict(self) -> dict[str, Any]:
        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()
            rules.append(rules_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "rules": rules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.tag_policy_rule_request import TagPolicyRuleRequest

        d = dict(src_dict)
        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = TagPolicyRuleRequest.from_dict(rules_item_data)

            rules.append(rules_item)

        update_tag_policy_request = cls(
            rules=rules,
        )

        return update_tag_policy_request
