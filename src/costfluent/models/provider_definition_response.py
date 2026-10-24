from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProviderDefinitionResponse")


@_attrs_define
class ProviderDefinitionResponse:
    """
    Attributes:
        key (str):
        type_ (str):
        display_name (str):
        requires_parent_provider (bool):
        required_credential_fields (list[str]):
        optional_setting_fields (list[str]):
        kind (str):
        icon_url (None | str | Unset):
    """

    key: str
    type_: str
    display_name: str
    requires_parent_provider: bool
    required_credential_fields: list[str]
    optional_setting_fields: list[str]
    kind: str
    icon_url: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        type_ = self.type_

        display_name = self.display_name

        requires_parent_provider = self.requires_parent_provider

        required_credential_fields = self.required_credential_fields

        optional_setting_fields = self.optional_setting_fields

        kind = self.kind

        icon_url: None | str | Unset
        if isinstance(self.icon_url, Unset):
            icon_url = UNSET
        else:
            icon_url = self.icon_url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "type": type_,
                "displayName": display_name,
                "requiresParentProvider": requires_parent_provider,
                "requiredCredentialFields": required_credential_fields,
                "optionalSettingFields": optional_setting_fields,
                "kind": kind,
            }
        )
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = d.pop("key")

        type_ = d.pop("type")

        display_name = d.pop("displayName")

        requires_parent_provider = d.pop("requiresParentProvider")

        required_credential_fields = cast(list[str], d.pop("requiredCredentialFields"))

        optional_setting_fields = cast(list[str], d.pop("optionalSettingFields"))

        kind = d.pop("kind")

        def _parse_icon_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon_url = _parse_icon_url(d.pop("iconUrl", UNSET))

        provider_definition_response = cls(
            key=key,
            type_=type_,
            display_name=display_name,
            requires_parent_provider=requires_parent_provider,
            required_credential_fields=required_credential_fields,
            optional_setting_fields=optional_setting_fields,
            kind=kind,
            icon_url=icon_url,
        )

        return provider_definition_response
