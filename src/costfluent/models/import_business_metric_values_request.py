from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.business_metric_value_request import BusinessMetricValueRequest


T = TypeVar("T", bound="ImportBusinessMetricValuesRequest")


@_attrs_define
class ImportBusinessMetricValuesRequest:
    """
    Attributes:
        values (list[BusinessMetricValueRequest] | None | Unset):
    """

    values: list[BusinessMetricValueRequest] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        values: list[dict[str, Any]] | None | Unset
        if isinstance(self.values, Unset):
            values = UNSET
        elif isinstance(self.values, list):
            values = []
            for values_type_0_item_data in self.values:
                values_type_0_item = values_type_0_item_data.to_dict()
                values.append(values_type_0_item)

        else:
            values = self.values

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.business_metric_value_request import BusinessMetricValueRequest

        d = dict(src_dict)

        def _parse_values(
            data: object,
        ) -> list[BusinessMetricValueRequest] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                values_type_0 = []
                _values_type_0 = data
                for values_type_0_item_data in _values_type_0:
                    values_type_0_item = BusinessMetricValueRequest.from_dict(
                        values_type_0_item_data
                    )

                    values_type_0.append(values_type_0_item)

                return values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BusinessMetricValueRequest] | None | Unset, data)

        values = _parse_values(d.pop("values", UNSET))

        import_business_metric_values_request = cls(
            values=values,
        )

        return import_business_metric_values_request
