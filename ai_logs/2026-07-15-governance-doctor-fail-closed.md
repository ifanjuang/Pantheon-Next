# Governance Doctor fail-closed contract

Date: 2026-07-15

Status: implemented read-only validation hardening.
Boundary profile: validation_only_trace.

## Change

- Added explicit `pass`, `fail`, `not_run` and `capability_gap` outcomes to every Doctor check.
- Added mandatory/informational classification and stable expected, evaluated, passed, failed and not-run counts.
- Made missing schemas, missing or empty required corpora, malformed YAML, invalid schemas and unavailable validators blocking.
- Made the aggregate green only when every mandatory check ran and passed.
- Aligned the register-instance and vertical-slice CI scripts with the fail-closed result.
- Added isolated regression tests for the former fail-open paths.

## Why

The previous Doctor could return green after silently skipping malformed YAML, absent schemas, empty instance corpora or unavailable validation dependencies. A read-only check is useful only if success proves that its required surface was actually evaluated.

## Evidence

```text
governing issue: #362
mandatory checks: 5
informational checks: 1
explicit outcomes: pass, fail, not_run, capability_gap
targeted regression suite: 36 passed
full MCP unittest suite: 136 passed
real repository Doctor result: pass
real repository Doctor checks: 6 evaluated, 6 passed
real repository Doctor items: 551 expected, 551 evaluated, 551 passed
register-instance CLI: pass, 5 instances
vertical-slice CLI: pass, 6 instances
governance scripts: status, links, authority index, axis vocabulary,
  truncation, registers, vertical slice and APU integrity passed
ruff lint: passed
```

## Boundary

Protected paths touched: no.
Runtime impact: read-only validation result only.
Authority impact: none; the Doctor verifies and cites but does not decide, fix or promote.
External action: GitHub documentation and code-review workflow only.
Professional data: none used or transmitted.

## Local distinctions

```text
no_handled_error != check_passed
zero_discovered != healthy
dependency_missing != informational_success
validation_passed != authorization
doctor_green != professional_proof
```
