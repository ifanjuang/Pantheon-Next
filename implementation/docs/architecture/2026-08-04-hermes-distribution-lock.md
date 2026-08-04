# Hermes distribution composition lock

Date: 2026-08-04

Status: candidate implementation/deployment composition — non-authoritative.

## Purpose

The Hermes integration keeps independently owned components while recording one reproducible operational core:

```text
external run binding
bounded context bridge plugin
Runs API observer
```

Skills, policy MCP and dashboard remain available candidates in `Pantheon-Next`, but are not included in `pantheon-standard.lock.yaml` until explicitly selected. The lock is a composition, not a catalog.

## Integrity contract

The lock now follows `pantheon.hermes_distribution_lock` revision 2.

It records:

- reviewed `Pantheon-Next` and `pantheon-mvp` source revisions;
- exact SHA-256 content digests for every selected component;
- deterministic `file` or `tree` digest modes;
- an exact Hermes version target;
- a nullable Hermes artifact digest while no real installation has been observed.

Repository refs provide provenance. Exact component identity is established by content digests because a lock stored inside `pantheon-mvp` cannot contain the future SHA of its own final commit.

```text
source revision recorded != final self-containing commit
component digest matched != component installed
runtime version reviewed != runtime artifact observed
```

## Shared validator

`mvp_vertical/hermes_distribution.py` owns:

- schema validation;
- repository-root containment;
- deterministic file and tree digests;
- required core component checks;
- stable route checks;
- non-authority checks.

`tools/check_hermes_distribution_lock.py` remains a compatibility wrapper for CI. The architecture workflow validates against `Pantheon-Next/main` and publishes a factual JSON report.

## One-shot operator CLI

The packaged command is:

```text
pantheon-hermes
```

Supported operations:

```text
verify-distribution
observe
launch
reconcile
```

The CLI exposes existing bounded classes only. It owns no daemon, queue, scheduler, polling loop, automatic retry, provider router, model selection, installation, activation or approval.

`launch` performs one sequence:

```text
observe reviewed Hermes surface
→ reserve one admitted launch
→ submit one run
→ record the exact runtime start
→ exit
```

`reconcile` reads one launch receipt, observes the runtime once, records a terminal candidate when safely mappable and exits.

## Composed acceptance

`tests/test_hermes_distribution_acceptance.py` continues to join the real run binding and context bridge handlers with deterministic external fakes. Additional tests cover digest integrity and the one-shot CLI.

They explicitly preserve:

```text
automatic_retry_performed = false
provider_routing_performed = false
technical_receipt_is_evidence = false
result_accepted = false
evidence_admitted = false
project_mutated = false
```

## Remaining external operation

Repository tests do not prove a real Hermes installation. The operator runbook is owned in:

```text
Pantheon-Next/docs/install/HERMES_EXECUTION_BRIDGE_RUNBOOK.md
```

A real acceptance still requires the exact Hermes artifact digest, plugin installation, tool-surface qualification, host `task_id/session_id` correlation, one human-admitted read-only run and verified rollback.

## Boundaries

```text
composition pinned != components installed
components installed != binding activated
acceptance passed != task authorized
launch reservation != runtime dispatch
runtime return != accepted result
runtime output != Evidence
```

The lock and CLI are not a runtime, installer, scheduler, queue, provider router, plugin manager, memory system, approval engine or source of truth.
