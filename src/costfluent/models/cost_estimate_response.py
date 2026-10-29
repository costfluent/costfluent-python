from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_estimate_actual_response import CostEstimateActualResponse
    from ..models.cost_estimate_planned_response import CostEstimatePlannedResponse
    from ..models.cost_estimate_resource_response import CostEstimateResourceResponse
    from ..models.cost_estimate_tag_response import CostEstimateTagResponse


T = TypeVar("T", bound="CostEstimateResponse")


@_attrs_define
class CostEstimateResponse:
    """
    Attributes:
        id (str):
        workspace_id (str):
        source (str):
        currency (str):
        state (str):
        planned (CostEstimatePlannedResponse):
        resource_count (int):
        created_at (datetime.datetime):
        repository (None | str | Unset):
        pull_request (int | None | Unset):
        plan (None | str | Unset):
        source_version (None | str | Unset):
        commit (None | str | Unset):
        url (None | str | Unset):
        tag (CostEstimateTagResponse | None | Unset):
        applied_on (datetime.date | None | Unset):
        outcome (None | str | Unset):
        actual (CostEstimateActualResponse | None | Unset):
        resources (list[CostEstimateResourceResponse] | None | Unset):
        updated_at (datetime.datetime | None | Unset):
        closed_at (datetime.datetime | None | Unset):
    """

    id: str
    workspace_id: str
    source: str
    currency: str
    state: str
    planned: CostEstimatePlannedResponse
    resource_count: int
    created_at: datetime.datetime
    repository: None | str | Unset = UNSET
    pull_request: int | None | Unset = UNSET
    plan: None | str | Unset = UNSET
    source_version: None | str | Unset = UNSET
    commit: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    tag: CostEstimateTagResponse | None | Unset = UNSET
    applied_on: datetime.date | None | Unset = UNSET
    outcome: None | str | Unset = UNSET
    actual: CostEstimateActualResponse | None | Unset = UNSET
    resources: list[CostEstimateResourceResponse] | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    closed_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.cost_estimate_actual_response import CostEstimateActualResponse
        from ..models.cost_estimate_tag_response import CostEstimateTagResponse

        id = self.id

        workspace_id = self.workspace_id

        source = self.source

        currency = self.currency

        state = self.state

        planned = self.planned.to_dict()

        resource_count = self.resource_count

        created_at = self.created_at.isoformat()

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
        elif isinstance(self.tag, CostEstimateTagResponse):
            tag = self.tag.to_dict()
        else:
            tag = self.tag

        applied_on: None | str | Unset
        if isinstance(self.applied_on, Unset):
            applied_on = UNSET
        elif isinstance(self.applied_on, datetime.date):
            applied_on = self.applied_on.isoformat()
        else:
            applied_on = self.applied_on

        outcome: None | str | Unset
        if isinstance(self.outcome, Unset):
            outcome = UNSET
        else:
            outcome = self.outcome

        actual: dict[str, Any] | None | Unset
        if isinstance(self.actual, Unset):
            actual = UNSET
        elif isinstance(self.actual, CostEstimateActualResponse):
            actual = self.actual.to_dict()
        else:
            actual = self.actual

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

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        closed_at: None | str | Unset
        if isinstance(self.closed_at, Unset):
            closed_at = UNSET
        elif isinstance(self.closed_at, datetime.datetime):
            closed_at = self.closed_at.isoformat()
        else:
            closed_at = self.closed_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "workspaceId": workspace_id,
                "source": source,
                "currency": currency,
                "state": state,
                "planned": planned,
                "resourceCount": resource_count,
                "createdAt": created_at,
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
        if applied_on is not UNSET:
            field_dict["appliedOn"] = applied_on
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if actual is not UNSET:
            field_dict["actual"] = actual
        if resources is not UNSET:
            field_dict["resources"] = resources
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if closed_at is not UNSET:
            field_dict["closedAt"] = closed_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.cost_estimate_actual_response import CostEstimateActualResponse
        from ..models.cost_estimate_planned_response import CostEstimatePlannedResponse
        from ..models.cost_estimate_resource_response import (
            CostEstimateResourceResponse,
        )
        from ..models.cost_estimate_tag_response import CostEstimateTagResponse

        d = dict(src_dict)
        id = d.pop("id")

        workspace_id = d.pop("workspaceId")

        source = d.pop("source")

        currency = d.pop("currency")

        state = d.pop("state")

        planned = CostEstimatePlannedResponse.from_dict(d.pop("planned"))

        resource_count = d.pop("resourceCount")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

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

        def _parse_tag(data: object) -> CostEstimateTagResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tag_type_0 = CostEstimateTagResponse.from_dict(data)

                return tag_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CostEstimateTagResponse | None | Unset, data)

        tag = _parse_tag(d.pop("tag", UNSET))

        def _parse_applied_on(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                applied_on_type_0 = datetime.date.fromisoformat(data)

                return applied_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        applied_on = _parse_applied_on(d.pop("appliedOn", UNSET))

        def _parse_outcome(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        outcome = _parse_outcome(d.pop("outcome", UNSET))

        def _parse_actual(data: object) -> CostEstimateActualResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actual_type_0 = CostEstimateActualResponse.from_dict(data)

                return actual_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CostEstimateActualResponse | None | Unset, data)

        actual = _parse_actual(d.pop("actual", UNSET))

        def _parse_resources(
            data: object,
        ) -> list[CostEstimateResourceResponse] | None | Unset:
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
                    resources_type_0_item = CostEstimateResourceResponse.from_dict(
                        resources_type_0_item_data
                    )

                    resources_type_0.append(resources_type_0_item)

                return resources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CostEstimateResourceResponse] | None | Unset, data)

        resources = _parse_resources(d.pop("resources", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))

        def _parse_closed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closed_at_type_0 = datetime.datetime.fromisoformat(data)

                return closed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        closed_at = _parse_closed_at(d.pop("closedAt", UNSET))

        cost_estimate_response = cls(
            id=id,
            workspace_id=workspace_id,
            source=source,
            currency=currency,
            state=state,
            planned=planned,
            resource_count=resource_count,
            created_at=created_at,
            repository=repository,
            pull_request=pull_request,
            plan=plan,
            source_version=source_version,
            commit=commit,
            url=url,
            tag=tag,
            applied_on=applied_on,
            outcome=outcome,
            actual=actual,
            resources=resources,
            updated_at=updated_at,
            closed_at=closed_at,
        )

        return cost_estimate_response
