# Adaptive Request Method — owned-seam convergence — 2026-08-29

## Objective

Continue #787 from merged `main` `c80950fab80df20bf62eea88cab78b86fb0cac1d` by removing rules from `ADAPTIVE_REQUEST_METHOD.md` that are already owned by Context Stack and Source Need doctrine. The goal is to expose Adaptive's actual local responsibility before deciding whether it remains a standalone owner.

## Scope

- `docs/governance/ADAPTIVE_REQUEST_METHOD.md`

No authority index, schema, test, CI, runtime or implementation file is changed.

## Observed need

After #803 removed generic boundary boilerplate, Adaptive still repeated two substantial ownership areas:

1. HESTIA/context sufficiency, already defined by `CONTEXT_STACK.md`;
2. Source Need Candidate structure, source families and source routes, already defined by `SOURCE_NEED_AND_REGISTRY.md`.

`SOURCE_NEED_AND_REGISTRY.md` itself names Adaptive only as the request-time consumer when a source need appears. `CONTEXT_STACK.md` owns Context Stack composition, sufficiency states, Context Stack Change Candidates and HESTIA's candidate-role boundary.

## Authority-index observation

`ADAPTIVE_REQUEST_METHOD.md` currently declares `Status: active support doctrine` but no row for it was found in `docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md`. Indexed neighboring owners include `REQUEST_LIFECYCLE.md`, `DOSSIER_SITUATION_INTAKE.md`, `WORKFLOW_FORGING_PROTOCOL.md`, `GOVERNED_METHOD_STANDARD.md` and `GOVERNED_AUTONOMY_GRADIENT.md`.

This slice does not silently promote, demote or add Adaptive to the index. The discrepancy is intentionally left visible for the next owner decision.

## Existing owners checked

- `CONTEXT_STACK.md` — candidate support doctrine for context composition/sufficiency and HESTIA candidate context-watch.
- `SOURCE_NEED_AND_REGISTRY.md` — active support doctrine for Source Need Candidate, source families, routes, registry and freshness.
- `REQUEST_LIFECYCLE.md` — indexed active support owner for cap/lifecycle choreography.
- `GOVERNED_METHOD_STANDARD.md` — indexed active support owner for generic professional method movements.

## Changes

Adaptive now:

- keeps proportional activation based on ambiguity, context, source, risk, memory and output consequence;
- keeps its request decomposition vocabulary;
- keeps input/output separation, complexity drivers, output-consequence adaptation and safe defaults;
- references `CONTEXT_STACK.md` for context-sufficiency semantics instead of redefining HESTIA and Context Stack statuses;
- references `SOURCE_NEED_AND_REGISTRY.md` for Source Need structure, source families/routes/registry/freshness instead of maintaining a second source policy;
- explicitly states that it does not own Context Stack, source policy, Evidence, approval, memory, workflow execution or runtime authority.

## Overlap analysis

Before this change, Adaptive contained roughly 100 lines of duplicated context/source doctrine. After the change, the remaining responsibility is narrower:

```text
proportional request activation
+ request decomposition
+ input/output consequence relationship
+ safe fallback posture
```

That remaining core will be compared next against `GOVERNED_METHOD_STANDARD.md` and `REQUEST_LIFECYCLE.md` before any index promotion or mother-document absorption decision.

## Affected consumers

Documentation readers only. Source Need and Context Stack consumers gain a clearer single owner; no executable consumer changes.

## Migration and rollback

Documentation-only convergence. No migration or runtime change. Rollback is a normal Git revert.

## Role / Rite / Space

- Role: ATHENA for method composition, MNEMOSYNE for owner continuity, THEMIS for authority boundaries.
- Rite: Concordance des sources across exact main, #787, Adaptive, Context Stack and Source Need owners.
- Space: Pantheon Next governance repository.

These labels create no runtime state.

## Authority impact

No new authority is created. Context Stack and Source Need ownership is clarified; Adaptive's existing unindexed active-support status is not silently resolved in this PR.

## Runtime impact

None. No client, runtime, retrieval engine, source registry backend, context engine, scheduler, queue, provider, memory system, approval system or external action changes.

## Preserved invariants

```text
context != Evidence
retrieved != truth
registered source != Evidence
runtime success != authorization
memory != Evidence
projection != persistence
method composition != authority duplication
```

## Truncation / verification

Exact compare before this log:

```text
ADAPTIVE_REQUEST_METHOD.md  +34 / -101
```

The removed material is specifically the duplicated HESTIA/context-sufficiency and source need/family/route definitions. No proportional-activation, request-decomposition, output-consequence or safe-default section is removed.

Merge only after Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency are green on the exact final HEAD and the final patch plus reviews/threads/comments are read.