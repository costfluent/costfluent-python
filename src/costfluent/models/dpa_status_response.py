from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.dpa_execution_response import DpaExecutionResponse


T = TypeVar("T", bound="DpaStatusResponse")


@_attrs_define
class DpaStatusResponse:
    """
    Attributes:
        required (bool):
        in_force (bool):
        current (DpaExecutionResponse | None):
        history (list[DpaExecutionResponse]):
        collection_refusal (None | str):
    """

    required: bool
    in_force: bool
    current: DpaExecutionResponse | None
    history: list[DpaExecutionResponse]
    collection_refusal: None | str

    def to_dict(self) -> dict[str, Any]:
        from ..models.dpa_execution_response import DpaExecutionResponse

        required = self.required

        in_force = self.in_force

        current: dict[str, Any] | None
        if isinstance(self.current, DpaExecutionResponse):
            current = self.current.to_dict()
        else:
            current = self.current

        history = []
        for history_item_data in self.history:
            history_item = history_item_data.to_dict()
            history.append(history_item)

        collection_refusal: None | str
        collection_refusal = self.collection_refusal

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "required": required,
                "inForce": in_force,
                "current": current,
                "history": history,
                "collectionRefusal": collection_refusal,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dpa_execution_response import DpaExecutionResponse

        d = dict(src_dict)
        required = d.pop("required")

        in_force = d.pop("inForce")

        def _parse_current(data: object) -> DpaExecutionResponse | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_type_0 = DpaExecutionResponse.from_dict(data)

                return current_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DpaExecutionResponse | None, data)

        current = _parse_current(d.pop("current"))

        history = []
        _history = d.pop("history")
        for history_item_data in _history:
            history_item = DpaExecutionResponse.from_dict(history_item_data)

            history.append(history_item)

        def _parse_collection_refusal(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        collection_refusal = _parse_collection_refusal(d.pop("collectionRefusal"))

        dpa_status_response = cls(
            required=required,
            in_force=in_force,
            current=current,
            history=history,
            collection_refusal=collection_refusal,
        )

        return dpa_status_response
