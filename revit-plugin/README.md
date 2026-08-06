# Revit Local Adapter Reference Skeleton

Status: non-executable reference skeleton — documented non-implemented.

Canonical boundary: `../docs/governance/REVIT_LOCAL_ADAPTER.md`.

This directory is a reference layout for a future external Revit add-in and local Host Agent. It is not the Pantheon governance kernel and it does not currently contain a compiling add-in, `.addin` manifest, Revit command, Host Agent, relay, MCP server, installer or runnable integration.

```text
Pantheon Next governs contracts and status.
pantheon-mvp persists project, task, authorization and result state.
Hermes may orchestrate an admitted métier workflow.
A local Host Agent adapts transport.
The external Revit add-in executes inside Revit.
Cockpit exposes preflight and review.
The human decides consequential effects.
```

## Product scope

The initial product scope follows the responsibilities of the architect:

```text
architecture and spatial design
economy and quantities
construction-site review
thermal-data preparation and RE2020 consistency
ACV and carbon analysis
```

Structure, HVAC, plumbing and electrical systems may be observed as context, but their detailed design and professional dimensioning are outside the first scope.

## Full-local requirement

The primary path must remain operable without Internet access and without Autodesk-hosted execution services.

```text
Autodesk Assistant is not required
Autodesk Public MCP is not required
APS is not required
a cloud LLM is not required
a hidden remote fallback is forbidden
```

## Code-hosting boundary

Production add-in and Host Agent code should live in a dedicated implementation repository.

This skeleton may illustrate contracts, DTOs and fixtures only. Its presence does not adopt a binding or authorize this repository to become a runtime, installer, scheduler, queue, provider router or plugin manager.

## Current reference content

```text
revit-plugin/
  README.md
  STATUS.md
  docs/
    ARCHITECTURE.md
    EXECUTION_MODEL.md
    KNOWLEDGE_SOURCE_POLICY.md
    PYTHON_AND_GENERATED_SNIPPETS.md
    CONTEXT_PACK_CONTRACT.md
    ACTION_LOG_CONTRACT.md
  src/.gitkeep
  tools/python/README.md
  samples/
    context-pack.example.json
    action-log.example.jsonl
```

## Contract map

```text
ARCHITECTURE.md
-> components, interface boundaries, capability registry and local exposure

EXECUTION_MODEL.md
-> execution states, read/write flows, freshness, idempotency and refusal

CONTEXT_PACK_CONTRACT.md
-> Revit Context Snapshot specialization

ACTION_LOG_CONTRACT.md
-> operation request, preflight, action authorization and technical report
```

The generic governance owners remain:

```text
Module Manifest
Capability Passport or generalized capability record
Workflow Manifest
Task Contract
Context Pack
DecisionRequest
Decision record
ChangeCandidate
Execution Result
Result Candidate
Evidence Pack Candidate
Capability Gap
```

## Binding metadata

Product version, .NET target, packaging method and Revit API compatibility are binding metadata. They are not part of the architecture identity.

The reference target must not be treated as adopted until a real implementation repository, package identity and compatibility matrix exist.

## First admissible proof

```text
read the active document and view
read the explicit selection
publish a closed capability manifest
produce a bounded Revit Context Snapshot
return a local technical trace
refuse stale or out-of-scope work
perform no model mutation
```

Any writable proof requires:

```text
a reviewed write capability
a fresh preflight
an exact ChangeCandidate
a single-use authorization
a named Revit transaction
changed-element journaling
rollback or manual-reversal posture
separate result review
```

```text
compiled != installed
installed != approved
locally_enabled != task_authorized
loaded != activated
transaction_success != accepted_result
runtime_success != Evidence
```

## Planning boundary

This directory documents the target contract and interface shape only. It does not define implementation order, dates or release milestones.
