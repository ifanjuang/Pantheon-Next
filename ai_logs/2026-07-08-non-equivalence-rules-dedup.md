# Non-equivalence rules dedup pass

Date: 2026-07-08

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Context

After adding boundary profiles, the next repeated pattern was the recurring list of status-collapse warnings:

```text
schema_valid != approved
runtime_success != evidence
installed != approved
healthy != safe
retrieved != truth
template != implementation
```

These distinctions are central, but copying long lists into every document creates drift.

## Change

Added:

```text
docs/governance/NON_EQUIVALENCE_RULES.md
```

Updated:

```text
CONTRIBUTING.md
docs/governance/BOUNDARY_PROFILES.md
docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md
```

## Decision

Use `NON_EQUIVALENCE_RULES.md` as the canonical reference for recurring “X does not mean Y” distinctions.

Documents should repeat only the distinctions that are locally material.

## Boundary

Documentation only.

This change adds no:

```text
schema
test
CI workflow
runtime code
OpenWebUI Function / Pipe / Filter / Action
Hermes skill or contract
approval engine
memory promotion
scheduler
queue
provider router
external action authorization
```

## Preserved distinctions

```text
non_equivalence_rule != review
canonical_list != automatic gate
trace != doctrine
schema_valid != approved
runtime_success != evidence
```
