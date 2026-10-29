from enum import StrEnum


class BudgetAlertBasisValue(StrEnum):
    ACTUAL = "actual"
    FORECAST = "forecast"

    def __str__(self) -> str:
        return str(self.value)
