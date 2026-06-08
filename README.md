# Oreo Cream Yummy Marshmallow Yummy

A public, domain-neutral judgment harness for separating claims, evidence, maturity, scope, risk, and release readiness.

This repository does not publish private project internals, hidden system rules, proprietary technical architectures, private datasets, private prompts, credentials, or deployment details. It only defines a reusable public procedure for checking whether an idea, design, document, product plan, research direction, or implementation claim has been promoted beyond its evidence.

## What This Is

Oreo Cream Yummy Marshmallow Yummy is a document-first harness. It helps a reviewer ask:

- What exactly is the target?
- What is inside scope and outside scope?
- What claim is being made?
- What evidence supports that claim?
- Which maturity level is actually reached?
- Which level is the first blocking level?
- Is the claim over-promoted?
- Are time, modality, source, and evidence being mixed?
- Is the result safe to publish or release?

The harness is not an autonomous agent, not a secret system, not a runtime, not a proof engine, and not release evidence by itself.

## First Reading Order

1. [Public Boundary](docs/00_PUBLIC_BOUNDARY.md)
2. [Architecture](docs/01_ARCHITECTURE.md)
3. [SRVL v4 Normalized Ladder](docs/02_SRVL_V4_LADDER.md)
4. [Gate Sequence](docs/03_GATE_SEQUENCE.md)
5. [Gate Contracts](docs/04_GATE_CONTRACTS.md)
6. [Verdict System](docs/05_VERDICT_SYSTEM.md)
7. [Redaction and Publication Policy](docs/06_REDACTION_POLICY.md)
8. [Examples](docs/07_EXAMPLES.md)
9. [Harness Runtime](docs/08_HARNESS_RUNTIME.md)
10. [Meta Fixtures](docs/09_META_FIXTURES.md)
11. [Completion Boundary](docs/10_COMPLETION_BOUNDARY.md)

## Core Principle

A claim may only rise to the level directly supported by evidence. Existence is not implementation. Implementation is not runtime operation. Runtime operation is not verification. Verification is not purpose satisfaction. Purpose satisfaction is not release readiness.

## Public Packet

Use `schemas/public-judgment-packet.schema.json` for structured reviews.

See `examples/software-feature-review.json` and `examples/research-direction-review.json` for safe public examples.

## Local Checks

Run the public safety scan before publishing changes:

```bash
python3 harness/public_safety_scan.py .
python3 harness/validate_public_packet.py schemas/public-judgment-packet.schema.json examples/software-feature-review.json examples/research-direction-review.json fixtures/meta/valid_pass_scoped.json
python3 harness/run_meta_fixtures.py
```

This scan checks for common public-leak risks such as absolute local paths, credentials, private-key blocks, environment files, and obvious secret-like tokens. It does not contain or publish private project-specific names.
