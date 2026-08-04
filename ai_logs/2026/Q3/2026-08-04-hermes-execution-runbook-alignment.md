# Hermes execution runbook alignment — 2026-08-04

Status: completed documentation and validation candidate. No Hermes command was executed and no runtime was installed, configured, activated or task-authorized.

## Objective

Align the manual Hermes execution runbook with the profile and memory qualification contract merged in `pantheon-mvp`.

## Repository state checked

```text
Pantheon-Next main: bd9dc3406b1f04caa522699d9afd03cb07ded569
pantheon-mvp main: 898eb21a4cb48f8302cb32f02c3240a9867df43e
```

The MVP implementation now requires an exact named profile route, a reviewed tool allowlist and a fresh sanitized memory-status receipt before observation or launch.

## Existing runbook gaps

The previous runbook:

```text
did not require /p/<profile> in HERMES_API_BASE
did not capture the profile memory posture
did not pass --expected-profile or --memory-status-receipt
did not repeat the tool policy on launch
listed tool qualification fields at the wrong result level
listed reconciliation fields that are not top-level CLI outputs
```

## Decisions applied

The runbook now requires:

```text
HERMES_GOVERNED_PROFILE=pantheon-governed
HERMES_API_BASE ending in /p/pantheon-governed
one memory receipt before observation
one fresh memory receipt immediately before launch
receipt age <= 300 seconds
exact allowlist and required tools on observe and launch
no X-Hermes-Session-Key
explicit nested result paths
separate inspection of the recorded Pantheon API response
```

The memory capture must run in an environment where the Hermes CLI resolves the exact target profile home. A receipt from another profile, host or configuration is not interchangeable.

## Reconciliation correction

The top-level reconciliation receipt establishes only technical recording behavior such as:

```text
pantheon_return_recorded
scheduler_effect
retry_effect
technical_receipt_is_evidence
```

Any bounded Pantheon API response is carried under `recorded`. Runtime success or return recording does not establish result acceptance, Evidence admission or Project mutation.

## Validation

The existing Hermes distribution contract test now checks:

```text
two exact memory captures
profile route and no trailing /v1
required observe arguments
required launch arguments
nested tool and memory fields
five-minute freshness
absence of obsolete top-level result assertions
non-authority boundaries
```

## Non-effects

```text
no runtime
no installation
no profile configuration
no memory mutation
no external action
no activation
no task authorization
no Evidence admission
```
