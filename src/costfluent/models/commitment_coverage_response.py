from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commitment_figures_response import CommitmentFiguresResponse
    from ..models.currency_amount import CurrencyAmount


T = TypeVar("T", bound="CommitmentCoverageResponse")


@_attrs_define
class CommitmentCoverageResponse:
    """
    Attributes:
        granularity (str):
        data (list[CommitmentFiguresResponse]):
        totals (list[CommitmentFiguresResponse]):
        unconverted (list[CurrencyAmount]):
        currency (None | str | Unset):
        history_floor (datetime.date | None | Unset):
    """

    granularity: str
    data: list[CommitmentFiguresResponse]
    totals: list[CommitmentFiguresResponse]
    unconverted: list[CurrencyAmount]
    currency: None | str | Unset = UNSET
    history_floor: datetime.date | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        granularity = self.granularity

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        totals = []
        for totals_item_data in self.totals:
            totals_item = totals_item_data.to_dict()
            totals.append(totals_item)

        unconverted = []
        for unconverted_item_data in self.unconverted:
            unconverted_item = unconverted_item_data.to_dict()
            unconverted.append(unconverted_item)

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

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "granularity": granularity,
                "data": data,
                "totals": totals,
                "unconverted": unconverted,
            }
        )
        if currency is not UNSET:
            field_dict["currency"] = currency
        if history_floor is not UNSET:
            field_dict["historyFloor"] = history_floor

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.commitment_figures_response import CommitmentFiguresResponse
        from ..models.currency_amount import CurrencyAmount

        d = dict(src_dict)
        granularity = d.pop("granularity")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = CommitmentFiguresResponse.from_dict(data_item_data)

            data.append(data_item)

        totals = []
        _totals = d.pop("totals")
        for totals_item_data in _totals:
            totals_item = CommitmentFiguresResponse.from_dict(totals_item_data)

            totals.append(totals_item)

        unconverted = []
        _unconverted = d.pop("unconverted")
        for unconverted_item_data in _unconverted:
            unconverted_item = CurrencyAmount.from_dict(unconverted_item_data)

            unconverted.append(unconverted_item)

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

        commitment_coverage_response = cls(
            granularity=granularity,
            data=data,
            totals=totals,
            unconverted=unconverted,
            currency=currency,
            history_floor=history_floor,
        )

        return commitment_coverage_response
