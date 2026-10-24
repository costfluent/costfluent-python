from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.business_metric_value_response_labels import (
        BusinessMetricValueResponseLabels,
    )


T = TypeVar("T", bound="BusinessMetricValueResponse")


@_attrs_define
class BusinessMetricValueResponse:
    """
    Attributes:
        date (datetime.date):
        amount (str):
        labels (BusinessMetricValueResponseLabels):
    """

    date: datetime.date
    amount: str
    labels: BusinessMetricValueResponseLabels

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        amount = self.amount

        labels = self.labels.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "date": date,
                "amount": amount,
                "labels": labels,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.business_metric_value_response_labels import (
            BusinessMetricValueResponseLabels,
        )

        d = dict(src_dict)
        date = datetime.date.fromisoformat(d.pop("date"))

        amount = d.pop("amount")

        labels = BusinessMetricValueResponseLabels.from_dict(d.pop("labels"))

        business_metric_value_response = cls(
            date=date,
            amount=amount,
            labels=labels,
        )

        return business_metric_value_response
