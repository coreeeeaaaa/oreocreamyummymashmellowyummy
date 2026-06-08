# Public Boundary

This repository is intentionally generic.

## Allowed

- Public judgment procedures
- Generic maturity ladders
- Generic gate contracts
- Generic public schemas
- Generic examples
- Redaction and publication rules
- Review templates that do not expose private systems

## Forbidden

- Private project names
- Private architecture details
- Private prompts or hidden system instructions
- Private datasets or source documents
- Private repository paths
- Local filesystem paths
- Credentials, tokens, cookies, keys, or secrets
- Deployment configuration
- Private verifier details
- Internal trace, witness, fixture, or memory records
- Any claim that this public harness proves a private system is complete

## Separation Rule

This public repository may define how to judge a claim. It must not reveal the private object being judged unless that object is intentionally public.

Public procedure is allowed. Private implementation detail is not.

## Publication Rule

Before publishing, every added file must be checked for:

- private identity leakage
- local path leakage
- credential leakage
- private architecture leakage
- raw log or trace leakage
- false completion claims
- release readiness overclaim

If any of these are present, the file must be held, redacted, or removed from the public packet.

