from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TagKeyResponse")


@_attrs_define
class TagKeyResponse:
    """
    Attributes:
        id (str):
        key (str):
        provider_keys (list[str]):
        created_at (datetime.datetime):
        is_hidden (bool):
        is_preferred (bool):
        last_seen_at (datetime.datetime | None | Unset):
    """

    id: str
    key: str
    provider_keys: list[str]
    created_at: datetime.datetime
    is_hidden: bool
    is_preferred: bool
    last_seen_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        key = self.key

        provider_keys = self.provider_keys

        created_at = self.created_at.isoformat()

        is_hidden = self.is_hidden

        is_preferred = self.is_preferred

        last_seen_at: None | str | Unset
        if isinstance(self.last_seen_at, Unset):
            last_seen_at = UNSET
        elif isinstance(self.last_seen_at, datetime.datetime):
            last_seen_at = self.last_seen_at.isoformat()
        else:
            last_seen_at = self.last_seen_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "key": key,
                "providerKeys": provider_keys,
                "createdAt": created_at,
                "isHidden": is_hidden,
                "isPreferred": is_preferred,
            }
        )
        if last_seen_at is not UNSET:
            field_dict["lastSeenAt"] = last_seen_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        key = d.pop("key")

        provider_keys = cast(list[str], d.pop("providerKeys"))

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        is_hidden = d.pop("isHidden")

        is_preferred = d.pop("isPreferred")

        def _parse_last_seen_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_seen_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_seen_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_seen_at = _parse_last_seen_at(d.pop("lastSeenAt", UNSET))

        tag_key_response = cls(
            id=id,
            key=key,
            provider_keys=provider_keys,
            created_at=created_at,
            is_hidden=is_hidden,
            is_preferred=is_preferred,
            last_seen_at=last_seen_at,
        )

        return tag_key_response
