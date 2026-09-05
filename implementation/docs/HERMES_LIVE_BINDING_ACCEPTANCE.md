# Hermes Live Binding Acceptance

Status: operator-only external acceptance candidate — implemented / not run against a live target / activation not authorized.

Date: 2026-07-26

## Purpose

This document defines the first live target proof for the governed Hermes Runs binding already merged into this external executable repository.

It is deliberately an acceptance helper, not an installer, activator, scheduler, queue, retry worker, provider router, plugin manager, approval engine or production runbook.

```text
source/API contract reviewed
!= target installation proven

target test pass
!= production adoption
```

## Upstream contract basis

Current Hermes API documentation exposes:

```text
GET  /v1/capabilities
GET  /v1/toolsets
POST /v1/runs
GET  /v1/runs/{run_id}
GET  /v1/runs/{run_id}/events
```

Current Hermes source also maps a supplied Runs API `session_id` to the `task_id` passed to `run_conversation`.

That source review materially reduces uncertainty but is not a live deployment proof.

The target acceptance therefore still verifies:

```text
run status session_id == Pantheon admission_id
Pantheon context tools are actually exposed
Pantheon context tools are actually invoked
out-of-scope entity read is refused
active context closes after governed return
```

## Operator helper

```text
scripts/hermes_live_binding_acceptance.py
```

Default mode is observation only.

It reads:

```text
Hermes GET /v1/capabilities
Hermes GET /v1/toolsets
```

and produces no runtime effect.

A live synthetic run requires all of:

```text
--run-live
--ack SYNTHETIC_ONLY
--admission-id admission-...
--idempotency-key <operator-chosen unique key>
```

The helper never creates an Execution Admission itself. The operator must prepare the synthetic Work Issue / Task Contract / Context Pack / admission through the governed path first.

## Synthetic admission guard

Before reserving any launch, the helper re-reads the immutable Execution Envelope and refuses unless:

```text
question contains PANTHEON_HERMES_LIVE_ACCEPTANCE_V1
root entity_id contains "synthetic"
question explicitly requests pantheon_context_manifest
question explicitly requests pantheon_context_entity
Runs API status = compatible
concrete Hermes tool surface = qualified
```

A suitable synthetic question is conceptually:

```text
PANTHEON_HERMES_LIVE_ACCEPTANCE_V1
Call pantheon_context_manifest first.
Then call pantheon_context_entity for the synthetic root entity returned by the manifest.
Summarize only this synthetic context.
```

No professional/real dossier should be used for this proof.

## Reviewed tool surface

Without an explicit `--allowed-tool`, the helper accepts the reviewed Pantheon
context plugin surface:

```text
pantheon_context_manifest
pantheon_context_entity
pantheon_untrusted_read
pantheon_untrusted_search
```

Only the two context tools remain required for the synthetic context-binding
acceptance:

```text
pantheon_context_manifest
pantheon_context_entity
```

The guarded read/search tools are allowed because they are part of the installed
reviewed plugin surface, but the synthetic acceptance does not have to invoke
them. Additional tools outside this four-tool surface must still be named
individually with repeated `--allowed-tool` arguments and therefore remain an
operator-reviewed expansion.

```text
allowed tool != required tool
plugin installed != profile qualified
profile reachable != safe
prompt says read-only != tool authority removed
```

## Live sequence

```text
read-only Runs/toolset observation
        ↓
validate synthetic immutable Execution Envelope
        ↓
ExternalHermesRunBinding.launch()
        ↓
immutable launch reservation
        ↓
REPEATABLE READ Launch Context Snapshot
        ↓
exactly one Hermes POST /v1/runs
        ↓
real run_id
        ↓
Pantheon start registration
        ↓
Hermes run status session echo check
        ↓
Pantheon active-context manifest check
        ↓
intentional out-of-scope entity probe -> must be refused
        ↓
read one finite Hermes /events SSE stream
        ↓
require tool.started + tool.completed for both context tools
        ↓
read terminal Hermes status
        ↓
explicit one-shot reconciliation when completed/failed
        ↓
active-context must be closed after governed return
```

The helper does not poll in the background.

## PASS criteria

A target proof is `pass` only when every required check is true:

```text
Runs API compatible
tool surface qualified
status.session_id == admission_id
synthetic root present in active manifest
out-of-scope entity read refused by exact Context Pack boundary
pantheon_context_manifest started and completed without error
pantheon_context_entity started and completed without error
Hermes runtime completed
Pantheon return reconciled
active-context closed after return
```

