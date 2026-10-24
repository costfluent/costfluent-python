from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency_amount import CurrencyAmount
    from ..models.forecast_month_response import ForecastMonthResponse


T = TypeVar("T", bound="CostForecastResponse")


@_attrs_define
class CostForecastResponse:
    """
    Attributes:
        is_available (bool):
        forecast (list[ForecastMonthResponse]):
        unconverted (list[CurrencyAmount]):
        current_month_actual (None | str | Unset):
        current_month_forecast (None | str | Unset):
        method (None | str | Unset):
        currency (None | str | Unset):
        confidence_percent (float | None | Unset):
        generated_at (datetime.datetime | None | Unset):
    """

    is_available: bool
    forecast: list[ForecastMonthResponse]
    unconverted: list[CurrencyAmount]
    current_month_actual: None | str | Unset = UNSET
    current_month_forecast: None | str | Unset = UNSET
    method: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    confidence_percent: float | None | Unset = UNSET
    generated_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_available = self.is_available

        forecast = []
        for forecast_item_data in self.forecast:
            forecast_item = forecast_item_data.to_dict()
            forecast.append(forecast_item)

        unconverted = []
        for unconverted_item_data in self.unconverted:
            unconverted_item = unconverted_item_data.to_dict()
            unconverted.append(unconverted_item)

        current_month_actual: None | str | Unset
        if isinstance(self.current_month_actual, Unset):
            current_month_actual = UNSET
        else:
            current_month_actual = self.current_month_actual

        current_month_forecast: None | str | Unset
        if isinstance(self.current_month_forecast, Unset):
            current_month_forecast = UNSET
        else:
            current_month_forecast = self.current_month_forecast

        method: None | str | Unset
        if isinstance(self.method, Unset):
            method = UNSET
        else:
            method = self.method

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        confidence_percent: float | None | Unset
        if isinstance(self.confidence_percent, Unset):
            confidence_percent = UNSET
        else:
            confidence_percent = self.confidence_percent

        generated_at: None | str | Unset
        if isinstance(self.generated_at, Unset):
            generated_at = UNSET
        elif isinstance(self.generated_at, datetime.datetime):
            generated_at = self.generated_at.isoformat()
        else:
            generated_at = self.generated_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "isAvailable": is_available,
                "forecast": forecast,
                "unconverted": unconverted,
            }
        )
        if current_month_actual is not UNSET:
            field_dict["currentMonthActual"] = current_month_actual
        if current_month_forecast is not UNSET:
            field_dict["currentMonthForecast"] = current_month_forecast
        if method is not UNSET:
            field_dict["method"] = method
        if currency is not UNSET:
            field_dict["currency"] = currency
        if confidence_percent is not UNSET:
            field_dict["confidencePercent"] = confidence_percent
        if generated_at is not UNSET:
            field_dict["generatedAt"] = generated_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.currency_amount import CurrencyAmount
        from ..models.forecast_month_response import ForecastMonthResponse

        d = dict(src_dict)
        is_available = d.pop("isAvailable")

        forecast = []
        _forecast = d.pop("forecast")
        for forecast_item_data in _forecast:
            forecast_item = ForecastMonthResponse.from_dict(forecast_item_data)

            forecast.append(forecast_item)

        unconverted = []
        _unconverted = d.pop("unconverted")
        for unconverted_item_data in _unconverted:
            unconverted_item = CurrencyAmount.from_dict(unconverted_item_data)

            unconverted.append(unconverted_item)

        def _parse_current_month_actual(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_month_actual = _parse_current_month_actual(
            d.pop("currentMonthActual", UNSET)
        )

        def _parse_current_month_forecast(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_month_forecast = _parse_current_month_forecast(
            d.pop("currentMonthForecast", UNSET)
        )

        def _parse_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        method = _parse_method(d.pop("method", UNSET))

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_confidence_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        confidence_percent = _parse_confidence_percent(
            d.pop("confidencePercent", UNSET)
        )

        def _parse_generated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                generated_at_type_0 = datetime.datetime.fromisoformat(data)

                return generated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        generated_at = _parse_generated_at(d.pop("generatedAt", UNSET))

        cost_forecast_response = cls(
            is_available=is_available,
            forecast=forecast,
            unconverted=unconverted,
            current_month_actual=current_month_actual,
            current_month_forecast=current_month_forecast,
            method=method,
            currency=currency,
            confidence_percent=confidence_percent,
            generated_at=generated_at,
        )

        return cost_forecast_response
