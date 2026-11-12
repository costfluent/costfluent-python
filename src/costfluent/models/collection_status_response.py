from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collection_month_response import CollectionMonthResponse
    from ..models.collection_status_summary_response import (
        CollectionStatusSummaryResponse,
    )
    from ..models.missing_range_response import MissingRangeResponse


T = TypeVar("T", bound="CollectionStatusResponse")


@_attrs_define
class CollectionStatusResponse:
    """
    Attributes:
        summary (CollectionStatusSummaryResponse):
        months (list[CollectionMonthResponse]):
        missing (list[MissingRangeResponse]):
        amounts_withheld_reason (None | str | Unset):
    """

    summary: CollectionStatusSummaryResponse
    months: list[CollectionMonthResponse]
    missing: list[MissingRangeResponse]
    amounts_withheld_reason: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        summary = self.summary.to_dict()

        months = []
        for months_item_data in self.months:
            months_item = months_item_data.to_dict()
            months.append(months_item)

        missing = []
        for missing_item_data in self.missing:
            missing_item = missing_item_data.to_dict()
            missing.append(missing_item)

        amounts_withheld_reason: None | str | Unset
        if isinstance(self.amounts_withheld_reason, Unset):
            amounts_withheld_reason = UNSET
        else:
            amounts_withheld_reason = self.amounts_withheld_reason

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "summary": summary,
                "months": months,
                "missing": missing,
            }
        )
        if amounts_withheld_reason is not UNSET:
            field_dict["amountsWithheldReason"] = amounts_withheld_reason

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.collection_month_response import CollectionMonthResponse
        from ..models.collection_status_summary_response import (
            CollectionStatusSummaryResponse,
        )
        from ..models.missing_range_response import MissingRangeResponse

        d = dict(src_dict)
        summary = CollectionStatusSummaryResponse.from_dict(d.pop("summary"))

        months = []
        _months = d.pop("months")
        for months_item_data in _months:
            months_item = CollectionMonthResponse.from_dict(months_item_data)

            months.append(months_item)

        missing = []
        _missing = d.pop("missing")
        for missing_item_data in _missing:
            missing_item = MissingRangeResponse.from_dict(missing_item_data)

            missing.append(missing_item)

        def _parse_amounts_withheld_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amounts_withheld_reason = _parse_amounts_withheld_reason(
            d.pop("amountsWithheldReason", UNSET)
        )

        collection_status_response = cls(
            summary=summary,
            months=months,
            missing=missing,
            amounts_withheld_reason=amounts_withheld_reason,
        )

        return collection_status_response
