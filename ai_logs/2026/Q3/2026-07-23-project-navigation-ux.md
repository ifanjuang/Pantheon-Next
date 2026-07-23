# 2026-07-23 — Architecture project navigation UX extension

Status: validation-only intervention trace.

## Request

The maintainer requested that every architecture project appear in the Cockpit as a project-specific folder/card with a solid-color background and two information densities:

- recto: essential project identity;
- verso or details: parcel numbers, typed surfaces, PLU zones, applicable regulations, client names and primary contact information.

The maintainer also requested two dedicated project cards:

- `Intervenants & contacts`, including clients and bureaux d'études;
- `Entreprises`, including contractors organized by work lot.

## Documents consulted

The extension was reconciled against:

- `docs/governance/PANTHEON_COCKPIT_UX_SPEC.md`;
- `docs/governance/CARD_STACK_MODEL.md`;
- `docs/governance/KNOWLEDGE_NAVIGATION_UX.md`;
- `docs/domain-packs/architecture/PROJECT_UNDERSTANDING.md`;
- `docs/domain-packs/architecture/PROJECT_UNDERSTANDING_ADAPTER_CONTRACT.md`;
- `docs/domain-packs/architecture/PROJECT_OBJECT_MODEL.md`;
- `docs/domain-packs/architecture/DOCUMENT_AND_KNOWLEDGE_ORGANIZATION.md`.

## Decision recorded

A new architecture-domain UX specialization was added:

- `docs/domain-packs/architecture/PROJECT_NAVIGATION_UX.md`.

The model distinguishes:

```text
Project Card / project folder
= solid-color project navigation container

Knowledge folder
= gradient-filled Knowledge navigation container

Knowledge item
= neutral card with thick gradient outline

Intervenants & contacts / Entreprises
= neutral project-scoped cards with solid project-color accent
```

The project color expresses project identity only. It does not encode approval, risk, certainty, phase, archive, Evidence or runtime state.

## Data posture

The Project Card is a presentation projection, not a parallel truth store.

Parcel references, surface values, PLU zones and regulation candidates remain source-backed, dated and status-qualified.

```text
zone displayed != regulatory conclusion
surface displayed != filing value approved
company selected != company contracted
contact extracted != participant confirmed
```

The project profile reuses Architecture Project Understanding claims and project-object relationships where appropriate.

## Contact and company decisions

The participant model separates person and organization identity from the project relationship.

The company model separates the company master record from its project-specific engagement, lot, consultation, contract and works status.

Client and commercial data remain permission-aware.

## Classification

```text
authority class: candidate support doctrine
repository state: documented non-implemented
runtime state: unchanged
protected paths touched: none
schema or test change: none
installation or activation: none
```

The architecture authority map already contains a grouped row covering `docs/domain-packs/architecture/`, so the new candidate is visible without adding a competing authority row.

## Non-effects

This intervention creates no:

- Cockpit component;
- CRM or ERP;
- contact database;
- cadastral or PLU connector;
- project storage migration;
- Hermes Skill;
- approval engine;
- archive service;
- external action.
