from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.month_amount_response import MonthAmountResponse
    from ..models.provider_total_response import ProviderTotalResponse
    from ..models.restatement_response import RestatementResponse


T = TypeVar("T", bound="CollectionMonthResponse")


@_attrs_define
class CollectionMonthResponse:
    """
    Attributes:
        month (datetime.date):
        is_imported (bool):
        record_count (int):
        on_request (bool):
        provider_total (ProviderTotalResponse):
        last_imported_at (datetime.datetime | None | Unset):
        restatement (None | RestatementResponse | Unset):
        amounts (list[MonthAmountResponse] | None | Unset):
    """

    month: datetime.date
    is_imported: bool
    record_count: int
    on_request: bool
    provider_total: ProviderTotalResponse
    last_imported_at: datetime.datetime | None | Unset = UNSET
    restatement: None | RestatementResponse | Unset = UNSET
    amounts: list[MonthAmountResponse] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.restatement_response import RestatementResponse

        month = self.month.isoformat()

        is_imported = self.is_imported

        record_count = self.record_count

        on_request = self.on_request

        provider_total = self.provider_total.to_dict()

        last_imported_at: None | str | Unset
        if isinstance(self.last_imported_at, Unset):
            last_imported_at = UNSET
        elif isinstance(self.last_imported_at, datetime.datetime):
            last_imported_at = self.last_imported_at.isoformat()
        else:
            last_imported_at = self.last_imported_at

        restatement: dict[str, Any] | None | Unset
        if isinstance(self.restatement, Unset):
            restatement = UNSET
        elif isinstance(self.restatement, RestatementResponse):
            restatement = self.restatement.to_dict()
        else:
            restatement = self.restatement

        amounts: list[dict[str, Any]] | None | Unset
        if isinstance(self.amounts, Unset):
            amounts = UNSET
        elif isinstance(self.amounts, list):
            amounts = []
            for amounts_type_0_item_data in self.amounts:
                amounts_type_0_item = amounts_type_0_item_data.to_dict()
                amounts.append(amounts_type_0_item)

        else:
            amounts = self.amounts

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "month": month,
                "isImported": is_imported,
                "recordCount": record_count,
                "onRequest": on_request,
                "providerTotal": provider_total,
            }
        )
        if last_imported_at is not UNSET:
            field_dict["lastImportedAt"] = last_imported_at
        if restatement is not UNSET:
            field_dict["restatement"] = restatement
        if amounts is not UNSET:
            field_dict["amounts"] = amounts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.month_amount_response import MonthAmountResponse
        from ..models.provider_total_response import ProviderTotalResponse
        from ..models.restatement_response import RestatementResponse

        d = dict(src_dict)
        month = datetime.date.fromisoformat(d.pop("month"))

        is_imported = d.pop("isImported")

        record_count = d.pop("recordCount")

        on_request = d.pop("onRequest")

        provider_total = ProviderTotalResponse.from_dict(d.pop("providerTotal"))

        def _parse_last_imported_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_imported_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_imported_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_imported_at = _parse_last_imported_at(d.pop("lastImportedAt", UNSET))

        def _parse_restatement(data: object) -> None | RestatementResponse | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                restatement_type_0 = RestatementResponse.from_dict(data)

                return restatement_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RestatementResponse | Unset, data)

        restatement = _parse_restatement(d.pop("restatement", UNSET))

        def _parse_amounts(data: object) -> list[MonthAmountResponse] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                amounts_type_0 = []
                _amounts_type_0 = data
                for amounts_type_0_item_data in _amounts_type_0:
                    amounts_type_0_item = MonthAmountResponse.from_dict(
                        amounts_type_0_item_data
                    )

                    amounts_type_0.append(amounts_type_0_item)

                return amounts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MonthAmountResponse] | None | Unset, data)

        amounts = _parse_amounts(d.pop("amounts", UNSET))

        collection_month_response = cls(
            month=month,
            is_imported=is_imported,
            record_count=record_count,
            on_request=on_request,
            provider_total=provider_total,
            last_imported_at=last_imported_at,
            restatement=restatement,
            amounts=amounts,
        )

        return collection_month_response
