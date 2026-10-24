from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_response_config import AppResponseConfig


T = TypeVar("T", bound="AppResponse")


@_attrs_define
class AppResponse:
    """
    Attributes:
        id (str):
        key (str):
        name (str):
        config (AppResponseConfig):
        is_enabled (bool):
        created_at (datetime.datetime):
        signing_secret (None | str | Unset):
    """

    id: str
    key: str
    name: str
    config: AppResponseConfig
    is_enabled: bool
    created_at: datetime.datetime
    signing_secret: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        key = self.key

        name = self.name

        config = self.config.to_dict()

        is_enabled = self.is_enabled

        created_at = self.created_at.isoformat()

        signing_secret: None | str | Unset
        if isinstance(self.signing_secret, Unset):
            signing_secret = UNSET
        else:
            signing_secret = self.signing_secret

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "key": key,
                "name": name,
                "config": config,
                "isEnabled": is_enabled,
                "createdAt": created_at,
            }
        )
        if signing_secret is not UNSET:
            field_dict["signingSecret"] = signing_secret

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.app_response_config import AppResponseConfig

        d = dict(src_dict)
        id = d.pop("id")

        key = d.pop("key")

        name = d.pop("name")

        config = AppResponseConfig.from_dict(d.pop("config"))

        is_enabled = d.pop("isEnabled")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        def _parse_signing_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        signing_secret = _parse_signing_secret(d.pop("signingSecret", UNSET))

        app_response = cls(
            id=id,
            key=key,
            name=name,
            config=config,
            is_enabled=is_enabled,
            created_at=created_at,
            signing_secret=signing_secret,
        )

        return app_response
