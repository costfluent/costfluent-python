from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connection_test_response_metadata_type_0 import (
        ConnectionTestResponseMetadataType0,
    )


T = TypeVar("T", bound="ConnectionTestResponse")


@_attrs_define
class ConnectionTestResponse:
    """
    Attributes:
        success (bool):
        message (None | str | Unset):
        metadata (ConnectionTestResponseMetadataType0 | None | Unset):
    """

    success: bool
    message: None | str | Unset = UNSET
    metadata: ConnectionTestResponseMetadataType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.connection_test_response_metadata_type_0 import (
            ConnectionTestResponseMetadataType0,
        )

        success = self.success

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, ConnectionTestResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "success": success,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.connection_test_response_metadata_type_0 import (
            ConnectionTestResponseMetadataType0,
        )

        d = dict(src_dict)
        success = d.pop("success")

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_metadata(
            data: object,
        ) -> ConnectionTestResponseMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = ConnectionTestResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConnectionTestResponseMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        connection_test_response = cls(
            success=success,
            message=message,
            metadata=metadata,
        )

        return connection_test_response
