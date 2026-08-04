# Hermes distribution composition lock

Date: 2026-08-04

Status: candidate implementation/deployment composition — non-authoritative.

## Purpose

The Hermes integration already contains independently owned components:

```text
external run binding
bounded context bridge plugin
Runs API observer
selected skills
optional policy MCP
optional dashboard
```

This change records one reproducible composition without merging those components into a new runtime, installer, plugin manager or authority layer.

## Candidate lock

```text
hermes/distribution/pantheon-standard.lock.yaml
```

The lock pins exact reviewed commits for `Pantheon-Next` and `pantheon-mvp`, records the observed Hermes runtime family, lists required and optional components, and declares the acceptance checks that a deployment must pass.

The required operational core is:

```text
run_binding
context_bridge
runtime_observer
```

Skills, policy MCP and dashboard remain separately reviewable and default-off.

## Validation

`tools/check_hermes_distribution_lock.py` validates:

- the `Pantheon-Next` distribution-lock schema;
- unique component identities;
- component paths inside the two checked-out repositories;
- required core component kinds;
- default-off posture;
- mandatory static, route, end-to-end and no-authority checks;
- stable internal Pantheon route identities;
- preserved upstream Hermes `/v1/runs` protocol;
- absence of authority claims.

The cross-repository architecture workflow now publishes the resulting factual report beside the existing architecture and module-usage inventories.

## Composed acceptance

`tests/test_hermes_distribution_acceptance.py` joins the real `ExternalHermesRunBinding` and the real `pantheon-context-bridge` handlers with deterministic external fakes. It verifies one admitted read-only launch, exact context access and candidate return.

It explicitly verifies:

```text
automatic_retry_performed = false
provider_routing_performed = false
technical_receipt_is_evidence = false
result_accepted = false
evidence_admitted = false
project_mutated = false
```

## Boundaries

```text
composition pinned != components installed
components installed != binding activated
acceptance passed != task authorized
launch reservation != runtime dispatch
runtime return != accepted result
runtime output != Evidence
```

The lock is not a scheduler, queue, provider router, installer, plugin manager, memory system, approval engine or source of truth.
