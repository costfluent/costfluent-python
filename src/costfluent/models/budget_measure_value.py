from enum import StrEnum


class BudgetMeasureValue(StrEnum):
    COST = "cost"
    USAGE = "usage"

    def __str__(self) -> str:
        return str(self.value)
