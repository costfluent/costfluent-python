from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_error_entry_params_type_0 import ApiErrorEntryParamsType0


T = TypeVar("T", bound="ApiErrorEntry")


@_attrs_define
class ApiErrorEntry:
    """
    Attributes:
        name (str):
        reason (str):
        code (None | str | Unset):
        params (ApiErrorEntryParamsType0 | None | Unset):
    """

    name: str
    reason: str
    code: None | str | Unset = UNSET
    params: ApiErrorEntryParamsType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_error_entry_params_type_0 import ApiErrorEntryParamsType0

        name = self.name

        reason = self.reason

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        params: dict[str, Any] | None | Unset
        if isinstance(self.params, Unset):
            params = UNSET
        elif isinstance(self.params, ApiErrorEntryParamsType0):
            params = self.params.to_dict()
        else:
            params = self.params

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "reason": reason,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.api_error_entry_params_type_0 import ApiErrorEntryParamsType0

        d = dict(src_dict)
        name = d.pop("name")

        reason = d.pop("reason")

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_params(data: object) -> ApiErrorEntryParamsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                params_type_0 = ApiErrorEntryParamsType0.from_dict(data)

                return params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApiErrorEntryParamsType0 | None | Unset, data)

        params = _parse_params(d.pop("params", UNSET))

        api_error_entry = cls(
            name=name,
            reason=reason,
            code=code,
            params=params,
        )

        return api_error_entry
