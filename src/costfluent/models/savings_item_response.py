from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SavingsItemResponse")


@_attrs_define
class SavingsItemResponse:
    """
    Attributes:
        id (str):
        title (str):
        evidence (str):
        estimated_monthly_saving (str):
        currency (str):
        cost_basis (str):
        owner (str):
        confidence (str):
        risk (str):
        effort (str):
        status (str):
        source (str):
        created_at (datetime.datetime):
        rejection_reason (None | str | Unset):
        verified_monthly_saving (None | str | Unset):
        kind (None | str | Unset):
        resource (None | str | Unset):
        scope (None | str | Unset):
        last_seen_at (datetime.datetime | None | Unset):
        last_measurement_outcome (None | str | Unset):
        last_measurement_scope (None | str | Unset):
        last_measurement_realized_monthly (None | str | Unset):
        last_measured_at (datetime.datetime | None | Unset):
        accepted_at (datetime.datetime | None | Unset):
        implemented_at (datetime.datetime | None | Unset):
        verified_at (datetime.datetime | None | Unset):
        rejected_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    id: str
    title: str
    evidence: str
    estimated_monthly_saving: str
    currency: str
    cost_basis: str
    owner: str
    confidence: str
    risk: str
    effort: str
    status: str
    source: str
    created_at: datetime.datetime
    rejection_reason: None | str | Unset = UNSET
    verified_monthly_saving: None | str | Unset = UNSET
    kind: None | str | Unset = UNSET
    resource: None | str | Unset = UNSET
    scope: None | str | Unset = UNSET
    last_seen_at: datetime.datetime | None | Unset = UNSET
    last_measurement_outcome: None | str | Unset = UNSET
    last_measurement_scope: None | str | Unset = UNSET
    last_measurement_realized_monthly: None | str | Unset = UNSET
    last_measured_at: datetime.datetime | None | Unset = UNSET
    accepted_at: datetime.datetime | None | Unset = UNSET
    implemented_at: datetime.datetime | None | Unset = UNSET
    verified_at: datetime.datetime | None | Unset = UNSET
    rejected_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        evidence = self.evidence

        estimated_monthly_saving = self.estimated_monthly_saving

        currency = self.currency

        cost_basis = self.cost_basis

        owner = self.owner

        confidence = self.confidence

        risk = self.risk

        effort = self.effort

        status = self.status

        source = self.source

        created_at = self.created_at.isoformat()

        rejection_reason: None | str | Unset
        if isinstance(self.rejection_reason, Unset):
            rejection_reason = UNSET
        else:
            rejection_reason = self.rejection_reason

        verified_monthly_saving: None | str | Unset
        if isinstance(self.verified_monthly_saving, Unset):
            verified_monthly_saving = UNSET
        else:
            verified_monthly_saving = self.verified_monthly_saving

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        resource: None | str | Unset
        if isinstance(self.resource, Unset):
            resource = UNSET
        else:
            resource = self.resource

        scope: None | str | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        else:
            scope = self.scope

        last_seen_at: None | str | Unset
        if isinstance(self.last_seen_at, Unset):
            last_seen_at = UNSET
        elif isinstance(self.last_seen_at, datetime.datetime):
            last_seen_at = self.last_seen_at.isoformat()
        else:
            last_seen_at = self.last_seen_at

        last_measurement_outcome: None | str | Unset
        if isinstance(self.last_measurement_outcome, Unset):
            last_measurement_outcome = UNSET
        else:
            last_measurement_outcome = self.last_measurement_outcome

        last_measurement_scope: None | str | Unset
        if isinstance(self.last_measurement_scope, Unset):
            last_measurement_scope = UNSET
        else:
            last_measurement_scope = self.last_measurement_scope

        last_measurement_realized_monthly: None | str | Unset
        if isinstance(self.last_measurement_realized_monthly, Unset):
            last_measurement_realized_monthly = UNSET
        else:
            last_measurement_realized_monthly = self.last_measurement_realized_monthly

        last_measured_at: None | str | Unset
        if isinstance(self.last_measured_at, Unset):
            last_measured_at = UNSET
        elif isinstance(self.last_measured_at, datetime.datetime):
            last_measured_at = self.last_measured_at.isoformat()
        else:
            last_measured_at = self.last_measured_at

        accepted_at: None | str | Unset
        if isinstance(self.accepted_at, Unset):
            accepted_at = UNSET
        elif isinstance(self.accepted_at, datetime.datetime):
            accepted_at = self.accepted_at.isoformat()
        else:
            accepted_at = self.accepted_at

        implemented_at: None | str | Unset
        if isinstance(self.implemented_at, Unset):
            implemented_at = UNSET
        elif isinstance(self.implemented_at, datetime.datetime):
            implemented_at = self.implemented_at.isoformat()
        else:
            implemented_at = self.implemented_at

        verified_at: None | str | Unset
        if isinstance(self.verified_at, Unset):
            verified_at = UNSET
        elif isinstance(self.verified_at, datetime.datetime):
            verified_at = self.verified_at.isoformat()
        else:
            verified_at = self.verified_at

        rejected_at: None | str | Unset
        if isinstance(self.rejected_at, Unset):
            rejected_at = UNSET
        elif isinstance(self.rejected_at, datetime.datetime):
            rejected_at = self.rejected_at.isoformat()
        else:
            rejected_at = self.rejected_at

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
                "title": title,
                "evidence": evidence,
                "estimatedMonthlySaving": estimated_monthly_saving,
                "currency": currency,
                "costBasis": cost_basis,
                "owner": owner,
                "confidence": confidence,
                "risk": risk,
                "effort": effort,
                "status": status,
                "source": source,
                "createdAt": created_at,
            }
        )
        if rejection_reason is not UNSET:
            field_dict["rejectionReason"] = rejection_reason
        if verified_monthly_saving is not UNSET:
            field_dict["verifiedMonthlySaving"] = verified_monthly_saving
        if kind is not UNSET:
            field_dict["kind"] = kind
        if resource is not UNSET:
            field_dict["resource"] = resource
        if scope is not UNSET:
            field_dict["scope"] = scope
        if last_seen_at is not UNSET:
            field_dict["lastSeenAt"] = last_seen_at
        if last_measurement_outcome is not UNSET:
            field_dict["lastMeasurementOutcome"] = last_measurement_outcome
        if last_measurement_scope is not UNSET:
            field_dict["lastMeasurementScope"] = last_measurement_scope
        if last_measurement_realized_monthly is not UNSET:
            field_dict["lastMeasurementRealizedMonthly"] = (
                last_measurement_realized_monthly
            )
        if last_measured_at is not UNSET:
            field_dict["lastMeasuredAt"] = last_measured_at
        if accepted_at is not UNSET:
            field_dict["acceptedAt"] = accepted_at
        if implemented_at is not UNSET:
            field_dict["implementedAt"] = implemented_at
        if verified_at is not UNSET:
            field_dict["verifiedAt"] = verified_at
        if rejected_at is not UNSET:
            field_dict["rejectedAt"] = rejected_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        evidence = d.pop("evidence")

        estimated_monthly_saving = d.pop("estimatedMonthlySaving")

        currency = d.pop("currency")

        cost_basis = d.pop("costBasis")

        owner = d.pop("owner")

        confidence = d.pop("confidence")

        risk = d.pop("risk")

        effort = d.pop("effort")

        status = d.pop("status")

        source = d.pop("source")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        def _parse_rejection_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rejection_reason = _parse_rejection_reason(d.pop("rejectionReason", UNSET))

        def _parse_verified_monthly_saving(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        verified_monthly_saving = _parse_verified_monthly_saving(
            d.pop("verifiedMonthlySaving", UNSET)
        )

        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))

        def _parse_resource(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource = _parse_resource(d.pop("resource", UNSET))

        def _parse_scope(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scope = _parse_scope(d.pop("scope", UNSET))

        def _parse_last_seen_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_seen_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_seen_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_seen_at = _parse_last_seen_at(d.pop("lastSeenAt", UNSET))

        def _parse_last_measurement_outcome(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_measurement_outcome = _parse_last_measurement_outcome(
            d.pop("lastMeasurementOutcome", UNSET)
        )

        def _parse_last_measurement_scope(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_measurement_scope = _parse_last_measurement_scope(
            d.pop("lastMeasurementScope", UNSET)
        )

        def _parse_last_measurement_realized_monthly(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_measurement_realized_monthly = _parse_last_measurement_realized_monthly(
            d.pop("lastMeasurementRealizedMonthly", UNSET)
        )

        def _parse_last_measured_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_measured_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_measured_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_measured_at = _parse_last_measured_at(d.pop("lastMeasuredAt", UNSET))

        def _parse_accepted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                accepted_at_type_0 = datetime.datetime.fromisoformat(data)

                return accepted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        accepted_at = _parse_accepted_at(d.pop("acceptedAt", UNSET))

        def _parse_implemented_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                implemented_at_type_0 = datetime.datetime.fromisoformat(data)

                return implemented_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        implemented_at = _parse_implemented_at(d.pop("implementedAt", UNSET))

        def _parse_verified_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                verified_at_type_0 = datetime.datetime.fromisoformat(data)

                return verified_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        verified_at = _parse_verified_at(d.pop("verifiedAt", UNSET))

        def _parse_rejected_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rejected_at_type_0 = datetime.datetime.fromisoformat(data)

                return rejected_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        rejected_at = _parse_rejected_at(d.pop("rejectedAt", UNSET))

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

        savings_item_response = cls(
            id=id,
            title=title,
            evidence=evidence,
            estimated_monthly_saving=estimated_monthly_saving,
            currency=currency,
            cost_basis=cost_basis,
            owner=owner,
            confidence=confidence,
            risk=risk,
            effort=effort,
            status=status,
            source=source,
            created_at=created_at,
            rejection_reason=rejection_reason,
            verified_monthly_saving=verified_monthly_saving,
            kind=kind,
            resource=resource,
            scope=scope,
            last_seen_at=last_seen_at,
            last_measurement_outcome=last_measurement_outcome,
            last_measurement_scope=last_measurement_scope,
            last_measurement_realized_monthly=last_measurement_realized_monthly,
            last_measured_at=last_measured_at,
            accepted_at=accepted_at,
            implemented_at=implemented_at,
            verified_at=verified_at,
            rejected_at=rejected_at,
            updated_at=updated_at,
        )

        return savings_item_response
