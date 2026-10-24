from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReorderAllocationRulesRequest")


@_attrs_define
class ReorderAllocationRulesRequest:
    """
    Attributes:
        workspace_id (str):
        rule_ids (list[str] | Unset):
    """

    workspace_id: str
    rule_ids: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        rule_ids: list[str] | Unset = UNSET
        if not isinstance(self.rule_ids, Unset):
            rule_ids = self.rule_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workspaceId": workspace_id,
            }
        )
        if rule_ids is not UNSET:
            field_dict["ruleIds"] = rule_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        rule_ids = cast(list[str], d.pop("ruleIds", UNSET))

        reorder_allocation_rules_request = cls(
            workspace_id=workspace_id,
            rule_ids=rule_ids,
        )

        return reorder_allocation_rules_request
