# Hermes profile and memory observation — 2026-08-04

Status: implemented candidate on a feature branch. No target Hermes installation or live acceptance was observed.

## Objective

Extend the existing one-shot Hermes observer so a launch cannot be qualified only from API reachability and a tool allowlist.

## Governing source

Pantheon-Next main at review:

```text
278654a7804b042ac5f507242024924d8477ce47
```

The governed profile requires:

```text
explicit /p/<profile> route
external provider off
built-in MEMORY.md injection off
built-in USER.md profile injection off
memory tool off
X-Hermes-Session-Key absent
explicit tool allowlist
```

## Existing implementation checked

```text
mvp_vertical/hermes_runs_observer.py
mvp_vertical/hermes_cli.py
mvp_vertical/hermes_run_binding.py
tests/test_hermes_runs_observer.py
tests/test_hermes_cli.py
tests/test_hermes_run_binding.py
```

The previous observer read only `/v1/capabilities` and `/v1/toolsets`. It could not prove the route identity or built-in memory-injection state.

## Implemented slice

### Read-only memory capture

`pantheon-hermes capture-memory-status` invokes exactly:

```text
hermes -p <profile> memory status
```

without a shell, retry, background worker or mutation command.

The parser retains only:

```text
profile
command
exit code
capture time
output digest
external-provider state
built-in memory-injection state
built-in user-profile state
memory-tool state
qualification status
```

Raw command output is not retained.

The receipt must have the exact CLI observation source, a timezone-aware capture time and a maximum age of five minutes. Stale, future-dated, manually re-attributed or otherwise malformed receipts fail closed.

### Observer qualification

The observer now combines three independent surfaces:

```text
profile route
reviewed tool surface
fresh sanitized profile-memory receipt
```

A profile is qualified only when all three are qualified. Missing or active memory axes fail closed.

The capture and qualification remain inside the existing digest-bound `runtime-observer` component. No fourth distribution component was introduced.

The observer and Runs client send only the bearer authorization header. They do not send `X-Hermes-Session-Key`.

### CLI admission

`observe` and `launch` now require:

```text
--expected-profile
--memory-status-receipt
--allowed-tool
```

Reconciliation remains a one-shot observation of an already launched run.

## Integrity posture

The distribution remains composed of exactly:

```text
run-binding
context-bridge
runtime-observer
```

The lock digests the modified run-binding and consolidated observer files. Component composition, activation state, task authorization state and authority flags remain unchanged.

## Non-effects

```text
no daemon
no scheduler
no queue
no automatic retry
no arbitrary profile-file read
no memory deletion
no memory configuration mutation
no provider/model routing
no Evidence admission
no activation
no task authorization
```

## Remaining live proof

```text
exact Hermes 0.20 artifact digest
real named profile route
real fresh memory status capture
real OpenWebUI enrichment posture
one admitted synthetic launch
one one-shot reconciliation
```
