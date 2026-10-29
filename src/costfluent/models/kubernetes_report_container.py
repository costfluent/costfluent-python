from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kubernetes_report_container_gpu_requests_type_0 import (
        KubernetesReportContainerGpuRequestsType0,
    )


T = TypeVar("T", bound="KubernetesReportContainer")


@_attrs_define
class KubernetesReportContainer:
    """
    Attributes:
        name (str | Unset):
        observed_seconds (float | Unset):
        cpu_request_cores (float | Unset):
        memory_request_bytes (int | Unset):
        gpu_request (int | Unset):
        gpu_requests (KubernetesReportContainerGpuRequestsType0 | None | Unset):
        cpu_usage_core_seconds (float | Unset):
        memory_usage_byte_seconds (float | Unset):
        cpu_allocated_core_seconds (float | Unset):
        memory_allocated_byte_seconds (float | Unset):
        cpu_usage_peak_cores (float | Unset):
        memory_usage_peak_bytes (int | Unset):
    """

    name: str | Unset = UNSET
    observed_seconds: float | Unset = UNSET
    cpu_request_cores: float | Unset = UNSET
    memory_request_bytes: int | Unset = UNSET
    gpu_request: int | Unset = UNSET
    gpu_requests: KubernetesReportContainerGpuRequestsType0 | None | Unset = UNSET
    cpu_usage_core_seconds: float | Unset = UNSET
    memory_usage_byte_seconds: float | Unset = UNSET
    cpu_allocated_core_seconds: float | Unset = UNSET
    memory_allocated_byte_seconds: float | Unset = UNSET
    cpu_usage_peak_cores: float | Unset = UNSET
    memory_usage_peak_bytes: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.kubernetes_report_container_gpu_requests_type_0 import (
            KubernetesReportContainerGpuRequestsType0,
        )

        name = self.name

        observed_seconds = self.observed_seconds

        cpu_request_cores = self.cpu_request_cores

        memory_request_bytes = self.memory_request_bytes

        gpu_request = self.gpu_request

        gpu_requests: dict[str, Any] | None | Unset
        if isinstance(self.gpu_requests, Unset):
            gpu_requests = UNSET
        elif isinstance(self.gpu_requests, KubernetesReportContainerGpuRequestsType0):
            gpu_requests = self.gpu_requests.to_dict()
        else:
            gpu_requests = self.gpu_requests

        cpu_usage_core_seconds = self.cpu_usage_core_seconds

        memory_usage_byte_seconds = self.memory_usage_byte_seconds

        cpu_allocated_core_seconds = self.cpu_allocated_core_seconds

        memory_allocated_byte_seconds = self.memory_allocated_byte_seconds

        cpu_usage_peak_cores = self.cpu_usage_peak_cores

        memory_usage_peak_bytes = self.memory_usage_peak_bytes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if observed_seconds is not UNSET:
            field_dict["observed_seconds"] = observed_seconds
        if cpu_request_cores is not UNSET:
            field_dict["cpu_request_cores"] = cpu_request_cores
        if memory_request_bytes is not UNSET:
            field_dict["memory_request_bytes"] = memory_request_bytes
        if gpu_request is not UNSET:
            field_dict["gpu_request"] = gpu_request
        if gpu_requests is not UNSET:
            field_dict["gpu_requests"] = gpu_requests
        if cpu_usage_core_seconds is not UNSET:
            field_dict["cpu_usage_core_seconds"] = cpu_usage_core_seconds
        if memory_usage_byte_seconds is not UNSET:
            field_dict["memory_usage_byte_seconds"] = memory_usage_byte_seconds
        if cpu_allocated_core_seconds is not UNSET:
            field_dict["cpu_allocated_core_seconds"] = cpu_allocated_core_seconds
        if memory_allocated_byte_seconds is not UNSET:
            field_dict["memory_allocated_byte_seconds"] = memory_allocated_byte_seconds
        if cpu_usage_peak_cores is not UNSET:
            field_dict["cpu_usage_peak_cores"] = cpu_usage_peak_cores
        if memory_usage_peak_bytes is not UNSET:
            field_dict["memory_usage_peak_bytes"] = memory_usage_peak_bytes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.kubernetes_report_container_gpu_requests_type_0 import (
            KubernetesReportContainerGpuRequestsType0,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        observed_seconds = d.pop("observed_seconds", UNSET)

        cpu_request_cores = d.pop("cpu_request_cores", UNSET)

        memory_request_bytes = d.pop("memory_request_bytes", UNSET)

        gpu_request = d.pop("gpu_request", UNSET)

        def _parse_gpu_requests(
            data: object,
        ) -> KubernetesReportContainerGpuRequestsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                gpu_requests_type_0 = (
                    KubernetesReportContainerGpuRequestsType0.from_dict(data)
                )

                return gpu_requests_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KubernetesReportContainerGpuRequestsType0 | None | Unset, data)

        gpu_requests = _parse_gpu_requests(d.pop("gpu_requests", UNSET))

        cpu_usage_core_seconds = d.pop("cpu_usage_core_seconds", UNSET)

        memory_usage_byte_seconds = d.pop("memory_usage_byte_seconds", UNSET)

        cpu_allocated_core_seconds = d.pop("cpu_allocated_core_seconds", UNSET)

        memory_allocated_byte_seconds = d.pop("memory_allocated_byte_seconds", UNSET)

        cpu_usage_peak_cores = d.pop("cpu_usage_peak_cores", UNSET)

        memory_usage_peak_bytes = d.pop("memory_usage_peak_bytes", UNSET)

        kubernetes_report_container = cls(
            name=name,
            observed_seconds=observed_seconds,
            cpu_request_cores=cpu_request_cores,
            memory_request_bytes=memory_request_bytes,
            gpu_request=gpu_request,
            gpu_requests=gpu_requests,
            cpu_usage_core_seconds=cpu_usage_core_seconds,
            memory_usage_byte_seconds=memory_usage_byte_seconds,
            cpu_allocated_core_seconds=cpu_allocated_core_seconds,
            memory_allocated_byte_seconds=memory_allocated_byte_seconds,
            cpu_usage_peak_cores=cpu_usage_peak_cores,
            memory_usage_peak_bytes=memory_usage_peak_bytes,
        )

        return kubernetes_report_container
