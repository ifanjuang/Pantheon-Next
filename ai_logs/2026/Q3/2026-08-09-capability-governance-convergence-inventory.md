# 2026-08-09 — Capability governance convergence inventory

## Objective

Start tranche I with repository truth only, while H continues independently.

## Verified

- `CAPABILITY_PLACEMENT.md` is active support doctrine.
- `CAPABILITY_REGISTRY.md` remains candidate / to verify.
- `HERMES_CAPABILITY_BINDINGS.md` remains candidate support doctrine / documented non-implemented.
- `skill_manifest.schema.yaml` owns Skill-oriented declaration fields.
- `workflow_manifest.schema.yaml` already separates `capability_id` from optional `skill_manifest_ref`.
- `pantheon-mvp` current `CapabilityRecord` mixes a Capability name with runtime/component kinds and therefore requires consumer review before semantic extension.
- Tool Card catalogue is non-authoritative projection data.
- Agent Plugin package/component observations already provide useful implementation provenance.
- existing Execution Admission remains the task/run legitimacy seam.
- Pantheon-Next PRs #554/#555 and pantheon-mvp PR #201 were closed without merge and are historical only.

## Result

Created a non-normative audit under `docs/audits/` and parent issue #620 with the proposed I0–I9 sequence.

No schema, runtime, API, registry authority, Capability admission, activation, Hermes configuration or Evidence behavior was changed.

## Boundary

```text
inventory finding != architecture promotion
Capability != Skill
Capability != implementation
binding selected != dependency adopted
admitted != task authorized
runtime success != Evidence
Cockpit projection != authority
H adapter qualification != I admission
```
