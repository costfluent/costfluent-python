from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SavingsViewResponse")


@_attrs_define
class SavingsViewResponse:
    """
    Attributes:
        id (str):
        title (str):
        tab (str):
        created_at (datetime.datetime):
        source (None | str | Unset):
        kind (None | str | Unset):
        cloud_account_id (None | str | Unset):
        minimum_monthly_saving (None | str | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    id: str
    title: str
    tab: str
    created_at: datetime.datetime
    source: None | str | Unset = UNSET
    kind: None | str | Unset = UNSET
    cloud_account_id: None | str | Unset = UNSET
    minimum_monthly_saving: None | str | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        tab = self.tab

        created_at = self.created_at.isoformat()

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
                "id": id,
                "title": title,
                "tab": tab,
                "createdAt": created_at,
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
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        tab = d.pop("tab")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

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

        savings_view_response = cls(
            id=id,
            title=title,
            tab=tab,
            created_at=created_at,
            source=source,
            kind=kind,
            cloud_account_id=cloud_account_id,
            minimum_monthly_saving=minimum_monthly_saving,
            updated_at=updated_at,
        )

        return savings_view_response
