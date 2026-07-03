# 2026-07-03 — CogniCore distillation path

## Change

Updated:

- `docs/governance/reference_reviews/COGNICORE_RUNTIME_REVIEW.md`

Added a section explaining how to distill CogniCore patterns into Pantheon Next if needed.

## Why

The user asked to indicate how the CogniCore review should be distilled into the repository if it becomes useful.

The addition avoids direct tool adoption and defines a staged path:

1. keep as external reference;
2. distill only tool-agnostic runtime-memory rules;
3. use `EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md` as the first generic target;
4. create a `COGNICORE_HERMES_ADAPTER_CANDIDATE.md` only if a concrete Hermes-side experiment is considered;
5. keep any prototype outside the Pantheon kernel.

## Classification

Accepted:

- staged distillation method;
- `Runtime Recall Signal` as a possible abstract candidate concept;
- gates for memory, evidence, override, approval and implementation.

Refused:

- direct CogniCore adoption;
- kernel import;
- schema or test creation;
- runtime or adapter implementation;
- automatic memory promotion, approval or truth status.

## Repo state

Documented non-implemented.

No protected path was modified.
No schema, test, runtime, dependency, adapter, skill, approval engine, memory engine or external action was created.
