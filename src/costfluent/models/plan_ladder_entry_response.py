from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlanLadderEntryResponse")


@_attrs_define
class PlanLadderEntryResponse:
    """
    Attributes:
        code (str):
        name (str):
        currency (str):
        history_days (int):
        features (list[str]):
        self_serve_available (bool):
        price_amount (None | str | Unset):
        spend_ceiling (None | str | Unset):
        max_connections (int | None | Unset):
        max_allocation_rules (int | None | Unset):
    """

    code: str
    name: str
    currency: str
    history_days: int
    features: list[str]
    self_serve_available: bool
    price_amount: None | str | Unset = UNSET
    spend_ceiling: None | str | Unset = UNSET
    max_connections: int | None | Unset = UNSET
    max_allocation_rules: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        name = self.name

        currency = self.currency

        history_days = self.history_days

        features = self.features

        self_serve_available = self.self_serve_available

        price_amount: None | str | Unset
        if isinstance(self.price_amount, Unset):
            price_amount = UNSET
        else:
            price_amount = self.price_amount

        spend_ceiling: None | str | Unset
        if isinstance(self.spend_ceiling, Unset):
            spend_ceiling = UNSET
        else:
            spend_ceiling = self.spend_ceiling

        max_connections: int | None | Unset
        if isinstance(self.max_connections, Unset):
            max_connections = UNSET
        else:
            max_connections = self.max_connections

        max_allocation_rules: int | None | Unset
        if isinstance(self.max_allocation_rules, Unset):
            max_allocation_rules = UNSET
        else:
            max_allocation_rules = self.max_allocation_rules

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "name": name,
                "currency": currency,
                "historyDays": history_days,
                "features": features,
                "selfServeAvailable": self_serve_available,
            }
        )
        if price_amount is not UNSET:
            field_dict["priceAmount"] = price_amount
        if spend_ceiling is not UNSET:
            field_dict["spendCeiling"] = spend_ceiling
        if max_connections is not UNSET:
            field_dict["maxConnections"] = max_connections
        if max_allocation_rules is not UNSET:
            field_dict["maxAllocationRules"] = max_allocation_rules

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        code = d.pop("code")

        name = d.pop("name")

        currency = d.pop("currency")

        history_days = d.pop("historyDays")

        features = cast(list[str], d.pop("features"))

        self_serve_available = d.pop("selfServeAvailable")

        def _parse_price_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        price_amount = _parse_price_amount(d.pop("priceAmount", UNSET))

        def _parse_spend_ceiling(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        spend_ceiling = _parse_spend_ceiling(d.pop("spendCeiling", UNSET))

        def _parse_max_connections(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_connections = _parse_max_connections(d.pop("maxConnections", UNSET))

        def _parse_max_allocation_rules(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_allocation_rules = _parse_max_allocation_rules(
            d.pop("maxAllocationRules", UNSET)
        )

        plan_ladder_entry_response = cls(
            code=code,
            name=name,
            currency=currency,
            history_days=history_days,
            features=features,
            self_serve_available=self_serve_available,
            price_amount=price_amount,
            spend_ceiling=spend_ceiling,
            max_connections=max_connections,
            max_allocation_rules=max_allocation_rules,
        )

        return plan_ladder_entry_response
