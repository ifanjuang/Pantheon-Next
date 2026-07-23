# AI Logs

Status: active support note — AI log policy and navigation — implemented as documentation.
Boundary profile: validation_only_trace.

This directory stores validation-only traces for material AI-assisted repository interventions.

AI logs support review. They are not doctrine, approval, runtime evidence by default or a substitute for Git history and pull-request discussion.

## Purpose

AI logs may preserve:

- a consequential governance change and its rationale;
- a protected-path intervention and its explicit boundary;
- an architecture decision that is not otherwise visible in the changed owner documents;
- a validation or external-runtime observation that must remain distinct from adoption;
- a consolidation or removal mapping needed to understand current placement.

## Granularity rule

Default:

```text
one coherent pull request
-> at most one AI log
```

A separate log is expected when the pull request materially changes one or more of:

- doctrine or authority;
- runtime-status claims;
- protected paths;
- schemas, tests or CI;
- installation, activation, update or rollback posture;
- memory or Evidence behavior;
- an external action or external-runtime observation;
- removal or consolidation whose mapping would otherwise be lost.

A separate log is normally unnecessary for:

- spelling or formatting corrections;
- link repairs with no status effect;
- generated-index refreshes;
- small wording alignment already explained by the pull-request body;
- a mechanical edit that changes no doctrine, authority, runtime status or protected path.

Do not split one coherent intervention into multiple logs merely because it used several commits.

## Required content

When a log is created, use `LOG_FORMAT.md` unless the intervention requires a longer audit structure.

The log should state:

- what changed;
- why it changed;
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
- duplicate the full pull-request body without adding durable trace value;
- rewrite old logs merely to make historical language look current.

Historical logs remain facts about their date. Current status comes from `docs/governance/STATUS.md`, `docs/governance/WHAT_RUNS.md` and the registered authority index corpus.

## Placement and naming convention

New logs use the calendar year and quarter of the date in their filename:

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

The existing flat files remain valid historical paths. They are not moved in bulk and must not be rewritten merely to satisfy the new placement rule.

## Index and retention

`INDEX.md` is generated and provides newest-first navigation across both the historical flat corpus and quarterly subdirectories. After adding, moving or removing a log, run:

```bash
python3 .github/scripts/generate_ai_logs_index.py
```

The generator is navigation-only. It does not move, delete, compact, classify or sign traces.

Removal of a log from the working tree requires a separately reviewed change that verifies active references first. Git history remains the archive. There is no automatic deletion, scheduled compaction, monthly digest or retroactive mass migration.

```text
quarterly placement for new logs != migration of old logs
removed from working tree != removed from Git history
index generation != trace approval
```

## Final rule

```text
Trace what changes consequential understanding.
Do not create trace merely to record that a file was touched.
```
