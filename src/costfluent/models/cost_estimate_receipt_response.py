from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_estimate_planned_response import CostEstimatePlannedResponse


T = TypeVar("T", bound="CostEstimateReceiptResponse")


@_attrs_define
class CostEstimateReceiptResponse:
    """
    Attributes:
        id (str):
        state (str):
        applied_on (datetime.date | None | Unset):
        planned (CostEstimatePlannedResponse | None | Unset):
    """

    id: str
    state: str
    applied_on: datetime.date | None | Unset = UNSET
    planned: CostEstimatePlannedResponse | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.cost_estimate_planned_response import CostEstimatePlannedResponse

        id = self.id

        state = self.state

        applied_on: None | str | Unset
        if isinstance(self.applied_on, Unset):
            applied_on = UNSET
        elif isinstance(self.applied_on, datetime.date):
            applied_on = self.applied_on.isoformat()
        else:
            applied_on = self.applied_on

        planned: dict[str, Any] | None | Unset
        if isinstance(self.planned, Unset):
            planned = UNSET
        elif isinstance(self.planned, CostEstimatePlannedResponse):
            planned = self.planned.to_dict()
        else:
            planned = self.planned

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "state": state,
            }
        )
        if applied_on is not UNSET:
            field_dict["appliedOn"] = applied_on
        if planned is not UNSET:
            field_dict["planned"] = planned

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.cost_estimate_planned_response import CostEstimatePlannedResponse

        d = dict(src_dict)
        id = d.pop("id")

        state = d.pop("state")

        def _parse_applied_on(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                applied_on_type_0 = datetime.date.fromisoformat(data)

                return applied_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        applied_on = _parse_applied_on(d.pop("appliedOn", UNSET))

        def _parse_planned(data: object) -> CostEstimatePlannedResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                planned_type_0 = CostEstimatePlannedResponse.from_dict(data)

                return planned_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CostEstimatePlannedResponse | None | Unset, data)

        planned = _parse_planned(d.pop("planned", UNSET))

        cost_estimate_receipt_response = cls(
            id=id,
            state=state,
            applied_on=applied_on,
            planned=planned,
        )

        return cost_estimate_receipt_response
