from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.budget_alert_basis_value import BudgetAlertBasisValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="BudgetAlertRequest")


@_attrs_define
class BudgetAlertRequest:
    """
    Attributes:
        threshold_percent (int | Unset):
        basis (BudgetAlertBasisValue | Unset):
    """

    threshold_percent: int | Unset = UNSET
    basis: BudgetAlertBasisValue | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        threshold_percent = self.threshold_percent

        basis: str | Unset = UNSET
        if not isinstance(self.basis, Unset):
            basis = self.basis.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if threshold_percent is not UNSET:
            field_dict["thresholdPercent"] = threshold_percent
        if basis is not UNSET:
            field_dict["basis"] = basis

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        threshold_percent = d.pop("thresholdPercent", UNSET)

        _basis = d.pop("basis", UNSET)
        basis: BudgetAlertBasisValue | Unset
        if isinstance(_basis, Unset):
            basis = UNSET
        else:
            basis = BudgetAlertBasisValue(_basis)

        budget_alert_request = cls(
            threshold_percent=threshold_percent,
            basis=basis,
        )

        return budget_alert_request
