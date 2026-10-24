from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..models.comparison_period import ComparisonPeriod
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCostAlertRequest")


@_attrs_define
class CreateCostAlertRequest:
    """
    Attributes:
        workspace_id (str):
        name (str):
        threshold_type (str):
        threshold_value (str):
        comparison_period (ComparisonPeriod | None | Unset):
        minimum_amount (None | str | Unset):
        provider_ids (list[str] | None | Unset):
        filter_ (None | str | Unset):
        app_ids (list[str] | None | Unset):
        evaluation_frequency_minutes (int | Unset):
    """

    workspace_id: str
    name: str
    threshold_type: str
    threshold_value: str
    comparison_period: ComparisonPeriod | None | Unset = UNSET
    minimum_amount: None | str | Unset = UNSET
    provider_ids: list[str] | None | Unset = UNSET
    filter_: None | str | Unset = UNSET
    app_ids: list[str] | None | Unset = UNSET
    evaluation_frequency_minutes: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        name = self.name

        threshold_type = self.threshold_type

        threshold_value = self.threshold_value

        comparison_period: None | str | Unset
        if isinstance(self.comparison_period, Unset):
            comparison_period = UNSET
        elif isinstance(self.comparison_period, ComparisonPeriod):
            comparison_period = self.comparison_period.value
        else:
            comparison_period = self.comparison_period

        minimum_amount: None | str | Unset
        if isinstance(self.minimum_amount, Unset):
            minimum_amount = UNSET
        else:
            minimum_amount = self.minimum_amount

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

        app_ids: list[str] | None | Unset
        if isinstance(self.app_ids, Unset):
            app_ids = UNSET
        elif isinstance(self.app_ids, list):
            app_ids = self.app_ids

        else:
            app_ids = self.app_ids

        evaluation_frequency_minutes = self.evaluation_frequency_minutes

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workspaceId": workspace_id,
                "name": name,
                "thresholdType": threshold_type,
                "thresholdValue": threshold_value,
            }
        )
        if comparison_period is not UNSET:
            field_dict["comparisonPeriod"] = comparison_period
        if minimum_amount is not UNSET:
            field_dict["minimumAmount"] = minimum_amount
        if provider_ids is not UNSET:
            field_dict["providerIds"] = provider_ids
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if app_ids is not UNSET:
            field_dict["appIds"] = app_ids
        if evaluation_frequency_minutes is not UNSET:
            field_dict["evaluationFrequencyMinutes"] = evaluation_frequency_minutes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        name = d.pop("name")

        threshold_type = d.pop("thresholdType")

        threshold_value = d.pop("thresholdValue")

        def _parse_comparison_period(data: object) -> ComparisonPeriod | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                comparison_period_type_0 = ComparisonPeriod(data)

                return comparison_period_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ComparisonPeriod | None | Unset, data)

        comparison_period = _parse_comparison_period(d.pop("comparisonPeriod", UNSET))

        def _parse_minimum_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        minimum_amount = _parse_minimum_amount(d.pop("minimumAmount", UNSET))

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

        def _parse_app_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                app_ids_type_0 = cast(list[str], data)

                return app_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        app_ids = _parse_app_ids(d.pop("appIds", UNSET))

        evaluation_frequency_minutes = d.pop("evaluationFrequencyMinutes", UNSET)

        create_cost_alert_request = cls(
            workspace_id=workspace_id,
            name=name,
            threshold_type=threshold_type,
            threshold_value=threshold_value,
            comparison_period=comparison_period,
            minimum_amount=minimum_amount,
            provider_ids=provider_ids,
            filter_=filter_,
            app_ids=app_ids,
            evaluation_frequency_minutes=evaluation_frequency_minutes,
        )

        return create_cost_alert_request
