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
- `closure_contract`
- `claims`
- `evidence`
- `srvl_results`
- `gate_results` for gates 0 through 11
- `pipeline_results` for research verification steps 1 through 5
- `axis_reviews` for theory, design, implementation, environment, and operations
- `defect_register`
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

## Closure Contract

The `closure_contract` binds the stopping logic to packet validation.

It must contain:

- `required_evidence`
- `public_boundary`
- `local_repair_boundary`
- `local_repair_remaining_count`
- `refusal_reason_policy`
- `lightweight_preservation_rule`

`PASS_SCOPED` requires `local_repair_remaining_count = 0`.

## Pipeline Result Rule

Every public judgment packet must include exactly one result row for each research verification step from 1 through 5.

If a pipeline step is `HOLD` or `FAIL`, it must name its blocking condition. `PASS_SCOPED` cannot contain a `HOLD` or `FAIL` pipeline step.

## Gate-Level Contracts

| Gate | Must read | Must write | PASS requires | HOLD requires | FAIL requires |
|---:|---|---|---|---|---|
| 0 | raw target | normalized packet | packet fields are readable | target is underspecified | target cannot be represented |
| 1 | target, scope, not_scope, purpose | frozen scope record | scope and non-scope are explicit | owner must define boundary | scope contradicts target |
| 2 | frozen scope, claims | atomic claim list | broad claims are split | claim needs owner clarification | claim is circular or empty |
| 3 | claims, time, modality, layer | separation record | past/current/future and actual/possible/counterfactual are separated | missing modality or time data | layers are falsely merged |
| 4 | claims, evidence | evidence bindings | every claim has evidence or explicit no-evidence state | evidence exists but is incomplete | claim has no evidence and is promoted |
| 5 | evidence bindings | SRVL results | levels follow direct evidence | level is underdetermined | level exceeds evidence |
| 6 | purpose, metrics, threshold | measurement record | object, unit, procedure, and threshold exist | metric not yet fixed | metric is circular or impossible |
| 7 | packet, fixtures, counterexamples | boundary findings | negative and boundary classes are addressed | required case is missing | false close appears |
| 8 | SRVL, evidence, claims | promotion findings | no forbidden promotion remains | promotion status unknown | overclaim is present |
| 9 | findings, blockers | repair record | local fixes are done or exact blocker named | blocker owner unknown | local fix is skipped |
| 10 | publication packet | redaction findings | no public-unsafe content remains | uncertain public risk remains | sensitive content remains |
| 11 | all prior gate results | final verdict | verdict matches evidence and blockers | required gate is held | verdict contradicts evidence |

## Empty-Stage Rule

A gate is empty if it only names a concern but has no read fields, write fields, pass condition, hold condition, fail condition, or downstream effect. Empty gates must be repaired before the procedure is claimed complete.

## Complete-Gate Result Rule

Every public judgment packet must include exactly one result row for each always-on gate from 0 through 11. Missing gates and duplicate gates are invalid.
