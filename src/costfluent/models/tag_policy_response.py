from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tag_policy_rule_response import TagPolicyRuleResponse


T = TypeVar("T", bound="TagPolicyResponse")


@_attrs_define
class TagPolicyResponse:
    """
    Attributes:
        rules (list[TagPolicyRuleResponse]):
        report_id (None | str | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    rules: list[TagPolicyRuleResponse]
    report_id: None | str | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()
            rules.append(rules_item)

        report_id: None | str | Unset
        if isinstance(self.report_id, Unset):
            report_id = UNSET
        else:
            report_id = self.report_id

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
                "rules": rules,
            }
        )
        if report_id is not UNSET:
            field_dict["reportId"] = report_id
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.tag_policy_rule_response import TagPolicyRuleResponse

        d = dict(src_dict)
        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = TagPolicyRuleResponse.from_dict(rules_item_data)

            rules.append(rules_item)

        def _parse_report_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        report_id = _parse_report_id(d.pop("reportId", UNSET))

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

        tag_policy_response = cls(
            rules=rules,
            report_id=report_id,
            updated_at=updated_at,
        )

        return tag_policy_response
