from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MeResponse")


@_attrs_define
class MeResponse:
    """
    Attributes:
        organization_id (str):
        token_type (str):
        token_name (str):
        capabilities (list[str]):
        workspace_id (None | str | Unset):
        default_workspace_id (None | str | Unset):
        cluster_id (None | str | Unset):
    """

    organization_id: str
    token_type: str
    token_name: str
    capabilities: list[str]
    workspace_id: None | str | Unset = UNSET
    default_workspace_id: None | str | Unset = UNSET
    cluster_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        organization_id = self.organization_id

        token_type = self.token_type

        token_name = self.token_name

        capabilities = self.capabilities

        workspace_id: None | str | Unset
        if isinstance(self.workspace_id, Unset):
            workspace_id = UNSET
        else:
            workspace_id = self.workspace_id

        default_workspace_id: None | str | Unset
        if isinstance(self.default_workspace_id, Unset):
            default_workspace_id = UNSET
        else:
            default_workspace_id = self.default_workspace_id

        cluster_id: None | str | Unset
        if isinstance(self.cluster_id, Unset):
            cluster_id = UNSET
        else:
            cluster_id = self.cluster_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "organizationId": organization_id,
                "tokenType": token_type,
                "tokenName": token_name,
                "capabilities": capabilities,
            }
        )
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if default_workspace_id is not UNSET:
            field_dict["defaultWorkspaceId"] = default_workspace_id
        if cluster_id is not UNSET:
            field_dict["clusterId"] = cluster_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        organization_id = d.pop("organizationId")

        token_type = d.pop("tokenType")

        token_name = d.pop("tokenName")

        capabilities = cast(list[str], d.pop("capabilities"))

        def _parse_workspace_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        workspace_id = _parse_workspace_id(d.pop("workspaceId", UNSET))

        def _parse_default_workspace_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_workspace_id = _parse_default_workspace_id(
            d.pop("defaultWorkspaceId", UNSET)
        )

        def _parse_cluster_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cluster_id = _parse_cluster_id(d.pop("clusterId", UNSET))

        me_response = cls(
            organization_id=organization_id,
            token_type=token_type,
            token_name=token_name,
            capabilities=capabilities,
            workspace_id=workspace_id,
            default_workspace_id=default_workspace_id,
            cluster_id=cluster_id,
        )

        return me_response
