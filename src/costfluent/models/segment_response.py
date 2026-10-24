from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.segment_split_response import SegmentSplitResponse


T = TypeVar("T", bound="SegmentResponse")


@_attrs_define
class SegmentResponse:
    """
    Attributes:
        id (str):
        team_label (str):
        product (str):
        cost_centre (str):
        is_shared (bool):
        label (str):
        created_at (datetime.datetime):
        team_id (None | str | Unset):
        team_name (None | str | Unset):
        split (None | SegmentSplitResponse | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    id: str
    team_label: str
    product: str
    cost_centre: str
    is_shared: bool
    label: str
    created_at: datetime.datetime
    team_id: None | str | Unset = UNSET
    team_name: None | str | Unset = UNSET
    split: None | SegmentSplitResponse | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.segment_split_response import SegmentSplitResponse

        id = self.id

        team_label = self.team_label

        product = self.product

        cost_centre = self.cost_centre

        is_shared = self.is_shared

        label = self.label

        created_at = self.created_at.isoformat()

        team_id: None | str | Unset
        if isinstance(self.team_id, Unset):
            team_id = UNSET
        else:
            team_id = self.team_id

        team_name: None | str | Unset
        if isinstance(self.team_name, Unset):
            team_name = UNSET
        else:
            team_name = self.team_name

        split: dict[str, Any] | None | Unset
        if isinstance(self.split, Unset):
            split = UNSET
        elif isinstance(self.split, SegmentSplitResponse):
            split = self.split.to_dict()
        else:
            split = self.split

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "teamLabel": team_label,
                "product": product,
                "costCentre": cost_centre,
                "isShared": is_shared,
                "label": label,
                "createdAt": created_at,
            }
        )
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if team_name is not UNSET:
            field_dict["teamName"] = team_name
        if split is not UNSET:
            field_dict["split"] = split
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.segment_split_response import SegmentSplitResponse

        d = dict(src_dict)
        id = d.pop("id")

        team_label = d.pop("teamLabel")

        product = d.pop("product")

        cost_centre = d.pop("costCentre")

        is_shared = d.pop("isShared")

        label = d.pop("label")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        def _parse_team_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        team_id = _parse_team_id(d.pop("teamId", UNSET))

        def _parse_team_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        team_name = _parse_team_name(d.pop("teamName", UNSET))

        def _parse_split(data: object) -> None | SegmentSplitResponse | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                split_type_0 = SegmentSplitResponse.from_dict(data)

                return split_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SegmentSplitResponse | Unset, data)

        split = _parse_split(d.pop("split", UNSET))

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

        segment_response = cls(
            id=id,
            team_label=team_label,
            product=product,
            cost_centre=cost_centre,
            is_shared=is_shared,
            label=label,
            created_at=created_at,
            team_id=team_id,
            team_name=team_name,
            split=split,
            updated_at=updated_at,
        )

        return segment_response
