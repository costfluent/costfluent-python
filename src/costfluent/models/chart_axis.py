from enum import StrEnum


class ChartAxis(StrEnum):
    DATE = "date"
    GROUP = "group"

    def __str__(self) -> str:
        return str(self.value)
