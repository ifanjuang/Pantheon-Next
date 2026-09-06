# Hermes external context minimal v1

Date: 2026-09-06

Status: candidate implementation / qualification only.

## Objective

Replace the superseded shell-provenance exploration in #975 with the smallest demonstrated external-content boundary around the existing `pantheon-context-bridge`.

```text
Pantheon Context Pack result -> deterministic Context Admission -> Hermes
Gateway inlined attachment   -> deterministic Context Admission -> Hermes
```

## Selected simplification

The candidate deliberately does **not** implement:

- terminal fetch detection;
- curl/wget/git/gh parsing;
- pending or taint state;
- `post_tool_call` provenance;
- dynamic eligible filesystem roots;
- guarded filesystem read/search tools;
- filesystem sandboxing;
- scanner-driven admission disposition;
- a new provenance, ingestion, memory or Evidence owner.

Shell execution and filesystem mutation remain Hermes runtime concerns. A future need for controlled external ingress must first demonstrate a concrete governed operation; it must not be inferred from terminal text.

## Existing owners reused

- `pantheon-context-bridge` remains the model-bound Context Admission bridge.
- Context Pack / Execution Admission remain scope/task owners.
- Hermes remains the external execution/tool runtime.
- Document/Information/Knowledge owners remain the durable professional content paths.
- Evidence/approval/memory authorities are unchanged.

## Contract

```text
transport into model != instruction authority
transport as data != truth
transport as data != Evidence
attachment content != user request
runtime success != authorization
```

Context Admission is now deterministic. The Hermes threat scanner is not consulted by this transport transform. If threat scanning is later useful, it belongs to a separate observation/risk path rather than changing the content role supplied to the model.

## Gateway attachment rule

Only adapter-inlined document content matching the reviewed Hermes gateway shape is rewritten. A user-authored caption remains outside the data block only when it is provably the suffix of the normalized event text. If separation cannot be proven, the whole combined content is demoted to data and fixed guidance asks for a user request.

## Done gate

This slice is complete only when:

1. the diff remains bounded to the bridge, focused tests and the deterministic distribution digest update;
2. no shell/filesystem provenance state is introduced;
3. current `main` is the merge base;
4. required architecture/governance/runtime/implementation checks are green on one exact head;
5. live Hermes qualification remains separate from merge and from task authorization.
