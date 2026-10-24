from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DeleteCostReportSubscriptionRequest")


@_attrs_define
class DeleteCostReportSubscriptionRequest:
    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        delete_cost_report_subscription_request = cls()

        return delete_cost_report_subscription_request
