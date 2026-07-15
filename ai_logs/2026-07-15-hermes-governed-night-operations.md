# Hermes governed night operations

Date: 2026-07-15

Status: validation-only trace — dashboard observation and non-executable
operations template implemented; no schedule created or executed.
Boundary profile: validation_only_trace.

## Change

- Added a bounded night-operations template for backup preflight, PDF ingestion
  and scoped vectorization, retrieval quality, memory consolidation review,
  contradiction/drift review and a local morning digest.
- Added live read-only observation of native Hermes Cron jobs to the Pantheon
  Modules dashboard.
- Required explicit runtime timezone, profile, workdir, input/output scope and
  finite trial/expiry before a recurring operation can be considered ready.
- Kept schedule creation outside the plugin because the audited native Hermes
  dashboard create API does not expose a finite repeat or expiry field.
- Fixed the dashboard refresh list so the MCP catalog is read once rather than
  twice.

## Why

The operator needs understandable timings and an action list without turning a
dashboard card into an unbounded unattended execution loop. Hermes already owns
Cron and reports job state. The safest compatible first increment is therefore:

```text
Pantheon template proposes a bounded operation
→ Hermes native Cron state is observed
→ human reviews runtime-specific activation outside this plugin
```

## Upstream verification

Hermes Agent commit `8b209e0dd7b8e308d5b923fa80f7a72f71042636`
was inspected on 2026-07-15.

Observed native dashboard support:

```text
GET /api/cron/jobs
POST /api/cron/jobs
POST /api/cron/jobs/{id}/pause
POST /api/cron/jobs/{id}/resume
POST /api/cron/jobs/{id}/trigger
DELETE /api/cron/jobs/{id}
```

The create payload exposes schedule, prompt, profile, workdir, skills, model,
provider, script and toolsets, but not the core `repeat` limit. Hermes Cron
itself supports finite `repeat` through other native paths. The plugin therefore
observes jobs and links to native Cron but does not create recurring jobs.

Hermes documentation also states that jobs use the host's local timezone. The
template leaves `runtime_timezone` required rather than assuming the browser or
operator timezone matches the host.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: tests only, with explicit user authorization to
continue the dashboard work.
Runtime impact: external dashboard read path only after installation; no
Pantheon runtime, scheduler or backend.
Authority impact: none; action entries remain operator-review-required
candidates.
Schema/test/CI impact: additive template and dashboard contract tests; no schema
or CI change.
External action: no Hermes job, adapter, memory operation, index write, backup,
notification or schedule was created, changed or run.
Memory behavior: consolidation produces review candidates only; deletion,
automatic merge, canonicalization and Registre Probatoire promotion stay
forbidden.
