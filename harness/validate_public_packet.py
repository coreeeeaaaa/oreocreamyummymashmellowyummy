#!/usr/bin/env python3
"""Validate public judgment packets against the repository schema."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def fail(message: str) -> int:
    print(f"PUBLIC_PACKET_VALIDATION_FAIL: {message}")
    return 1


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        raise ValueError(f"{path}: invalid json: {exc}") from exc


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
    final_verdict = packet.get("final_verdict")
    if final_verdict == "PASS_SCOPED" and first_blocking is not None:
        errors.append(f"{path}: PASS_SCOPED cannot have first_blocking_level")

    if packet.get("forbidden_promotion_clean") is False and not packet.get("forbidden_promotion_findings"):
        errors.append(f"{path}: forbidden_promotion_clean=false requires findings")
    if packet.get("redaction_clean") is False and not packet.get("redaction_findings"):
        errors.append(f"{path}: redaction_clean=false requires findings")

    gate_ids = {row.get("gate_id") for row in packet.get("gate_results", []) if isinstance(row, dict)}
    if 11 not in gate_ids:
        errors.append(f"{path}: gate_results must include Final Verdict Gate 11")

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
