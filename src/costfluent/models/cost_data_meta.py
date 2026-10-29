from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency_presentation import CurrencyPresentation


T = TypeVar("T", bound="CostDataMeta")


@_attrs_define
class CostDataMeta:
    """
    Attributes:
        start_date (datetime.date):
        end_date (datetime.date):
        granularity (str):
        measure (str):
        total_records (int):
        presentation (CurrencyPresentation):
        commitment_discounts (str):
        data_version (str):
        total_cost (None | str | Unset):
        currency (None | str | Unset):
        history_floor (datetime.date | None | Unset):
        data_through (datetime.date | None | Unset):
    """

    start_date: datetime.date
    end_date: datetime.date
    granularity: str
    measure: str
    total_records: int
    presentation: CurrencyPresentation
    commitment_discounts: str
    data_version: str
    total_cost: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    history_floor: datetime.date | None | Unset = UNSET
    data_through: datetime.date | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        granularity = self.granularity

        measure = self.measure

        total_records = self.total_records

        presentation = self.presentation.to_dict()

        commitment_discounts = self.commitment_discounts

        data_version = self.data_version

        total_cost: None | str | Unset
        if isinstance(self.total_cost, Unset):
            total_cost = UNSET
        else:
            total_cost = self.total_cost

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

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

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "startDate": start_date,
                "endDate": end_date,
                "granularity": granularity,
                "measure": measure,
                "totalRecords": total_records,
                "presentation": presentation,
                "commitmentDiscounts": commitment_discounts,
                "dataVersion": data_version,
            }
        )
        if total_cost is not UNSET:
            field_dict["totalCost"] = total_cost
        if currency is not UNSET:
            field_dict["currency"] = currency
        if history_floor is not UNSET:
            field_dict["historyFloor"] = history_floor
        if data_through is not UNSET:
            field_dict["dataThrough"] = data_through

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.currency_presentation import CurrencyPresentation

        d = dict(src_dict)
        start_date = datetime.date.fromisoformat(d.pop("startDate"))

        end_date = datetime.date.fromisoformat(d.pop("endDate"))

        granularity = d.pop("granularity")

        measure = d.pop("measure")

        total_records = d.pop("totalRecords")

        presentation = CurrencyPresentation.from_dict(d.pop("presentation"))

        commitment_discounts = d.pop("commitmentDiscounts")

        data_version = d.pop("dataVersion")

        def _parse_total_cost(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_cost = _parse_total_cost(d.pop("totalCost", UNSET))

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

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

        cost_data_meta = cls(
            start_date=start_date,
            end_date=end_date,
            granularity=granularity,
            measure=measure,
            total_records=total_records,
            presentation=presentation,
            commitment_discounts=commitment_discounts,
            data_version=data_version,
            total_cost=total_cost,
            currency=currency,
            history_floor=history_floor,
            data_through=data_through,
        )

        return cost_data_meta
