# AI log — workflow navigation

Date: 2026-06-14.

## Scope

Navigation pass after the Dossier Situation Intake and Workflow Forging Protocol additions.

## Changes

- Updated `docs/governance/README.md` to include the intake and forging documents in the read path.
- Updated `docs/assets/README.md` from a bootstrap stub into an active index of visual documentation assets.

## Decision

Accepted:

- `Dossier Situation Intake` belongs before workflow forging.
- A workflow may be generated on the flow only as a `Workflow Candidate`.
- Visual assets must show whether a feature is implemented, candidate, validation-only or documentation-only.

Refused:

- Treating a visual flow, dashboard button or generated workflow as runtime authorization.

## Repo state

Documented non-implemented.

No runtime, schema, test, connector, approval engine, workflow engine, Notion sync or Registre storage was added in this pass.
