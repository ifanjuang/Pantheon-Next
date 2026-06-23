# AI Log — Communication Pattern Registry

Date: 2026-06-23  
Actor: ChatGPT  
Scope: template registry / documented non-implemented

## Task

The user agreed to create a minimal registry for architecture communication patterns.

## Change made

Added:

```text
templates/architecture_probative_instruction/communication_patterns/00_index/registry.md
```

## What the registry does

The registry records communication pattern candidates created from architecture probative instruction work.

It is not a library of approved emails and does not authorize external transmission.

Initial entries include:

```text
PAT-COMM-0001 — Project-owner role boundary reminder
PAT-COMM-0002 — Contractor open-items source request
PAT-COMM-0003 — Role-chain reminder MOA / MOE / contractor
PAT-COMM-0004 — Pre-reception open-items reminder structure
PAT-COMM-0005 — PRO / DCE non-EXE footer candidate
PAT-COMM-0006 — PRO / EXE boundary mail candidate
PAT-COMM-0007 — Internal professional-risk review cartouche
PAT-COMM-0008 — Rejected: vague validation wording
```

## Accepted

```text
- Create a lightweight index rather than a full library of ready-to-send mails.
- Mark patterns as candidate-only.
- Preserve source_basis, risk level and external_gate for every row.
- Include a rejected pattern bucket to prevent unsafe reuse.
```

## Refused

```text
- No automatic mail generation.
- No external send.
- No legal advice.
- No insurer advice.
- No project record.
- No memory promotion.
- No runtime, schema, tests, operations, platform, Docker, .env or pyproject change.
```

## To verify

```text
- Add one metadata file per registered pattern before reuse.
- Convert only reviewed recurring drafts to pattern_candidate.
- Keep project-specific drafts as draft_candidate.
- Move unsafe formulations to rejected_or_obsolete with rejection reason.
```

## Repo state

Documented non-implemented.

Candidate registry only.
