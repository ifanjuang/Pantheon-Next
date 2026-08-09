# 2026-08-09 — I2 implementation provenance convergence

Parent: #620

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

## Constraint

Reuse existing Capability Passport / Skill Manifest / Agent Plugin provenance semantics before creating a new registry or manager. Any schema change must remain data-only and must not install, activate, bind or authorize anything.
