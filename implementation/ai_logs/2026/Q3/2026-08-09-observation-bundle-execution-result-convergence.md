# 2026-08-09 — Observation Bundle Execution Result convergence

## Objective

Consume the canonical Project Anatomy Observation Bundle in `pantheon-mvp`
without creating another runtime, persistence owner, admission path or authority.

Pantheon-Next authority merged in:

```text
ifanjuang/Pantheon-Next@7cef8075525e016b7554b29bf0ed2c1cf673e855
```

MVP main verified before the slice:

```text
dd85aae12235f667434d94190dec5a9e808bb569
```

## Repository truth

- `execution_results` already owns append-only typed runtime returns;
- result payloads and review dispositions are already separate records;
- the active APU owner already has the registry required to validate the four
  Project Anatomy primitives;
- write-command preparation already persists an exact embedded source
  representation and identity relation, but also repeated three unconstrained
  top-level references removed by the canonical contract review;
- existing SQL setup is idempotent and already evolves the closed result-kind
  constraint; no new table or migration lineage is needed.

## Convergence decision

Add `observation_bundle` as one more typed Execution Result kind. Its payload must:

- use the exact canonical schema ref;
- validate against the verbatim vendored Observation Bundle schema and its four
  referenced Project Anatomy schemas;
- carry the same `project_ref` and `task_contract_ref` as its Execution Result;
- retain candidate-only authority;
- remain append-only and require a distinct later review/adoption path for any
  Project Anatomy write, Evidence admission, decision or memory effect.

No Observation Bundle table, ingestion service, direct APU projection, Evidence
path, scheduler, plugin persistence or automatic application is introduced.

## Write-command continuity

The canonical write-command candidate now defines its bounded effect only with:

```text
source_representation
+ identity_relation_claim
```

MVP therefore removes `target_stable_object_ref`, `source_candidate_ref` and
`source_artifact_ref` from the governed command JSON. Existing database columns
with those names remain internal indexes derived from the embedded effect. The
application gate checks those indexes against the immutable payload before use.

## Freshness and coverage

- `source_representation.freshness_token` and bundle `freshness_token` are source
  snapshot freshness; for Revit they remain document freshness;
- view and selection freshness remain adapter execution guards;
- partial or unknown coverage cannot authorize absence inference;
- every non-success outcome also forces absence inference off.

## Authority boundary

Contract validation means conformance only. It does not establish fact, Evidence,
decision, memory, professional stable identity, APU write or external-effect
authorization.
