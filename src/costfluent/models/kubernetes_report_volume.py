from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kubernetes_report_volume_claim_labels_type_0 import (
        KubernetesReportVolumeClaimLabelsType0,
    )
    from ..models.kubernetes_report_volume_storage_class_annotations_type_0 import (
        KubernetesReportVolumeStorageClassAnnotationsType0,
    )


T = TypeVar("T", bound="KubernetesReportVolume")


@_attrs_define
class KubernetesReportVolume:
    """
    Attributes:
        name (str | Unset):
        capacity_bytes (int | Unset):
        storage_class (None | str | Unset):
        csi_driver (None | str | Unset):
        volume_handle (None | str | Unset):
        phase (None | str | Unset):
        claim_namespace (None | str | Unset):
        claim_name (None | str | Unset):
        observed_seconds (float | Unset):
        storage_class_annotations (KubernetesReportVolumeStorageClassAnnotationsType0 | None | Unset):
        claim_labels (KubernetesReportVolumeClaimLabelsType0 | None | Unset):
    """

    name: str | Unset = UNSET
    capacity_bytes: int | Unset = UNSET
    storage_class: None | str | Unset = UNSET
    csi_driver: None | str | Unset = UNSET
    volume_handle: None | str | Unset = UNSET
    phase: None | str | Unset = UNSET
    claim_namespace: None | str | Unset = UNSET
    claim_name: None | str | Unset = UNSET
    observed_seconds: float | Unset = UNSET
    storage_class_annotations: (
        KubernetesReportVolumeStorageClassAnnotationsType0 | None | Unset
    ) = UNSET
    claim_labels: KubernetesReportVolumeClaimLabelsType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.kubernetes_report_volume_claim_labels_type_0 import (
            KubernetesReportVolumeClaimLabelsType0,
        )
        from ..models.kubernetes_report_volume_storage_class_annotations_type_0 import (
            KubernetesReportVolumeStorageClassAnnotationsType0,
        )

        name = self.name

        capacity_bytes = self.capacity_bytes

        storage_class: None | str | Unset
        if isinstance(self.storage_class, Unset):
            storage_class = UNSET
        else:
            storage_class = self.storage_class

        csi_driver: None | str | Unset
        if isinstance(self.csi_driver, Unset):
            csi_driver = UNSET
        else:
            csi_driver = self.csi_driver

        volume_handle: None | str | Unset
        if isinstance(self.volume_handle, Unset):
            volume_handle = UNSET
        else:
            volume_handle = self.volume_handle

        phase: None | str | Unset
        if isinstance(self.phase, Unset):
            phase = UNSET
        else:
            phase = self.phase

        claim_namespace: None | str | Unset
        if isinstance(self.claim_namespace, Unset):
            claim_namespace = UNSET
        else:
            claim_namespace = self.claim_namespace

        claim_name: None | str | Unset
        if isinstance(self.claim_name, Unset):
            claim_name = UNSET
        else:
            claim_name = self.claim_name

        observed_seconds = self.observed_seconds

        storage_class_annotations: dict[str, Any] | None | Unset
        if isinstance(self.storage_class_annotations, Unset):
            storage_class_annotations = UNSET
        elif isinstance(
            self.storage_class_annotations,
            KubernetesReportVolumeStorageClassAnnotationsType0,
        ):
            storage_class_annotations = self.storage_class_annotations.to_dict()
        else:
            storage_class_annotations = self.storage_class_annotations

        claim_labels: dict[str, Any] | None | Unset
        if isinstance(self.claim_labels, Unset):
            claim_labels = UNSET
        elif isinstance(self.claim_labels, KubernetesReportVolumeClaimLabelsType0):
            claim_labels = self.claim_labels.to_dict()
        else:
            claim_labels = self.claim_labels

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if capacity_bytes is not UNSET:
            field_dict["capacity_bytes"] = capacity_bytes
        if storage_class is not UNSET:
            field_dict["storage_class"] = storage_class
        if csi_driver is not UNSET:
            field_dict["csi_driver"] = csi_driver
        if volume_handle is not UNSET:
            field_dict["volume_handle"] = volume_handle
        if phase is not UNSET:
            field_dict["phase"] = phase
        if claim_namespace is not UNSET:
            field_dict["claim_namespace"] = claim_namespace
        if claim_name is not UNSET:
            field_dict["claim_name"] = claim_name
        if observed_seconds is not UNSET:
            field_dict["observed_seconds"] = observed_seconds
        if storage_class_annotations is not UNSET:
            field_dict["storage_class_annotations"] = storage_class_annotations
        if claim_labels is not UNSET:
            field_dict["claim_labels"] = claim_labels

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.kubernetes_report_volume_claim_labels_type_0 import (
            KubernetesReportVolumeClaimLabelsType0,
        )
        from ..models.kubernetes_report_volume_storage_class_annotations_type_0 import (
            KubernetesReportVolumeStorageClassAnnotationsType0,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        capacity_bytes = d.pop("capacity_bytes", UNSET)

        def _parse_storage_class(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_class = _parse_storage_class(d.pop("storage_class", UNSET))

        def _parse_csi_driver(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        csi_driver = _parse_csi_driver(d.pop("csi_driver", UNSET))

        def _parse_volume_handle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        volume_handle = _parse_volume_handle(d.pop("volume_handle", UNSET))

        def _parse_phase(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phase = _parse_phase(d.pop("phase", UNSET))

        def _parse_claim_namespace(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        claim_namespace = _parse_claim_namespace(d.pop("claim_namespace", UNSET))

        def _parse_claim_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        claim_name = _parse_claim_name(d.pop("claim_name", UNSET))

        observed_seconds = d.pop("observed_seconds", UNSET)

        def _parse_storage_class_annotations(
            data: object,
        ) -> KubernetesReportVolumeStorageClassAnnotationsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                storage_class_annotations_type_0 = (
                    KubernetesReportVolumeStorageClassAnnotationsType0.from_dict(data)
                )

                return storage_class_annotations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                KubernetesReportVolumeStorageClassAnnotationsType0 | None | Unset, data
            )

        storage_class_annotations = _parse_storage_class_annotations(
            d.pop("storage_class_annotations", UNSET)
        )

        def _parse_claim_labels(
            data: object,
        ) -> KubernetesReportVolumeClaimLabelsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                claim_labels_type_0 = KubernetesReportVolumeClaimLabelsType0.from_dict(
                    data
                )

                return claim_labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KubernetesReportVolumeClaimLabelsType0 | None | Unset, data)

        claim_labels = _parse_claim_labels(d.pop("claim_labels", UNSET))

        kubernetes_report_volume = cls(
            name=name,
            capacity_bytes=capacity_bytes,
            storage_class=storage_class,
            csi_driver=csi_driver,
            volume_handle=volume_handle,
            phase=phase,
            claim_namespace=claim_namespace,
            claim_name=claim_name,
            observed_seconds=observed_seconds,
            storage_class_annotations=storage_class_annotations,
            claim_labels=claim_labels,
        )

        return kubernetes_report_volume
