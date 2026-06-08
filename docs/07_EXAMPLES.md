# Examples

These examples are intentionally generic.

## Software Feature

Target: import button for a note app.

Possible verdict:

```yaml
highest_passed_level: L10
first_blocking_level: L11
blocking_reason: integration boundary with storage and file parser not closed
final_verdict: HOLD_EXACT_BLOCKER
```

Reason: the feature is designed, but not integration-ready or runtime-proven.

## Research Direction

Target: a new method for evaluating uncertain decisions.

Possible verdict:

```yaml
highest_passed_level: L7
first_blocking_level: L8
blocking_reason: symbols and operational meaning are not yet bound to observable cases
final_verdict: HOLD_EXACT_BLOCKER
```

Reason: the method is logically coherent but not semantically bound to examples and evidence.

## Business Plan

Target: subscription product for a small market.

Possible verdict:

```yaml
highest_passed_level: L6
first_blocking_level: L7
blocking_reason: revenue assumptions and retention assumptions conflict under declared pricing
final_verdict: FAIL_CONTRADICTED
```

Reason: contracts exist, but composition creates a contradiction.

