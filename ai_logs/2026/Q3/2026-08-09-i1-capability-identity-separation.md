# 2026-08-09 — I1 Capability identity separation

Parent: #620
Issue: #626

## Objective

Remove the remaining doctrine-level identity collapse between abstract Pantheon Capability identity and backing Skill identity without adding a new schema or runtime owner.

## Repository basis

I0 proved that current schemas already carry separate fields:

```text
workflow_manifest capability_step.capability_id
workflow_manifest capability_step.skill_manifest_ref -> skill_manifest.skill_id
skill_manifest.skill_id
```

`CAPABILITY_REGISTRY.md` still required `skill_manifest.skill_id == capability_step.capability_id`, contradicting that shape.

## Change

- keep `capability_id` as abstract governance identity;
- keep `skill_id` as Skill/admission identity;
- make backing linkage explicit through `skill_manifest_ref`;
- state that lexical equality, if it occurs, never creates semantic identity;
- preserve the shared risk vocabulary without sharing identity;
- keep implementation/release modeling deferred to I2;
- add a repository test that prevents the equality-collapse rule from returning.

## Boundaries

```text
Capability != Skill
Capability != Tool Card
Capability != implementation
Skill discovered != Capability declared
Skill installed != Capability approved
binding != task authorization
```

No schema, API, migration, runtime, installer, provider router, scheduler, queue, Hermes configuration, Evidence admission, Execution Admission or H Project Anatomy behavior is changed.

## MVP decision

`pantheon-mvp/mvp_vertical/capability_manager.py` remains unchanged in I1. Its `CapabilityRecord` name/type semantics are a convergence question, but I0 did not prove that a code split is required. I2 should first exercise stable `capability_id` across multiple implementation candidates/releases and only then narrow or rename the existing lifecycle seam if the test fails.
