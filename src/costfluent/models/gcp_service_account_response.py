from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GcpServiceAccountResponse")


@_attrs_define
class GcpServiceAccountResponse:
    """
    Attributes:
        service_account_email (str):
        organization_id (None | str | Unset):
        directory_customer_id (None | str | Unset):
    """

    service_account_email: str
    organization_id: None | str | Unset = UNSET
    directory_customer_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        service_account_email = self.service_account_email

        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        else:
            organization_id = self.organization_id

        directory_customer_id: None | str | Unset
        if isinstance(self.directory_customer_id, Unset):
            directory_customer_id = UNSET
        else:
            directory_customer_id = self.directory_customer_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "serviceAccountEmail": service_account_email,
            }
        )
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if directory_customer_id is not UNSET:
            field_dict["directoryCustomerId"] = directory_customer_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        service_account_email = d.pop("serviceAccountEmail")

        def _parse_organization_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organization_id = _parse_organization_id(d.pop("organizationId", UNSET))

        def _parse_directory_customer_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        directory_customer_id = _parse_directory_customer_id(
            d.pop("directoryCustomerId", UNSET)
        )

        gcp_service_account_response = cls(
            service_account_email=service_account_email,
            organization_id=organization_id,
            directory_customer_id=directory_customer_id,
        )

        return gcp_service_account_response
