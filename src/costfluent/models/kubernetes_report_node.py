from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kubernetes_report_node_annotations_type_0 import (
        KubernetesReportNodeAnnotationsType0,
    )
    from ..models.kubernetes_report_node_gpu_labels_type_0 import (
        KubernetesReportNodeGpuLabelsType0,
    )
    from ..models.kubernetes_report_node_gpu_resources_type_0 import (
        KubernetesReportNodeGpuResourcesType0,
    )
    from ..models.kubernetes_report_node_labels_type_0 import (
        KubernetesReportNodeLabelsType0,
    )


T = TypeVar("T", bound="KubernetesReportNode")


@_attrs_define
class KubernetesReportNode:
    """
    Attributes:
        name (str | Unset):
        provider_id (None | str | Unset):
        instance_type (None | str | Unset):
        region (None | str | Unset):
        zone (None | str | Unset):
        spot (bool | Unset):
        observed_seconds (float | Unset):
        capacity_cpu_cores (float | Unset):
        capacity_memory_bytes (int | Unset):
        capacity_gpu (int | Unset):
        gpu_resources (KubernetesReportNodeGpuResourcesType0 | None | Unset):
        allocatable_cpu_cores (float | Unset):
        allocatable_memory_bytes (int | Unset):
        labels (KubernetesReportNodeLabelsType0 | None | Unset):
        annotations (KubernetesReportNodeAnnotationsType0 | None | Unset):
        gpu_labels (KubernetesReportNodeGpuLabelsType0 | None | Unset):
    """

    name: str | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    instance_type: None | str | Unset = UNSET
    region: None | str | Unset = UNSET
    zone: None | str | Unset = UNSET
    spot: bool | Unset = UNSET
    observed_seconds: float | Unset = UNSET
    capacity_cpu_cores: float | Unset = UNSET
    capacity_memory_bytes: int | Unset = UNSET
    capacity_gpu: int | Unset = UNSET
    gpu_resources: KubernetesReportNodeGpuResourcesType0 | None | Unset = UNSET
    allocatable_cpu_cores: float | Unset = UNSET
    allocatable_memory_bytes: int | Unset = UNSET
    labels: KubernetesReportNodeLabelsType0 | None | Unset = UNSET
    annotations: KubernetesReportNodeAnnotationsType0 | None | Unset = UNSET
    gpu_labels: KubernetesReportNodeGpuLabelsType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.kubernetes_report_node_annotations_type_0 import (
            KubernetesReportNodeAnnotationsType0,
        )
        from ..models.kubernetes_report_node_gpu_labels_type_0 import (
            KubernetesReportNodeGpuLabelsType0,
        )
        from ..models.kubernetes_report_node_gpu_resources_type_0 import (
            KubernetesReportNodeGpuResourcesType0,
        )
        from ..models.kubernetes_report_node_labels_type_0 import (
            KubernetesReportNodeLabelsType0,
        )

        name = self.name

        provider_id: None | str | Unset
        if isinstance(self.provider_id, Unset):
            provider_id = UNSET
        else:
            provider_id = self.provider_id

        instance_type: None | str | Unset
        if isinstance(self.instance_type, Unset):
            instance_type = UNSET
        else:
            instance_type = self.instance_type

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        zone: None | str | Unset
        if isinstance(self.zone, Unset):
            zone = UNSET
        else:
            zone = self.zone

        spot = self.spot

        observed_seconds = self.observed_seconds

        capacity_cpu_cores = self.capacity_cpu_cores

        capacity_memory_bytes = self.capacity_memory_bytes

        capacity_gpu = self.capacity_gpu

        gpu_resources: dict[str, Any] | None | Unset
        if isinstance(self.gpu_resources, Unset):
            gpu_resources = UNSET
        elif isinstance(self.gpu_resources, KubernetesReportNodeGpuResourcesType0):
            gpu_resources = self.gpu_resources.to_dict()
        else:
            gpu_resources = self.gpu_resources

        allocatable_cpu_cores = self.allocatable_cpu_cores

        allocatable_memory_bytes = self.allocatable_memory_bytes

        labels: dict[str, Any] | None | Unset
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, KubernetesReportNodeLabelsType0):
            labels = self.labels.to_dict()
        else:
            labels = self.labels

        annotations: dict[str, Any] | None | Unset
        if isinstance(self.annotations, Unset):
            annotations = UNSET
        elif isinstance(self.annotations, KubernetesReportNodeAnnotationsType0):
            annotations = self.annotations.to_dict()
        else:
            annotations = self.annotations

        gpu_labels: dict[str, Any] | None | Unset
        if isinstance(self.gpu_labels, Unset):
            gpu_labels = UNSET
        elif isinstance(self.gpu_labels, KubernetesReportNodeGpuLabelsType0):
            gpu_labels = self.gpu_labels.to_dict()
        else:
            gpu_labels = self.gpu_labels

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if provider_id is not UNSET:
            field_dict["provider_id"] = provider_id
        if instance_type is not UNSET:
            field_dict["instance_type"] = instance_type
        if region is not UNSET:
            field_dict["region"] = region
        if zone is not UNSET:
            field_dict["zone"] = zone
        if spot is not UNSET:
            field_dict["spot"] = spot
        if observed_seconds is not UNSET:
            field_dict["observed_seconds"] = observed_seconds
        if capacity_cpu_cores is not UNSET:
            field_dict["capacity_cpu_cores"] = capacity_cpu_cores
        if capacity_memory_bytes is not UNSET:
            field_dict["capacity_memory_bytes"] = capacity_memory_bytes
        if capacity_gpu is not UNSET:
            field_dict["capacity_gpu"] = capacity_gpu
        if gpu_resources is not UNSET:
            field_dict["gpu_resources"] = gpu_resources
        if allocatable_cpu_cores is not UNSET:
            field_dict["allocatable_cpu_cores"] = allocatable_cpu_cores
        if allocatable_memory_bytes is not UNSET:
            field_dict["allocatable_memory_bytes"] = allocatable_memory_bytes
        if labels is not UNSET:
            field_dict["labels"] = labels
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if gpu_labels is not UNSET:
            field_dict["gpu_labels"] = gpu_labels

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.kubernetes_report_node_annotations_type_0 import (
            KubernetesReportNodeAnnotationsType0,
        )
        from ..models.kubernetes_report_node_gpu_labels_type_0 import (
            KubernetesReportNodeGpuLabelsType0,
        )
        from ..models.kubernetes_report_node_gpu_resources_type_0 import (
            KubernetesReportNodeGpuResourcesType0,
        )
        from ..models.kubernetes_report_node_labels_type_0 import (
            KubernetesReportNodeLabelsType0,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_provider_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_id = _parse_provider_id(d.pop("provider_id", UNSET))

        def _parse_instance_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instance_type = _parse_instance_type(d.pop("instance_type", UNSET))

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_zone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        zone = _parse_zone(d.pop("zone", UNSET))

        spot = d.pop("spot", UNSET)

        observed_seconds = d.pop("observed_seconds", UNSET)

        capacity_cpu_cores = d.pop("capacity_cpu_cores", UNSET)

        capacity_memory_bytes = d.pop("capacity_memory_bytes", UNSET)

        capacity_gpu = d.pop("capacity_gpu", UNSET)

        def _parse_gpu_resources(
            data: object,
        ) -> KubernetesReportNodeGpuResourcesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                gpu_resources_type_0 = KubernetesReportNodeGpuResourcesType0.from_dict(
                    data
                )

                return gpu_resources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KubernetesReportNodeGpuResourcesType0 | None | Unset, data)

        gpu_resources = _parse_gpu_resources(d.pop("gpu_resources", UNSET))

        allocatable_cpu_cores = d.pop("allocatable_cpu_cores", UNSET)

        allocatable_memory_bytes = d.pop("allocatable_memory_bytes", UNSET)

        def _parse_labels(
            data: object,
        ) -> KubernetesReportNodeLabelsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                labels_type_0 = KubernetesReportNodeLabelsType0.from_dict(data)

                return labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KubernetesReportNodeLabelsType0 | None | Unset, data)

        labels = _parse_labels(d.pop("labels", UNSET))

        def _parse_annotations(
            data: object,
        ) -> KubernetesReportNodeAnnotationsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                annotations_type_0 = KubernetesReportNodeAnnotationsType0.from_dict(
                    data
                )

                return annotations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KubernetesReportNodeAnnotationsType0 | None | Unset, data)

        annotations = _parse_annotations(d.pop("annotations", UNSET))

        def _parse_gpu_labels(
            data: object,
        ) -> KubernetesReportNodeGpuLabelsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                gpu_labels_type_0 = KubernetesReportNodeGpuLabelsType0.from_dict(data)

                return gpu_labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KubernetesReportNodeGpuLabelsType0 | None | Unset, data)

        gpu_labels = _parse_gpu_labels(d.pop("gpu_labels", UNSET))

        kubernetes_report_node = cls(
            name=name,
            provider_id=provider_id,
            instance_type=instance_type,
            region=region,
            zone=zone,
            spot=spot,
            observed_seconds=observed_seconds,
            capacity_cpu_cores=capacity_cpu_cores,
            capacity_memory_bytes=capacity_memory_bytes,
            capacity_gpu=capacity_gpu,
            gpu_resources=gpu_resources,
            allocatable_cpu_cores=allocatable_cpu_cores,
            allocatable_memory_bytes=allocatable_memory_bytes,
            labels=labels,
            annotations=annotations,
            gpu_labels=gpu_labels,
        )

        return kubernetes_report_node
