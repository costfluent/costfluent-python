from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kubernetes_report_node import KubernetesReportNode
    from ..models.kubernetes_report_pod import KubernetesReportPod
    from ..models.kubernetes_report_volume import KubernetesReportVolume


T = TypeVar("T", bound="KubernetesReport")


@_attrs_define
class KubernetesReport:
    """
    Attributes:
        schema_version (int | Unset):
        cluster_id (str | Unset):
        agent_version (str | Unset):
        agent_instance_id (str | Unset):
        window_start (datetime.datetime | Unset):
        window_end (datetime.datetime | Unset):
        nodes (list[KubernetesReportNode] | Unset):
        pods (list[KubernetesReportPod] | Unset):
        volumes (list[KubernetesReportVolume] | None | Unset):
    """

    schema_version: int | Unset = UNSET
    cluster_id: str | Unset = UNSET
    agent_version: str | Unset = UNSET
    agent_instance_id: str | Unset = UNSET
    window_start: datetime.datetime | Unset = UNSET
    window_end: datetime.datetime | Unset = UNSET
    nodes: list[KubernetesReportNode] | Unset = UNSET
    pods: list[KubernetesReportPod] | Unset = UNSET
    volumes: list[KubernetesReportVolume] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        schema_version = self.schema_version

        cluster_id = self.cluster_id

        agent_version = self.agent_version

        agent_instance_id = self.agent_instance_id

        window_start: str | Unset = UNSET
        if not isinstance(self.window_start, Unset):
            window_start = self.window_start.isoformat()

        window_end: str | Unset = UNSET
        if not isinstance(self.window_end, Unset):
            window_end = self.window_end.isoformat()

        nodes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item = nodes_item_data.to_dict()
                nodes.append(nodes_item)

        pods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pods, Unset):
            pods = []
            for pods_item_data in self.pods:
                pods_item = pods_item_data.to_dict()
                pods.append(pods_item)

        volumes: list[dict[str, Any]] | None | Unset
        if isinstance(self.volumes, Unset):
            volumes = UNSET
        elif isinstance(self.volumes, list):
            volumes = []
            for volumes_type_0_item_data in self.volumes:
                volumes_type_0_item = volumes_type_0_item_data.to_dict()
                volumes.append(volumes_type_0_item)

        else:
            volumes = self.volumes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if schema_version is not UNSET:
            field_dict["schema_version"] = schema_version
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if agent_version is not UNSET:
            field_dict["agent_version"] = agent_version
        if agent_instance_id is not UNSET:
            field_dict["agent_instance_id"] = agent_instance_id
        if window_start is not UNSET:
            field_dict["window_start"] = window_start
        if window_end is not UNSET:
            field_dict["window_end"] = window_end
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if pods is not UNSET:
            field_dict["pods"] = pods
        if volumes is not UNSET:
            field_dict["volumes"] = volumes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.kubernetes_report_node import KubernetesReportNode
        from ..models.kubernetes_report_pod import KubernetesReportPod
        from ..models.kubernetes_report_volume import KubernetesReportVolume

        d = dict(src_dict)
        schema_version = d.pop("schema_version", UNSET)

        cluster_id = d.pop("cluster_id", UNSET)

        agent_version = d.pop("agent_version", UNSET)

        agent_instance_id = d.pop("agent_instance_id", UNSET)

        _window_start = d.pop("window_start", UNSET)
        window_start: datetime.datetime | Unset
        if isinstance(_window_start, Unset):
            window_start = UNSET
        else:
            window_start = datetime.datetime.fromisoformat(_window_start)

        _window_end = d.pop("window_end", UNSET)
        window_end: datetime.datetime | Unset
        if isinstance(_window_end, Unset):
            window_end = UNSET
        else:
            window_end = datetime.datetime.fromisoformat(_window_end)

        _nodes = d.pop("nodes", UNSET)
        nodes: list[KubernetesReportNode] | Unset = UNSET
        if _nodes is not UNSET:
            nodes = []
            for nodes_item_data in _nodes:
                nodes_item = KubernetesReportNode.from_dict(nodes_item_data)

                nodes.append(nodes_item)

        _pods = d.pop("pods", UNSET)
        pods: list[KubernetesReportPod] | Unset = UNSET
        if _pods is not UNSET:
            pods = []
            for pods_item_data in _pods:
                pods_item = KubernetesReportPod.from_dict(pods_item_data)

                pods.append(pods_item)

        def _parse_volumes(data: object) -> list[KubernetesReportVolume] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                volumes_type_0 = []
                _volumes_type_0 = data
                for volumes_type_0_item_data in _volumes_type_0:
                    volumes_type_0_item = KubernetesReportVolume.from_dict(
                        volumes_type_0_item_data
                    )

                    volumes_type_0.append(volumes_type_0_item)

                return volumes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[KubernetesReportVolume] | None | Unset, data)

        volumes = _parse_volumes(d.pop("volumes", UNSET))

        kubernetes_report = cls(
            schema_version=schema_version,
            cluster_id=cluster_id,
            agent_version=agent_version,
            agent_instance_id=agent_instance_id,
            window_start=window_start,
            window_end=window_end,
            nodes=nodes,
            pods=pods,
            volumes=volumes,
        )

        return kubernetes_report
