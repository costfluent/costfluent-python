from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency_presentation import CurrencyPresentation
    from ..models.provider_cost_breakdown import ProviderCostBreakdown
    from ..models.service_cost_breakdown import ServiceCostBreakdown


T = TypeVar("T", bound="CostSummaryResponse")


@_attrs_define
class CostSummaryResponse:
    """
    Attributes:
        presentation (CurrencyPresentation):
        top_services (list[ServiceCostBreakdown]):
        by_provider (list[ProviderCostBreakdown]):
        total_cost (None | str | Unset):
        total_list_cost (None | str | Unset):
        total_amortized_cost (None | str | Unset):
        currency (None | str | Unset):
        cost_change (None | str | Unset):
        cost_change_percent (float | None | Unset):
        history_floor (datetime.date | None | Unset):
        data_through (datetime.date | None | Unset):
        compared_through (datetime.date | None | Unset):
    """

    presentation: CurrencyPresentation
    top_services: list[ServiceCostBreakdown]
    by_provider: list[ProviderCostBreakdown]
    total_cost: None | str | Unset = UNSET
    total_list_cost: None | str | Unset = UNSET
    total_amortized_cost: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    cost_change: None | str | Unset = UNSET
    cost_change_percent: float | None | Unset = UNSET
    history_floor: datetime.date | None | Unset = UNSET
    data_through: datetime.date | None | Unset = UNSET
    compared_through: datetime.date | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        presentation = self.presentation.to_dict()

        top_services = []
        for top_services_item_data in self.top_services:
            top_services_item = top_services_item_data.to_dict()
            top_services.append(top_services_item)

        by_provider = []
        for by_provider_item_data in self.by_provider:
            by_provider_item = by_provider_item_data.to_dict()
            by_provider.append(by_provider_item)

        total_cost: None | str | Unset
        if isinstance(self.total_cost, Unset):
            total_cost = UNSET
        else:
            total_cost = self.total_cost

        total_list_cost: None | str | Unset
        if isinstance(self.total_list_cost, Unset):
            total_list_cost = UNSET
        else:
            total_list_cost = self.total_list_cost

        total_amortized_cost: None | str | Unset
        if isinstance(self.total_amortized_cost, Unset):
            total_amortized_cost = UNSET
        else:
            total_amortized_cost = self.total_amortized_cost

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        cost_change: None | str | Unset
        if isinstance(self.cost_change, Unset):
            cost_change = UNSET
        else:
            cost_change = self.cost_change

        cost_change_percent: float | None | Unset
        if isinstance(self.cost_change_percent, Unset):
            cost_change_percent = UNSET
        else:
            cost_change_percent = self.cost_change_percent

        history_floor: None | str | Unset
        if isinstance(self.history_floor, Unset):
            history_floor = UNSET
        elif isinstance(self.history_floor, datetime.date):
            history_floor = self.history_floor.isoformat()
        else:
            history_floor = self.history_floor

        data_through: None | str | Unset
        if isinstance(self.data_through, Unset):
            data_through = UNSET
        elif isinstance(self.data_through, datetime.date):
            data_through = self.data_through.isoformat()
        else:
            data_through = self.data_through

        compared_through: None | str | Unset
        if isinstance(self.compared_through, Unset):
            compared_through = UNSET
        elif isinstance(self.compared_through, datetime.date):
            compared_through = self.compared_through.isoformat()
        else:
            compared_through = self.compared_through

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "presentation": presentation,
                "topServices": top_services,
                "byProvider": by_provider,
            }
        )
        if total_cost is not UNSET:
            field_dict["totalCost"] = total_cost
        if total_list_cost is not UNSET:
            field_dict["totalListCost"] = total_list_cost
        if total_amortized_cost is not UNSET:
            field_dict["totalAmortizedCost"] = total_amortized_cost
        if currency is not UNSET:
            field_dict["currency"] = currency
        if cost_change is not UNSET:
            field_dict["costChange"] = cost_change
        if cost_change_percent is not UNSET:
            field_dict["costChangePercent"] = cost_change_percent
        if history_floor is not UNSET:
            field_dict["historyFloor"] = history_floor
        if data_through is not UNSET:
            field_dict["dataThrough"] = data_through
        if compared_through is not UNSET:
            field_dict["comparedThrough"] = compared_through

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.currency_presentation import CurrencyPresentation
        from ..models.provider_cost_breakdown import ProviderCostBreakdown
        from ..models.service_cost_breakdown import ServiceCostBreakdown

        d = dict(src_dict)
        presentation = CurrencyPresentation.from_dict(d.pop("presentation"))

        top_services = []
        _top_services = d.pop("topServices")
        for top_services_item_data in _top_services:
            top_services_item = ServiceCostBreakdown.from_dict(top_services_item_data)

            top_services.append(top_services_item)

        by_provider = []
        _by_provider = d.pop("byProvider")
        for by_provider_item_data in _by_provider:
            by_provider_item = ProviderCostBreakdown.from_dict(by_provider_item_data)

            by_provider.append(by_provider_item)

        def _parse_total_cost(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_cost = _parse_total_cost(d.pop("totalCost", UNSET))

        def _parse_total_list_cost(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_list_cost = _parse_total_list_cost(d.pop("totalListCost", UNSET))

        def _parse_total_amortized_cost(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_amortized_cost = _parse_total_amortized_cost(
            d.pop("totalAmortizedCost", UNSET)
        )

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_cost_change(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cost_change = _parse_cost_change(d.pop("costChange", UNSET))

        def _parse_cost_change_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cost_change_percent = _parse_cost_change_percent(
            d.pop("costChangePercent", UNSET)
        )

        def _parse_history_floor(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                history_floor_type_0 = datetime.date.fromisoformat(data)

                return history_floor_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        history_floor = _parse_history_floor(d.pop("historyFloor", UNSET))

        def _parse_data_through(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                data_through_type_0 = datetime.date.fromisoformat(data)

                return data_through_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        data_through = _parse_data_through(d.pop("dataThrough", UNSET))

        def _parse_compared_through(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                compared_through_type_0 = datetime.date.fromisoformat(data)

                return compared_through_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        compared_through = _parse_compared_through(d.pop("comparedThrough", UNSET))

        cost_summary_response = cls(
            presentation=presentation,
            top_services=top_services,
            by_provider=by_provider,
            total_cost=total_cost,
            total_list_cost=total_list_cost,
            total_amortized_cost=total_amortized_cost,
            currency=currency,
            cost_change=cost_change,
            cost_change_percent=cost_change_percent,
            history_floor=history_floor,
            data_through=data_through,
            compared_through=compared_through,
        )

        return cost_summary_response
