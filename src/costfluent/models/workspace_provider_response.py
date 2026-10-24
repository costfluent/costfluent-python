from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkspaceProviderResponse")


@_attrs_define
class WorkspaceProviderResponse:
    """
    Attributes:
        id (str):
        workspace_id (str):
        provider_id (str):
        provider_name (str):
        is_enabled (bool):
        account_ids (list[str]):
        added_at (datetime.datetime):
        provider_key (None | str | Unset):
    """

    id: str
    workspace_id: str
    provider_id: str
    provider_name: str
    is_enabled: bool
    account_ids: list[str]
    added_at: datetime.datetime
    provider_key: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workspace_id = self.workspace_id

        provider_id = self.provider_id

        provider_name = self.provider_name

        is_enabled = self.is_enabled

        account_ids = self.account_ids

        added_at = self.added_at.isoformat()

        provider_key: None | str | Unset
        if isinstance(self.provider_key, Unset):
            provider_key = UNSET
        else:
            provider_key = self.provider_key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "workspaceId": workspace_id,
                "providerId": provider_id,
                "providerName": provider_name,
                "isEnabled": is_enabled,
                "accountIds": account_ids,
                "addedAt": added_at,
            }
        )
        if provider_key is not UNSET:
            field_dict["providerKey"] = provider_key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        workspace_id = d.pop("workspaceId")

        provider_id = d.pop("providerId")

        provider_name = d.pop("providerName")

        is_enabled = d.pop("isEnabled")

        account_ids = cast(list[str], d.pop("accountIds"))

        added_at = datetime.datetime.fromisoformat(d.pop("addedAt"))

        def _parse_provider_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_key = _parse_provider_key(d.pop("providerKey", UNSET))

        workspace_provider_response = cls(
            id=id,
            workspace_id=workspace_id,
            provider_id=provider_id,
            provider_name=provider_name,
            is_enabled=is_enabled,
            account_ids=account_ids,
            added_at=added_at,
            provider_key=provider_key,
        )

        return workspace_provider_response
