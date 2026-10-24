from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency_presentation import CurrencyPresentation
    from ..models.unit_quantity import UnitQuantity


T = TypeVar("T", bound="ReportSummaryResponse")


@_attrs_define
class ReportSummaryResponse:
    """
    Attributes:
        presentation (CurrencyPresentation):
        measure (str):
        totals_by_unit (list[UnitQuantity]):
        total_cost (None | str | Unset):
        previous_period_cost (None | str | Unset):
        change_percent (float | None | Unset):
        compared_through (datetime.date | None | Unset):
        compared_cost (None | str | Unset):
        previous_compared_through (datetime.date | None | Unset):
        currency (None | str | Unset):
    """

    presentation: CurrencyPresentation
    measure: str
    totals_by_unit: list[UnitQuantity]
    total_cost: None | str | Unset = UNSET
    previous_period_cost: None | str | Unset = UNSET
    change_percent: float | None | Unset = UNSET
    compared_through: datetime.date | None | Unset = UNSET
    compared_cost: None | str | Unset = UNSET
    previous_compared_through: datetime.date | None | Unset = UNSET
    currency: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        presentation = self.presentation.to_dict()

        measure = self.measure

        totals_by_unit = []
        for totals_by_unit_item_data in self.totals_by_unit:
            totals_by_unit_item = totals_by_unit_item_data.to_dict()
            totals_by_unit.append(totals_by_unit_item)

        total_cost: None | str | Unset
        if isinstance(self.total_cost, Unset):
            total_cost = UNSET
        else:
            total_cost = self.total_cost

        previous_period_cost: None | str | Unset
        if isinstance(self.previous_period_cost, Unset):
            previous_period_cost = UNSET
        else:
            previous_period_cost = self.previous_period_cost

        change_percent: float | None | Unset
        if isinstance(self.change_percent, Unset):
            change_percent = UNSET
        else:
            change_percent = self.change_percent

        compared_through: None | str | Unset
        if isinstance(self.compared_through, Unset):
            compared_through = UNSET
        elif isinstance(self.compared_through, datetime.date):
            compared_through = self.compared_through.isoformat()
        else:
            compared_through = self.compared_through

        compared_cost: None | str | Unset
        if isinstance(self.compared_cost, Unset):
            compared_cost = UNSET
        else:
            compared_cost = self.compared_cost

        previous_compared_through: None | str | Unset
        if isinstance(self.previous_compared_through, Unset):
            previous_compared_through = UNSET
        elif isinstance(self.previous_compared_through, datetime.date):
            previous_compared_through = self.previous_compared_through.isoformat()
        else:
            previous_compared_through = self.previous_compared_through

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "presentation": presentation,
                "measure": measure,
                "totalsByUnit": totals_by_unit,
            }
        )
        if total_cost is not UNSET:
            field_dict["totalCost"] = total_cost
        if previous_period_cost is not UNSET:
            field_dict["previousPeriodCost"] = previous_period_cost
        if change_percent is not UNSET:
            field_dict["changePercent"] = change_percent
        if compared_through is not UNSET:
            field_dict["comparedThrough"] = compared_through
        if compared_cost is not UNSET:
            field_dict["comparedCost"] = compared_cost
        if previous_compared_through is not UNSET:
            field_dict["previousComparedThrough"] = previous_compared_through
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.currency_presentation import CurrencyPresentation
        from ..models.unit_quantity import UnitQuantity

        d = dict(src_dict)
        presentation = CurrencyPresentation.from_dict(d.pop("presentation"))

        measure = d.pop("measure")

        totals_by_unit = []
        _totals_by_unit = d.pop("totalsByUnit")
        for totals_by_unit_item_data in _totals_by_unit:
            totals_by_unit_item = UnitQuantity.from_dict(totals_by_unit_item_data)

            totals_by_unit.append(totals_by_unit_item)

        def _parse_total_cost(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_cost = _parse_total_cost(d.pop("totalCost", UNSET))

        def _parse_previous_period_cost(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_period_cost = _parse_previous_period_cost(
            d.pop("previousPeriodCost", UNSET)
        )

        def _parse_change_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        change_percent = _parse_change_percent(d.pop("changePercent", UNSET))

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

        def _parse_compared_cost(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        compared_cost = _parse_compared_cost(d.pop("comparedCost", UNSET))

        def _parse_previous_compared_through(
            data: object,
        ) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                previous_compared_through_type_0 = datetime.date.fromisoformat(data)

                return previous_compared_through_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        previous_compared_through = _parse_previous_compared_through(
            d.pop("previousComparedThrough", UNSET)
        )

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        report_summary_response = cls(
            presentation=presentation,
            measure=measure,
            totals_by_unit=totals_by_unit,
            total_cost=total_cost,
            previous_period_cost=previous_period_cost,
            change_percent=change_percent,
            compared_through=compared_through,
            compared_cost=compared_cost,
            previous_compared_through=previous_compared_through,
            currency=currency,
        )

        return report_summary_response
