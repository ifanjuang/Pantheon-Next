# OpenWebUI Plugin Security Gate

Status: candidate support gate — documented non-implemented.

This document defines the minimum review package for an OpenWebUI plugin that can execute scripts, render active content, access browser storage, bridge MCP applications, call network resources or influence consequential user decisions.

It does not implement a scanner, sandbox, installer, approval engine, runtime monitor or plugin manager.

## Scope

The gate applies when a plugin can affect one or more of:

```text
browser origin;
DOM or iframe isolation;
cookies, localStorage or sessionStorage;
authenticated session state;
network egress;
MCP tools or resources;
external writes;
artifact provenance;
status or approval presentation;
retention or deletion;
model or tool defaults.
```

## Required review record

Every candidate must record:

```text
upstream_repository;
upstream_release_or_commit;
retrieved_at;
license_status;
maintenance_status;
capability_slot;
placement;
permissions;
data_classes;
network_targets;
external_effects;
install_status;
health_status;
update_status;
activation_status;
approval_status;
rollback_status;
known_limits;
review_owner;
review_date.
```

## Gates

### G0 — placement

Confirm:

```text
what Pantheon governs;
what Hermes executes;
what OpenWebUI exposes;
what the human approves;
what remains forbidden.
```

Failure condition: the plugin is described as Pantheon core, Pantheon runtime, approval authority, canonical memory or proof engine.

### G1 — provenance and supply chain

Require:

- exact repository and maintainer identity;
- pinned release or commit;
- license review;
- dependency and build-path inventory;
- update and abandonment signals;
- reproducible retrieval record when feasible.

Failure condition: unpinned mutable source, unclear license, opaque binary or undeclared installer behavior.

### G2 — browser isolation

Review:

- iframe sandbox flags;
- same-origin behavior;
- parent DOM access;
- cookie and storage access;
- postMessage origin checks;
- content security policy;
- dynamic script and event-handler execution;
- remote resource loading;
- navigation and popup behavior.

Failure condition: an untrusted artifact can reach authenticated parent context or unrestricted browser state.

### G3 — data boundary

Declare:

- accepted data classifications;
- forbidden client or professional data;
- persistence behavior;
- telemetry;
- retention;
- export and deletion behavior;
- whether plugin output may enter an Evidence Pack Candidate.

Failure condition: sensitive data handling is implicit, persistent or externally transmitted without a governed record.

### G4 — tool and MCP scope

For bridges or active tools, require:

- explicit server allowlist;
- explicit tool and resource allowlist;
- read-only, interactive and mutation modes;
- network and filesystem boundaries;
- external-write gates;
- visible active binding identity;
- unsupported-semantics reporting.

Failure condition: loading an application implicitly authorizes its tools or external effects.

### G5 — status semantics

The UI must distinguish:

```text
candidate;
to_verify;
approved_for_sandbox;
installed;
healthy;
degraded;
update_available;
active;
suspended;
rejected.
```

Failure condition: color, animation, layout or wording makes `healthy` look like `safe`, `installed` look like `approved`, or `runtime_success` look like evidence.

### G6 — sandbox benchmark

Use fictional fixtures first. Record:

- test inputs;
- expected allowed behavior;
- expected denied behavior;
- observed network calls;
- observed storage access;
- observed DOM access;
- accessibility results;
- resource consumption;
- failure and recovery behavior.

Failure condition: testing requires production credentials, client data or unrestricted tools.

### G7 — rollback

Require:

- disable path;
- uninstall path performed by the owning runtime or operator;
- configuration backup;
- artifact preservation rule;
- session recovery behavior;
- known irreversible effects;
- post-rollback verification.

Failure condition: the plugin cannot be disabled without losing governed records or exposing OpenWebUI to an unrecoverable state.

### G8 — human approval

Approval floor:

```text
sandbox installation: human approval;
project activation: human approval;
production activation: human approval;
permission expansion: human approval;
external-write enablement: human approval;
breaking or security-sensitive update: human approval.
```

The review package may support a decision. It does not make the decision automatically.

## Decision outputs

The gate may produce only:

```text
External Binding Review Candidate;
Threat Model Candidate;
Sandbox Test Report Candidate;
Installation Proposal;
Activation Proposal;
Update Review Candidate;
Rollback Plan Candidate;
Capability Gap.
```

It must not produce:

```text
proof of safety;
automatic approval;
automatic installation;
automatic activation;
automatic update;
canonical memory;
professional validation.
```

## Initial application

For `Classic298/Inline Visualizer v2`:

```text
placement: OpenWebUI display binding
current_gate: G1-G3 review required
installation: not proposed
activation: unavailable
next_action: bounded threat model plus fictional fixture
```

For `Classic298/MCP App Bridge`:

```text
placement: OpenWebUI MCP application bridge
current_gate: G1-G5 review required
installation: not proposed
activation: unavailable
next_action: remain watchlist until same-origin, session and MCP scope isolation are demonstrated
```

## Final rule

```text
A plugin may be useful without being safe.
A plugin may be installed without being approved.
A plugin may be healthy without being authorized.
OpenWebUI exposes.
Hermes executes.
Pantheon governs.
The human decides.
```