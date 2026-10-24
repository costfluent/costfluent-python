from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AcknowledgeAnomalyRequest")


@_attrs_define
class AcknowledgeAnomalyRequest:
    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        acknowledge_anomaly_request = cls()

        return acknowledge_anomaly_request
