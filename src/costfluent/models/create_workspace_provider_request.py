from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWorkspaceProviderRequest")


@_attrs_define
class CreateWorkspaceProviderRequest:
    """
    Attributes:
        workspace_id (str):
        provider_id (str):
        account_ids (list[str] | None | Unset):
    """

    workspace_id: str
    provider_id: str
    account_ids: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        provider_id = self.provider_id

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
                "providerId": provider_id,
            }
        )
        if account_ids is not UNSET:
            field_dict["accountIds"] = account_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        provider_id = d.pop("providerId")

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

        create_workspace_provider_request = cls(
            workspace_id=workspace_id,
            provider_id=provider_id,
            account_ids=account_ids,
        )

        return create_workspace_provider_request
