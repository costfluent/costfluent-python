from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="FxPolicyResponse")


@_attrs_define
class FxPolicyResponse:
    """
    Attributes:
        token (str):
        method (str):
        source (str):
        presentation_currency (str):
        effective_from (datetime.date):
        effective_to_exclusive (datetime.date | None):
        set_at (datetime.datetime):
        is_current (bool):
        description (str):
    """

    token: str
    method: str
    source: str
    presentation_currency: str
    effective_from: datetime.date
    effective_to_exclusive: datetime.date | None
    set_at: datetime.datetime
    is_current: bool
    description: str

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        method = self.method

        source = self.source

        presentation_currency = self.presentation_currency

        effective_from = self.effective_from.isoformat()

        effective_to_exclusive: None | str
        if isinstance(self.effective_to_exclusive, datetime.date):
            effective_to_exclusive = self.effective_to_exclusive.isoformat()
        else:
            effective_to_exclusive = self.effective_to_exclusive

        set_at = self.set_at.isoformat()

        is_current = self.is_current

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "token": token,
                "method": method,
                "source": source,
                "presentationCurrency": presentation_currency,
                "effectiveFrom": effective_from,
                "effectiveToExclusive": effective_to_exclusive,
                "setAt": set_at,
                "isCurrent": is_current,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        token = d.pop("token")

        method = d.pop("method")

        source = d.pop("source")

        presentation_currency = d.pop("presentationCurrency")

        effective_from = datetime.date.fromisoformat(d.pop("effectiveFrom"))

        def _parse_effective_to_exclusive(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_to_exclusive_type_0 = datetime.date.fromisoformat(data)

                return effective_to_exclusive_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        effective_to_exclusive = _parse_effective_to_exclusive(
            d.pop("effectiveToExclusive")
        )

        set_at = datetime.datetime.fromisoformat(d.pop("setAt"))

        is_current = d.pop("isCurrent")

        description = d.pop("description")

        fx_policy_response = cls(
            token=token,
            method=method,
            source=source,
            presentation_currency=presentation_currency,
            effective_from=effective_from,
            effective_to_exclusive=effective_to_exclusive,
            set_at=set_at,
            is_current=is_current,
            description=description,
        )

        return fx_policy_response
