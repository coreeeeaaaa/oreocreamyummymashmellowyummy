#!/usr/bin/env python3
"""Validate public judgment packets against the repository schema."""

from __future__ import annotations

import json
import sys
from pathlib import Path


FINAL_VERDICT_TO_GATE_11 = {
    "PASS_SCOPED": "PASS",
    "HOLD_EXACT_BLOCKER": "HOLD",
    "FAIL_CONTRADICTED": "FAIL",
    "REJECT_OVERCLAIM": "FAIL",
    "REDACTION_REQUIRED": "HOLD",
}

REQUIRED_AXES = {"theory", "design", "implementation", "environment", "operations"}
REQUIRED_CLOSURE_FIELDS = {
    "required_evidence",
    "public_boundary",
    "local_repair_boundary",
    "local_repair_remaining_count",
    "refusal_reason_policy",
    "lightweight_preservation_rule",
}
REQUIRED_PIPELINE_STEPS = {1, 2, 3, 4, 5}


def fail(message: str) -> int:
    print(f"PUBLIC_PACKET_VALIDATION_FAIL: {message}")
    return 1


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        raise ValueError(f"{path}: invalid json: {exc}") from exc


def level_number(level: str | None) -> int | None:
    if not isinstance(level, str) or not level.startswith("L"):
        return None
    try:
        value = int(level[1:])
    except ValueError:
        return None
    return value if 0 <= value <= 16 else None


