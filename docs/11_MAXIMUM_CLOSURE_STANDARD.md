# Maximum Closure Standard

This standard defines when a public review may stop.

It is not a motivational standard. It is a stopping contract for public artifacts, public procedures, and public judgment packets.

## Completion

Completion is not approval language. Completion means that no evidence-backed refusal reason remains inside the declared scope.

If a rational refusal reason remains, the result is `HOLD` or `FAIL`.

If no new contradiction, omission, risk, degradation, boundary gap, authority conflict, or verification blocker can be shown, do not invent vague "more improvement" language.

## Required Scope Split

Before closure is judged, record:

- `scope`: what the review is allowed to decide,
- `not_scope`: what the review must not decide,
- `purpose`: why the target exists,
- `required_evidence`: evidence classes needed for the claim,
- `public_boundary`: material that must not be published,
- `local_repair_boundary`: what can be fixed inside this review.

If this split is missing, closure is `HOLD`.

## Maximum Improvement

Improvement is not adding more material.

The maximum public form is reached by removing:

- forbidden claims
- impossible requirements
- meaningless duplication
- boundary contamination
- function-reducing simplifications
- unsupported promotion
- public-risk material

and preserving the strongest remaining structure.

## Refusal Reason Taxonomy

A refusal reason is any concrete reason that prevents scoped pass. It must be classified as one of:

- `CONTRADICTION`: the claim conflicts with another claim, invariant, or result.
- `OMISSION`: a required field, gate, axis, fixture, or evidence row is missing.
- `PUBLIC_RISK`: private, sensitive, local, or unpublished material may be exposed.
- `OVERCLAIM`: the stated claim exceeds the strongest evidence.
- `FUNCTION_LOSS`: a simplification removes required capability or preservation.
- `BOUNDARY_MIX`: scope, non-scope, time, modality, or evidence class is mixed.
- `UNVERIFIED_RUNTIME`: a runtime or operational claim lacks direct behavior evidence.
- `UNREPAIRED_LOCAL_GAP`: a locally fixable gap was left for future work.
- `FUNDAMENTAL_UNFIT`: the design cannot satisfy its stated purpose without redesign.

Vague concerns are not refusal reasons until they identify the broken field, gate, axis, or claim.

## Lightweight Rule

Reducing capability is not lightweighting.

Lightweighting is accepted only when capability and information preservation are maintained while reducing duplication, size, operational friction, or resource cost.

Accepted lightweighting must state:

- what was removed,
- what was preserved,
- what evidence still supports the claim,
- what recovery or reconstruction path remains,
- and why no required function was downgraded.

## Stop Rule

Stop only when:

- refusal reasons are removed,
- more work would create duplication, public risk, or scope pollution,
- and the current artifact has direct evidence for its scoped claim.

Do not stop when:

- scope is mixed,
- old and current standards conflict,
- failure handling is absent,
- handoff is impossible,
- implementation and documentation are separated without a bridge,
- or functionality preservation is unproven.

## Repair Loop

Closure requires this loop:

1. derive the scoped completion bar,
2. inspect actual artifacts,
3. identify refusal reasons,
4. classify each reason as locally fixable, external blocker, intentional boundary, or out-of-scope claim,
5. repair all locally fixable reasons,
6. rerun validation and public safety checks,
7. record remaining blockers and boundaries,
8. emit the final verdict.

`PASS_SCOPED` is forbidden while any locally fixable refusal reason remains.

## Evidence Rule

The final verdict may not be stronger than the strongest evidence class required by the claim.

- Design-only evidence cannot prove runtime behavior.
- Runtime behavior cannot prove release readiness.
- A clean public scan cannot prove product correctness.
- A valid packet cannot prove the reviewed target itself is valid unless the packet contains the required evidence.

## Public Boundary

Maximum closure for this repository also means public-safe closure.

Do not publish:

- private project names,
- private architecture,
- local paths,
- credentials or tokens,
- unpublished implementation details,
- raw logs containing private state,
- internal prompts or private proof machinery.

The strongest public artifact is the generic procedure and harness, not the private system it may have been inspired by.
