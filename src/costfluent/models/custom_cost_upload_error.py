from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CustomCostUploadError")


@_attrs_define
class CustomCostUploadError:
    """
    Attributes:
        row_number (int):
        field (str):
        message (str):
    """

    row_number: int
    field: str
    message: str

    def to_dict(self) -> dict[str, Any]:
        row_number = self.row_number

        field = self.field

        message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "rowNumber": row_number,
                "field": field,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        row_number = d.pop("rowNumber")

        field = d.pop("field")

        message = d.pop("message")

        custom_cost_upload_error = cls(
            row_number=row_number,
            field=field,
            message=message,
        )

        return custom_cost_upload_error