## FAIL and INCONCLUSIVE

`fail` means a completed observation contradicts the required boundary, for example:

```text
session echo mismatch
unexpected or missing tool surface
required context tool never called
required context tool returned error
out-of-scope read unexpectedly succeeded
runtime failed instead of completed
active context remained readable after governed return
```

`inconclusive` is used when the transport proof is incomplete, notably when the SSE event stream cannot be observed completely.

```text
inconclusive != pass
```

## Runtime approval behavior

If Hermes emits an `approval.request`, the helper does not answer it.

```text
acceptance helper != approval actor
```

A run that waits for runtime approval therefore remains operator-visible and does not become a hidden automatic approval path.

## Ambiguous launch behavior

The existing Run Binding already refuses automatic retry after an uncertain `POST /v1/runs` result.

The acceptance helper preserves that rule.

It also never calls `/stop` automatically after a failed acceptance check because a stop is a separate runtime effect and may itself have governance consequences.

```text
acceptance failed
!= automatic retry instruction
!= automatic stop instruction
```

## Credentials

Prefer environment variables:

```text
HERMES_API_BASE
HERMES_API_SERVER_KEY
PANTHEON_HERMES_API_BASE
PANTHEON_HERMES_API_KEY
```

The helper does not print either API key in its receipt.

Example observation only:

```bash
HERMES_API_SERVER_KEY='***' \
python scripts/hermes_live_binding_acceptance.py \
  --hermes-url http://hermes:8642
```

Example synthetic live proof:

```bash
HERMES_API_SERVER_KEY='***' \
PANTHEON_HERMES_API_KEY='***' \
python scripts/hermes_live_binding_acceptance.py \
  --run-live \
  --ack SYNTHETIC_ONLY \
  --admission-id admission-... \
  --idempotency-key live-proof-2026-07-26-001
```

This command candidate assumes the operator has separately installed/configured the reviewed Hermes profile and plugin. The helper does not perform those actions.

## Receipt semantics

The JSON receipt always includes:

```text
synthetic = true
technical_receipt_is_evidence = false
activation_changed = false
production_authorization = false
```

A live receipt additionally records bounded observations such as:

```text
run_id
session echo check
context-tool event assessment
out-of-scope refusal check
one-shot reconciliation result
target_binding_status = pass | fail | inconclusive
```

No secrets are intentionally projected.

## Responsibility allocation

### Pantheon governs

- the pre-existing Work Issue / Task Contract / Context Pack;
- Execution Admission;
- launch reservation and snapshot meaning;
- exact context boundary;
- runtime observation meaning;
- later consequential-effect gates;
- Evidence / Knowledge / Decision boundaries.

### Hermes executes

- the actual synthetic run;
- its configured provider/model selection;
- the reviewed Pantheon plugin tools exposed by the qualified profile;
- the two required context tools when the synthetic prompt calls them;
- runtime status/events/output.

### External acceptance helper executes

- read-only API/toolset observation;
- one explicitly acknowledged synthetic launch through the already-governed binding;
- finite event observation;
- negative scope probe;
- one-shot terminal reconciliation.

It owns no queue, schedule, autonomous monitor or retry loop.

### Human approves

- creation of the synthetic Work Issue/admission;
- explicit `SYNTHETIC_ONLY` launch acknowledgement;
- any future plugin/profile installation, enablement or activation;
- any future real-dossier authorization.

### Forbidden

- real professional dossier in the first live proof;
- automatic plugin installation or enablement;
- automatic runtime approval;
- automatic retry after ambiguous submission;
- automatic stop as a reaction to acceptance failure;
- global Agency Data access;
- source binary dereference through context tools;
- acceptance pass being treated as Evidence or production authorization.

## Current status

```text
operator acceptance helper        implemented candidate
unit tests                         implemented candidate
upstream session->task mapping     source reviewed
live target proof                  not run
plugin installation                not performed by this helper
plugin enablement                  not performed by this helper
activation                         not authorized
real-dossier use                   forbidden for first proof
```

## Final rule

```text
A synthetic live acceptance can prove that the selected external binding behaves
as reviewed on one target.

It cannot approve itself.
It cannot activate itself.
It cannot convert runtime success into Evidence.
```
