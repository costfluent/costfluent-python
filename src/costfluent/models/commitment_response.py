from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommitmentResponse")


@_attrs_define
class CommitmentResponse:
    """
    Attributes:
        id (str):
        provider_id (str):
        provider_name (str):
        provider (str):
        type_ (str):
        description (str):
        account (str):
        region (str):
        service (str):
        status (str):
        provider_status (str):
        currency (str):
        utilization_from (datetime.date):
        utilization_to (datetime.date):
        last_read_at (datetime.datetime):
        starts_at (datetime.datetime | None | Unset):
        ends_at (datetime.datetime | None | Unset):
        days_until_expiry (int | None | Unset):
        term_years (int | None | Unset):
        payment_option (None | str | Unset):
        hourly_commitment (None | str | Unset):
        full_term_cost (None | str | Unset):
        utilization_percentage (float | None | Unset):
        unused_cost (None | str | Unset):
    """

    id: str
    provider_id: str
    provider_name: str
    provider: str
    type_: str
    description: str
    account: str
    region: str
    service: str
    status: str
    provider_status: str
    currency: str
    utilization_from: datetime.date
    utilization_to: datetime.date
    last_read_at: datetime.datetime
    starts_at: datetime.datetime | None | Unset = UNSET
    ends_at: datetime.datetime | None | Unset = UNSET
    days_until_expiry: int | None | Unset = UNSET
    term_years: int | None | Unset = UNSET
    payment_option: None | str | Unset = UNSET
    hourly_commitment: None | str | Unset = UNSET
    full_term_cost: None | str | Unset = UNSET
    utilization_percentage: float | None | Unset = UNSET
    unused_cost: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        provider_id = self.provider_id

        provider_name = self.provider_name

        provider = self.provider

        type_ = self.type_

        description = self.description

        account = self.account

        region = self.region

        service = self.service

        status = self.status

        provider_status = self.provider_status

        currency = self.currency

        utilization_from = self.utilization_from.isoformat()

        utilization_to = self.utilization_to.isoformat()

        last_read_at = self.last_read_at.isoformat()

        starts_at: None | str | Unset
        if isinstance(self.starts_at, Unset):
            starts_at = UNSET
        elif isinstance(self.starts_at, datetime.datetime):
            starts_at = self.starts_at.isoformat()
        else:
            starts_at = self.starts_at

        ends_at: None | str | Unset
        if isinstance(self.ends_at, Unset):
            ends_at = UNSET
        elif isinstance(self.ends_at, datetime.datetime):
            ends_at = self.ends_at.isoformat()
        else:
            ends_at = self.ends_at

        days_until_expiry: int | None | Unset
        if isinstance(self.days_until_expiry, Unset):
            days_until_expiry = UNSET
        else:
            days_until_expiry = self.days_until_expiry

        term_years: int | None | Unset
        if isinstance(self.term_years, Unset):
            term_years = UNSET
        else:
            term_years = self.term_years

        payment_option: None | str | Unset
        if isinstance(self.payment_option, Unset):
            payment_option = UNSET
        else:
            payment_option = self.payment_option

        hourly_commitment: None | str | Unset
        if isinstance(self.hourly_commitment, Unset):
            hourly_commitment = UNSET
        else:
            hourly_commitment = self.hourly_commitment

        full_term_cost: None | str | Unset
        if isinstance(self.full_term_cost, Unset):
            full_term_cost = UNSET
        else:
            full_term_cost = self.full_term_cost

        utilization_percentage: float | None | Unset
        if isinstance(self.utilization_percentage, Unset):
            utilization_percentage = UNSET
        else:
            utilization_percentage = self.utilization_percentage

        unused_cost: None | str | Unset
        if isinstance(self.unused_cost, Unset):
            unused_cost = UNSET
        else:
            unused_cost = self.unused_cost

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "providerId": provider_id,
                "providerName": provider_name,
                "provider": provider,
                "type": type_,
                "description": description,
                "account": account,
                "region": region,
                "service": service,
                "status": status,
                "providerStatus": provider_status,
                "currency": currency,
                "utilizationFrom": utilization_from,
                "utilizationTo": utilization_to,
                "lastReadAt": last_read_at,
            }
        )
        if starts_at is not UNSET:
            field_dict["startsAt"] = starts_at
        if ends_at is not UNSET:
            field_dict["endsAt"] = ends_at
        if days_until_expiry is not UNSET:
            field_dict["daysUntilExpiry"] = days_until_expiry
        if term_years is not UNSET:
            field_dict["termYears"] = term_years
        if payment_option is not UNSET:
            field_dict["paymentOption"] = payment_option
        if hourly_commitment is not UNSET:
            field_dict["hourlyCommitment"] = hourly_commitment
        if full_term_cost is not UNSET:
            field_dict["fullTermCost"] = full_term_cost
        if utilization_percentage is not UNSET:
            field_dict["utilizationPercentage"] = utilization_percentage
        if unused_cost is not UNSET:
            field_dict["unusedCost"] = unused_cost

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        provider_id = d.pop("providerId")

        provider_name = d.pop("providerName")

        provider = d.pop("provider")

        type_ = d.pop("type")

        description = d.pop("description")

        account = d.pop("account")

        region = d.pop("region")

        service = d.pop("service")

        status = d.pop("status")

        provider_status = d.pop("providerStatus")

        currency = d.pop("currency")

        utilization_from = datetime.date.fromisoformat(d.pop("utilizationFrom"))

        utilization_to = datetime.date.fromisoformat(d.pop("utilizationTo"))

        last_read_at = datetime.datetime.fromisoformat(d.pop("lastReadAt"))

        def _parse_starts_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                starts_at_type_0 = datetime.datetime.fromisoformat(data)

                return starts_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        starts_at = _parse_starts_at(d.pop("startsAt", UNSET))

        def _parse_ends_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ends_at_type_0 = datetime.datetime.fromisoformat(data)

                return ends_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        ends_at = _parse_ends_at(d.pop("endsAt", UNSET))

        def _parse_days_until_expiry(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        days_until_expiry = _parse_days_until_expiry(d.pop("daysUntilExpiry", UNSET))

        def _parse_term_years(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        term_years = _parse_term_years(d.pop("termYears", UNSET))

        def _parse_payment_option(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_option = _parse_payment_option(d.pop("paymentOption", UNSET))

        def _parse_hourly_commitment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hourly_commitment = _parse_hourly_commitment(d.pop("hourlyCommitment", UNSET))

        def _parse_full_term_cost(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_term_cost = _parse_full_term_cost(d.pop("fullTermCost", UNSET))

        def _parse_utilization_percentage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        utilization_percentage = _parse_utilization_percentage(
            d.pop("utilizationPercentage", UNSET)
        )

        def _parse_unused_cost(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unused_cost = _parse_unused_cost(d.pop("unusedCost", UNSET))

        commitment_response = cls(
            id=id,
            provider_id=provider_id,
            provider_name=provider_name,
            provider=provider,
            type_=type_,
            description=description,
            account=account,
            region=region,
            service=service,
            status=status,
            provider_status=provider_status,
            currency=currency,
            utilization_from=utilization_from,
            utilization_to=utilization_to,
            last_read_at=last_read_at,
            starts_at=starts_at,
            ends_at=ends_at,
            days_until_expiry=days_until_expiry,
            term_years=term_years,
            payment_option=payment_option,
            hourly_commitment=hourly_commitment,
            full_term_cost=full_term_cost,
            utilization_percentage=utilization_percentage,
            unused_cost=unused_cost,
        )

        return commitment_response
