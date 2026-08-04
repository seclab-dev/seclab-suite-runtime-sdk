import json
from pathlib import Path

from seclab_suite_runtime import OperationEvent, RuntimeDescriptor
from seclab_suite_runtime.types import OperationImpact, OperationOutcome, OperationTarget

FIXTURES = Path(__file__).parents[3] / "contracts" / "fixtures"


def test_shared_runtime_fixture() -> None:
    descriptor = RuntimeDescriptor.load(FIXTURES / "runtime" / "uds-valid.json")
    assert descriptor.schema_version == 1
    descriptor.require_identity("seclab.host-scanner", "instance-1")


def test_shared_event_fixture() -> None:
    value = json.loads((FIXTURES / "operation-events" / "success.json").read_text())
    event = OperationEvent(
        event_id=value["eventId"],
        operation_context_id=value["operationContextId"],
        event_code=value["eventCode"],
        zh_cn=value["eventLabel"]["zhCn"],
        en_us=value["eventLabel"]["enUs"],
        outcome=OperationOutcome(value["outcome"]),
        impact=OperationImpact(value["impact"]),
        target=OperationTarget(kind=value["target"]["kind"], id=value["target"]["id"]),
        task_id=value["taskId"],
        parameters=value["parameters"],
    )
    assert event.to_dict()["eventCode"] == "scan_submitted"
