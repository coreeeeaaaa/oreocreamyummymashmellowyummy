# Meta Fixtures

Meta fixtures test the harness itself.

## Rule

Files beginning with `valid_` must pass.

Files beginning with `invalid_` must fail.

The meta-fixture runner fails if a negative fixture accidentally passes or if a positive fixture fails.

## Current Fixture Classes

- `valid_pass_scoped.json`: complete public packet with all gates 0 through 11.
- `invalid_missing_gate.json`: detects incomplete gate coverage.
- `invalid_overclaim.json`: detects a claim that exceeds the highest supported SRVL level.
- `invalid_redaction_dirty.json`: detects contradiction between redaction status and final verdict.

The valid fixture must include all five axis reviews. Negative fixtures must carry defect-register entries that explain why the packet is intentionally invalid.

## Purpose

The fixtures prevent the harness from becoming a checklist that only accepts happy-path examples.
