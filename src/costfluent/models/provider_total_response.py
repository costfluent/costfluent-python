from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProviderTotalResponse")


@_attrs_define
class ProviderTotalResponse:
    """
    Attributes:
        status (str):
        reason (None | str | Unset):
        provider_amount (None | str | Unset):
        costfluent_amount (None | str | Unset):
        difference (None | str | Unset):
        tolerance (None | str | Unset):
        currency (None | str | Unset):
        compared_at (datetime.datetime | None | Unset):
    """

    status: str
    reason: None | str | Unset = UNSET
    provider_amount: None | str | Unset = UNSET
    costfluent_amount: None | str | Unset = UNSET
    difference: None | str | Unset = UNSET
    tolerance: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    compared_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        provider_amount: None | str | Unset
        if isinstance(self.provider_amount, Unset):
            provider_amount = UNSET
        else:
            provider_amount = self.provider_amount

        costfluent_amount: None | str | Unset
        if isinstance(self.costfluent_amount, Unset):
            costfluent_amount = UNSET
        else:
            costfluent_amount = self.costfluent_amount

        difference: None | str | Unset
        if isinstance(self.difference, Unset):
            difference = UNSET
        else:
            difference = self.difference

        tolerance: None | str | Unset
        if isinstance(self.tolerance, Unset):
            tolerance = UNSET
        else:
            tolerance = self.tolerance

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        compared_at: None | str | Unset
        if isinstance(self.compared_at, Unset):
            compared_at = UNSET
        elif isinstance(self.compared_at, datetime.datetime):
            compared_at = self.compared_at.isoformat()
        else:
            compared_at = self.compared_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason
        if provider_amount is not UNSET:
            field_dict["providerAmount"] = provider_amount
        if costfluent_amount is not UNSET:
            field_dict["costfluentAmount"] = costfluent_amount
        if difference is not UNSET:
            field_dict["difference"] = difference
        if tolerance is not UNSET:
            field_dict["tolerance"] = tolerance
        if currency is not UNSET:
            field_dict["currency"] = currency
        if compared_at is not UNSET:
            field_dict["comparedAt"] = compared_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = d.pop("status")

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_provider_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_amount = _parse_provider_amount(d.pop("providerAmount", UNSET))

        def _parse_costfluent_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        costfluent_amount = _parse_costfluent_amount(d.pop("costfluentAmount", UNSET))

        def _parse_difference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        difference = _parse_difference(d.pop("difference", UNSET))

        def _parse_tolerance(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tolerance = _parse_tolerance(d.pop("tolerance", UNSET))

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_compared_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                compared_at_type_0 = datetime.datetime.fromisoformat(data)

                return compared_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        compared_at = _parse_compared_at(d.pop("comparedAt", UNSET))

        provider_total_response = cls(
            status=status,
            reason=reason,
            provider_amount=provider_amount,
            costfluent_amount=costfluent_amount,
            difference=difference,
            tolerance=tolerance,
            currency=currency,
            compared_at=compared_at,
        )

        return provider_total_response
