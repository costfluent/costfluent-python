from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BudgetAlertRequest")


@_attrs_define
class BudgetAlertRequest:
    """
    Attributes:
        threshold_percent (int | Unset):
    """

    threshold_percent: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        threshold_percent = self.threshold_percent

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if threshold_percent is not UNSET:
            field_dict["thresholdPercent"] = threshold_percent

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        threshold_percent = d.pop("thresholdPercent", UNSET)

        budget_alert_request = cls(
            threshold_percent=threshold_percent,
        )

        return budget_alert_request
