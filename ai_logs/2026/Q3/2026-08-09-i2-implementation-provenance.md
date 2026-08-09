# 2026-08-09 — I2 implementation provenance convergence

Parent: #620
Issue: #630

## Objective

Determine the smallest existing-contract extension needed to identify an exact executable implementation/release without conflating runtime availability, Capability governance, binding, admission, activation or task authorization.

## Repository facts

- Capability Passport classifies a governed capability unit and supports resource/prompt/tool/skill primitives.
- Skill Manifest owns Skill-oriented declaration/admission identity but currently has no generic immutable implementation release provenance block.
- Agent Plugin normalization already records package name/version/digest plus component id/kind/ref and observed_at.
- Execution Admission remains the task/run legitimacy seam.

## Demonstrated gap

For a non-Agent-Plugin Skill or Tool, current governance material cannot uniformly express the exact executable artifact with immutable provenance comparable to the Agent Plugin observation pattern.

A title, skill_id, free-form dependency URL or description hash is not sufficient to distinguish release A from release B of the same governed capability.

## Convergence decision

Extend the existing Capability Passport with one optional, closed `implementation_provenance` object rather than creating a new implementation registry or widening the Skill Manifest into a universal runtime-artifact contract.

When the block is present it records:

```text
source_kind
source_ref / repository_ref
commit_ref and/or content_digest
package_name / package_version / package_digest
component_id / component_kind / component_ref
observed_at
```

At least one immutable release anchor is required:

```text
commit_ref OR content_digest OR package_digest
```

The package/component field names intentionally match the existing Agent Plugin normalized observation vocabulary.

## Semantics

```text
same Capability may be reviewed against replacement releases
new release != new Capability by default
digest known != safe
artifact discovered != admitted
provenance recorded != binding selected
binding selected != dependency adopted
provenance recorded != activated
provenance recorded != task-authorized
compatibility observation != Evidence
```

The provenance block is descriptive review/observation data only. It performs no discovery, installation, binding selection, admission, activation, execution or authorization.

## Tests

I2 adds guards that prove:

- a generic Skill passport can carry immutable release provenance;
- two exact releases may keep the same governed Capability/passport identity;
- a provenance block without an immutable anchor fails validation;
- Agent Plugin package/component vocabulary is reusable without translation synonyms;
- runtime inventory fields such as installed paths are rejected by the closed object.

## Boundary

No runtime registry, installer, plugin manager, package manager, provider router, scheduler, queue, automatic admission, automatic activation, Execution Admission change, Evidence admission or H qualification behavior is added.