def validate_packet(path: Path, schema: dict) -> list[str]:
    errors: list[str] = []
    packet = load_json(path)
    required = schema["required"]
    allowed = set(schema["properties"])
    for field in required:
        if field not in packet:
            errors.append(f"{path}: missing required field {field}")
    for field in packet:
        if field not in allowed:
            errors.append(f"{path}: unknown field {field}")

    srvl = packet.get("srvl_results", {})
    first_blocking = srvl.get("first_blocking_level")
    highest_passed = srvl.get("highest_passed_level")
    final_verdict = packet.get("final_verdict")
    if final_verdict == "PASS_SCOPED" and first_blocking is not None:
        errors.append(f"{path}: PASS_SCOPED cannot have first_blocking_level")
    if final_verdict != "PASS_SCOPED" and first_blocking is None:
        errors.append(f"{path}: non-PASS verdict requires first_blocking_level")
    if final_verdict != "PASS_SCOPED" and not srvl.get("blocking_reason"):
        errors.append(f"{path}: non-PASS verdict requires blocking_reason")
    if final_verdict != "PASS_SCOPED" and not packet.get("required_next_action"):
        errors.append(f"{path}: non-PASS verdict requires required_next_action")

    closure = packet.get("closure_contract", {})
    if not isinstance(closure, dict):
        errors.append(f"{path}: closure_contract must be an object")
        closure = {}
    closure_fields = set(closure)
    if closure_fields != REQUIRED_CLOSURE_FIELDS:
        missing = sorted(REQUIRED_CLOSURE_FIELDS - closure_fields)
        extra = sorted(closure_fields - REQUIRED_CLOSURE_FIELDS)
        errors.append(f"{path}: closure_contract fields invalid; missing={missing} extra={extra}")
    for field_name in ("required_evidence", "public_boundary", "local_repair_boundary"):
        value = closure.get(field_name)
        if not isinstance(value, list) or not value:
            errors.append(f"{path}: closure_contract.{field_name} must be a non-empty list")
    for field_name in ("refusal_reason_policy", "lightweight_preservation_rule"):
        value = closure.get(field_name)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{path}: closure_contract.{field_name} must be non-empty")
    repair_remaining = closure.get("local_repair_remaining_count")
    if not isinstance(repair_remaining, int) or repair_remaining < 0:
        errors.append(f"{path}: closure_contract.local_repair_remaining_count must be a non-negative integer")
    if final_verdict == "PASS_SCOPED" and repair_remaining != 0:
        errors.append(f"{path}: PASS_SCOPED requires local_repair_remaining_count=0")

    highest_num = level_number(highest_passed)
    blocking_num = level_number(first_blocking)
    if first_blocking is not None and highest_num is not None and blocking_num is not None:
        if blocking_num <= highest_num:
            errors.append(f"{path}: first_blocking_level must be above highest_passed_level")

    if packet.get("forbidden_promotion_clean") is False and not packet.get("forbidden_promotion_findings"):
        errors.append(f"{path}: forbidden_promotion_clean=false requires findings")
    if packet.get("redaction_clean") is False and not packet.get("redaction_findings"):
        errors.append(f"{path}: redaction_clean=false requires findings")
    if packet.get("forbidden_promotion_clean") is False and final_verdict != "REJECT_OVERCLAIM":
        errors.append(f"{path}: forbidden promotion findings require final_verdict=REJECT_OVERCLAIM")
    if final_verdict == "REJECT_OVERCLAIM" and packet.get("forbidden_promotion_clean") is not False:
        errors.append(f"{path}: REJECT_OVERCLAIM requires forbidden_promotion_clean=false")
    if packet.get("redaction_clean") is False and final_verdict != "REDACTION_REQUIRED":
        errors.append(f"{path}: redaction findings require final_verdict=REDACTION_REQUIRED")
    if final_verdict == "REDACTION_REQUIRED" and packet.get("redaction_clean") is not False:
        errors.append(f"{path}: REDACTION_REQUIRED requires redaction_clean=false")

    evidence_ids = {row.get("evidence_id") for row in packet.get("evidence", []) if isinstance(row, dict)}
    for claim in packet.get("claims", []):
        if not isinstance(claim, dict):
            continue
        claimed_level_num = level_number(claim.get("claimed_level"))
        if highest_num is not None and claimed_level_num is not None and claimed_level_num > highest_num:
            errors.append(f"{path}: claim {claim.get('claim_id')} exceeds highest_passed_level")
        for evidence_ref in claim.get("evidence_refs", []):
            if evidence_ref not in evidence_ids:
                errors.append(f"{path}: claim {claim.get('claim_id')} references missing evidence {evidence_ref}")

    gate_rows = packet.get("gate_results", [])
    gate_ids = [row.get("gate_id") for row in gate_rows if isinstance(row, dict)]
    expected_gate_ids = set(range(12))
    actual_gate_ids = set(gate_ids)
    if actual_gate_ids != expected_gate_ids:
        missing = sorted(expected_gate_ids - actual_gate_ids)
        extra = sorted(actual_gate_ids - expected_gate_ids)
        errors.append(f"{path}: gate_results must include exactly gates 0-11; missing={missing} extra={extra}")
    if len(gate_ids) != len(actual_gate_ids):
        errors.append(f"{path}: gate_results must not contain duplicate gate_id values")
    gate_by_id = {row.get("gate_id"): row for row in gate_rows if isinstance(row, dict)}
    if packet.get("forbidden_promotion_clean") is False and gate_by_id.get(8, {}).get("verdict") != "FAIL":
        errors.append(f"{path}: gate 8 must FAIL when forbidden_promotion_clean=false")
    if packet.get("forbidden_promotion_clean") is True and gate_by_id.get(8, {}).get("verdict") == "FAIL":
        errors.append(f"{path}: gate 8 cannot FAIL when forbidden_promotion_clean=true")
    if packet.get("redaction_clean") is False and gate_by_id.get(10, {}).get("verdict") != "FAIL":
        errors.append(f"{path}: gate 10 must FAIL when redaction_clean=false")
    if packet.get("redaction_clean") is True and gate_by_id.get(10, {}).get("verdict") == "FAIL":
        errors.append(f"{path}: gate 10 cannot FAIL when redaction_clean=true")
    expected_gate_11 = FINAL_VERDICT_TO_GATE_11.get(final_verdict)
    if expected_gate_11 and gate_by_id.get(11, {}).get("verdict") != expected_gate_11:
        errors.append(f"{path}: gate 11 verdict must match final_verdict {final_verdict}")

    pipeline_rows = packet.get("pipeline_results", [])
    pipeline_ids = [row.get("step_id") for row in pipeline_rows if isinstance(row, dict)]
    pipeline_set = set(pipeline_ids)
    if pipeline_set != REQUIRED_PIPELINE_STEPS:
        missing = sorted(REQUIRED_PIPELINE_STEPS - pipeline_set)
        extra = sorted(pipeline_set - REQUIRED_PIPELINE_STEPS)
        errors.append(f"{path}: pipeline_results must include exactly steps 1-5; missing={missing} extra={extra}")
    if len(pipeline_ids) != len(pipeline_set):
        errors.append(f"{path}: pipeline_results must not contain duplicate step_id values")
    if final_verdict == "PASS_SCOPED":
        blocking_steps = [
            row.get("step_id")
            for row in pipeline_rows
            if isinstance(row, dict) and row.get("verdict") in {"HOLD", "FAIL"}
        ]
        if blocking_steps:
            errors.append(f"{path}: PASS_SCOPED cannot have HOLD/FAIL pipeline steps: {blocking_steps}")
    for row in pipeline_rows:
        if not isinstance(row, dict):
            continue
        if row.get("verdict") in {"HOLD", "FAIL"} and not row.get("blocking_condition"):
            errors.append(f"{path}: HOLD/FAIL pipeline step {row.get('step_id')} requires blocking_condition")

    axis_rows = packet.get("axis_reviews", [])
    axes = [row.get("axis") for row in axis_rows if isinstance(row, dict)]
    axis_set = set(axes)
    if axis_set != REQUIRED_AXES:
        missing = sorted(REQUIRED_AXES - axis_set)
        extra = sorted(axis_set - REQUIRED_AXES)
        errors.append(f"{path}: axis_reviews must include exactly the five required axes; missing={missing} extra={extra}")
    if len(axes) != len(axis_set):
        errors.append(f"{path}: axis_reviews must not contain duplicate axis values")
    if final_verdict == "PASS_SCOPED":
        blocking_axes = [
            row.get("axis")
            for row in axis_rows
            if isinstance(row, dict) and row.get("verdict") in {"HOLD", "FAIL"}
        ]
        if blocking_axes:
            errors.append(f"{path}: PASS_SCOPED cannot have HOLD/FAIL axis reviews: {blocking_axes}")

    p0_defects = [
        row.get("defect_id")
        for row in packet.get("defect_register", [])
        if isinstance(row, dict) and row.get("severity") == "P0"
    ]
    if p0_defects and final_verdict not in {"FAIL_CONTRADICTED", "REDACTION_REQUIRED"}:
        errors.append(f"{path}: P0 defects block final verdict {final_verdict}: {p0_defects}")

    return errors


def main() -> int:
    if len(sys.argv) < 3:
        return fail("usage: validate_public_packet.py <schema> <packet> [<packet> ...]")
    schema = load_json(Path(sys.argv[1]))
    errors: list[str] = []
    for packet_path in sys.argv[2:]:
        errors.extend(validate_packet(Path(packet_path), schema))
    if errors:
        print("PUBLIC_PACKET_VALIDATION_FAIL")
        for error in errors:
            print(error)
        return 1
    print("PUBLIC_PACKET_VALIDATION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
