from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workspace_report_defaults_request import (
        WorkspaceReportDefaultsRequest,
    )


T = TypeVar("T", bound="UpdateWorkspaceRequest")


@_attrs_define
class UpdateWorkspaceRequest:
    """
    Attributes:
        name (None | str | Unset):
        currency (None | str | Unset):
        enable_currency_conversion (bool | None | Unset):
        conversion_currency (None | str | Unset):
        conversion_method (None | str | Unset):
        enable_automatic_syncing (bool | None | Unset):
        blend_commitment_discounts (bool | None | Unset):
        time_zone (None | str | Unset):
        report_defaults (None | Unset | WorkspaceReportDefaultsRequest):
        anomalies_exclude_marketplace (bool | None | Unset):
        anomalies_exclude_commitment_fees (bool | None | Unset):
        anomaly_notification_threshold (None | str | Unset):
    """

    name: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    enable_currency_conversion: bool | None | Unset = UNSET
    conversion_currency: None | str | Unset = UNSET
    conversion_method: None | str | Unset = UNSET
    enable_automatic_syncing: bool | None | Unset = UNSET
    blend_commitment_discounts: bool | None | Unset = UNSET
    time_zone: None | str | Unset = UNSET
    report_defaults: None | Unset | WorkspaceReportDefaultsRequest = UNSET
    anomalies_exclude_marketplace: bool | None | Unset = UNSET
    anomalies_exclude_commitment_fees: bool | None | Unset = UNSET
    anomaly_notification_threshold: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.workspace_report_defaults_request import (
            WorkspaceReportDefaultsRequest,
        )

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        enable_currency_conversion: bool | None | Unset
        if isinstance(self.enable_currency_conversion, Unset):
            enable_currency_conversion = UNSET
        else:
            enable_currency_conversion = self.enable_currency_conversion

        conversion_currency: None | str | Unset
        if isinstance(self.conversion_currency, Unset):
            conversion_currency = UNSET
        else:
            conversion_currency = self.conversion_currency

        conversion_method: None | str | Unset
        if isinstance(self.conversion_method, Unset):
            conversion_method = UNSET
        else:
            conversion_method = self.conversion_method

        enable_automatic_syncing: bool | None | Unset
        if isinstance(self.enable_automatic_syncing, Unset):
            enable_automatic_syncing = UNSET
        else:
            enable_automatic_syncing = self.enable_automatic_syncing

        blend_commitment_discounts: bool | None | Unset
        if isinstance(self.blend_commitment_discounts, Unset):
            blend_commitment_discounts = UNSET
        else:
            blend_commitment_discounts = self.blend_commitment_discounts

        time_zone: None | str | Unset
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = self.time_zone

        report_defaults: dict[str, Any] | None | Unset
        if isinstance(self.report_defaults, Unset):
            report_defaults = UNSET
        elif isinstance(self.report_defaults, WorkspaceReportDefaultsRequest):
            report_defaults = self.report_defaults.to_dict()
        else:
            report_defaults = self.report_defaults

        anomalies_exclude_marketplace: bool | None | Unset
        if isinstance(self.anomalies_exclude_marketplace, Unset):
            anomalies_exclude_marketplace = UNSET
        else:
            anomalies_exclude_marketplace = self.anomalies_exclude_marketplace

        anomalies_exclude_commitment_fees: bool | None | Unset
        if isinstance(self.anomalies_exclude_commitment_fees, Unset):
            anomalies_exclude_commitment_fees = UNSET
        else:
            anomalies_exclude_commitment_fees = self.anomalies_exclude_commitment_fees

        anomaly_notification_threshold: None | str | Unset
        if isinstance(self.anomaly_notification_threshold, Unset):
            anomaly_notification_threshold = UNSET
        else:
            anomaly_notification_threshold = self.anomaly_notification_threshold

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if currency is not UNSET:
            field_dict["currency"] = currency
        if enable_currency_conversion is not UNSET:
            field_dict["enableCurrencyConversion"] = enable_currency_conversion
        if conversion_currency is not UNSET:
            field_dict["conversionCurrency"] = conversion_currency
        if conversion_method is not UNSET:
            field_dict["conversionMethod"] = conversion_method
        if enable_automatic_syncing is not UNSET:
            field_dict["enableAutomaticSyncing"] = enable_automatic_syncing
        if blend_commitment_discounts is not UNSET:
            field_dict["blendCommitmentDiscounts"] = blend_commitment_discounts
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if report_defaults is not UNSET:
            field_dict["reportDefaults"] = report_defaults
        if anomalies_exclude_marketplace is not UNSET:
            field_dict["anomaliesExcludeMarketplace"] = anomalies_exclude_marketplace
        if anomalies_exclude_commitment_fees is not UNSET:
            field_dict["anomaliesExcludeCommitmentFees"] = (
                anomalies_exclude_commitment_fees
            )
        if anomaly_notification_threshold is not UNSET:
            field_dict["anomalyNotificationThreshold"] = anomaly_notification_threshold

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workspace_report_defaults_request import (
            WorkspaceReportDefaultsRequest,
        )

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_enable_currency_conversion(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_currency_conversion = _parse_enable_currency_conversion(
            d.pop("enableCurrencyConversion", UNSET)
        )

        def _parse_conversion_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conversion_currency = _parse_conversion_currency(
            d.pop("conversionCurrency", UNSET)
        )

        def _parse_conversion_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conversion_method = _parse_conversion_method(d.pop("conversionMethod", UNSET))

        def _parse_enable_automatic_syncing(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_automatic_syncing = _parse_enable_automatic_syncing(
            d.pop("enableAutomaticSyncing", UNSET)
        )

        def _parse_blend_commitment_discounts(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        blend_commitment_discounts = _parse_blend_commitment_discounts(
            d.pop("blendCommitmentDiscounts", UNSET)
        )

        def _parse_time_zone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_zone = _parse_time_zone(d.pop("timeZone", UNSET))

        def _parse_report_defaults(
            data: object,
        ) -> None | Unset | WorkspaceReportDefaultsRequest:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                report_defaults_type_0 = WorkspaceReportDefaultsRequest.from_dict(data)

                return report_defaults_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WorkspaceReportDefaultsRequest, data)

        report_defaults = _parse_report_defaults(d.pop("reportDefaults", UNSET))

        def _parse_anomalies_exclude_marketplace(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        anomalies_exclude_marketplace = _parse_anomalies_exclude_marketplace(
            d.pop("anomaliesExcludeMarketplace", UNSET)
        )

        def _parse_anomalies_exclude_commitment_fees(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        anomalies_exclude_commitment_fees = _parse_anomalies_exclude_commitment_fees(
            d.pop("anomaliesExcludeCommitmentFees", UNSET)
        )

        def _parse_anomaly_notification_threshold(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        anomaly_notification_threshold = _parse_anomaly_notification_threshold(
            d.pop("anomalyNotificationThreshold", UNSET)
        )

        update_workspace_request = cls(
            name=name,
            currency=currency,
            enable_currency_conversion=enable_currency_conversion,
            conversion_currency=conversion_currency,
            conversion_method=conversion_method,
            enable_automatic_syncing=enable_automatic_syncing,
            blend_commitment_discounts=blend_commitment_discounts,
            time_zone=time_zone,
            report_defaults=report_defaults,
            anomalies_exclude_marketplace=anomalies_exclude_marketplace,
            anomalies_exclude_commitment_fees=anomalies_exclude_commitment_fees,
            anomaly_notification_threshold=anomaly_notification_threshold,
        )

        return update_workspace_request
