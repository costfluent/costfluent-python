from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_efficiency_response import ResourceEfficiencyResponse


T = TypeVar("T", bound="KubernetesEfficiencyRowResponse")


@_attrs_define
class KubernetesEfficiencyRowResponse:
    """
    Attributes:
        cluster (str):
        cost (str):
        idle_cost (str):
        cpu (ResourceEfficiencyResponse):
        memory (ResourceEfficiencyResponse):
        namespace (None | str | Unset):
        workload (None | str | Unset):
    """

    cluster: str
    cost: str
    idle_cost: str
    cpu: ResourceEfficiencyResponse
    memory: ResourceEfficiencyResponse
    namespace: None | str | Unset = UNSET
    workload: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cluster = self.cluster

        cost = self.cost

        idle_cost = self.idle_cost

        cpu = self.cpu.to_dict()

        memory = self.memory.to_dict()

        namespace: None | str | Unset
        if isinstance(self.namespace, Unset):
            namespace = UNSET
        else:
            namespace = self.namespace

        workload: None | str | Unset
        if isinstance(self.workload, Unset):
            workload = UNSET
        else:
            workload = self.workload

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cluster": cluster,
                "cost": cost,
                "idleCost": idle_cost,
                "cpu": cpu,
                "memory": memory,
            }
        )
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if workload is not UNSET:
            field_dict["workload"] = workload

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.resource_efficiency_response import ResourceEfficiencyResponse

        d = dict(src_dict)
        cluster = d.pop("cluster")

        cost = d.pop("cost")

        idle_cost = d.pop("idleCost")

        cpu = ResourceEfficiencyResponse.from_dict(d.pop("cpu"))

        memory = ResourceEfficiencyResponse.from_dict(d.pop("memory"))

        def _parse_namespace(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        namespace = _parse_namespace(d.pop("namespace", UNSET))

        def _parse_workload(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        workload = _parse_workload(d.pop("workload", UNSET))

        kubernetes_efficiency_row_response = cls(
            cluster=cluster,
            cost=cost,
            idle_cost=idle_cost,
            cpu=cpu,
            memory=memory,
            namespace=namespace,
            workload=workload,
        )

        return kubernetes_efficiency_row_response
