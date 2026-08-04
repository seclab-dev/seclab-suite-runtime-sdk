"""操作事件公开类型。"""

from dataclasses import dataclass
from enum import StrEnum
from typing import TypeAlias


class OperationOutcome(StrEnum):
    SUCCESS = "success"
    FAILURE = "failure"
    PARTIAL = "partial"
    CANCELED = "canceled"
    TIMED_OUT = "timedOut"


class OperationImpact(StrEnum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"


@dataclass(frozen=True)
class OperationTarget:
    kind: str
    id: str
    display_name: str | None = None
    ownership: str | None = None


ParameterValue: TypeAlias = str | int | float | bool
