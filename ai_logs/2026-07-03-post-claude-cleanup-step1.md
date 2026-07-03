# AI log — post-Claude cleanup step 1

Date: 2026-07-03

## Scope

Executed step 1 of `docs/governance/OPEN_BRANCH_LANDING_PLAN.md`: post-Claude cleanup.

## Files changed

- `templates/openwebui/events/governed_audit_event.template.yaml`
- `templates/hermes/connection/hermes_openai_connection.template.yaml`

## Change summary

- Replaced brittle OpenWebUI event-count language (`>=28 event types`) with a version-dependent `current event/webhook catalog` formulation.
- Added an explicit instruction to verify the current Event Function catalog at implementation time.
- Moved `GET /health` out of `endpoints_used` and into `health_probe_to_verify` in the Hermes OpenAI-compatible connection template.
- Added a governance note: the health probe is a candidate operator check only, not Pantheon monitoring and not runtime-health truth.

## Decision classification

Accepted:

- Keep the OpenWebUI and Hermes templates as candidate template references.
- Clarify uncertainty rather than overstate upstream endpoint/event stability.

Refused:

- Treating event examples as a stable full catalog.
- Treating `GET /health` as an operationally verified Hermes endpoint.
- Treating a health probe as Pantheon monitoring, health truth, approval or runtime control.

To verify:

- Actual OpenWebUI Event Function catalog at implementation time.
- Actual Hermes runtime health endpoint before operational use.

## Repo state

- Documentation / template cleanup: implemented.
- Runtime implication: non applicable.
- Protected paths touched: none.
