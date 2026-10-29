from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.anomaly_contributor_response import AnomalyContributorResponse
    from ..models.anomaly_sku_contributor_response import AnomalySkuContributorResponse


T = TypeVar("T", bound="AnomalyResponse")


@_attrs_define
class AnomalyResponse:
    """
    Attributes:
        id (str):
        workspace_id (str):
        provider_id (str):
        anomaly_date (datetime.date):
        service_name (str):
        anomaly_type (str):
        severity (str):
        expected_cost (str):
        actual_cost (str):
        deviation_percent (float):
        description (str):
        currency (str):
        status (str):
        is_acknowledged (bool):
        detected_at (datetime.datetime):
        contributors (list[AnomalyContributorResponse]):
        sku_contributors (list[AnomalySkuContributorResponse]):
        region (None | str | Unset):
        status_reason (None | str | Unset):
        ignore_reason (None | str | Unset):
        acknowledged_at (datetime.datetime | None | Unset):
        attributed_resource_id (None | str | Unset):
        attributed_sku (None | str | Unset):
    """

    id: str
    workspace_id: str
    provider_id: str
    anomaly_date: datetime.date
    service_name: str
    anomaly_type: str
    severity: str
    expected_cost: str
    actual_cost: str
    deviation_percent: float
    description: str
    currency: str
    status: str
    is_acknowledged: bool
    detected_at: datetime.datetime
    contributors: list[AnomalyContributorResponse]
    sku_contributors: list[AnomalySkuContributorResponse]
    region: None | str | Unset = UNSET
    status_reason: None | str | Unset = UNSET
    ignore_reason: None | str | Unset = UNSET
    acknowledged_at: datetime.datetime | None | Unset = UNSET
    attributed_resource_id: None | str | Unset = UNSET
    attributed_sku: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workspace_id = self.workspace_id

        provider_id = self.provider_id

        anomaly_date = self.anomaly_date.isoformat()

        service_name = self.service_name

        anomaly_type = self.anomaly_type

        severity = self.severity

        expected_cost = self.expected_cost

        actual_cost = self.actual_cost

        deviation_percent = self.deviation_percent

        description = self.description

        currency = self.currency

        status = self.status

        is_acknowledged = self.is_acknowledged

        detected_at = self.detected_at.isoformat()

        contributors = []
        for contributors_item_data in self.contributors:
            contributors_item = contributors_item_data.to_dict()
            contributors.append(contributors_item)

        sku_contributors = []
        for sku_contributors_item_data in self.sku_contributors:
            sku_contributors_item = sku_contributors_item_data.to_dict()
            sku_contributors.append(sku_contributors_item)

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        status_reason: None | str | Unset
        if isinstance(self.status_reason, Unset):
            status_reason = UNSET
        else:
            status_reason = self.status_reason

        ignore_reason: None | str | Unset
        if isinstance(self.ignore_reason, Unset):
            ignore_reason = UNSET
        else:
            ignore_reason = self.ignore_reason

        acknowledged_at: None | str | Unset
        if isinstance(self.acknowledged_at, Unset):
            acknowledged_at = UNSET
        elif isinstance(self.acknowledged_at, datetime.datetime):
            acknowledged_at = self.acknowledged_at.isoformat()
        else:
            acknowledged_at = self.acknowledged_at

        attributed_resource_id: None | str | Unset
        if isinstance(self.attributed_resource_id, Unset):
            attributed_resource_id = UNSET
        else:
            attributed_resource_id = self.attributed_resource_id

        attributed_sku: None | str | Unset
        if isinstance(self.attributed_sku, Unset):
            attributed_sku = UNSET
        else:
            attributed_sku = self.attributed_sku

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "workspaceId": workspace_id,
                "providerId": provider_id,
                "anomalyDate": anomaly_date,
                "serviceName": service_name,
                "anomalyType": anomaly_type,
                "severity": severity,
                "expectedCost": expected_cost,
                "actualCost": actual_cost,
                "deviationPercent": deviation_percent,
                "description": description,
                "currency": currency,
                "status": status,
                "isAcknowledged": is_acknowledged,
                "detectedAt": detected_at,
                "contributors": contributors,
                "skuContributors": sku_contributors,
            }
        )
        if region is not UNSET:
            field_dict["region"] = region
        if status_reason is not UNSET:
            field_dict["statusReason"] = status_reason
        if ignore_reason is not UNSET:
            field_dict["ignoreReason"] = ignore_reason
        if acknowledged_at is not UNSET:
            field_dict["acknowledgedAt"] = acknowledged_at
        if attributed_resource_id is not UNSET:
            field_dict["attributedResourceId"] = attributed_resource_id
        if attributed_sku is not UNSET:
            field_dict["attributedSku"] = attributed_sku

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.anomaly_contributor_response import AnomalyContributorResponse
        from ..models.anomaly_sku_contributor_response import (
            AnomalySkuContributorResponse,
        )

        d = dict(src_dict)
        id = d.pop("id")

        workspace_id = d.pop("workspaceId")

        provider_id = d.pop("providerId")

        anomaly_date = datetime.date.fromisoformat(d.pop("anomalyDate"))

        service_name = d.pop("serviceName")

        anomaly_type = d.pop("anomalyType")

        severity = d.pop("severity")

        expected_cost = d.pop("expectedCost")

        actual_cost = d.pop("actualCost")

        deviation_percent = d.pop("deviationPercent")

        description = d.pop("description")

        currency = d.pop("currency")

        status = d.pop("status")

        is_acknowledged = d.pop("isAcknowledged")

        detected_at = datetime.datetime.fromisoformat(d.pop("detectedAt"))

        contributors = []
        _contributors = d.pop("contributors")
        for contributors_item_data in _contributors:
            contributors_item = AnomalyContributorResponse.from_dict(
                contributors_item_data
            )

            contributors.append(contributors_item)

        sku_contributors = []
        _sku_contributors = d.pop("skuContributors")
        for sku_contributors_item_data in _sku_contributors:
            sku_contributors_item = AnomalySkuContributorResponse.from_dict(
                sku_contributors_item_data
            )

            sku_contributors.append(sku_contributors_item)

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_status_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_reason = _parse_status_reason(d.pop("statusReason", UNSET))

        def _parse_ignore_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ignore_reason = _parse_ignore_reason(d.pop("ignoreReason", UNSET))

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

        def _parse_attributed_resource_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        attributed_resource_id = _parse_attributed_resource_id(
            d.pop("attributedResourceId", UNSET)
        )

        def _parse_attributed_sku(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        attributed_sku = _parse_attributed_sku(d.pop("attributedSku", UNSET))

        anomaly_response = cls(
            id=id,
            workspace_id=workspace_id,
            provider_id=provider_id,
            anomaly_date=anomaly_date,
            service_name=service_name,
            anomaly_type=anomaly_type,
            severity=severity,
            expected_cost=expected_cost,
            actual_cost=actual_cost,
            deviation_percent=deviation_percent,
            description=description,
            currency=currency,
            status=status,
            is_acknowledged=is_acknowledged,
            detected_at=detected_at,
            contributors=contributors,
            sku_contributors=sku_contributors,
            region=region,
            status_reason=status_reason,
            ignore_reason=ignore_reason,
            acknowledged_at=acknowledged_at,
            attributed_resource_id=attributed_resource_id,
            attributed_sku=attributed_sku,
        )

        return anomaly_response
