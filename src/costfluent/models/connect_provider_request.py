from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connect_provider_request_credentials import (
        ConnectProviderRequestCredentials,
    )
    from ..models.connect_provider_request_settings_type_0 import (
        ConnectProviderRequestSettingsType0,
    )


T = TypeVar("T", bound="ConnectProviderRequest")


@_attrs_define
class ConnectProviderRequest:
    """
    Attributes:
        key (str):
        credentials (ConnectProviderRequestCredentials):
        display_name (None | str | Unset):
        description (None | str | Unset):
        parent_provider_id (None | str | Unset):
        external_id (None | str | Unset):
        settings (ConnectProviderRequestSettingsType0 | None | Unset):
        sync_frequency_minutes (int | Unset):
    """

    key: str
    credentials: ConnectProviderRequestCredentials
    display_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    parent_provider_id: None | str | Unset = UNSET
    external_id: None | str | Unset = UNSET
    settings: ConnectProviderRequestSettingsType0 | None | Unset = UNSET
    sync_frequency_minutes: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.connect_provider_request_settings_type_0 import (
            ConnectProviderRequestSettingsType0,
        )

        key = self.key

        credentials = self.credentials.to_dict()

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        parent_provider_id: None | str | Unset
        if isinstance(self.parent_provider_id, Unset):
            parent_provider_id = UNSET
        else:
            parent_provider_id = self.parent_provider_id

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        settings: dict[str, Any] | None | Unset
        if isinstance(self.settings, Unset):
            settings = UNSET
        elif isinstance(self.settings, ConnectProviderRequestSettingsType0):
            settings = self.settings.to_dict()
        else:
            settings = self.settings

        sync_frequency_minutes = self.sync_frequency_minutes

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "credentials": credentials,
            }
        )
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if parent_provider_id is not UNSET:
            field_dict["parentProviderId"] = parent_provider_id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if settings is not UNSET:
            field_dict["settings"] = settings
        if sync_frequency_minutes is not UNSET:
            field_dict["syncFrequencyMinutes"] = sync_frequency_minutes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.connect_provider_request_credentials import (
            ConnectProviderRequestCredentials,
        )
        from ..models.connect_provider_request_settings_type_0 import (
            ConnectProviderRequestSettingsType0,
        )

        d = dict(src_dict)
        key = d.pop("key")

        credentials = ConnectProviderRequestCredentials.from_dict(d.pop("credentials"))

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_parent_provider_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_provider_id = _parse_parent_provider_id(d.pop("parentProviderId", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_settings(
            data: object,
        ) -> ConnectProviderRequestSettingsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                settings_type_0 = ConnectProviderRequestSettingsType0.from_dict(data)

                return settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConnectProviderRequestSettingsType0 | None | Unset, data)

        settings = _parse_settings(d.pop("settings", UNSET))

        sync_frequency_minutes = d.pop("syncFrequencyMinutes", UNSET)

        connect_provider_request = cls(
            key=key,
            credentials=credentials,
            display_name=display_name,
            description=description,
            parent_provider_id=parent_provider_id,
            external_id=external_id,
            settings=settings,
            sync_frequency_minutes=sync_frequency_minutes,
        )

        return connect_provider_request
