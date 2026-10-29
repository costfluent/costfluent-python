from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnomalyContributorResponse")


@_attrs_define
class AnomalyContributorResponse:
    """
    Attributes:
        resource_id (str):
        increase (str):
        account_id (None | str | Unset):
    """

    resource_id: str
    increase: str
    account_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        resource_id = self.resource_id

        increase = self.increase

        account_id: None | str | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "resourceId": resource_id,
                "increase": increase,
            }
        )
        if account_id is not UNSET:
            field_dict["accountId"] = account_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        resource_id = d.pop("resourceId")

        increase = d.pop("increase")

        def _parse_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_id = _parse_account_id(d.pop("accountId", UNSET))

        anomaly_contributor_response = cls(
            resource_id=resource_id,
            increase=increase,
            account_id=account_id,
        )

        return anomaly_contributor_response
