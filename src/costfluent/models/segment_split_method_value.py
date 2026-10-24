from enum import StrEnum


class SegmentSplitMethodValue(StrEnum):
    EVEN = "even"
    PERCENT = "percent"
    PROPORTIONAL = "proportional"

    def __str__(self) -> str:
        return str(self.value)
