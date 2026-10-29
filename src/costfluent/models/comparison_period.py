from enum import StrEnum


class ComparisonPeriod(StrEnum):
    PREVIOUSDAY = "previousDay"
    PREVIOUSMONTH = "previousMonth"
    PREVIOUSQUARTER = "previousQuarter"
    PREVIOUSWEEK = "previousWeek"
    SAMEDAYLASTMONTH = "sameDayLastMonth"

    def __str__(self) -> str:
        return str(self.value)
