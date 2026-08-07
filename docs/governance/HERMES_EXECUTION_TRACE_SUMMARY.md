# Hermes Execution Trace Summary

Status: candidate subordinate contract.

Issue: #563.

Dependency: execution-preparation convergence merged through PR #567.

This document defines an optional, bounded technical summary attached to the existing Runtime Return. It does not create a new execution object, graph authority, runtime, scheduler, queue, Evidence object, Decision or Work Issue state owner.

```text
Launch Context Snapshot
→ Hermes executes externally
→ Runtime Return
  └─ optional execution_trace_summary
```

## Purpose

The summary answers one narrow technical question:

> What execution facts were observed or reported between the immutable launch snapshot and the candidate return?

It does not decide whether the result is true, professionally valid, approved or admissible as Evidence.

```text
execution_trace_summary != Evidence
trace complete != result true
tool success != professional validation
runtime_reported != independently_observed
runtime success != Work Issue resolution
```

## Existing owners

The summary remains subordinate to:

- `HERMES_EXECUTION_ADMISSION_BRIDGE.md` for execution admission and return doctrine;
- `HERMES_RUN_LAUNCH_JUNCTION.md` for reservation and run correlation;
- `schemas/work_issue_slice.schema.yaml` for the persisted Work Issue/HermesRun slice;
- `pantheon-mvp` for executable Runtime Return validation and persistence;
- the external Hermes binding for runtime observation and normalization.

The convergence map merged through PR #567 confirms that no intermediate execution-plan owner is required.

## Minimal first slice

The first slice contains only:

```text
correlation
runtime identity
terminal execution counters
tool usage summary
observed limits
structured refusals
trace references
provenance groups
```

It excludes prompts, hidden reasoning, full tool payloads, arbitrary logs, source binaries, conversation history, a universal DAG, replay state, checkpoint state and provider/model routing decisions.

## Candidate shape

```yaml
execution_trace_summary:
  schema_version: hermes-execution-trace-summary-v1
  correlation:
    admission_id: admission-...
    launch_reservation_id: launch-reservation-...
    snapshot_id: launch-snapshot-...
    snapshot_digest: sha256:...
    run_id: run-...
  runtime:
    implementation: hermes-agent
    version: 0.20.0
    profile: pantheon-governed
  execution:
    started_at: 2026-08-07T00:00:00Z
    ended_at: 2026-08-07T00:00:05Z
    terminal_status: completed
    step_count: 3
    tool_call_count: 2
    retry_count: 0
    repair_count: 0
  tools:
    - tool_id: pantheon_context_manifest
      call_count: 1
      terminal_status: completed
  limits:
    max_steps: 12
    observed_steps: 3
    timeout_seconds: 180
    timed_out: false
  refusals:
    - code: context_entity_not_admitted
      count: 1
  trace_refs:
    - hermes://runs/run-...
  provenance:
    pantheon_observed:
      - correlation.admission_id
      - correlation.launch_reservation_id
      - correlation.snapshot_id
      - correlation.snapshot_digest
      - correlation.run_id
    binding_observed:
      - execution.started_at
      - execution.ended_at
      - execution.retry_count
    runtime_reported:
      - execution.step_count
      - execution.tool_call_count
      - tools
```

## Correlation rules

`pantheon-mvp` must verify every authoritative identity against persisted state:

```text
body admission_id == route admission_id
body run_id == route run_id
launch_reservation_id belongs to admission_id
snapshot_id belongs to launch_reservation_id
snapshot_digest equals persisted digest
run_id belongs to the consumed admission
```

A foreign or mismatched identity is refused atomically. The binding locks these values from launch receipts and bridge responses; the model must not generate or rewrite them.

## Runtime identity

The runtime block records the technical implementation observed for this run. It does not select, approve or adopt that runtime.

```text
runtime observed != runtime approved
profile qualified != task authorized
implementation available != dependency adopted
```

The first slice targets the reviewed Hermes implementation `0.20.0` and the named `pantheon-governed` profile when those facts are available from qualified launch posture.

## Counters, tools and limits

Counters are non-negative and bounded. Missing differs from zero. Tool usage is a summary, not a complete trace. Full arguments and outputs remain external.

A tool identifier outside the surface qualified before reservation must be refused or recorded as an explicit trace inconsistency.

```text
tool called != effect authorized
tool completed != result valid
tool available != capability adopted
```

The first slice may record maximum and observed steps, timeout configuration and whether timeout occurred. Token or cost fields require a demonstrated stable source and unit before addition.

## Refusals

Refusals are bounded technical denials, not Evidence or automatic proof of malicious intent. The first justified code is:

```text
context_entity_not_admitted
```

Any new refusal code requires a corresponding executable path and test.

## Trace references

`trace_refs` points to detailed external traces without embedding them.

```text
trace ref != trace content
trace content != Evidence
trace availability != result truth
```

The optional summary does not replace the existing normalized-return `trace_refs`.

## Provenance

Provenance is mandatory whenever the summary is present. Included field paths are grouped by source:

```text
pantheon_observed
binding_observed
runtime_reported
```

A path must not appear in more than one group in the first slice.

- `pantheon_observed`: verified from authoritative Pantheon state or bridge events.
- `binding_observed`: directly observed by the external binding.
- `runtime_reported`: supplied by Hermes about its internal execution.

No field becomes `pantheon_observed` merely because it arrived through a Pantheon endpoint.

## Partial summaries

The summary is optional during migration and may be partial. Missing information is omitted rather than invented. Exact correlation and provenance remain required for every included fact.

```text
summary absent != run invalid
summary partial != run failed
summary complete != result accepted
```

## Bounds

The executable schema must define explicit ceilings. Initial maxima:

```text
tools: 100
refusals: 100
trace_refs: 100
provenance paths per group: 200
string identifiers: 300 characters
```

`pantheon-mvp` may adopt stricter limits.

## Persistence

The first implementation persists the summary with the existing Hermes Runtime Return/HermesRun record, preferably within the current JSON return payload. A separate table or aggregate requires demonstrated query, integrity or retention needs.

```text
new field != new aggregate
```

## Required validation sequence

1. merge the candidate contract and examples;
2. extend only the existing `normalized_hermes_return` schema;
3. add failing `pantheon-mvp` correlation and bound tests;
4. implement validation and persistence;
5. produce the summary from the existing one-shot Hermes binding;
6. verify the governed Hermes 0.20.0 synthetic run;
7. add a Cockpit projection only after the executable contract stabilizes.

## Required tests

```text
foreign admission_id -> refused
foreign run_id -> refused
foreign launch reservation -> refused
foreign snapshot id or digest -> refused
negative counter -> refused
oversized collection -> refused
unqualified tool id -> refused or explicit inconsistency
false Pantheon-observed provenance -> refused
valid partial summary -> accepted
summary absent during migration -> accepted
valid complete summary -> persisted
runtime success -> no Work Issue closure
runtime success -> no Evidence, Decision or Knowledge creation
```

## Reference distillation

The contract distills bounded patterns only:

- Microsoft Conductor: deterministic status/limit reporting and pre-execution validation;
- Open Multi-Agent: stable run identity, executed-tool summaries and trace provenance;
- Docker Agent: possible future immutable artifact identities.

No external runtime or dependency is adopted.

## Final rule

```text
Pantheon qualifies the technical receipt.
Pantheon does not become the runtime.
Hermes reports or exposes execution facts.
The binding distinguishes observation from report.
The human decides consequential meaning.
```
