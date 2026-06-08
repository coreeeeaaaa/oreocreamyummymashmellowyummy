# Harness Runtime

This repository now includes a minimal public harness runtime.

It is not a private system runtime and it does not inspect private implementation details. It validates public judgment packets and public release safety.

## Runtime Commands

```bash
python3 harness/public_safety_scan.py .
python3 harness/validate_public_packet.py schemas/public-judgment-packet.schema.json examples/software-feature-review.json examples/research-direction-review.json fixtures/meta/valid_pass_scoped.json
python3 harness/run_meta_fixtures.py
```

## Runtime Responsibilities

- public leak pattern scan
- packet required-field validation
- unknown-field rejection
- gate 0 through 11 completeness
- duplicate gate rejection
- claim evidence-reference validation
- claim-level overpromotion rejection
- redaction contradiction rejection
- forbidden-promotion contradiction rejection
- final verdict to gate-result consistency
- gate-result to clean-state consistency
- final-verdict and gate-11 consistency
- closure-contract completeness
- local repair remaining count blocking
- research verification pipeline step coverage
- five-axis review completeness
- P0 defect blocking
- defect-register structure
- positive and negative meta-fixture execution

## Runtime Non-Responsibilities

- It does not prove a reviewed target is true.
- It does not run private systems.
- It does not replace human or agent judgment.
- It does not perform external security scanning.
- It does not publish private implementation evidence.
