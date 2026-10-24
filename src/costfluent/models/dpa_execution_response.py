from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="DpaExecutionResponse")


@_attrs_define
class DpaExecutionResponse:
    """
    Attributes:
        token (str):
        document_version (str):
        signed_at (datetime.date):
        signed_by_name (str):
        signed_by_role (str):
        recorded_at (datetime.datetime):
        is_current (bool):
        superseded_at (datetime.datetime | None):
    """

    token: str
    document_version: str
    signed_at: datetime.date
    signed_by_name: str
    signed_by_role: str
    recorded_at: datetime.datetime
    is_current: bool
    superseded_at: datetime.datetime | None

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        document_version = self.document_version

        signed_at = self.signed_at.isoformat()

        signed_by_name = self.signed_by_name

        signed_by_role = self.signed_by_role

        recorded_at = self.recorded_at.isoformat()

        is_current = self.is_current

        superseded_at: None | str
        if isinstance(self.superseded_at, datetime.datetime):
            superseded_at = self.superseded_at.isoformat()
        else:
            superseded_at = self.superseded_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "token": token,
                "documentVersion": document_version,
                "signedAt": signed_at,
                "signedByName": signed_by_name,
                "signedByRole": signed_by_role,
                "recordedAt": recorded_at,
                "isCurrent": is_current,
                "supersededAt": superseded_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        token = d.pop("token")

        document_version = d.pop("documentVersion")

        signed_at = datetime.date.fromisoformat(d.pop("signedAt"))

        signed_by_name = d.pop("signedByName")

        signed_by_role = d.pop("signedByRole")

        recorded_at = datetime.datetime.fromisoformat(d.pop("recordedAt"))

        is_current = d.pop("isCurrent")

        def _parse_superseded_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                superseded_at_type_0 = datetime.datetime.fromisoformat(data)

                return superseded_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        superseded_at = _parse_superseded_at(d.pop("supersededAt"))

        dpa_execution_response = cls(
            token=token,
            document_version=document_version,
            signed_at=signed_at,
            signed_by_name=signed_by_name,
            signed_by_role=signed_by_role,
            recorded_at=recorded_at,
            is_current=is_current,
            superseded_at=superseded_at,
        )

        return dpa_execution_response
