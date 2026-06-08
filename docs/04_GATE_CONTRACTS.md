# Gate Contracts

Each gate has the same contract shape.

## Contract Shape

```yaml
gate_id:
input:
read_fields:
write_fields:
pass_condition:
hold_condition:
fail_condition:
forbidden_promotion_checks:
evidence_required:
next_gate:
```

## Required Fields

Every review packet must contain:

- `target`
- `scope`
- `not_scope`
- `purpose`
- `claims`
- `evidence`
- `srvl_results`
- `first_blocking_level`
- `forbidden_promotion_findings`
- `redaction_findings`
- `final_verdict`

## Evidence Classes

- `A`: directly observed runtime behavior, trace, or measured output
- `B`: replay, witness, deterministic rerun, or checksum-backed artifact
- `C`: test, verifier, fixture, or validation result
- `D`: static schema, source, configuration, or document artifact
- `E`: explanation, rationale, or design prose
- `F`: unsupported assertion

Core behavior cannot pass on class `E` or `F` alone.

## Completion Rule

A gate may pass only when its direct pass condition is met. A neighboring gate cannot substitute for it.

