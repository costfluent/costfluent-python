from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceEfficiencyResponse")


@_attrs_define
class ResourceEfficiencyResponse:
    """
    Attributes:
        requested (float):
        used (float):
        peak (float):
        used_percent (float | None | Unset):
        peak_percent (float | None | Unset):
    """

    requested: float
    used: float
    peak: float
    used_percent: float | None | Unset = UNSET
    peak_percent: float | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        requested = self.requested

        used = self.used

        peak = self.peak

        used_percent: float | None | Unset
        if isinstance(self.used_percent, Unset):
            used_percent = UNSET
        else:
            used_percent = self.used_percent

        peak_percent: float | None | Unset
        if isinstance(self.peak_percent, Unset):
            peak_percent = UNSET
        else:
            peak_percent = self.peak_percent

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "requested": requested,
                "used": used,
                "peak": peak,
            }
        )
        if used_percent is not UNSET:
            field_dict["usedPercent"] = used_percent
        if peak_percent is not UNSET:
            field_dict["peakPercent"] = peak_percent

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        requested = d.pop("requested")

        used = d.pop("used")

        peak = d.pop("peak")

        def _parse_used_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        used_percent = _parse_used_percent(d.pop("usedPercent", UNSET))

        def _parse_peak_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        peak_percent = _parse_peak_percent(d.pop("peakPercent", UNSET))

        resource_efficiency_response = cls(
            requested=requested,
            used=used,
            peak=peak,
            used_percent=used_percent,
            peak_percent=peak_percent,
        )

        return resource_efficiency_response
