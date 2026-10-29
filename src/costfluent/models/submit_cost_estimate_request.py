from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_estimate_resource_request import CostEstimateResourceRequest
    from ..models.cost_estimate_tag_request import CostEstimateTagRequest


T = TypeVar("T", bound="SubmitCostEstimateRequest")


@_attrs_define
class SubmitCostEstimateRequest:
    """
    Attributes:
        workspace_id (str):
        source (str):
        currency (str):
        resources (list[CostEstimateResourceRequest]):
        repository (None | str | Unset):
        pull_request (int | None | Unset):
        plan (None | str | Unset):
        source_version (None | str | Unset):
        commit (None | str | Unset):
        url (None | str | Unset):
        tag (CostEstimateTagRequest | None | Unset):
    """

    workspace_id: str
    source: str
    currency: str
    resources: list[CostEstimateResourceRequest]
    repository: None | str | Unset = UNSET
    pull_request: int | None | Unset = UNSET
    plan: None | str | Unset = UNSET
    source_version: None | str | Unset = UNSET
    commit: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    tag: CostEstimateTagRequest | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.cost_estimate_tag_request import CostEstimateTagRequest

        workspace_id = self.workspace_id

        source = self.source

        currency = self.currency

        resources = []
        for resources_item_data in self.resources:
            resources_item = resources_item_data.to_dict()
            resources.append(resources_item)

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

        source_version: None | str | Unset
        if isinstance(self.source_version, Unset):
            source_version = UNSET
        else:
            source_version = self.source_version

        commit: None | str | Unset
        if isinstance(self.commit, Unset):
            commit = UNSET
        else:
            commit = self.commit

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        tag: dict[str, Any] | None | Unset
        if isinstance(self.tag, Unset):
            tag = UNSET
        elif isinstance(self.tag, CostEstimateTagRequest):
            tag = self.tag.to_dict()
        else:
            tag = self.tag

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workspaceId": workspace_id,
                "source": source,
                "currency": currency,
                "resources": resources,
            }
        )
        if repository is not UNSET:
            field_dict["repository"] = repository
        if pull_request is not UNSET:
            field_dict["pullRequest"] = pull_request
        if plan is not UNSET:
            field_dict["plan"] = plan
        if source_version is not UNSET:
            field_dict["sourceVersion"] = source_version
        if commit is not UNSET:
            field_dict["commit"] = commit
        if url is not UNSET:
            field_dict["url"] = url
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.cost_estimate_resource_request import CostEstimateResourceRequest
        from ..models.cost_estimate_tag_request import CostEstimateTagRequest

        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        source = d.pop("source")

        currency = d.pop("currency")

        resources = []
        _resources = d.pop("resources")
        for resources_item_data in _resources:
            resources_item = CostEstimateResourceRequest.from_dict(resources_item_data)

            resources.append(resources_item)

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

        def _parse_source_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_version = _parse_source_version(d.pop("sourceVersion", UNSET))

        def _parse_commit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commit = _parse_commit(d.pop("commit", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_tag(data: object) -> CostEstimateTagRequest | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tag_type_0 = CostEstimateTagRequest.from_dict(data)

                return tag_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CostEstimateTagRequest | None | Unset, data)

        tag = _parse_tag(d.pop("tag", UNSET))

        submit_cost_estimate_request = cls(
            workspace_id=workspace_id,
            source=source,
            currency=currency,
            resources=resources,
            repository=repository,
            pull_request=pull_request,
            plan=plan,
            source_version=source_version,
            commit=commit,
            url=url,
            tag=tag,
        )

        return submit_cost_estimate_request
