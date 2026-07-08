# MVP Prevalidator Readiness

Status: readiness note — documented non-implemented.

Date: 2026-07-08

This note consolidates the decisions that must be true before a local validator implementation may be attempted.

It adds no validator, command, CI workflow, runtime, database mapping, OpenWebUI feature, Hermes contract, approval engine or memory promotion.

## Ready for local/manual validator design

The following are now present:

```text
positive schema-target fixture
expected positive report
deliberate failing fixture
expected blocked report
central governance invariants
report vocabulary
Source Manifest / Retrieval Trace placement decision
local validator design
```

## Still not ready for CI

CI is still premature.

Missing before CI:

```text
actual local validator implementation
manual run report committed or attached
review of first validator output
status enum proposal based on real failures
alias equality policy implementation decision
```

## Local validator allowed scope

A future local validator may:

```text
parse YAML
validate central object schemas
check object references
check named governance invariants
emit a report
```

It must not:

```text
authorize external action
approve a draft
admit memory
write to database
call Hermes
call OpenWebUI
run as scheduler
block merges through CI
```

## Next recommended PR

The next PR may add a local/manual validator script only if it remains report-only and has no CI wiring.

Recommended title:

```text
scripts: add local MVP fixture validator
```

Required boundary in that PR:

```text
local command only
no GitHub Actions workflow
no runtime dependency adoption beyond parser/schema libraries if already acceptable
no OpenWebUI or Hermes integration
no external action
```
