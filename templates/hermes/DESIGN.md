# Hermes Template Design

Status: candidate template only — owner index; no runtime authority.

`templates/hermes/` versions declarative contracts consumed by an external Hermes installation. This document only indexes ownership and evolution checks. Canonical governance remains in its existing owners.

## Entry surfaces

```text
README.md   orientation and template inventory
DESIGN.md   owner map and evolution checklist
AGENTS.md   external runtime identity adapter
SKILLS.md   collection-level skill contract
CLAUDE.md   optional Claude-specific work adapter
```

Individual instructions remain in `skills/<skill>/SKILL.md`; profiles remain under `hermes/profiles/`.

## Repository responsibilities

- `Pantheon-Next`: doctrine, schemas, governed identities, statuses, Evidence rules, approvals, Capability Slots and declarative templates.
- `pantheon-mvp`: candidate PostgreSQL/API/Cockpit implementation, projections and adapters.
- Hermes: external execution, tools, models and runtime mechanics.
- Cockpit/OpenWebUI: user projection and decision surfaces.
- Human: consequential decisions.

Executable Hermes-side code remains outside this directory under `docs/governance/HERMES_CODE_HOSTING_BOUNDARY.md`.

## Owner map

- Pantheon Roles: `docs/governance/AGENTS.md`.
- Repository work rules: root `CLAUDE.md`.
- Hermes code placement: `docs/governance/HERMES_CODE_HOSTING_BOUNDARY.md`.
- Agent adapter: `templates/hermes/AGENTS.md`.
- Skill collection contract: `templates/hermes/SKILLS.md`.
- Individual skill behavior: `templates/hermes/skills/*/SKILL.md`.
- Handoff and return shapes: `templates/hermes/handoffs/` and `templates/hermes/returns/`.
- Connection candidates: `templates/hermes/connection/`.

This file does not redefine Context, Trace, Knowledge, Claim, Evidence, ChangeCandidate, Competence, Capability Slot, Runtime Profile or Runtime Observation.

## Evolution checklist

Review the template when:

- Pantheon-Next changes Role, Claim, Evidence, ChangeCandidate, Capability Slot, status or hosting semantics;
- pantheon-mvp changes Hermes handoff/admission/callback routes, Cockpit projections, ProjectClaim/ChangeCandidate behavior or adapter contracts;
- external Hermes changes profile loading, skill loading, transport, tools, memory, automation, sub-agent or approval behavior.

Check for:

- removed internal `/v1` routes or generation-labelled active identities;
- external protocols whose upstream versioning must be preserved;
- provenance, base revision, diff, idempotence and human-review gates;
- accidental promotion of installation, health, compatibility, activation, runtime success or retrieval into authority or Evidence.

Runtime Profile and Runtime Observation are currently tied to open governance and implementation PRs (#523 in Pantheon-Next and #201 in pantheon-mvp). Until merged, references to those exact models must be labelled candidate/proposed, not canonical or implemented.

Repository validation can check structure, references and forbidden patterns. It cannot establish external installation health, compatibility, safety, authorization, result acceptance or Evidence admission.
