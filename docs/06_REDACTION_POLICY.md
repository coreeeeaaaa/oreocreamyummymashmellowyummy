# Redaction and Publication Policy

This policy prevents public documentation from exposing private systems.

## Public-Safe Content

- Generic process
- Generic review packets
- Generic examples
- Generic gate definitions
- Public maturity levels
- Public schemas
- Public fixture categories

## Public-Unsafe Content

- private project names
- private repository names or local paths
- private architecture maps
- private prompts
- private datasets
- credentials or tokens
- secrets, cookies, keys, certificates
- raw operational logs
- unpublished verifier internals
- private traces, witnesses, memory, or fixture records

## Redaction Procedure

1. Identify whether the file is meant for public release.
2. Remove private names and private paths.
3. Replace private examples with generic examples.
4. Remove raw logs and traces.
5. Remove secrets and credentials.
6. Run `harness/public_safety_scan.py`.
7. If any issue remains, do not publish.

## Redaction Is Not Completion

Redaction only makes material safer to publish. It does not prove the reviewed target is mature, implemented, verified, or release-ready.

