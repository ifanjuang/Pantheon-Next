# MVP Vertical Blocks 1-2 — external execution repository trace

Status: validation-only trace — external runtime bundle audit.
Boundary profile: validation_only_trace.
Date: 2026-07-10.

## Summary

The `pantheon-mvp-vertical` bundle was reviewed as an external execution repository candidate, not as Pantheon Next doctrine and not as code to import into this repository.

The bundle reports Blocks 1 and 2 of the MVP vertical slice:

- Block 1: bounded ingestion, scoped retrieval and candidate/refusal output.
- Block 2: human decision gate, decision review surface and append-only Decision Records.

The OpenWebUI action included in the bundle remains candidate only. It is not installed, activated or approved by this trace.

## Local audit result

Observed locally from the attached bundle:

```text
bundle: valid
branch: main
head: c3e812666b319732e02aa73a9d16b91d420693da
commits: 2
files: 22
block 2 files:
  - mvp_vertical/gate.py
  - openwebui/mvp_gate_action.py
  - tests/test_block2_gate.py
local sandbox tests: 7 passed, 5 skipped
```

The skipped tests depend on pgvector / database runtime availability that was not available in the sandbox. The local result therefore confirms the non-database gate tests only; it does not independently reproduce the reported `12/12` result.

## Governance classification

```text
implemented in external bundle:
  - bounded ingestion / scoped retrieval slice
  - decision gate slice
  - append-only Decision Record write path

documented non-implemented in Pantheon Next:
  - no internal runtime is added here
  - no OpenWebUI action is installed here
  - no Register Candidate creation is added here

candidate only:
  - openwebui/mvp_gate_action.py
  - future cockpit exposure of the gate

partial / to verify:
  - external repository publication
  - first CI run in the external repository
  - full pgvector-backed test reproduction
```

## Boundary

```text
exposed_by: OpenWebUI candidate action, if later reviewed and installed by a human.
executed_by: external pantheon-mvp-vertical repository / Hermes-side runtime candidate.
governed_by: Pantheon Next status, evidence, approval, memory and retention gates.
approved_by: human decision only.
forbidden: importing the runtime into Pantheon Next, treating tests as approval, treating runtime success as evidence, installing the OpenWebUI action by implication, or creating Register Candidates automatically.
```

## Non-equivalence notes

```text
external bundle reviewed != repository published
runtime tests green != governance approval
OpenWebUI action present != action installed
retention_authorized flag != Register Candidate created
Decision Record written != memory promoted
```

## Pending sequence

1. Create or expose `ifanjuang/pantheon-mvp-vertical` as the external execution repository.
2. Push the bundle branch `main` to that repository.
3. Run the repository CI / pgvector-backed tests in the correct runtime environment.
4. Update this trace or add a follow-up trace with the external repository commit and CI result.
5. Start Block 3 only after the external repository is published and verifiable.

## Decision

Pantheon Next should receive this trace only. The executable MVP vertical code remains outside Pantheon Next unless a later explicit protected-path review decides otherwise.
