from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkspaceReportDefaultsRequest")


@_attrs_define
class WorkspaceReportDefaultsRequest:
    """
    Attributes:
        date_interval (None | str | Unset):
        date_bin (None | str | Unset):
        include_credits (bool | None | Unset):
        include_refunds (bool | None | Unset):
        include_tax (bool | None | Unset):
        amortize (bool | None | Unset):
        show_forecast (bool | None | Unset):
        compare_to_last_period (bool | None | Unset):
    """

    date_interval: None | str | Unset = UNSET
    date_bin: None | str | Unset = UNSET
    include_credits: bool | None | Unset = UNSET
    include_refunds: bool | None | Unset = UNSET
    include_tax: bool | None | Unset = UNSET
    amortize: bool | None | Unset = UNSET
    show_forecast: bool | None | Unset = UNSET
    compare_to_last_period: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        date_interval: None | str | Unset
        if isinstance(self.date_interval, Unset):
            date_interval = UNSET
        else:
            date_interval = self.date_interval

        date_bin: None | str | Unset
        if isinstance(self.date_bin, Unset):
            date_bin = UNSET
        else:
            date_bin = self.date_bin

        include_credits: bool | None | Unset
        if isinstance(self.include_credits, Unset):
            include_credits = UNSET
        else:
            include_credits = self.include_credits

        include_refunds: bool | None | Unset
        if isinstance(self.include_refunds, Unset):
            include_refunds = UNSET
        else:
            include_refunds = self.include_refunds

        include_tax: bool | None | Unset
        if isinstance(self.include_tax, Unset):
            include_tax = UNSET
        else:
            include_tax = self.include_tax

        amortize: bool | None | Unset
        if isinstance(self.amortize, Unset):
            amortize = UNSET
        else:
            amortize = self.amortize

        show_forecast: bool | None | Unset
        if isinstance(self.show_forecast, Unset):
            show_forecast = UNSET
        else:
            show_forecast = self.show_forecast

        compare_to_last_period: bool | None | Unset
        if isinstance(self.compare_to_last_period, Unset):
            compare_to_last_period = UNSET
        else:
            compare_to_last_period = self.compare_to_last_period

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if date_interval is not UNSET:
            field_dict["dateInterval"] = date_interval
        if date_bin is not UNSET:
            field_dict["dateBin"] = date_bin
        if include_credits is not UNSET:
            field_dict["includeCredits"] = include_credits
        if include_refunds is not UNSET:
            field_dict["includeRefunds"] = include_refunds
        if include_tax is not UNSET:
            field_dict["includeTax"] = include_tax
        if amortize is not UNSET:
            field_dict["amortize"] = amortize
        if show_forecast is not UNSET:
            field_dict["showForecast"] = show_forecast
        if compare_to_last_period is not UNSET:
            field_dict["compareToLastPeriod"] = compare_to_last_period

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_date_interval(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_interval = _parse_date_interval(d.pop("dateInterval", UNSET))

        def _parse_date_bin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_bin = _parse_date_bin(d.pop("dateBin", UNSET))

        def _parse_include_credits(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_credits = _parse_include_credits(d.pop("includeCredits", UNSET))

        def _parse_include_refunds(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_refunds = _parse_include_refunds(d.pop("includeRefunds", UNSET))

        def _parse_include_tax(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_tax = _parse_include_tax(d.pop("includeTax", UNSET))

        def _parse_amortize(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        amortize = _parse_amortize(d.pop("amortize", UNSET))

        def _parse_show_forecast(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_forecast = _parse_show_forecast(d.pop("showForecast", UNSET))

        def _parse_compare_to_last_period(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        compare_to_last_period = _parse_compare_to_last_period(
            d.pop("compareToLastPeriod", UNSET)
        )

        workspace_report_defaults_request = cls(
            date_interval=date_interval,
            date_bin=date_bin,
            include_credits=include_credits,
            include_refunds=include_refunds,
            include_tax=include_tax,
            amortize=amortize,
            show_forecast=show_forecast,
            compare_to_last_period=compare_to_last_period,
        )

        return workspace_report_defaults_request
