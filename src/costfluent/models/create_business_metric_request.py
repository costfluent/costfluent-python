from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateBusinessMetricRequest")


@_attrs_define
class CreateBusinessMetricRequest:
    """
    Attributes:
        workspace_id (str):
        name (str):
        unit (str):
        label_columns (list[str] | None | Unset):
    """

    workspace_id: str
    name: str
    unit: str
    label_columns: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        name = self.name

        unit = self.unit

        label_columns: list[str] | None | Unset
        if isinstance(self.label_columns, Unset):
            label_columns = UNSET
        elif isinstance(self.label_columns, list):
            label_columns = self.label_columns

        else:
            label_columns = self.label_columns

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workspaceId": workspace_id,
                "name": name,
                "unit": unit,
            }
        )
        if label_columns is not UNSET:
            field_dict["labelColumns"] = label_columns

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        name = d.pop("name")

        unit = d.pop("unit")

        def _parse_label_columns(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                label_columns_type_0 = cast(list[str], data)

                return label_columns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        label_columns = _parse_label_columns(d.pop("labelColumns", UNSET))

        create_business_metric_request = cls(
            workspace_id=workspace_id,
            name=name,
            unit=unit,
            label_columns=label_columns,
        )

        return create_business_metric_request
