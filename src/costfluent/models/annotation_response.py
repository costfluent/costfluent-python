from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnnotationResponse")


@_attrs_define
class AnnotationResponse:
    """
    Attributes:
        id (str):
        date (datetime.date):
        source (str):
        cost_report_ids (list[str]):
        created_at (datetime.datetime):
        text (None | str | Unset):
        budget_id (None | str | Unset):
        cost_alert_id (None | str | Unset):
        source_name (None | str | Unset):
        threshold_percent (int | None | Unset):
        threshold_basis (None | str | Unset):
        created_by_user_id (None | str | Unset):
        resolved_at (datetime.datetime | None | Unset):
        resolved_by_user_id (None | str | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    id: str
    date: datetime.date
    source: str
    cost_report_ids: list[str]
    created_at: datetime.datetime
    text: None | str | Unset = UNSET
    budget_id: None | str | Unset = UNSET
    cost_alert_id: None | str | Unset = UNSET
    source_name: None | str | Unset = UNSET
    threshold_percent: int | None | Unset = UNSET
    threshold_basis: None | str | Unset = UNSET
    created_by_user_id: None | str | Unset = UNSET
    resolved_at: datetime.datetime | None | Unset = UNSET
    resolved_by_user_id: None | str | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        date = self.date.isoformat()

        source = self.source

        cost_report_ids = self.cost_report_ids

        created_at = self.created_at.isoformat()

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        budget_id: None | str | Unset
        if isinstance(self.budget_id, Unset):
            budget_id = UNSET
        else:
            budget_id = self.budget_id

        cost_alert_id: None | str | Unset
        if isinstance(self.cost_alert_id, Unset):
            cost_alert_id = UNSET
        else:
            cost_alert_id = self.cost_alert_id

        source_name: None | str | Unset
        if isinstance(self.source_name, Unset):
            source_name = UNSET
        else:
            source_name = self.source_name

        threshold_percent: int | None | Unset
        if isinstance(self.threshold_percent, Unset):
            threshold_percent = UNSET
        else:
            threshold_percent = self.threshold_percent

        threshold_basis: None | str | Unset
        if isinstance(self.threshold_basis, Unset):
            threshold_basis = UNSET
        else:
            threshold_basis = self.threshold_basis

        created_by_user_id: None | str | Unset
        if isinstance(self.created_by_user_id, Unset):
            created_by_user_id = UNSET
        else:
            created_by_user_id = self.created_by_user_id

        resolved_at: None | str | Unset
        if isinstance(self.resolved_at, Unset):
            resolved_at = UNSET
        elif isinstance(self.resolved_at, datetime.datetime):
            resolved_at = self.resolved_at.isoformat()
        else:
            resolved_at = self.resolved_at

        resolved_by_user_id: None | str | Unset
        if isinstance(self.resolved_by_user_id, Unset):
            resolved_by_user_id = UNSET
        else:
            resolved_by_user_id = self.resolved_by_user_id

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
                "date": date,
                "source": source,
                "costReportIds": cost_report_ids,
                "createdAt": created_at,
            }
        )
        if text is not UNSET:
            field_dict["text"] = text
        if budget_id is not UNSET:
            field_dict["budgetId"] = budget_id
        if cost_alert_id is not UNSET:
            field_dict["costAlertId"] = cost_alert_id
        if source_name is not UNSET:
            field_dict["sourceName"] = source_name
        if threshold_percent is not UNSET:
            field_dict["thresholdPercent"] = threshold_percent
        if threshold_basis is not UNSET:
            field_dict["thresholdBasis"] = threshold_basis
        if created_by_user_id is not UNSET:
            field_dict["createdByUserId"] = created_by_user_id
        if resolved_at is not UNSET:
            field_dict["resolvedAt"] = resolved_at
        if resolved_by_user_id is not UNSET:
            field_dict["resolvedByUserId"] = resolved_by_user_id
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        date = datetime.date.fromisoformat(d.pop("date"))

        source = d.pop("source")

        cost_report_ids = cast(list[str], d.pop("costReportIds"))

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))

        def _parse_budget_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        budget_id = _parse_budget_id(d.pop("budgetId", UNSET))

        def _parse_cost_alert_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cost_alert_id = _parse_cost_alert_id(d.pop("costAlertId", UNSET))

        def _parse_source_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_name = _parse_source_name(d.pop("sourceName", UNSET))

        def _parse_threshold_percent(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        threshold_percent = _parse_threshold_percent(d.pop("thresholdPercent", UNSET))

        def _parse_threshold_basis(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        threshold_basis = _parse_threshold_basis(d.pop("thresholdBasis", UNSET))

        def _parse_created_by_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by_user_id = _parse_created_by_user_id(d.pop("createdByUserId", UNSET))

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

        def _parse_resolved_by_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolved_by_user_id = _parse_resolved_by_user_id(
            d.pop("resolvedByUserId", UNSET)
        )

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

        annotation_response = cls(
            id=id,
            date=date,
            source=source,
            cost_report_ids=cost_report_ids,
            created_at=created_at,
            text=text,
            budget_id=budget_id,
            cost_alert_id=cost_alert_id,
            source_name=source_name,
            threshold_percent=threshold_percent,
            threshold_basis=threshold_basis,
            created_by_user_id=created_by_user_id,
            resolved_at=resolved_at,
            resolved_by_user_id=resolved_by_user_id,
            updated_at=updated_at,
        )

        return annotation_response
