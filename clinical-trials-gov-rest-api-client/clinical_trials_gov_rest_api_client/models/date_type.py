from enum import Enum


class DateType(str, Enum):
    ACTUAL = "ACTUAL"
    ESTIMATED = "ESTIMATED"

    def __str__(self) -> str:
        return str(self.value)
