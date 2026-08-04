"""SecLab 套件后端 Runtime SDK。"""

from .client import RuntimeClient
from .descriptor import RuntimeDescriptor, RuntimeEndpoint
from .errors import AgentError, CapabilityDenied, InvalidDescriptor, InvalidEvent
from .operation_logs import (
    OPERATION_CONTEXT_HEADER,
    OperationEvent,
    operation_context_from_headers,
)
from .types import OperationImpact, OperationOutcome, OperationTarget

__all__ = [
    "OPERATION_CONTEXT_HEADER",
    "AgentError",
    "CapabilityDenied",
    "InvalidDescriptor",
    "InvalidEvent",
    "OperationEvent",
    "OperationImpact",
    "OperationOutcome",
    "OperationTarget",
    "RuntimeClient",
    "RuntimeDescriptor",
    "RuntimeEndpoint",
    "operation_context_from_headers",
]
