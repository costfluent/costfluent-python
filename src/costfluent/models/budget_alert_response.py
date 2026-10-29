from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BudgetAlertResponse")


@_attrs_define
class BudgetAlertResponse:
    """
    Attributes:
        threshold_percent (int):
        basis (str):
        app_ids (list[str]):
        is_triggered (bool):
        triggered_at (datetime.datetime | None | Unset):
    """

    threshold_percent: int
    basis: str
    app_ids: list[str]
    is_triggered: bool
    triggered_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        threshold_percent = self.threshold_percent

        basis = self.basis

        app_ids = self.app_ids

        is_triggered = self.is_triggered

        triggered_at: None | str | Unset
        if isinstance(self.triggered_at, Unset):
            triggered_at = UNSET
        elif isinstance(self.triggered_at, datetime.datetime):
            triggered_at = self.triggered_at.isoformat()
        else:
            triggered_at = self.triggered_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "thresholdPercent": threshold_percent,
                "basis": basis,
                "appIds": app_ids,
                "isTriggered": is_triggered,
            }
        )
        if triggered_at is not UNSET:
            field_dict["triggeredAt"] = triggered_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        threshold_percent = d.pop("thresholdPercent")

        basis = d.pop("basis")

        app_ids = cast(list[str], d.pop("appIds"))

        is_triggered = d.pop("isTriggered")

        def _parse_triggered_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                triggered_at_type_0 = datetime.datetime.fromisoformat(data)

                return triggered_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        triggered_at = _parse_triggered_at(d.pop("triggeredAt", UNSET))

        budget_alert_response = cls(
            threshold_percent=threshold_percent,
            basis=basis,
            app_ids=app_ids,
            is_triggered=is_triggered,
            triggered_at=triggered_at,
        )

        return budget_alert_response
