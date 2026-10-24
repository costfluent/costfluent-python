from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.create_app_request_config import CreateAppRequestConfig


T = TypeVar("T", bound="CreateAppRequest")


@_attrs_define
class CreateAppRequest:
    """
    Attributes:
        key (str):
        name (str):
        config (CreateAppRequestConfig):
    """

    key: str
    name: str
    config: CreateAppRequestConfig

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        name = self.name

        config = self.config.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "name": name,
                "config": config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_app_request_config import CreateAppRequestConfig

        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        config = CreateAppRequestConfig.from_dict(d.pop("config"))

        create_app_request = cls(
            key=key,
            name=name,
            config=config,
        )

        return create_app_request
