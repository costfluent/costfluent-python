from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_app_request_config_type_0 import UpdateAppRequestConfigType0


T = TypeVar("T", bound="UpdateAppRequest")


@_attrs_define
class UpdateAppRequest:
    """
    Attributes:
        name (None | str | Unset):
        config (None | Unset | UpdateAppRequestConfigType0):
    """

    name: None | str | Unset = UNSET
    config: None | Unset | UpdateAppRequestConfigType0 = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_app_request_config_type_0 import (
            UpdateAppRequestConfigType0,
        )

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        config: dict[str, Any] | None | Unset
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, UpdateAppRequestConfigType0):
            config = self.config.to_dict()
        else:
            config = self.config

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.update_app_request_config_type_0 import (
            UpdateAppRequestConfigType0,
        )

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_config(data: object) -> None | Unset | UpdateAppRequestConfigType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = UpdateAppRequestConfigType0.from_dict(data)

                return config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateAppRequestConfigType0, data)

        config = _parse_config(d.pop("config", UNSET))

        update_app_request = cls(
            name=name,
            config=config,
        )

        return update_app_request
