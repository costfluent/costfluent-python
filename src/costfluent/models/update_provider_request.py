from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_provider_request_credentials_type_0 import (
        UpdateProviderRequestCredentialsType0,
    )
    from ..models.update_provider_request_settings_type_0 import (
        UpdateProviderRequestSettingsType0,
    )


T = TypeVar("T", bound="UpdateProviderRequest")


@_attrs_define
class UpdateProviderRequest:
    """
    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        clear_description (bool | Unset):
        external_id (None | str | Unset):
        credentials (None | Unset | UpdateProviderRequestCredentialsType0):
        settings (None | Unset | UpdateProviderRequestSettingsType0):
        clear_settings (bool | Unset):
        sync_frequency_minutes (int | None | Unset):
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    clear_description: bool | Unset = UNSET
    external_id: None | str | Unset = UNSET
    credentials: None | Unset | UpdateProviderRequestCredentialsType0 = UNSET
    settings: None | Unset | UpdateProviderRequestSettingsType0 = UNSET
    clear_settings: bool | Unset = UNSET
    sync_frequency_minutes: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_provider_request_credentials_type_0 import (
            UpdateProviderRequestCredentialsType0,
        )
        from ..models.update_provider_request_settings_type_0 import (
            UpdateProviderRequestSettingsType0,
        )

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        clear_description = self.clear_description

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        credentials: dict[str, Any] | None | Unset
        if isinstance(self.credentials, Unset):
            credentials = UNSET
        elif isinstance(self.credentials, UpdateProviderRequestCredentialsType0):
            credentials = self.credentials.to_dict()
        else:
            credentials = self.credentials

        settings: dict[str, Any] | None | Unset
        if isinstance(self.settings, Unset):
            settings = UNSET
        elif isinstance(self.settings, UpdateProviderRequestSettingsType0):
            settings = self.settings.to_dict()
        else:
            settings = self.settings

        clear_settings = self.clear_settings

        sync_frequency_minutes: int | None | Unset
        if isinstance(self.sync_frequency_minutes, Unset):
            sync_frequency_minutes = UNSET
        else:
            sync_frequency_minutes = self.sync_frequency_minutes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if clear_description is not UNSET:
            field_dict["clearDescription"] = clear_description
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if settings is not UNSET:
            field_dict["settings"] = settings
        if clear_settings is not UNSET:
            field_dict["clearSettings"] = clear_settings
        if sync_frequency_minutes is not UNSET:
            field_dict["syncFrequencyMinutes"] = sync_frequency_minutes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.update_provider_request_credentials_type_0 import (
            UpdateProviderRequestCredentialsType0,
        )
        from ..models.update_provider_request_settings_type_0 import (
            UpdateProviderRequestSettingsType0,
        )

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        clear_description = d.pop("clearDescription", UNSET)

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_credentials(
            data: object,
        ) -> None | Unset | UpdateProviderRequestCredentialsType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credentials_type_0 = UpdateProviderRequestCredentialsType0.from_dict(
                    data
                )

                return credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateProviderRequestCredentialsType0, data)

        credentials = _parse_credentials(d.pop("credentials", UNSET))

        def _parse_settings(
            data: object,
        ) -> None | Unset | UpdateProviderRequestSettingsType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                settings_type_0 = UpdateProviderRequestSettingsType0.from_dict(data)

                return settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateProviderRequestSettingsType0, data)

        settings = _parse_settings(d.pop("settings", UNSET))

        clear_settings = d.pop("clearSettings", UNSET)

        def _parse_sync_frequency_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sync_frequency_minutes = _parse_sync_frequency_minutes(
            d.pop("syncFrequencyMinutes", UNSET)
        )

        update_provider_request = cls(
            name=name,
            description=description,
            clear_description=clear_description,
            external_id=external_id,
            credentials=credentials,
            settings=settings,
            clear_settings=clear_settings,
            sync_frequency_minutes=sync_frequency_minutes,
        )

        return update_provider_request
