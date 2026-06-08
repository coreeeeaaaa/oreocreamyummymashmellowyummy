# SRVL v4 Normalized Ladder

SRVL means System Readiness and Validity Ladder. It is a maturity ladder for preventing false completion.

## Verdict Values

- `PASS`: the level is directly satisfied by evidence.
- `HOLD`: the level is not yet satisfied, but no contradiction is proven.
- `FAIL`: the level is contradicted, invalid, or falsely promoted.

`PARTIAL` is not a final verdict. If useful, it may be recorded as a note under `HOLD`.

## Ladder

| Level | Name | Meaning |
|---:|---|---|
| L0 | ABSENT | The target does not exist. |
| L1 | EXISTS | A name, artifact, file, object, or candidate exists. |
| L2 | DEFINED | Scope, non-scope, target, and non-target are defined. |
| L3 | STRUCTURED | Primitive elements, relations, and dependency structure are identified. |
| L4 | TYPED_SPECIFIED | Inputs, outputs, state, transitions, forbidden conditions, and terminal states are specified. |
| L5 | CONTRACT_BOUND | Interfaces, schemas, invariants, preconditions, and postconditions are contract-bound. |
| L6 | COMPOSITION_VALID | Contracts compose without interface gaps, type mismatches, or invariant conflicts. |
| L7 | LOGICALLY_OR_MATHEMATICALLY_COHERENT | Declared states, transitions, invariants, preservation rules, and contradiction boundaries are coherent inside the declared domain. |
| L8 | SEMANTICALLY_BOUND | Surface signs, symbols, inputs, evidence, time, modality, boundary, and margin states are bound to intended meaning. |
| L9 | BOUNDARY_VALIDATED | Valid, invalid, ambiguous, impossible, adversarial, and boundary inputs do not false-close. |
| L10 | FUNCTIONALLY_DESIGNED | The intended procedure, algorithm, workflow, or state transition design is closed. |
| L11 | INTEGRATION_READY | Interfaces to modules, verifiers, consumers, operators, or runtimes are closed. |
| L12 | RUNTIME_OPERATING | The target runs under declared input, environment, and resource bounds. |
| L13 | VERIFIED | Declared positive, negative, boundary, and adversarial fixture sets pass under verifier. |
| L14 | OBSERVED_REPLAY_BACKED | Trace, log, witness, replay, rollback, reconstruction, or re-entry evidence exists in declared scope. |
| L15 | PURPOSE_SATISFYING | Pre-declared purpose and purpose metrics are satisfied under declared conditions. |
| L16 | RELEASE_READY | Security, permissions, documentation, compatibility, rollback, monitoring, and operational hygiene are ready. |

## Contiguous Level Rule

`highest_passed_level` means the highest contiguous level from L1 upward that has `PASS`.

If L4 is `HOLD`, then later evidence at L9 may be recorded, but `highest_passed_level` remains L3 until L4 is resolved.

## Dependent HOLD Rule

A `HOLD` blocks dependent upper claims. It does not automatically block independent scoped claims. Global completion is blocked if any required dependency is held.

