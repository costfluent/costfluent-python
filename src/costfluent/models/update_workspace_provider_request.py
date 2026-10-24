from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWorkspaceProviderRequest")


@_attrs_define
class UpdateWorkspaceProviderRequest:
    """
    Attributes:
        workspace_id (str):
        is_enabled (bool | None | Unset):
        account_ids (list[str] | None | Unset):
    """

    workspace_id: str
    is_enabled: bool | None | Unset = UNSET
    account_ids: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        is_enabled: bool | None | Unset
        if isinstance(self.is_enabled, Unset):
            is_enabled = UNSET
        else:
            is_enabled = self.is_enabled

        account_ids: list[str] | None | Unset
        if isinstance(self.account_ids, Unset):
            account_ids = UNSET
        elif isinstance(self.account_ids, list):
            account_ids = self.account_ids

        else:
            account_ids = self.account_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workspaceId": workspace_id,
            }
        )
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if account_ids is not UNSET:
            field_dict["accountIds"] = account_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        def _parse_is_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_enabled = _parse_is_enabled(d.pop("isEnabled", UNSET))

        def _parse_account_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                account_ids_type_0 = cast(list[str], data)

                return account_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        account_ids = _parse_account_ids(d.pop("accountIds", UNSET))

        update_workspace_provider_request = cls(
            workspace_id=workspace_id,
            is_enabled=is_enabled,
            account_ids=account_ids,
        )

        return update_workspace_provider_request
