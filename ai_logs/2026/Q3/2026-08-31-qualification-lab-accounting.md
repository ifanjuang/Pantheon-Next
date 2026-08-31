# What each qualification lab blocks merges for

Date: 2026-08-31

Status: validation-only trace — implemented read-only governance check.
Boundary profile: validation_only_trace.

## Objective

Seventeen workflows check out an external project and run it. Each one blocks
merges. Their maintenance cost grows with every upstream release, and they return
that cost only where a red result would change a decision. Nothing recorded which
decision any of them guards, and nothing checked whether a lab still tests what
the pin registry says was qualified.

## Change

- Added: `.github/scripts/check_qualification_labs.py`.
- Added: `.github/qualification-labs.json`.
- Added: `tests/test_qualification_labs.py`.
- Updated: `.github/workflows/governance-ci.yml` — one step, after the PyYAML
  install it needs.

## What this does not do

It does not arbitrate. Deciding which labs deserve a blocking slot is a human
decision, and inventing a guarded decision for a lab in order to fill a field
would defeat the instrument. Every entry therefore records `guards: null` today,
and the count of blocking-but-unarbitrated labs is capped at 17 so it can only
go down.

## What it does answer, mechanically

A lab either resolves its external targets from `external-pins.json` at run
time, or hardcodes them. Every hardcoded identifier must now be declared and
mapped to the registry pin it corresponds to, so a new frozen target cannot
appear unnoticed. Where a declared literal has drifted from the registry, the
lab qualifies a combination the repository no longer claims to have qualified,
while its green tick reads exactly like one that does.

Three labs are in that state, not one:

```text
Hermes Langfuse Observability Q1   HERMES_COMMIT 4c1f53be  registry 5fc308a7
Hermes Langfuse Self-hosted Q2     HERMES_COMMIT 4c1f53be  registry 5fc308a7
Hindsight Obsidian Hermes O3       HERMES_RELEASE_COMMIT 3c27eb62  registry 5fc308a7
                                   HINDSIGHT_VERSION 0.8.5        registry 0.9.1
                                   OBSIDIAN_SYNC_COMMIT b627aa6f   registry daf529aa
```

O3 is frozen deliberately and says so in a comment at the top of its workflow.
Q1 and Q2 say nothing. They were not previously known to be drifted.

A fourth observation falls out of the same pass: **Langfuse has no entry in
`external-pins.json` at all.** Q2 stands up a full Langfuse stack at a hardcoded
commit, and the qualification registry does not govern that target.

## Boundary

Protected paths touched: `.github/scripts/`, `.github/workflows/` — read-only
validation only.
Runtime impact: none. No workflow trigger is changed by this commit.
Authority impact: none.
Schema/test/CI impact: one CI step, failing on an undeclared or unaccounted lab.
External action: none.
Memory behavior: none.

## Local distinctions

```text
lab green            != qualification
blocking             != guards a decision
hardcoded target     != frozen deliberately
frozen deliberately  != still current
enumerated backlog   != arbitrated backlog
```

## Next decision

Yours, and it is the point of this change: for each of the seventeen, which
decision would be taken differently if it failed? A lab that guards one keeps its
blocking slot and deserves maintenance; a lab that guards none becomes
`workflow_dispatch`. Q1 and Q2 need a prior answer — whether their Hermes commit
should be re-pointed at the registry or declared frozen for a reason.
