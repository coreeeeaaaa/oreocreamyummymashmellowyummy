# Usage, Process, and Exception Flow

This document defines the operational use order for the public harness.

It is not a new gate. It is the procedure for applying the existing ladder, gates, closure contract, pipeline, axis review, redaction policy, validator, and meta fixtures without skipping or overpromoting any step.

## 1. Use Order

Use the harness in this order:

1. Read the public boundary.
2. Define the target, scope, non-scope, and purpose.
3. Create or update a public judgment packet.
4. Fill the closure contract.
5. Atomize claims.
6. Bind evidence.
7. Run gates 0 through 11.
8. Run research verification pipeline steps 1 through 5.
9. Complete five-axis adversarial review.
10. Fill the defect register.
11. Resolve forbidden promotion and redaction state.
12. Emit the final verdict.
13. Run the validator and meta fixtures.
14. Publish only if public safety scan is clean.

Do not run later steps as substitutes for earlier steps. A clean redaction scan does not prove claim correctness. A full gate table does not prove pipeline completion. A valid packet does not prove the reviewed target beyond the evidence inside the packet.

## 2. Processing Order

Processing order is fixed unless a recorded exception says otherwise.

```text
target
-> public boundary check
-> scope freeze
-> closure contract
-> claim atomization
-> layer/time/modality separation
-> evidence binding
-> SRVL maturity assignment
-> measurement and criteria check
-> counterexample and boundary check
-> forbidden promotion check
-> repair and re-entry check
-> public redaction check
-> research verification pipeline
-> five-axis adversarial review
-> defect register reconciliation
-> final verdict
-> validator
-> meta fixtures
-> public safety scan
```

## 3. Exception Handling

Exceptions are not informal notes. Every exception must route to one of the allowed verdicts or repair paths.

| Exception | Required handling | Final verdict boundary |
|---|---|---|
| target cannot be represented | record gate 0 `FAIL` | `FAIL_CONTRADICTED` |
| scope is unclear | hold at gate 1 | `HOLD_EXACT_BLOCKER` |
| broad claim hides multiple claims | return to gate 2 | `HOLD_EXACT_BLOCKER` until atomized |
| time, modality, or layer is mixed | return to gate 3 | `HOLD_EXACT_BLOCKER` or `REJECT_OVERCLAIM` |
| claim has no evidence | fail or demote at gate 4 | no `PASS_SCOPED` |
| claimed SRVL level exceeds evidence | gate 8 fails | `REJECT_OVERCLAIM` |
| metric is missing | gate 6 holds | `HOLD_EXACT_BLOCKER` |
| negative or boundary case is missing | gate 7 holds | `HOLD_EXACT_BLOCKER` |
| false close appears | gate 7 fails | `FAIL_CONTRADICTED` |
| local repair remains | gate 9 holds | no `PASS_SCOPED` |
| blocker owner is unknown | gate 9 holds | `HOLD_EXACT_BLOCKER` |
| public risk remains | gate 10 fails | `REDACTION_REQUIRED` |
| P0 defect exists | defect register blocks pass | `FAIL_CONTRADICTED` or `REDACTION_REQUIRED` |
| pipeline step missing | validator rejects packet | no `PASS_SCOPED` |
| pipeline step is `HOLD` or `FAIL` | name blocking condition | no `PASS_SCOPED` |
| axis review missing | validator rejects packet | no `PASS_SCOPED` |
| axis review is `HOLD` or `FAIL` | record defect or blocker | no `PASS_SCOPED` |
| final verdict contradicts gate 11 | validator rejects packet | no publication |

## 4. Re-entry Order

Use the nearest responsible earlier stage:

- scope defects re-enter at gate 1,
- claim shape defects re-enter at gate 2,
- time, modality, or layer defects re-enter at gate 3,
- evidence defects re-enter at gate 4,
- maturity overclaims re-enter at gate 5 or gate 8,
- metric defects re-enter at gate 6,
- counterexample defects re-enter at gate 7,
- local repair defects re-enter at gate 9,
- public-risk defects re-enter at gate 10,
- pipeline defects re-enter at the failed pipeline step,
- axis defects re-enter at the failed axis and then reconcile through the defect register.

Do not re-enter at a later stage to avoid the responsible earlier stage.

## 5. Validator-Enforced Exceptions

The validator enforces these exception classes:

- missing required fields,
- unknown fields,
- invalid first-blocking and highest-passed relation,
- `PASS_SCOPED` with `first_blocking_level`,
- non-pass verdict without blocker and next action,
- missing or invalid closure contract,
- `PASS_SCOPED` with local repair remaining,
- missing or duplicate gate rows,
- forbidden-promotion verdict contradiction,
- redaction verdict contradiction,
- final verdict and gate 11 mismatch,
- missing or duplicate pipeline steps,
- `PASS_SCOPED` with pipeline `HOLD` or `FAIL`,
- pipeline `HOLD` or `FAIL` without blocking condition,
- missing or duplicate axis reviews,
- `PASS_SCOPED` with axis `HOLD` or `FAIL`,
- P0 defect with non-blocking final verdict,
- claim evidence reference missing,
- claim level exceeding highest passed level.

## 6. Meta-Fixture-Enforced Exceptions

The meta fixtures enforce that:

- a complete valid packet passes,
- missing gate coverage fails,
- missing pipeline coverage fails,
- overclaim fails,
- dirty redaction with pass fails,
- unrepaired local work with pass fails.

## 7. Publication Rule

Publication is allowed only after:

1. packet validation passes,
2. meta fixtures pass,
3. public safety scan passes,
4. the public boundary remains clean,
5. no scoped result is promoted into private, global, runtime, production, or release claims.

If any publication risk appears, stop publication and route to the public redaction gate.

## 8. Minimal Command Order

Run:

```bash
python3 harness/validate_public_packet.py schemas/public-judgment-packet.schema.json examples/software-feature-review.json examples/research-direction-review.json fixtures/meta/valid_pass_scoped.json
python3 harness/run_meta_fixtures.py
python3 harness/public_safety_scan.py .
```

The safety scan may be run earlier as a pre-check, but it must also pass before publication.
