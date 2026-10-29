from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.applied_resource_request import AppliedResourceRequest


T = TypeVar("T", bound="ApplyCostEstimateRequest")


@_attrs_define
class ApplyCostEstimateRequest:
    """
    Attributes:
        workspace_id (str):
        repository (None | str | Unset):
        pull_request (int | None | Unset):
        plan (None | str | Unset):
        resources (list[AppliedResourceRequest] | None | Unset):
    """

    workspace_id: str
    repository: None | str | Unset = UNSET
    pull_request: int | None | Unset = UNSET
    plan: None | str | Unset = UNSET
    resources: list[AppliedResourceRequest] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        repository: None | str | Unset
        if isinstance(self.repository, Unset):
            repository = UNSET
        else:
            repository = self.repository

        pull_request: int | None | Unset
        if isinstance(self.pull_request, Unset):
            pull_request = UNSET
        else:
            pull_request = self.pull_request

        plan: None | str | Unset
        if isinstance(self.plan, Unset):
            plan = UNSET
        else:
            plan = self.plan

        resources: list[dict[str, Any]] | None | Unset
        if isinstance(self.resources, Unset):
            resources = UNSET
        elif isinstance(self.resources, list):
            resources = []
            for resources_type_0_item_data in self.resources:
                resources_type_0_item = resources_type_0_item_data.to_dict()
                resources.append(resources_type_0_item)

        else:
            resources = self.resources

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workspaceId": workspace_id,
            }
        )
        if repository is not UNSET:
            field_dict["repository"] = repository
        if pull_request is not UNSET:
            field_dict["pullRequest"] = pull_request
        if plan is not UNSET:
            field_dict["plan"] = plan
        if resources is not UNSET:
            field_dict["resources"] = resources

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.applied_resource_request import AppliedResourceRequest

        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        def _parse_repository(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repository = _parse_repository(d.pop("repository", UNSET))

        def _parse_pull_request(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pull_request = _parse_pull_request(d.pop("pullRequest", UNSET))

        def _parse_plan(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plan = _parse_plan(d.pop("plan", UNSET))

        def _parse_resources(
            data: object,
        ) -> list[AppliedResourceRequest] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                resources_type_0 = []
                _resources_type_0 = data
                for resources_type_0_item_data in _resources_type_0:
                    resources_type_0_item = AppliedResourceRequest.from_dict(
                        resources_type_0_item_data
                    )

                    resources_type_0.append(resources_type_0_item)

                return resources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AppliedResourceRequest] | None | Unset, data)

        resources = _parse_resources(d.pop("resources", UNSET))

        apply_cost_estimate_request = cls(
            workspace_id=workspace_id,
            repository=repository,
            pull_request=pull_request,
            plan=plan,
            resources=resources,
        )

        return apply_cost_estimate_request
