from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kubernetes_report_container import KubernetesReportContainer
    from ..models.kubernetes_report_pod_annotations_type_0 import (
        KubernetesReportPodAnnotationsType0,
    )
    from ..models.kubernetes_report_pod_labels_type_0 import (
        KubernetesReportPodLabelsType0,
    )
    from ..models.kubernetes_report_pod_namespace_labels_type_0 import (
        KubernetesReportPodNamespaceLabelsType0,
    )


T = TypeVar("T", bound="KubernetesReportPod")


@_attrs_define
class KubernetesReportPod:
    """
    Attributes:
        namespace (str | Unset):
        name (str | Unset):
        node (str | Unset):
        controller_kind (None | str | Unset):
        controller (None | str | Unset):
        labels (KubernetesReportPodLabelsType0 | None | Unset):
        annotations (KubernetesReportPodAnnotationsType0 | None | Unset):
        namespace_labels (KubernetesReportPodNamespaceLabelsType0 | None | Unset):
        containers (list[KubernetesReportContainer] | Unset):
    """

    namespace: str | Unset = UNSET
    name: str | Unset = UNSET
    node: str | Unset = UNSET
    controller_kind: None | str | Unset = UNSET
    controller: None | str | Unset = UNSET
    labels: KubernetesReportPodLabelsType0 | None | Unset = UNSET
    annotations: KubernetesReportPodAnnotationsType0 | None | Unset = UNSET
    namespace_labels: KubernetesReportPodNamespaceLabelsType0 | None | Unset = UNSET
    containers: list[KubernetesReportContainer] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.kubernetes_report_pod_annotations_type_0 import (
            KubernetesReportPodAnnotationsType0,
        )
        from ..models.kubernetes_report_pod_labels_type_0 import (
            KubernetesReportPodLabelsType0,
        )
        from ..models.kubernetes_report_pod_namespace_labels_type_0 import (
            KubernetesReportPodNamespaceLabelsType0,
        )

        namespace = self.namespace

        name = self.name

        node = self.node

        controller_kind: None | str | Unset
        if isinstance(self.controller_kind, Unset):
            controller_kind = UNSET
        else:
            controller_kind = self.controller_kind

        controller: None | str | Unset
        if isinstance(self.controller, Unset):
            controller = UNSET
        else:
            controller = self.controller

        labels: dict[str, Any] | None | Unset
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, KubernetesReportPodLabelsType0):
            labels = self.labels.to_dict()
        else:
            labels = self.labels

        annotations: dict[str, Any] | None | Unset
        if isinstance(self.annotations, Unset):
            annotations = UNSET
        elif isinstance(self.annotations, KubernetesReportPodAnnotationsType0):
            annotations = self.annotations.to_dict()
        else:
            annotations = self.annotations

        namespace_labels: dict[str, Any] | None | Unset
        if isinstance(self.namespace_labels, Unset):
            namespace_labels = UNSET
        elif isinstance(self.namespace_labels, KubernetesReportPodNamespaceLabelsType0):
            namespace_labels = self.namespace_labels.to_dict()
        else:
            namespace_labels = self.namespace_labels

        containers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.containers, Unset):
            containers = []
            for containers_item_data in self.containers:
                containers_item = containers_item_data.to_dict()
                containers.append(containers_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if name is not UNSET:
            field_dict["name"] = name
        if node is not UNSET:
            field_dict["node"] = node
        if controller_kind is not UNSET:
            field_dict["controller_kind"] = controller_kind
        if controller is not UNSET:
            field_dict["controller"] = controller
        if labels is not UNSET:
            field_dict["labels"] = labels
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if namespace_labels is not UNSET:
            field_dict["namespace_labels"] = namespace_labels
        if containers is not UNSET:
            field_dict["containers"] = containers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.kubernetes_report_container import KubernetesReportContainer
        from ..models.kubernetes_report_pod_annotations_type_0 import (
            KubernetesReportPodAnnotationsType0,
        )
        from ..models.kubernetes_report_pod_labels_type_0 import (
            KubernetesReportPodLabelsType0,
        )
        from ..models.kubernetes_report_pod_namespace_labels_type_0 import (
            KubernetesReportPodNamespaceLabelsType0,
        )

        d = dict(src_dict)
        namespace = d.pop("namespace", UNSET)

        name = d.pop("name", UNSET)

        node = d.pop("node", UNSET)

        def _parse_controller_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        controller_kind = _parse_controller_kind(d.pop("controller_kind", UNSET))

        def _parse_controller(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        controller = _parse_controller(d.pop("controller", UNSET))

        def _parse_labels(
            data: object,
        ) -> KubernetesReportPodLabelsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                labels_type_0 = KubernetesReportPodLabelsType0.from_dict(data)

                return labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KubernetesReportPodLabelsType0 | None | Unset, data)

        labels = _parse_labels(d.pop("labels", UNSET))

        def _parse_annotations(
            data: object,
        ) -> KubernetesReportPodAnnotationsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                annotations_type_0 = KubernetesReportPodAnnotationsType0.from_dict(data)

                return annotations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KubernetesReportPodAnnotationsType0 | None | Unset, data)

        annotations = _parse_annotations(d.pop("annotations", UNSET))

        def _parse_namespace_labels(
            data: object,
        ) -> KubernetesReportPodNamespaceLabelsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                namespace_labels_type_0 = (
                    KubernetesReportPodNamespaceLabelsType0.from_dict(data)
                )

                return namespace_labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KubernetesReportPodNamespaceLabelsType0 | None | Unset, data)

        namespace_labels = _parse_namespace_labels(d.pop("namespace_labels", UNSET))

        _containers = d.pop("containers", UNSET)
        containers: list[KubernetesReportContainer] | Unset = UNSET
        if _containers is not UNSET:
            containers = []
            for containers_item_data in _containers:
                containers_item = KubernetesReportContainer.from_dict(
                    containers_item_data
                )

                containers.append(containers_item)

        kubernetes_report_pod = cls(
            namespace=namespace,
            name=name,
            node=node,
            controller_kind=controller_kind,
            controller=controller,
            labels=labels,
            annotations=annotations,
            namespace_labels=namespace_labels,
            containers=containers,
        )

        return kubernetes_report_pod
