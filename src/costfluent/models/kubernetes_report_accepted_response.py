from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="KubernetesReportAcceptedResponse")


@_attrs_define
class KubernetesReportAcceptedResponse:
    """
    Attributes:
        id (str):
        cluster_id (str):
        status (str):
    """

    id: str
    cluster_id: str
    status: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        cluster_id = self.cluster_id

        status = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "cluster_id": cluster_id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        cluster_id = d.pop("cluster_id")

        status = d.pop("status")

        kubernetes_report_accepted_response = cls(
            id=id,
            cluster_id=cluster_id,
            status=status,
        )

        return kubernetes_report_accepted_response
