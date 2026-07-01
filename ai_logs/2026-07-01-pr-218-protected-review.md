# AI Log — PR #218 protected review

Date: 2026-07-01

Actor: ChatGPT

Scope:

- Performed protected-path read-only review of PR #218.
- Reviewed canonical boundaries:
  - `docs/governance/STATUS.md`
  - `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
  - `docs/governance/CAPABILITY_PLACEMENT.md`
  - `docs/governance/DOMAIN_PACK_SPEC.md`
  - `docs/governance/WORKFLOW_SCHEMA.md`
  - `docs/governance/CAPABILITY_REGISTRY.md`
- Reviewed changed protected paths:
  - `schemas/workflow_manifest.schema.yaml`
  - `schemas/examples/workflow_manifest.example.yaml`
  - `schemas/README.md`
- Reviewed changed example/doctrine paths:
  - `docs/examples/governed_composition_cerfa/README.md`
  - `docs/examples/governed_composition_marche_public/README.md`
  - `docs/governance/CAPABILITY_REGISTRY.md`

Status:

```text
validation-only / protected review trace
```

No protected path was modified by this review.

Decision position recorded on PR #218:

```text
Accepted as direction.
Protected path change not mergeable yet.
Request changes before merge.
```

Accepted direction:

```text
- governed_composition belongs as optional validation metadata on Workflow Manifest;
- examples are useful and correctly framed as fictional / documented non-implemented;
- boundary language is generally correct: no forge engine, no dispatch, no scheduling, no memory promotion;
- x-boundary adds composition_dispatch: false and forge_execution: false;
- CI is green on the PR head.
```

Requested changes:

```text
1. capability_steps is too permissive.
   It should require complete governance signatures:
   - capability_id
   - declared_scope
   - required_task_contract
   - evidence_pack_shape
   - approval_ceiling
   - register_behavior
   - risk_class
   - refusal_tests

2. post_execution_evidence is too permissive when required: true.
   If required is true, answer_verification and probative_certainty should also be required.

3. Add negative validation coverage for:
   - under-specified governed_composition steps;
   - required post_execution_evidence without V/E ratings.
```

Boundary:

This log does not approve a merge, modify schemas, execute Hermes, create a forge engine, dispatch work, schedule anything, promote memory, create a runtime or validate the PR as mergeable.
