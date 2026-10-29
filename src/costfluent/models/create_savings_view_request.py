from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSavingsViewRequest")


@_attrs_define
class CreateSavingsViewRequest:
    """
    Attributes:
        workspace_id (str):
        title (str):
        tab (str):
        source (None | str | Unset):
        kind (None | str | Unset):
        cloud_account_id (None | str | Unset):
        minimum_monthly_saving (None | str | Unset):
    """

    workspace_id: str
    title: str
    tab: str
    source: None | str | Unset = UNSET
    kind: None | str | Unset = UNSET
    cloud_account_id: None | str | Unset = UNSET
    minimum_monthly_saving: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        title = self.title

        tab = self.tab

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        cloud_account_id: None | str | Unset
        if isinstance(self.cloud_account_id, Unset):
            cloud_account_id = UNSET
        else:
            cloud_account_id = self.cloud_account_id

        minimum_monthly_saving: None | str | Unset
        if isinstance(self.minimum_monthly_saving, Unset):
            minimum_monthly_saving = UNSET
        else:
            minimum_monthly_saving = self.minimum_monthly_saving

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workspaceId": workspace_id,
                "title": title,
                "tab": tab,
            }
        )
        if source is not UNSET:
            field_dict["source"] = source
        if kind is not UNSET:
            field_dict["kind"] = kind
        if cloud_account_id is not UNSET:
            field_dict["cloudAccountId"] = cloud_account_id
        if minimum_monthly_saving is not UNSET:
            field_dict["minimumMonthlySaving"] = minimum_monthly_saving

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        title = d.pop("title")

        tab = d.pop("tab")

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))

        def _parse_cloud_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cloud_account_id = _parse_cloud_account_id(d.pop("cloudAccountId", UNSET))

        def _parse_minimum_monthly_saving(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        minimum_monthly_saving = _parse_minimum_monthly_saving(
            d.pop("minimumMonthlySaving", UNSET)
        )

        create_savings_view_request = cls(
            workspace_id=workspace_id,
            title=title,
            tab=tab,
            source=source,
            kind=kind,
            cloud_account_id=cloud_account_id,
            minimum_monthly_saving=minimum_monthly_saving,
        )

        return create_savings_view_request
