from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostAlertResponse")


@_attrs_define
class CostAlertResponse:
    """
    Attributes:
        id (str):
        name (str):
        threshold_type (str):
        threshold_value (str):
        app_ids (list[str]):
        evaluation_frequency_minutes (int):
        status (str):
        created_at (datetime.datetime):
        provider_ids (list[str] | None | Unset):
        filter_ (None | str | Unset):
        comparison_period (None | str | Unset):
        minimum_amount (None | str | Unset):
        last_evaluated_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    id: str
    name: str
    threshold_type: str
    threshold_value: str
    app_ids: list[str]
    evaluation_frequency_minutes: int
    status: str
    created_at: datetime.datetime
    provider_ids: list[str] | None | Unset = UNSET
    filter_: None | str | Unset = UNSET
    comparison_period: None | str | Unset = UNSET
    minimum_amount: None | str | Unset = UNSET
    last_evaluated_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        threshold_type = self.threshold_type

        threshold_value = self.threshold_value

        app_ids = self.app_ids

        evaluation_frequency_minutes = self.evaluation_frequency_minutes

        status = self.status

        created_at = self.created_at.isoformat()

        provider_ids: list[str] | None | Unset
        if isinstance(self.provider_ids, Unset):
            provider_ids = UNSET
        elif isinstance(self.provider_ids, list):
            provider_ids = self.provider_ids

        else:
            provider_ids = self.provider_ids

        filter_: None | str | Unset
        if isinstance(self.filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = self.filter_

        comparison_period: None | str | Unset
        if isinstance(self.comparison_period, Unset):
            comparison_period = UNSET
        else:
            comparison_period = self.comparison_period

        minimum_amount: None | str | Unset
        if isinstance(self.minimum_amount, Unset):
            minimum_amount = UNSET
        else:
            minimum_amount = self.minimum_amount

        last_evaluated_at: None | str | Unset
        if isinstance(self.last_evaluated_at, Unset):
            last_evaluated_at = UNSET
        elif isinstance(self.last_evaluated_at, datetime.datetime):
            last_evaluated_at = self.last_evaluated_at.isoformat()
        else:
            last_evaluated_at = self.last_evaluated_at

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
                "thresholdType": threshold_type,
                "thresholdValue": threshold_value,
                "appIds": app_ids,
                "evaluationFrequencyMinutes": evaluation_frequency_minutes,
                "status": status,
                "createdAt": created_at,
            }
        )
        if provider_ids is not UNSET:
            field_dict["providerIds"] = provider_ids
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if comparison_period is not UNSET:
            field_dict["comparisonPeriod"] = comparison_period
        if minimum_amount is not UNSET:
            field_dict["minimumAmount"] = minimum_amount
        if last_evaluated_at is not UNSET:
            field_dict["lastEvaluatedAt"] = last_evaluated_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        threshold_type = d.pop("thresholdType")

        threshold_value = d.pop("thresholdValue")

        app_ids = cast(list[str], d.pop("appIds"))

        evaluation_frequency_minutes = d.pop("evaluationFrequencyMinutes")

        status = d.pop("status")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        def _parse_provider_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                provider_ids_type_0 = cast(list[str], data)

                return provider_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        provider_ids = _parse_provider_ids(d.pop("providerIds", UNSET))

        def _parse_filter_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filter_ = _parse_filter_(d.pop("filter", UNSET))

        def _parse_comparison_period(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comparison_period = _parse_comparison_period(d.pop("comparisonPeriod", UNSET))

        def _parse_minimum_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        minimum_amount = _parse_minimum_amount(d.pop("minimumAmount", UNSET))

        def _parse_last_evaluated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_evaluated_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_evaluated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_evaluated_at = _parse_last_evaluated_at(d.pop("lastEvaluatedAt", UNSET))

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

        cost_alert_response = cls(
            id=id,
            name=name,
            threshold_type=threshold_type,
            threshold_value=threshold_value,
            app_ids=app_ids,
            evaluation_frequency_minutes=evaluation_frequency_minutes,
            status=status,
            created_at=created_at,
            provider_ids=provider_ids,
            filter_=filter_,
            comparison_period=comparison_period,
            minimum_amount=minimum_amount,
            last_evaluated_at=last_evaluated_at,
            updated_at=updated_at,
        )

        return cost_alert_response
