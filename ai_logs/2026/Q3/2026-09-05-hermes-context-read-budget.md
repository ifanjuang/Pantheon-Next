# 2026-09-05 — Hermes context read budget

## Objective

Distill the useful context-budget lessons from `dtiger1889-ops/obsidian-agent-integration` into the existing Hermes template responsibility without creating a new runtime, prompt registry, instruction compiler or authority owner.

## Verified baseline

Work starts from:

```text
Pantheon-Next main = fd39f1d377d57eb2dc03060c0f93b21763b745b7
```

Current main, recent commits, open PRs/issues, Hermes template owners and Obsidian owners were checked before the change. PR #971 (`feat(hermes): add data-only Context Admission boundary`) is parallel work on untrusted model-bound context; its changed paths do not overlap this slice.

The top-level `templates/hermes/*.md` orientation surface on the base measured:

```text
AGENTS.md   2,536 B
CLAUDE.md   2,651 B
DESIGN.md   4,351 B
README.md   8,791 B
SKILLS.md   1,999 B
-------------------
total      20,328 B
```

The changed surface measures 22,209 B and remains below the new 24 KiB repository review ceiling.

## Convergence

`templates/hermes/SKILLS.md` remains the collection-level skill contract. It now records a context read-budget discipline:

- one owner per durable convention; reference rather than duplicate;
- repository orientation-size checks are review ratchets, not Hermes token limits;
- actual mandatory runtime read sets must be observed separately;
- mandatory files should not be concatenated when the runtime can silently truncate output;
- a truncation-prone runtime needs deterministic complete-read proof such as a sentinel, byte count, digest or equivalent;
- context minimization must not remove governance boundaries.

`tests/test_hermes_context_read_budget.py` adds a repository-side ratchet only:

```text
top-level orientation surface <= 24 KiB
individual top-level file      <= 12 KiB
```

These ceilings are intentionally review thresholds rather than claims about external runtime capacity.

## Preserved boundaries

```text
repository size check != deployed runtime observation
file present != file read completely
context loaded != instruction authorized
smaller prompt != permission to drop governance
rule duplicated != rule reinforced
```

No Hermes runtime behavior, profile, distribution lock, Context Admission path, schema, capability binding, Evidence owner or authorization path changes.

## Verification

Repository changes are limited to the existing Hermes declarative template responsibility plus one focused regression and this AI log. GitHub CI remains the execution gate because the local container has no outbound GitHub network access.

## Status

Repository contract and regression prepared. External-runtime token/read behavior remains to be observed during an exact deployed Hermes qualification; this PR does not claim that proof.
