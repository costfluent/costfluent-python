from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency_amount import CurrencyAmount
    from ..models.kubernetes_efficiency_row_response import (
        KubernetesEfficiencyRowResponse,
    )


T = TypeVar("T", bound="KubernetesEfficiencyResponse")


@_attrs_define
class KubernetesEfficiencyResponse:
    """
    Attributes:
        level (str):
        rows (list[KubernetesEfficiencyRowResponse]):
        truncated (bool):
        unconverted (list[CurrencyAmount]):
        currency (None | str | Unset):
        history_floor (datetime.date | None | Unset):
    """

    level: str
    rows: list[KubernetesEfficiencyRowResponse]
    truncated: bool
    unconverted: list[CurrencyAmount]
    currency: None | str | Unset = UNSET
    history_floor: datetime.date | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        level = self.level

        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()
            rows.append(rows_item)

        truncated = self.truncated

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
                "level": level,
                "rows": rows,
                "truncated": truncated,
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
        from ..models.currency_amount import CurrencyAmount
        from ..models.kubernetes_efficiency_row_response import (
            KubernetesEfficiencyRowResponse,
        )

        d = dict(src_dict)
        level = d.pop("level")

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = KubernetesEfficiencyRowResponse.from_dict(rows_item_data)

            rows.append(rows_item)

        truncated = d.pop("truncated")

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

        kubernetes_efficiency_response = cls(
            level=level,
            rows=rows,
            truncated=truncated,
            unconverted=unconverted,
            currency=currency,
            history_floor=history_floor,
        )

        return kubernetes_efficiency_response
