# Research Verification Pipeline

This pipeline generalizes the research, proof, verification, meta-audit, and handoff prompts into a public procedure.

It does not publish private technical systems or private proof machinery.

## Pipeline Contract

The pipeline is a harness sequence. It is not a claim that a target is true.

Each step must produce a public-safe artifact that can be consumed by the next step:

| Step | Input | Output | Blocking condition |
|---:|---|---|---|
| 1 | rough target, constraints, risks | refined target packet | target, scope, or forbidden claims remain unclear |
| 2 | refined target packet | raw candidate ledger | only one angle exists or candidates are untyped |
| 3 | candidate ledger | verification ledger | claims lack evidence, domain tags, or bridge rules |
| 4 | verification ledger | meta-verification ledger | verifier result has circularity, contradiction, or overclaim |
| 5 | audited ledger | handoff package | reproduction, risk, or next action is missing |

No step may replace a later step. A refined target is not verification. A verification result is not meta-verification. A handoff package is not release evidence unless release evidence is in scope.

## Step 1. Refine

Clarify the target, constraints, forbidden shortcuts, output contract, and collision rules.

Do not skip or reorder phases without recording the reason.

Required output:

- target statement,
- scope and non-scope,
- success condition,
- failure condition,
- forbidden shortcut list,
- public boundary,
- evidence requirement,
- next-step input contract.

Failure cases:

- the target remains broad enough to hide multiple claims,
- success is phrased as effort or quantity,
- forbidden shortcuts are not explicit,
- public/private boundary is absent.

## Step 2. Raw Candidate Generation

Generate multiple structurally different candidate angles.

Rules:

- novelty is not truth,
- speculation must remain marked as candidate,
- every rough idea must carry a structural reason,
- failed attempts must be recorded,
- do not stop at the first promising direction.

Required output:

- candidate id,
- candidate type,
- structural reason,
- expected benefit,
- expected failure mode,
- dependency,
- evidence needed,
- discard reason when rejected.

Failure cases:

- candidates are paraphrases of the same idea,
- novelty is promoted as correctness,
- failed attempts are deleted,
- candidates bypass the refined target contract.

## Step 3. Dual Verification

Verify or reject candidates through at least two independent channels when the domain permits it.

Rules:

- every claim has a domain tag,
- every inference edge has a license,
- cross-channel claims require explicit bridge rules,
- gaps are ledgers, not hidden prose,
- final verdict cannot exceed the weakest required proof edge.

Independent channels may include:

- static specification review,
- implementation or runtime behavior,
- counterexample construction,
- external source evidence,
- adversarial review,
- reproducibility check,
- measurement or benchmark.

Required output:

- claim list,
- domain tags,
- evidence bindings,
- inference licenses,
- bridge rules,
- gap ledger,
- accepted and rejected candidate table.

Failure cases:

- evidence only repeats the claim,
- bridge rules are implied but not stated,
- a gap is hidden in prose,
- one channel's result is promoted into whole-target truth.

## Step 4. Meta Verification

Audit the verifier result, not the original problem from scratch.

Check:

- formal validity,
- evidence quality,
- contradiction,
- self-reference,
- circularity,
- hidden assumptions,
- category or type errors,
- unsafe operational claims,
- verdict strength.

Required output:

- verifier-scope statement,
- accepted verifier findings,
- rejected verifier findings,
- contradiction ledger,
- hidden-assumption ledger,
- overclaim findings,
- required repair actions.

Failure cases:

- meta verification restarts the problem and ignores the verifier artifact,
- the same assumption is used as both claim and proof,
- the verifier validates only file existence or formatting when behavior is claimed,
- a scoped result is promoted to global completion.

## Step 5. Handoff

Package only what survived audit.

Required handoff surfaces:

- source verdict digest,
- scope and non-scope,
- deliverables,
- test and acceptance plan,
- risk register,
- reproducibility package,
- open blockers,
- final decision,
- machine-readable report.

If handoff discovers a new logical or evidential defect, stop promotion and route back to verification or meta verification.

## Re-entry Rules

- Refinement defects route to Step 1.
- Candidate diversity defects route to Step 2.
- Evidence, bridge, or counterexample defects route to Step 3.
- Verifier overclaim or circularity defects route to Step 4.
- Reproduction, packaging, or operational defects route to Step 5.

If a defect is public-risk related, route through the public redaction gate before any publication.

## Final Verdict Boundary

This pipeline may conclude:

- `PASS_SCOPED`: all required steps for the declared scope passed.
- `HOLD_EXACT_BLOCKER`: a named blocker prevents pass.
- `FAIL_CONTRADICTED`: contradiction or impossible condition is proven.
- `REJECT_OVERCLAIM`: claim exceeds evidence.
- `REDACTION_REQUIRED`: publication risk remains.

It may not conclude private-system completion, production readiness, or external truth unless those claims are explicitly scoped and directly evidenced.
