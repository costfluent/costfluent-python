from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="UploadCustomCostsRequest")


@_attrs_define
class UploadCustomCostsRequest:
    """
    Attributes:
        file (list[File] | None | Unset):
    """

    file: list[File] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        file: list[FileTypes] | None | Unset
        if isinstance(self.file, Unset):
            file = UNSET
        elif isinstance(self.file, list):
            file = []
            for file_type_0_item_data in self.file:
                file_type_0_item = file_type_0_item_data.to_tuple()

                file.append(file_type_0_item)

        else:
            file = self.file

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.file, Unset):
            if isinstance(self.file, list):
                for file_type_0_item_element in self.file:
                    files.append(("file", file_type_0_item_element.to_tuple()))
            else:
                files.append(("file", (None, str(self.file).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_file(data: object) -> list[File] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                file_type_0 = []
                _file_type_0 = data
                for file_type_0_item_data in _file_type_0:
                    file_type_0_item = File(payload=BytesIO(file_type_0_item_data))

                    file_type_0.append(file_type_0_item)

                return file_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[File] | None | Unset, data)

        file = _parse_file(d.pop("file", UNSET))

        upload_custom_costs_request = cls(
            file=file,
        )

        return upload_custom_costs_request
