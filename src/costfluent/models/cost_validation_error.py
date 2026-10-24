from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CostValidationError")


@_attrs_define
class CostValidationError:
    """
    Attributes:
        row_index (int):
        field (str):
        message (str):
    """

    row_index: int
    field: str
    message: str

    def to_dict(self) -> dict[str, Any]:
        row_index = self.row_index

        field = self.field

        message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "rowIndex": row_index,
                "field": field,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        row_index = d.pop("rowIndex")

        field = d.pop("field")

        message = d.pop("message")

        cost_validation_error = cls(
            row_index=row_index,
            field=field,
            message=message,
        )

        return cost_validation_error
