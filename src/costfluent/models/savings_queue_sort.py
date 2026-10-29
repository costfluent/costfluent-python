from enum import StrEnum


class SavingsQueueSort(StrEnum):
    LARGESTSAVING = "largestSaving"
    NEWEST = "newest"

    def __str__(self) -> str:
        return str(self.value)
