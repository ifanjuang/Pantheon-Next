# Hermes Template Design

Status: candidate template only — architectural index; no runtime authority.

This document consolidates the design of the declarative Hermes template surfaces. It does not replace the canonical governance documents it references.

## Purpose

`templates/hermes/` versions the contracts that an external Hermes installation may consume. Pantheon Next governs these contracts but does not install, execute, schedule or operate Hermes.

The template is organized around four human entry surfaces:

```text
AGENTS.md   runtime-agent behavior and Role alignment boundary
CLAUDE.md   Claude-specific repository and review adapter
SKILLS.md   skill-set classification and review contract
DESIGN.md   architecture, ownership and evolution index
```

Individual skills remain under `skills/<skill>/SKILL.md`.

## Authority and repository placement

```text
Pantheon-Next
  owns doctrine, schemas, governed identities, statuses, Evidence rules,
  approvals, Capability Slots and declarative Hermes templates.

pantheon-mvp
  owns candidate PostgreSQL/API/Cockpit implementation, operational
  projections, adapters and bounded runtime-observation normalization.

Hermes
  owns external execution, skills, tools, models and runtime mechanics.

OpenWebUI / Cockpit
  exposes simple user projections and consequential decision surfaces.

Human
  decides consequential effects.
```

The dependency direction is one-way: runtime and implementation consumers may consume pinned Pantheon artifacts; Pantheon governance must not depend on their execution.

Executable Hermes-side code is excluded from this directory. The controlling decision is `docs/governance/HERMES_CODE_HOSTING_BOUNDARY.md`.

## Contract flow

```text
abstract capability
  -> candidate binding
  -> installation observation
  -> health observation
  -> compatibility classification
  -> activation decision
  -> task authorization
  -> governed handoff
  -> external runtime execution
  -> runtime observations + candidate return
  -> Pantheon classification / ChangeCandidate / Evidence review
  -> human consequential decision
```

No arrow is automatic.

## Existing concept reuse

Use existing Pantheon concepts before introducing another template field or document:

- Context for bounded task material;
- Trace for execution and transformation lineage;
- Knowledge for governed reusable content;
- Claim for source-backed consequential values;
- Evidence for admitted proof under its own rules;
- ChangeCandidate for consequential proposed mutation;
- Competence and Capability Slot for abstract ability;
- Runtime Profile for an observed external runtime configuration;
- Runtime Observation for reported or observed execution state.

A template projection may simplify display without flattening provenance, status or authority in the backing model.

## Four-surface ownership

### AGENTS.md

Defines how external runtime identities behave and how they may align with canonical Pantheon Roles. It must never redefine Role authority.

Canonical owner: `docs/governance/AGENTS.md`.

### CLAUDE.md

Adapts the contract for Claude-based development and review sessions. The repository-root `CLAUDE.md` remains authoritative for work in Pantheon Next.

### SKILLS.md and skills/*/SKILL.md

`SKILLS.md` defines the set-level contract. Each `SKILL.md` defines one bounded skill candidate. Availability or installation does not imply adoption, activation or authorization.

### DESIGN.md

Owns only this architectural index and the cross-repository evolution checklist. It must point to canonical owners instead of restating their complete doctrine.

## Cross-repository evolution checklist

Review this template whenever either repository changes any of the following:

### Pantheon-Next

- Role, Rite, Space or governance-owner identities;
- Context, Trace, Claim, Evidence or ChangeCandidate semantics;
- Capability Slot, binding, activation or approval semantics;
- Hermes hosting or integration boundaries;
- canonical status vocabulary;
- stable artifact naming policy.

### pantheon-mvp

- Hermes handoff, admission or callback routes;
- Runtime Profile or Runtime Observation normalization;
- Cockpit projections of capabilities, tools, skills or runtime state;
- ProjectClaim or ChangeCandidate API behavior;
- provenance, revision, diff, idempotence or human-review gates;
- adapter contracts consumed by an external Hermes runtime.

### External Hermes

- profile and skill-loading conventions;
- API transport and versioned external protocol;
- native tools, memory, automation, sub-agent or approval behavior;
- compatibility changes affecting the pinned installation.

External release observation does not adopt the release. Update a template only after classifying the delta against current Pantheon owners and implementation consumers.

## Stable naming and routes

Pantheon internal application routes use stable responsibility identities rather than internal generation prefixes. Do not reintroduce removed internal `/v1` routes or active filenames based on V2, V3 or similar generation labels.

An external upstream protocol may remain versioned when that version is part of the upstream contract. Internal stability and external protocol versioning are separate concerns.

## Runtime profile and observation

Runtime Profile and Runtime Observation are projections of an external installation. They may describe identity, version, binding, compatibility, capability support, progress, result, failure, capability gap or risk escalation.

They do not prove:

```text
reported != observed
healthy != compatible
compatible != safe
compatible != activated
activated != task_authorized
completed != accepted
runtime_success != Evidence
```

## Consequential change path

When a Hermes return proposes a consequential mutation, prefer a ChangeCandidate retaining:

- provenance;
- exact base revision;
- explicit diff;
- idempotency identity;
- scope and authorization context;
- review status;
- human decision.

A simple Cockpit card may project that proposal, but the card state must not become backend authority.

## Validation boundary

Repository checks may validate structure, references and forbidden patterns. They cannot establish installation health, runtime compatibility, safety, activation, task authorization, result acceptance or Evidence admission.
