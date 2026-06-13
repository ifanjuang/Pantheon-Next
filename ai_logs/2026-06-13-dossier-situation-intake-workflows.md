# AI log — Dossier Situation Intake and workflow-under-hood examples

Date: 2026-06-13.

## Request

The maintainer validated the addition of practical workflow examples for architecture / ERP work and asked whether an `Isis`-like function should clarify unclear user questions and gather project situation context such as phase, geography and relational tension with client or mairie.

## Canonical check

The role registry was checked in `docs/governance/AGENTS.md`.

Canonical roles currently are:

- ATHENA;
- ARGOS;
- THEMIS;
- APOLLO;
- ZEUS;
- IRIS;
- HEPHAISTOS.

`ISIS` is not a canonical role in the current registry.

Decision: do not add a new canonical role. Add a function / intake object instead.

## Changes made

- Added `docs/governance/DOSSIER_SITUATION_INTAKE.md`.
- Added `docs/assets/workflow-under-hood/README.md`.
- Added `docs/assets/workflow-under-hood/architecture_workflow_under_hood.html`.
- Added `docs/examples/architecture_erp_effectif_impact_workflow/README.md`.
- Added `docs/examples/architecture_notice_securite_incendie_workflow/README.md`.
- Updated `docs/examples/README.md` to index the workflow examples and add situation intake to the reading rule.
- Updated the workflow-under-hood HTML to show `Dossier Situation Brief` before Task Contract and workflow launch.

## Accepted

- The system should clarify the real professional situation before forging a workflow.
- The mechanism should collect phase, geography, project identity, versions, sources, contract scope, relation context and tensions.
- IRIS clarifies wording, but cannot own the whole intake alone.
- The intake should be a function / object, not a new role.
- A workflow may be generated on the fly, but its authority must remain governed.

## Refused

- Adding `ISIS` as a canonical Pantheon Role without prior doctrine reconciliation.
- Treating a generated workflow as durable or authorized by default.
- Allowing the intake to promote memory, mutate the Registre Probatoire or authorize transmission.

## Role mapping

```text
IRIS clarifies the user's wording.
ATHENA structures the problem and workflow family.
ARGOS situates sources, versions, geography and evidence.
THEMIS qualifies tension, risk and approval boundary.
APOLLO checks completeness and usability.
ZEUS arbitrates status and next procedure.
HEPHAISTOS forges workflow / artifact candidates after intake.
```

## Boundary

Documentation and visual support only.

No runtime, schema, tests, connector, OCR, vision, Notion sync, Registre storage, approval engine, email access, PDF annotation or external action was implemented.

Repo state: documented non-implemented.
