# Verdict System

## Final Verdicts

### PASS_SCOPED

The claim passes inside the declared scope. This does not imply global completion or release readiness.

### HOLD_EXACT_BLOCKER

The claim is not contradicted, but a required condition is missing. The blocker must be exact.

### FAIL_CONTRADICTED

The claim is contradicted by evidence, logic, missing contract, invalid transition, failed fixture, or boundary collapse.

### REJECT_OVERCLAIM

The claim attempts to rise above its evidence level.

### REDACTION_REQUIRED

The material may be structurally useful but is not safe to publish.

## Required Report

```yaml
target:
scope:
not_scope:
purpose:
claims:
highest_passed_level:
first_blocking_level:
blocking_reason:
evidence_class:
evidence:
gate_results:
forbidden_promotion_clean:
forbidden_promotion_findings:
redaction_clean:
redaction_findings:
required_next_action:
final_verdict:
```

## No-Overclaim Rule

The final report must state what is not proven. Missing proof is not failure by itself, but it blocks promotion.
