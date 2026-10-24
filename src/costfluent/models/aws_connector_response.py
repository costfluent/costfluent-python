from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AwsConnectorResponse")


@_attrs_define
class AwsConnectorResponse:
    """
    Attributes:
        principal_arn (str):
        external_id (str):
        region (str):
        template_url (None | str | Unset):
    """

    principal_arn: str
    external_id: str
    region: str
    template_url: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        principal_arn = self.principal_arn

        external_id = self.external_id

        region = self.region

        template_url: None | str | Unset
        if isinstance(self.template_url, Unset):
            template_url = UNSET
        else:
            template_url = self.template_url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "principalArn": principal_arn,
                "externalId": external_id,
                "region": region,
            }
        )
        if template_url is not UNSET:
            field_dict["templateUrl"] = template_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        principal_arn = d.pop("principalArn")

        external_id = d.pop("externalId")

        region = d.pop("region")

        def _parse_template_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template_url = _parse_template_url(d.pop("templateUrl", UNSET))

        aws_connector_response = cls(
            principal_arn=principal_arn,
            external_id=external_id,
            region=region,
            template_url=template_url,
        )

        return aws_connector_response
