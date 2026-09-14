# AI Logs

Status: optional support note — historical and exceptional AI-assisted repository trace.
Boundary profile: validation_only_trace.

This directory stores validation-only traces for material AI-assisted repository interventions when the durable context would otherwise be difficult to reconstruct from the authoritative repository record.

AI logs are optional support material. They are not doctrine, approval, runtime evidence by default, workflow state, Hermes memory or a substitute for Git history, pull-request discussion, tests, schemas or owner documents.

## Default trace path

Prefer the existing authoritative record first:

```text
owner documents
+ schemas / contracts / tests
+ Git commit history
+ pull-request rationale
-> sufficient by default
```

Create a separate AI log only when a consequential boundary, external-runtime observation, consolidation/removal mapping or architectural rationale would otherwise be lost or materially ambiguous.

Target state: no skill, workflow, Hermes runtime, governance baseline or Doctor health check depends on an AI log being present. The CI baseline treats this corpus as optional; legacy Doctor coupling is tracked separately until removed and tested.

## Purpose

An AI log may preserve:

- a consequential governance change whose rationale is not already clear in the owner documents and pull request;
- a protected-path intervention and its explicit boundary when that boundary is not otherwise durable;
- an architecture decision that is not otherwise visible in the changed owner documents;
- a validation or external-runtime observation that must remain distinct from adoption;
- a consolidation or removal mapping needed to understand current placement.

## Granularity rule

Default:

```text
one coherent pull request
-> zero AI logs normally
-> at most one when exceptional trace value remains
```

A separate log is normally unnecessary when the commit, pull request, tests, schemas and owner documents already preserve the consequential understanding.

Do not create a log merely because a pull request changes doctrine, CI, tests, schemas or protected paths. Create one only when the additional trace carries durable information that those authoritative surfaces do not already preserve.

Do not split one coherent intervention into multiple logs merely because it used several commits.

## Required content

When a log is created, use `LOG_FORMAT.md` unless the intervention requires a longer audit structure.

The log should state:

- what changed;
- why the additional trace is needed beyond Git/PR/owner documents;
- the authority or repository-state effect;
- runtime and protected-path effects;
- risks and limitations;
- what remains non-implemented, external or to verify;
- the local non-equivalences that matter.

Use a boundary profile instead of copying the complete non-runtime boilerplate.

## Rules

AI logs must not:

- create doctrine by themselves;
- claim implementation from documentation, a schema, a prototype or a test alone;
- expose secrets or private project data;
- contain hidden chain-of-thought;
- store workflow/session state required for Hermes execution or recovery;
- duplicate the full pull-request body without adding durable trace value;
- rewrite old logs merely to make historical language look current.

Historical logs remain facts about their date. Current status comes from `docs/governance/STATUS.md`, `docs/governance/WHAT_RUNS.md` and the registered authority index corpus.

## Placement and naming convention

When an exceptional new log is justified, use the calendar year and quarter of the date in its filename:

```text
ai_logs/YYYY/Qn/YYYY-MM-DD-short-description.md
```

Example:

```text
ai_logs/2026/Q3/2026-07-23-quarterly-ai-log-paths.md
```

Quarter mapping:

```text
Q1 -> January to March
Q2 -> April to June
Q3 -> July to September
Q4 -> October to December
```

The existing flat files remain valid historical paths. They are not moved in bulk and must not be rewritten merely to satisfy the newer placement rule.

## Index and retention

While `ai_logs/` remains in the working tree, `INDEX.md` provides newest-first navigation across both the historical flat corpus and quarterly subdirectories. After adding, moving or removing a log, run:

```bash
python3 .github/scripts/generate_ai_logs_index.py
```

The generator is navigation-only. It does not move, delete, compact, classify or sign traces.

Removal of a historical log from the working tree requires a separately reviewed change that verifies active references first. Git history remains the archive. There is no automatic deletion, scheduled compaction, monthly digest or retroactive mass migration.

```text
AI log present != runtime dependency
AI log absent != missing workflow state
removed from working tree != removed from Git history
index generation != trace approval
```

## Final rule

```text
Prefer authoritative owner docs, contracts, tests, Git and PR history.
Add an AI log only when consequential understanding would otherwise be lost.
```
