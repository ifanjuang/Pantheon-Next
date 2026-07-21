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

## Naming convention

```text
YYYY-MM-DD-short-description.md
```

Example:

```text
2026-07-20-document-knowledge-runtime-reconciliation.md
```

## Index and archive

`INDEX.md` is generated and provides newest-first navigation. After adding, moving or removing a log, run:

```bash
python3 .github/scripts/generate_ai_logs_index.py
```

The flat corpus may be archived by year and quarter in a separately reviewed, reversible change. Archive placement changes navigation only; it does not change a log's validation-only status.

## Final rule

```text
Trace what changes consequential understanding.
Do not create trace merely to record that a file was touched.
```
