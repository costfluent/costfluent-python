from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_cost_upload_error import CustomCostUploadError
    from ..models.custom_cost_upload_response_billed_totals_type_0 import (
        CustomCostUploadResponseBilledTotalsType0,
    )


T = TypeVar("T", bound="CustomCostUploadResponse")


@_attrs_define
class CustomCostUploadResponse:
    """
    Attributes:
        id (str):
        status (str):
        file_name (str):
        file_size_bytes (int):
        total_rows (int):
        success_rows (int):
        error_rows (int):
        uploaded_at (datetime.datetime):
        covered_from (datetime.date | None | Unset):
        covered_to (datetime.date | None | Unset):
        billed_totals (CustomCostUploadResponseBilledTotalsType0 | None | Unset):
        processed_at (datetime.datetime | None | Unset):
        errors (list[CustomCostUploadError] | None | Unset):
    """

    id: str
    status: str
    file_name: str
    file_size_bytes: int
    total_rows: int
    success_rows: int
    error_rows: int
    uploaded_at: datetime.datetime
    covered_from: datetime.date | None | Unset = UNSET
    covered_to: datetime.date | None | Unset = UNSET
    billed_totals: CustomCostUploadResponseBilledTotalsType0 | None | Unset = UNSET
    processed_at: datetime.datetime | None | Unset = UNSET
    errors: list[CustomCostUploadError] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_cost_upload_response_billed_totals_type_0 import (
            CustomCostUploadResponseBilledTotalsType0,
        )

        id = self.id

        status = self.status

        file_name = self.file_name

        file_size_bytes = self.file_size_bytes

        total_rows = self.total_rows

        success_rows = self.success_rows

        error_rows = self.error_rows

        uploaded_at = self.uploaded_at.isoformat()

        covered_from: None | str | Unset
        if isinstance(self.covered_from, Unset):
            covered_from = UNSET
        elif isinstance(self.covered_from, datetime.date):
            covered_from = self.covered_from.isoformat()
        else:
            covered_from = self.covered_from

        covered_to: None | str | Unset
        if isinstance(self.covered_to, Unset):
            covered_to = UNSET
        elif isinstance(self.covered_to, datetime.date):
            covered_to = self.covered_to.isoformat()
        else:
            covered_to = self.covered_to

        billed_totals: dict[str, Any] | None | Unset
        if isinstance(self.billed_totals, Unset):
            billed_totals = UNSET
        elif isinstance(self.billed_totals, CustomCostUploadResponseBilledTotalsType0):
            billed_totals = self.billed_totals.to_dict()
        else:
            billed_totals = self.billed_totals

        processed_at: None | str | Unset
        if isinstance(self.processed_at, Unset):
            processed_at = UNSET
        elif isinstance(self.processed_at, datetime.datetime):
            processed_at = self.processed_at.isoformat()
        else:
            processed_at = self.processed_at

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
                "id": id,
                "status": status,
                "fileName": file_name,
                "fileSizeBytes": file_size_bytes,
                "totalRows": total_rows,
                "successRows": success_rows,
                "errorRows": error_rows,
                "uploadedAt": uploaded_at,
            }
        )
        if covered_from is not UNSET:
            field_dict["coveredFrom"] = covered_from
        if covered_to is not UNSET:
            field_dict["coveredTo"] = covered_to
        if billed_totals is not UNSET:
            field_dict["billedTotals"] = billed_totals
        if processed_at is not UNSET:
            field_dict["processedAt"] = processed_at
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.custom_cost_upload_error import CustomCostUploadError
        from ..models.custom_cost_upload_response_billed_totals_type_0 import (
            CustomCostUploadResponseBilledTotalsType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        status = d.pop("status")

        file_name = d.pop("fileName")

        file_size_bytes = d.pop("fileSizeBytes")

        total_rows = d.pop("totalRows")

        success_rows = d.pop("successRows")

        error_rows = d.pop("errorRows")

        uploaded_at = datetime.datetime.fromisoformat(d.pop("uploadedAt"))

        def _parse_covered_from(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                covered_from_type_0 = datetime.date.fromisoformat(data)

                return covered_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        covered_from = _parse_covered_from(d.pop("coveredFrom", UNSET))

        def _parse_covered_to(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                covered_to_type_0 = datetime.date.fromisoformat(data)

                return covered_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        covered_to = _parse_covered_to(d.pop("coveredTo", UNSET))

        def _parse_billed_totals(
            data: object,
        ) -> CustomCostUploadResponseBilledTotalsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                billed_totals_type_0 = (
                    CustomCostUploadResponseBilledTotalsType0.from_dict(data)
                )

                return billed_totals_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CustomCostUploadResponseBilledTotalsType0 | None | Unset, data)

        billed_totals = _parse_billed_totals(d.pop("billedTotals", UNSET))

        def _parse_processed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                processed_at_type_0 = datetime.datetime.fromisoformat(data)

                return processed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        processed_at = _parse_processed_at(d.pop("processedAt", UNSET))

        def _parse_errors(data: object) -> list[CustomCostUploadError] | None | Unset:
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
                    errors_type_0_item = CustomCostUploadError.from_dict(
                        errors_type_0_item_data
                    )

                    errors_type_0.append(errors_type_0_item)

                return errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CustomCostUploadError] | None | Unset, data)

        errors = _parse_errors(d.pop("errors", UNSET))

        custom_cost_upload_response = cls(
            id=id,
            status=status,
            file_name=file_name,
            file_size_bytes=file_size_bytes,
            total_rows=total_rows,
            success_rows=success_rows,
            error_rows=error_rows,
            uploaded_at=uploaded_at,
            covered_from=covered_from,
            covered_to=covered_to,
            billed_totals=billed_totals,
            processed_at=processed_at,
            errors=errors,
        )

        return custom_cost_upload_response
