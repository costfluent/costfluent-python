from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.fx_policy_response import FxPolicyResponse


T = TypeVar("T", bound="FxPolicyStatusResponse")


@_attrs_define
class FxPolicyStatusResponse:
    """
    Attributes:
        available (bool):
        current (FxPolicyResponse | None):
        history (list[FxPolicyResponse]):
    """

    available: bool
    current: FxPolicyResponse | None
    history: list[FxPolicyResponse]

    def to_dict(self) -> dict[str, Any]:
        from ..models.fx_policy_response import FxPolicyResponse

        available = self.available

        current: dict[str, Any] | None
        if isinstance(self.current, FxPolicyResponse):
            current = self.current.to_dict()
        else:
            current = self.current

        history = []
        for history_item_data in self.history:
            history_item = history_item_data.to_dict()
            history.append(history_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "available": available,
                "current": current,
                "history": history,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.fx_policy_response import FxPolicyResponse

        d = dict(src_dict)
        available = d.pop("available")

        def _parse_current(data: object) -> FxPolicyResponse | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_type_0 = FxPolicyResponse.from_dict(data)

                return current_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FxPolicyResponse | None, data)

        current = _parse_current(d.pop("current"))

        history = []
        _history = d.pop("history")
        for history_item_data in _history:
            history_item = FxPolicyResponse.from_dict(history_item_data)

            history.append(history_item)

        fx_policy_status_response = cls(
            available=available,
            current=current,
            history=history,
        )

        return fx_policy_status_response
