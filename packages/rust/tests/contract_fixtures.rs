use seclab_suite_runtime::{OperationEvent, RuntimeDescriptor};

#[test]
fn shared_fixtures_match_rust_types() {
    let runtime = include_str!("../../../contracts/fixtures/runtime/uds-valid.json");
    let descriptor: RuntimeDescriptor = serde_json::from_str(runtime).unwrap();
    assert_eq!(descriptor.schema_version, 1);
    assert!(
        descriptor
            .require_identity("seclab.host-scanner", "instance-1")
            .is_ok()
    );
    assert!(
        descriptor
            .require_identity("seclab.packet", "instance-1")
            .is_err()
    );
    let https = include_str!("../../../contracts/fixtures/runtime/https-valid.json");
    let https: RuntimeDescriptor = serde_json::from_str(https).unwrap();
    assert_eq!(https.suite_id, "seclab.packet");

    let event = include_str!("../../../contracts/fixtures/operation-events/success.json");
    let event: OperationEvent = serde_json::from_str(event).unwrap();
    assert_eq!(event.event_code, "scan_submitted");
}
