# Gate Sequence

The gate sequence is the operational order for applying the ladder.

## 0. Intake Normalizer

Normalize the target into a review packet. This is not a pass gate.

## 1. Scope Freeze Gate

Lock:

- target
- scope
- non-scope
- purpose
- allowed evidence
- forbidden claims

## 2. Claim Atomization Gate

Split broad claims into atomic claims.

Bad: "The system is complete."  
Good: "The parser accepts declared input set X and rejects declared invalid set Y."

## 3. Layer-Time-Modality Separation Gate

Separate:

- past, current, future
- actual, possible, counterfactual
- observed, inferred, assumed
- scoped, global
- design, implementation, runtime, verification, release

## 4. Evidence Binding Gate

Every claim must bind to evidence. If no evidence exists, the claim cannot pass.

## 5. SRVL Maturity Gate

Assign the claim to the highest supported SRVL level.

## 6. Measurement and Criteria Gate

Check whether the target has measurable objects, units, thresholds, procedures, and failure rules.

## 7. Counterexample and Boundary Gate

Test whether adversarial, negative, ambiguous, boundary, or impossible cases break the claim.

## 8. Forbidden Promotion Gate

Reject promotions such as:

- existence to implementation
- implementation to runtime
- runtime to verification
- verification to purpose satisfaction
- purpose satisfaction to release readiness
- scoped pass to global pass
- report text to runtime evidence

## 9. Repair and Re-entry Gate

If locally fixable gaps exist, repair before final verdict. If not locally fixable, record exact blocker and owner.

## 10. Public Redaction Gate

Before publication, remove private names, private paths, credentials, private architecture, raw logs, and unpublished implementation details.

## 11. Final Verdict Gate

Emit one verdict:

- `PASS_SCOPED`
- `HOLD_EXACT_BLOCKER`
- `FAIL_CONTRADICTED`
- `REJECT_OVERCLAIM`
- `REDACTION_REQUIRED`

