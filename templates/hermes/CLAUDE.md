# Claude Adapter for Hermes

Status: candidate template only — assistant-specific instruction adapter.

This file adapts the Hermes template contract for Claude-based development or review sessions. It is not the repository-root `CLAUDE.md`, does not replace Pantheon doctrine and does not authorize a runtime, model, provider, tool or task.

Read in this order before significant work:

1. repository-root `CLAUDE.md`;
2. the relevant canonical governance owners;
3. `templates/hermes/DESIGN.md`;
4. `templates/hermes/AGENTS.md`;
5. the selected `skills/<skill>/SKILL.md`;
6. the exact handoff and return templates for the task;
7. current `main`, open pull requests and active implementation consumers.

## Working posture

Treat the repositories as separate authority layers:

```text
Pantheon-Next = governance, doctrine, schemas, statuses and template owners
pantheon-mvp = candidate operational implementation and projections
Hermes = external execution runtime
OpenWebUI / Cockpit = exposure and decision surfaces
human = consequential decision
```

Before adding a concept, verify whether Context, Trace, Knowledge, Evidence, Claim, ChangeCandidate, Competence, Capability Slot, Runtime Profile or Runtime Observation already covers the need.

Prefer consolidation over a new layer.

## Required distinctions

Always preserve:

```text
installed != approved
healthy != safe
compatible != activated
activated != task_authorized
runtime_success != Evidence
retrieved != truth
binding_selected != dependency_adopted
UI status != authorization
```

A Claude session may prepare code, documents, patches, reviews and candidates. It must not infer permission to merge, publish, transmit or execute consequential effects from the task's technical feasibility.

## Repository evolution checks

For every change involving Hermes templates:

- compare the template against current `Pantheon-Next/main` doctrine and schemas;
- inspect current `pantheon-mvp/main` consumers and open PRs;
- reject stale internal `/v1` routes while preserving externally versioned upstream protocols where required;
- reject active artifact identities based on generation labels such as V2, V3 or temporary versioned filenames;
- preserve provenance, base revision, diff, idempotence and human review for consequential ChangeCandidates;
- treat Runtime Profile and Runtime Observation as projections of an external runtime, not new Pantheon authorities;
- record material intervention under `ai_logs/<year>/Q<n>/`.

## Skills

A selected `SKILL.md` describes bounded execution guidance. Loading a skill does not install its tools, approve its dependencies, activate its Capability Slot or authorize its use for the current task.

Executable scripts must not be added under `templates/hermes/` or `hermes/`. The hosting boundary is owned by `docs/governance/HERMES_CODE_HOSTING_BOUNDARY.md`.

## Output discipline

Separate facts, interpretation, recommendation and uncertainty. Report exact files and checks. Return incomplete work as incomplete; do not fabricate Evidence, acceptance, approval or runtime health.
