#!/usr/bin/env python3
"""Run positive and negative public harness meta-fixtures."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "public-judgment-packet.schema.json"
VALIDATOR = ROOT / "harness" / "validate_public_packet.py"
FIXTURE_DIR = ROOT / "fixtures" / "meta"


def main() -> int:
    fixtures = sorted(FIXTURE_DIR.glob("*.json"))
    if not fixtures:
        print("META_FIXTURE_RUN_FAIL: no fixtures")
        return 1

    failures: list[str] = []
    for fixture in fixtures:
        expected_pass = fixture.name.startswith("valid_")
        result = subprocess.run(
            [sys.executable, str(VALIDATOR), str(SCHEMA), str(fixture)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        observed_pass = result.returncode == 0
        if expected_pass != observed_pass:
            failures.append(
                f"{fixture.name}: expected {'PASS' if expected_pass else 'FAIL'} "
                f"observed {'PASS' if observed_pass else 'FAIL'}\n{result.stdout}"
            )

    if failures:
        print("META_FIXTURE_RUN_FAIL")
        for failure in failures:
            print(failure)
        return 1

    print("META_FIXTURE_RUN_PASS")
    print(f"fixtures_checked={len(fixtures)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
