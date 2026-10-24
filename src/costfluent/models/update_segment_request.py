from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.segment_split_request import SegmentSplitRequest


T = TypeVar("T", bound="UpdateSegmentRequest")


@_attrs_define
class UpdateSegmentRequest:
    """
    Attributes:
        team_id (None | str | Unset):
        team_label (None | str | Unset):
        product (None | str | Unset):
        cost_centre (None | str | Unset):
        label (None | str | Unset):
        split (None | SegmentSplitRequest | Unset):
    """

    team_id: None | str | Unset = UNSET
    team_label: None | str | Unset = UNSET
    product: None | str | Unset = UNSET
    cost_centre: None | str | Unset = UNSET
    label: None | str | Unset = UNSET
    split: None | SegmentSplitRequest | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.segment_split_request import SegmentSplitRequest

        team_id: None | str | Unset
        if isinstance(self.team_id, Unset):
            team_id = UNSET
        else:
            team_id = self.team_id

        team_label: None | str | Unset
        if isinstance(self.team_label, Unset):
            team_label = UNSET
        else:
            team_label = self.team_label

        product: None | str | Unset
        if isinstance(self.product, Unset):
            product = UNSET
        else:
            product = self.product

        cost_centre: None | str | Unset
        if isinstance(self.cost_centre, Unset):
            cost_centre = UNSET
        else:
            cost_centre = self.cost_centre

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        split: dict[str, Any] | None | Unset
        if isinstance(self.split, Unset):
            split = UNSET
        elif isinstance(self.split, SegmentSplitRequest):
            split = self.split.to_dict()
        else:
            split = self.split

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if team_label is not UNSET:
            field_dict["teamLabel"] = team_label
        if product is not UNSET:
            field_dict["product"] = product
        if cost_centre is not UNSET:
            field_dict["costCentre"] = cost_centre
        if label is not UNSET:
            field_dict["label"] = label
        if split is not UNSET:
            field_dict["split"] = split

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.segment_split_request import SegmentSplitRequest

        d = dict(src_dict)

        def _parse_team_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        team_id = _parse_team_id(d.pop("teamId", UNSET))

        def _parse_team_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        team_label = _parse_team_label(d.pop("teamLabel", UNSET))

        def _parse_product(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product = _parse_product(d.pop("product", UNSET))

        def _parse_cost_centre(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cost_centre = _parse_cost_centre(d.pop("costCentre", UNSET))

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_split(data: object) -> None | SegmentSplitRequest | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                split_type_0 = SegmentSplitRequest.from_dict(data)

                return split_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SegmentSplitRequest | Unset, data)

        split = _parse_split(d.pop("split", UNSET))

        update_segment_request = cls(
            team_id=team_id,
            team_label=team_label,
            product=product,
            cost_centre=cost_centre,
            label=label,
            split=split,
        )

        return update_segment_request
