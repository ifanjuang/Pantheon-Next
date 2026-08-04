# Hermes template four-surface consolidation

Date: 2026-08-04

Status: candidate documentation change; no runtime, installation, activation or authorization.

## Observed need

The Hermes template already contained connection fragments, handoffs, returns and agentskills.io `SKILL.md` candidates, while Pantheon governance separately owned the canonical `AGENTS.md` Role registry and the repository-root `CLAUDE.md` work rules.

The template lacked a stable, explicit four-surface entry contract for runtime agents, Claude-specific review, skills as a set and architectural evolution.

## Existing owners checked

- repository-root `CLAUDE.md`;
- `docs/governance/AGENTS.md`;
- `docs/governance/HERMES_CODE_HOSTING_BOUNDARY.md`;
- `templates/hermes/README.md`;
- existing `templates/hermes/skills/*/SKILL.md` candidates;
- current `pantheon-mvp` Hermes route, ChangeCandidate and Runtime Profile / Runtime Observation evolution;
- open governance and implementation PRs concerning external Hermes runtime profiles and observations.

## Change

Added four stable template entry surfaces:

```text
templates/hermes/AGENTS.md
templates/hermes/CLAUDE.md
templates/hermes/SKILLS.md
templates/hermes/DESIGN.md
```

Updated `templates/hermes/README.md` to index those surfaces and state the cross-repository evolution posture.

## Reuse and boundaries

No new governed concept was introduced. The files reuse and point to existing Role, Context, Trace, Knowledge, Claim, Evidence, ChangeCandidate, Competence, Capability Slot, Runtime Profile and Runtime Observation owners.

The files are adapters and indexes. They do not redefine canonical authority.

```text
role alignment != authority delegation
skill documented != skill installed
healthy != compatible
compatible != safe
activated != task authorized
runtime success != Evidence
```

Executable Hermes-side code remains excluded by `HERMES_CODE_HOSTING_BOUNDARY.md`.

## Evolution alignment

The new design surface explicitly accounts for:

- stable internal route identities after removal of obsolete internal `/v1` prefixes;
- preservation of versioned upstream protocols where externally required;
- stable active artifact names rather than generation-labelled V2/V3 files;
- Runtime Profile and Runtime Observation as external-runtime projections;
- provenance, base revision, diff, idempotence and human review for consequential ChangeCandidates;
- separate Pantheon-Next, pantheon-mvp, Hermes, Cockpit and human responsibilities.

## Impact

Documentation only. No schema, runtime, scheduler, queue, provider router, plugin manager, memory engine, approval automation, installation or task authorization is added.
