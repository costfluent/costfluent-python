from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.business_metric_value_request_labels_type_0 import (
        BusinessMetricValueRequestLabelsType0,
    )


T = TypeVar("T", bound="BusinessMetricValueRequest")


@_attrs_define
class BusinessMetricValueRequest:
    """
    Attributes:
        date (datetime.date | Unset):
        amount (str | Unset):
        labels (BusinessMetricValueRequestLabelsType0 | None | Unset):
    """

    date: datetime.date | Unset = UNSET
    amount: str | Unset = UNSET
    labels: BusinessMetricValueRequestLabelsType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.business_metric_value_request_labels_type_0 import (
            BusinessMetricValueRequestLabelsType0,
        )

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        amount = self.amount

        labels: dict[str, Any] | None | Unset
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, BusinessMetricValueRequestLabelsType0):
            labels = self.labels.to_dict()
        else:
            labels = self.labels

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if amount is not UNSET:
            field_dict["amount"] = amount
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.business_metric_value_request_labels_type_0 import (
            BusinessMetricValueRequestLabelsType0,
        )

        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = datetime.date.fromisoformat(_date)

        amount = d.pop("amount", UNSET)

        def _parse_labels(
            data: object,
        ) -> BusinessMetricValueRequestLabelsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                labels_type_0 = BusinessMetricValueRequestLabelsType0.from_dict(data)

                return labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BusinessMetricValueRequestLabelsType0 | None | Unset, data)

        labels = _parse_labels(d.pop("labels", UNSET))

        business_metric_value_request = cls(
            date=date,
            amount=amount,
            labels=labels,
        )

        return business_metric_value_request
