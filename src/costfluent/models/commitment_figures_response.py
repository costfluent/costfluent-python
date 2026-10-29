from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommitmentFiguresResponse")


@_attrs_define
class CommitmentFiguresResponse:
    """
    Attributes:
        provider (str):
        covered_on_demand_cost (str):
        eligible_on_demand_cost (str):
        actual_cost (str):
        used_commitment (str):
        date (datetime.date | None | Unset):
        unused_commitment (None | str | Unset):
        coverage_percent (float | None | Unset):
        effective_savings_rate_percent (float | None | Unset):
        utilization_percent (float | None | Unset):
    """

    provider: str
    covered_on_demand_cost: str
    eligible_on_demand_cost: str
    actual_cost: str
    used_commitment: str
    date: datetime.date | None | Unset = UNSET
    unused_commitment: None | str | Unset = UNSET
    coverage_percent: float | None | Unset = UNSET
    effective_savings_rate_percent: float | None | Unset = UNSET
    utilization_percent: float | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider

        covered_on_demand_cost = self.covered_on_demand_cost

        eligible_on_demand_cost = self.eligible_on_demand_cost

        actual_cost = self.actual_cost

        used_commitment = self.used_commitment

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.date):
            date = self.date.isoformat()
        else:
            date = self.date

        unused_commitment: None | str | Unset
        if isinstance(self.unused_commitment, Unset):
            unused_commitment = UNSET
        else:
            unused_commitment = self.unused_commitment

        coverage_percent: float | None | Unset
        if isinstance(self.coverage_percent, Unset):
            coverage_percent = UNSET
        else:
            coverage_percent = self.coverage_percent

        effective_savings_rate_percent: float | None | Unset
        if isinstance(self.effective_savings_rate_percent, Unset):
            effective_savings_rate_percent = UNSET
        else:
            effective_savings_rate_percent = self.effective_savings_rate_percent

        utilization_percent: float | None | Unset
        if isinstance(self.utilization_percent, Unset):
            utilization_percent = UNSET
        else:
            utilization_percent = self.utilization_percent

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "provider": provider,
                "coveredOnDemandCost": covered_on_demand_cost,
                "eligibleOnDemandCost": eligible_on_demand_cost,
                "actualCost": actual_cost,
                "usedCommitment": used_commitment,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date
        if unused_commitment is not UNSET:
            field_dict["unusedCommitment"] = unused_commitment
        if coverage_percent is not UNSET:
            field_dict["coveragePercent"] = coverage_percent
        if effective_savings_rate_percent is not UNSET:
            field_dict["effectiveSavingsRatePercent"] = effective_savings_rate_percent
        if utilization_percent is not UNSET:
            field_dict["utilizationPercent"] = utilization_percent

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        provider = d.pop("provider")

        covered_on_demand_cost = d.pop("coveredOnDemandCost")

        eligible_on_demand_cost = d.pop("eligibleOnDemandCost")

        actual_cost = d.pop("actualCost")

        used_commitment = d.pop("usedCommitment")

        def _parse_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = datetime.date.fromisoformat(data)

                return date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_unused_commitment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unused_commitment = _parse_unused_commitment(d.pop("unusedCommitment", UNSET))

        def _parse_coverage_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        coverage_percent = _parse_coverage_percent(d.pop("coveragePercent", UNSET))

        def _parse_effective_savings_rate_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        effective_savings_rate_percent = _parse_effective_savings_rate_percent(
            d.pop("effectiveSavingsRatePercent", UNSET)
        )

        def _parse_utilization_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        utilization_percent = _parse_utilization_percent(
            d.pop("utilizationPercent", UNSET)
        )

        commitment_figures_response = cls(
            provider=provider,
            covered_on_demand_cost=covered_on_demand_cost,
            eligible_on_demand_cost=eligible_on_demand_cost,
            actual_cost=actual_cost,
            used_commitment=used_commitment,
            date=date,
            unused_commitment=unused_commitment,
            coverage_percent=coverage_percent,
            effective_savings_rate_percent=effective_savings_rate_percent,
            utilization_percent=utilization_percent,
        )

        return commitment_figures_response
