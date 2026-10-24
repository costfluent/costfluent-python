from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workspace_report_defaults_response import (
        WorkspaceReportDefaultsResponse,
    )


T = TypeVar("T", bound="WorkspaceResponse")


@_attrs_define
class WorkspaceResponse:
    """
    Attributes:
        id (str):
        name (str):
        currency (str):
        enable_currency_conversion (bool):
        conversion_method (str):
        enable_automatic_syncing (bool):
        time_zone (str):
        report_defaults (WorkspaceReportDefaultsResponse):
        anomalies_exclude_marketplace (bool):
        anomalies_exclude_commitment_fees (bool):
        anomaly_notification_threshold (str):
        provider_count (int):
        created_at (datetime.datetime):
        conversion_currency (None | str | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    id: str
    name: str
    currency: str
    enable_currency_conversion: bool
    conversion_method: str
    enable_automatic_syncing: bool
    time_zone: str
    report_defaults: WorkspaceReportDefaultsResponse
    anomalies_exclude_marketplace: bool
    anomalies_exclude_commitment_fees: bool
    anomaly_notification_threshold: str
    provider_count: int
    created_at: datetime.datetime
    conversion_currency: None | str | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        currency = self.currency

        enable_currency_conversion = self.enable_currency_conversion

        conversion_method = self.conversion_method

        enable_automatic_syncing = self.enable_automatic_syncing

        time_zone = self.time_zone

        report_defaults = self.report_defaults.to_dict()

        anomalies_exclude_marketplace = self.anomalies_exclude_marketplace

        anomalies_exclude_commitment_fees = self.anomalies_exclude_commitment_fees

        anomaly_notification_threshold = self.anomaly_notification_threshold

        provider_count = self.provider_count

        created_at = self.created_at.isoformat()

        conversion_currency: None | str | Unset
        if isinstance(self.conversion_currency, Unset):
            conversion_currency = UNSET
        else:
            conversion_currency = self.conversion_currency

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
                "currency": currency,
                "enableCurrencyConversion": enable_currency_conversion,
                "conversionMethod": conversion_method,
                "enableAutomaticSyncing": enable_automatic_syncing,
                "timeZone": time_zone,
                "reportDefaults": report_defaults,
                "anomaliesExcludeMarketplace": anomalies_exclude_marketplace,
                "anomaliesExcludeCommitmentFees": anomalies_exclude_commitment_fees,
                "anomalyNotificationThreshold": anomaly_notification_threshold,
                "providerCount": provider_count,
                "createdAt": created_at,
            }
        )
        if conversion_currency is not UNSET:
            field_dict["conversionCurrency"] = conversion_currency
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workspace_report_defaults_response import (
            WorkspaceReportDefaultsResponse,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        currency = d.pop("currency")

        enable_currency_conversion = d.pop("enableCurrencyConversion")

        conversion_method = d.pop("conversionMethod")

        enable_automatic_syncing = d.pop("enableAutomaticSyncing")

        time_zone = d.pop("timeZone")

        report_defaults = WorkspaceReportDefaultsResponse.from_dict(
            d.pop("reportDefaults")
        )

        anomalies_exclude_marketplace = d.pop("anomaliesExcludeMarketplace")

        anomalies_exclude_commitment_fees = d.pop("anomaliesExcludeCommitmentFees")

        anomaly_notification_threshold = d.pop("anomalyNotificationThreshold")

        provider_count = d.pop("providerCount")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        def _parse_conversion_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conversion_currency = _parse_conversion_currency(
            d.pop("conversionCurrency", UNSET)
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

        workspace_response = cls(
            id=id,
            name=name,
            currency=currency,
            enable_currency_conversion=enable_currency_conversion,
            conversion_method=conversion_method,
            enable_automatic_syncing=enable_automatic_syncing,
            time_zone=time_zone,
            report_defaults=report_defaults,
            anomalies_exclude_marketplace=anomalies_exclude_marketplace,
            anomalies_exclude_commitment_fees=anomalies_exclude_commitment_fees,
            anomaly_notification_threshold=anomaly_notification_threshold,
            provider_count=provider_count,
            created_at=created_at,
            conversion_currency=conversion_currency,
            updated_at=updated_at,
        )

        return workspace_response
