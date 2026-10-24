from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_validation_error import CostValidationError


T = TypeVar("T", bound="SubmitCostsResponse")


@_attrs_define
class SubmitCostsResponse:
    """
    Attributes:
        batch_id (str):
        total_rows (int):
        accepted_rows (int):
        rejected_rows (int):
        errors (list[CostValidationError] | None | Unset):
    """

    batch_id: str
    total_rows: int
    accepted_rows: int
    rejected_rows: int
    errors: list[CostValidationError] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        batch_id = self.batch_id

        total_rows = self.total_rows

        accepted_rows = self.accepted_rows

        rejected_rows = self.rejected_rows

        errors: list[dict[str, Any]] | None | Unset
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = []
            for errors_type_0_item_data in self.errors:
                errors_type_0_item = errors_type_0_item_data.to_dict()
                errors.append(errors_type_0_item)

        else:
            errors = self.errors

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "batchId": batch_id,
                "totalRows": total_rows,
                "acceptedRows": accepted_rows,
                "rejectedRows": rejected_rows,
            }
        )
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.cost_validation_error import CostValidationError

        d = dict(src_dict)
        batch_id = d.pop("batchId")

        total_rows = d.pop("totalRows")

        accepted_rows = d.pop("acceptedRows")

        rejected_rows = d.pop("rejectedRows")

        def _parse_errors(data: object) -> list[CostValidationError] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = []
                _errors_type_0 = data
                for errors_type_0_item_data in _errors_type_0:
                    errors_type_0_item = CostValidationError.from_dict(
                        errors_type_0_item_data
                    )

                    errors_type_0.append(errors_type_0_item)

                return errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CostValidationError] | None | Unset, data)

        errors = _parse_errors(d.pop("errors", UNSET))

        submit_costs_response = cls(
            batch_id=batch_id,
            total_rows=total_rows,
            accepted_rows=accepted_rows,
            rejected_rows=rejected_rows,
            errors=errors,
        )

        return submit_costs_response
