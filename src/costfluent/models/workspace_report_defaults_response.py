from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WorkspaceReportDefaultsResponse")


@_attrs_define
class WorkspaceReportDefaultsResponse:
    """
    Attributes:
        date_interval (str):
        date_bin (str):
        include_credits (bool):
        include_refunds (bool):
        include_tax (bool):
        amortize (bool):
        show_forecast (bool):
        compare_to_last_period (bool):
    """

    date_interval: str
    date_bin: str
    include_credits: bool
    include_refunds: bool
    include_tax: bool
    amortize: bool
    show_forecast: bool
    compare_to_last_period: bool

    def to_dict(self) -> dict[str, Any]:
        date_interval = self.date_interval

        date_bin = self.date_bin

        include_credits = self.include_credits

        include_refunds = self.include_refunds

        include_tax = self.include_tax

        amortize = self.amortize

        show_forecast = self.show_forecast

        compare_to_last_period = self.compare_to_last_period

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dateInterval": date_interval,
                "dateBin": date_bin,
                "includeCredits": include_credits,
                "includeRefunds": include_refunds,
                "includeTax": include_tax,
                "amortize": amortize,
                "showForecast": show_forecast,
                "compareToLastPeriod": compare_to_last_period,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        date_interval = d.pop("dateInterval")

        date_bin = d.pop("dateBin")

        include_credits = d.pop("includeCredits")

        include_refunds = d.pop("includeRefunds")

        include_tax = d.pop("includeTax")

        amortize = d.pop("amortize")

        show_forecast = d.pop("showForecast")

        compare_to_last_period = d.pop("compareToLastPeriod")

        workspace_report_defaults_response = cls(
            date_interval=date_interval,
            date_bin=date_bin,
            include_credits=include_credits,
            include_refunds=include_refunds,
            include_tax=include_tax,
            amortize=amortize,
            show_forecast=show_forecast,
            compare_to_last_period=compare_to_last_period,
        )

        return workspace_report_defaults_response
