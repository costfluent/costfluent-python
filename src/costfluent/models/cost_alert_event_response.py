from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostAlertEventResponse")


@_attrs_define
class CostAlertEventResponse:
    """
    Attributes:
        id (str):
        triggered_at (datetime.datetime):
        threshold_value (str):
        actual_value (str):
        status (str):
        comparison_value (None | str | Unset):
        affected_provider_ids (list[str] | None | Unset):
        acknowledged_by_user_id (None | str | Unset):
        acknowledged_at (datetime.datetime | None | Unset):
        resolved_at (datetime.datetime | None | Unset):
    """

    id: str
    triggered_at: datetime.datetime
    threshold_value: str
    actual_value: str
    status: str
    comparison_value: None | str | Unset = UNSET
    affected_provider_ids: list[str] | None | Unset = UNSET
    acknowledged_by_user_id: None | str | Unset = UNSET
    acknowledged_at: datetime.datetime | None | Unset = UNSET
    resolved_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        triggered_at = self.triggered_at.isoformat()

        threshold_value = self.threshold_value

        actual_value = self.actual_value

        status = self.status

        comparison_value: None | str | Unset
        if isinstance(self.comparison_value, Unset):
            comparison_value = UNSET
        else:
            comparison_value = self.comparison_value

        affected_provider_ids: list[str] | None | Unset
        if isinstance(self.affected_provider_ids, Unset):
            affected_provider_ids = UNSET
        elif isinstance(self.affected_provider_ids, list):
            affected_provider_ids = self.affected_provider_ids

        else:
            affected_provider_ids = self.affected_provider_ids

        acknowledged_by_user_id: None | str | Unset
        if isinstance(self.acknowledged_by_user_id, Unset):
            acknowledged_by_user_id = UNSET
        else:
            acknowledged_by_user_id = self.acknowledged_by_user_id

        acknowledged_at: None | str | Unset
        if isinstance(self.acknowledged_at, Unset):
            acknowledged_at = UNSET
        elif isinstance(self.acknowledged_at, datetime.datetime):
            acknowledged_at = self.acknowledged_at.isoformat()
        else:
            acknowledged_at = self.acknowledged_at

        resolved_at: None | str | Unset
        if isinstance(self.resolved_at, Unset):
            resolved_at = UNSET
        elif isinstance(self.resolved_at, datetime.datetime):
            resolved_at = self.resolved_at.isoformat()
        else:
            resolved_at = self.resolved_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "triggeredAt": triggered_at,
                "thresholdValue": threshold_value,
                "actualValue": actual_value,
                "status": status,
            }
        )
        if comparison_value is not UNSET:
            field_dict["comparisonValue"] = comparison_value
        if affected_provider_ids is not UNSET:
            field_dict["affectedProviderIds"] = affected_provider_ids
        if acknowledged_by_user_id is not UNSET:
            field_dict["acknowledgedByUserId"] = acknowledged_by_user_id
        if acknowledged_at is not UNSET:
            field_dict["acknowledgedAt"] = acknowledged_at
        if resolved_at is not UNSET:
            field_dict["resolvedAt"] = resolved_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        triggered_at = datetime.datetime.fromisoformat(d.pop("triggeredAt"))

        threshold_value = d.pop("thresholdValue")

        actual_value = d.pop("actualValue")

        status = d.pop("status")

        def _parse_comparison_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comparison_value = _parse_comparison_value(d.pop("comparisonValue", UNSET))

        def _parse_affected_provider_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                affected_provider_ids_type_0 = cast(list[str], data)

                return affected_provider_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        affected_provider_ids = _parse_affected_provider_ids(
            d.pop("affectedProviderIds", UNSET)
        )

        def _parse_acknowledged_by_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        acknowledged_by_user_id = _parse_acknowledged_by_user_id(
            d.pop("acknowledgedByUserId", UNSET)
        )

        def _parse_acknowledged_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                acknowledged_at_type_0 = datetime.datetime.fromisoformat(data)

                return acknowledged_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        acknowledged_at = _parse_acknowledged_at(d.pop("acknowledgedAt", UNSET))

        def _parse_resolved_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_at_type_0 = datetime.datetime.fromisoformat(data)

                return resolved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        resolved_at = _parse_resolved_at(d.pop("resolvedAt", UNSET))

        cost_alert_event_response = cls(
            id=id,
            triggered_at=triggered_at,
            threshold_value=threshold_value,
            actual_value=actual_value,
            status=status,
            comparison_value=comparison_value,
            affected_provider_ids=affected_provider_ids,
            acknowledged_by_user_id=acknowledged_by_user_id,
            acknowledged_at=acknowledged_at,
            resolved_at=resolved_at,
        )

        return cost_alert_event_response
