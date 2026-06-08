# Adversarial Review Protocol

This protocol is public and generic. It audits whether a target survives hostile review without relying on private project internals.

The protocol is a cross-check layer. It does not ask the target to understand itself. It checks whether externally readable artifacts support the claim.

## Five Axes

Every review must include these axes or explicitly mark an axis as not applicable:

1. Theory
2. Design
3. Implementation
4. Environment
5. Operations

Passing one axis does not pass another axis.

## Axis Contracts

| Axis | Question | PASS requires | Common false pass |
|---|---|---|---|
| Theory | Is the claim internally coherent? | definitions, invariants, contradiction boundaries, and non-goals agree | elegant language without failure conditions |
| Design | Is the structure fit for the purpose? | interfaces, responsibilities, state transitions, and dependencies are closed | diagrams or names without consumers |
| Implementation | Does the artifact do the claimed work? | executable behavior, transformation, rejection, or deliverable path exists | file existence, imports, wrappers, or stubs |
| Environment | Can the work run under declared constraints? | dependencies, permissions, resources, and reproducibility are bounded | assuming the author's local machine |
| Operations | Can the result be used, repaired, rolled back, and handed off? | runbook, risk handling, evidence trail, and next actions exist | one-time success without maintenance path |

Axis result values:

- `PASS`: evidence satisfies the axis.
- `HOLD`: evidence is incomplete or blocker remains.
- `FAIL`: contradiction, unsafe condition, or false promotion exists.
- `NOT_APPLICABLE`: the axis is genuinely outside scope and the reason is recorded.

## Cross-Axis Review

Check failures at boundaries:

- theory and operations
- design and implementation
- implementation and operations
- design and operations
- environment and operations
- theory and design

Boundary failures must be recorded as `cross_axis` defects. Do not hide them inside one axis summary.

## Reviewer Personas

Use at least these public-safe personas:

- uninformed good-faith user
- malicious insider
- external attacker
- future maintainer
- extreme input generator
- economic exhaustion actor
- self-reference or recursion actor

The purpose of personas is defect discovery, not stylistic commentary. Each persona must either produce a defect, produce a tested non-issue, or be marked not applicable with a reason.

## Independent Reproduction

The reviewer must be able to reproduce the claimed procedure from documentation and artifacts without asking the original author.

Any point that requires author explanation is a documentation or handoff defect.

Required reproduction material:

- input packet or target description,
- command or reading path,
- expected output shape,
- pass/fail criteria,
- negative case or rejection case,
- public boundary check,
- final report template.

## Defect Severity

- `P0`: irreversible harm, security breach, data loss, complete stop, or unsafe publication.
- `P1`: core function failure with costly recovery.
- `P2`: feature or boundary failure that blocks the next release or claim.
- `P3`: documentation, usability, or non-core defect.
- `P4`: improvement opportunity, not a defect.

P0 blocks scoped pass.

Defect rows must include:

- defect id,
- severity,
- axis,
- affected claim or gate,
- evidence,
- required action,
- disposition.

Severity is not effort. A small bug can be P0 if it leaks private data. A large rewrite can be P4 if it only improves style.

## Fundamental Unfixability

If the target's design philosophy conflicts with the stated safety or purpose constraints, do not keep patching symptoms. Record fundamental unfixability and route to redesign.

Examples:

- a public artifact requires private secrets to be meaningful,
- a verifier only checks reports while the claim is runtime behavior,
- a lightweighting rule removes required preservation,
- a workflow claims completion while skipping its own negative cases.

## Pass Boundary

Adversarial review can pass only when:

- all five axes are present or explicitly not applicable,
- cross-axis defects are checked,
- P0 defects are absent,
- P1/P2 defects are repaired or converted into exact blockers,
- public redaction is clean,
- no scoped result is promoted into global or release completion,
- independent reproduction is possible from public artifacts.

If any of these are missing, the review is `HOLD` or `FAIL`, not a weak pass.
