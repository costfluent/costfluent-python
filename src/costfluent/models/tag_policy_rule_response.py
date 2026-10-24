from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TagPolicyRuleResponse")


@_attrs_define
class TagPolicyRuleResponse:
    """
    Attributes:
        account_ids (list[str]):
        required_keys (list[str]):
        provider (None | str | Unset):
    """

    account_ids: list[str]
    required_keys: list[str]
    provider: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        account_ids = self.account_ids

        required_keys = self.required_keys

        provider: None | str | Unset
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "accountIds": account_ids,
                "requiredKeys": required_keys,
            }
        )
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        account_ids = cast(list[str], d.pop("accountIds"))

        required_keys = cast(list[str], d.pop("requiredKeys"))

        def _parse_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider = _parse_provider(d.pop("provider", UNSET))

        tag_policy_rule_response = cls(
            account_ids=account_ids,
            required_keys=required_keys,
            provider=provider,
        )

        return tag_policy_rule_response
