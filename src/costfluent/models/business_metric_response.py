from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BusinessMetricResponse")


@_attrs_define
class BusinessMetricResponse:
    """
    Attributes:
        id (str):
        name (str):
        unit (str):
        label_columns (list[str]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime | None | Unset):
    """

    id: str
    name: str
    unit: str
    label_columns: list[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        unit = self.unit

        label_columns = self.label_columns

        created_at = self.created_at.isoformat()

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "unit": unit,
                "labelColumns": label_columns,
                "createdAt": created_at,
            }
        )
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        unit = d.pop("unit")

        label_columns = cast(list[str], d.pop("labelColumns"))

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))

        business_metric_response = cls(
            id=id,
            name=name,
            unit=unit,
            label_columns=label_columns,
            created_at=created_at,
            updated_at=updated_at,
        )

        return business_metric_response
