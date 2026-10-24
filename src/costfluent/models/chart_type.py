from enum import StrEnum


class ChartType(StrEnum):
    AREA = "area"
    BAR = "bar"
    LINE = "line"
    PIE = "pie"
    STACKEDBAR = "stackedBar"
    TABLE = "table"

    def __str__(self) -> str:
        return str(self.value)
