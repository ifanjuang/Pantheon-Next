# AI log — Hermes runtime-efficiency qualification harness

Date: 2026-09-12
Issue: #1047
Baseline main: `836219b7e9c271d64a4850bd2484d3767c56a38f`

## Objective

Create the smallest reversible measurement surface needed to decide whether the selected governed Hermes runtime has a demonstrated efficiency problem worth optimizing with a SoL-inspired mechanism.

No SoL-Pi integration, Hermes runtime change or Pantheon architecture change is authorized by this slice.

## Repository findings before change

- `HERMES_INTEGRATION.md` already assigns profiles, skills, tools, plugins, delegation and context mechanics to Hermes rather than Pantheon.
- `CONTEXT_STACK.md` already owns proportional context and the stopping rule; it explicitly does not implement a context optimizer.
- `MEMORY.md` keeps runtime memory outside Pantheon Evidence/Registre authority.
- `EVIDENCE_PACK.md` keeps runtime output and technical traces distinct from Evidence.
- `hermes_scoped_context.py` already enforces exact admitted identity/run boundaries and a bounded rich-text surface.
- the repository already uses isolated `implementation/labs/` qualifications that add no product boot path or authority.
- no open issue was found for SoL-Pi, ObservationPack, Action Fusion, runtime efficiency or equivalent responsibility.

## Decision

Do not create an efficiency owner, reducer owner, context-distillation slot, new Role, new Rite, new memory path or second orchestrator.

Add only:

```text
recorded observation A
recorded observation B
        ↓
provider-neutral quality-first comparison
        ↓
qualification result
```

The comparison must enforce the reusable lineage when refs are observed:

```text
used ⊆ admitted ⊆ retrieved
```

Lower token/tool cost cannot outrank a candidate with worse required source recall or quality/provenance checks.

## Implemented

- `implementation/labs/hermes_runtime_efficiency/compare.py`
  - provider-neutral observation parser;
  - exact-case / variant validation;
  - runtime/model/profile/settings comparability signals;
  - optional operational metrics with unknown-preserving semantics;
  - source-recall and required-quality gate;
  - `used ⊆ admitted ⊆ retrieved` validation;
  - cost deltas without a universal score;
  - qualification-only decisions.
- `implementation/labs/hermes_runtime_efficiency/README.md`
  - four representative live cases;
  - owner boundaries and non-goals;
  - removal test and decision order.
- `implementation/tests/test_hermes_runtime_efficiency_lab.py`
  - lower-cost quality regression rejection;
  - unknown-metric preservation;
  - identity mismatch handling;
  - lineage fail-closed checks;
  - no product/runtime integration guard.
- isolated CI workflow for the lab tests.

## Review hardening

PR review identified three ways the initial harness could overstate a gain. They were treated as correctness defects in the existing lab, not as reasons to add architecture.

The slice now also enforces:

- both baseline and candidate must be `complete` before operational cost can qualify a candidate;
- candidate `blocked` / `failed` remains a regression, while other non-complete comparisons are inconclusive;
- observed source recall requires stable opaque `source_recall_check_ids` whose count exactly matches `source_recall_checks`;
- A/B source-recall perimeter equality is based on those stable identities, not merely on the number of checks;
- `elapsed_seconds` must be finite and non-negative;
- report JSON is emitted with `allow_nan=False`;
- targeted tests cover early termination, equal-count/different-perimeter recall, and `NaN` / infinity rejection.

The strengthened non-equivalences are:

```text
partial execution != equivalent execution
same check count != same source-recall perimeter
lower cost != better result
```

## Explicitly not implemented

```text
no SoL-Pi package
no Pi runtime
no Hermes plugin
no ObservationPack port
no Action Fusion port
no reducer
no context compaction trigger
no remote model/log transmission
no runtime configuration mutation
no persistence
no Evidence admission
```

## Next evidence required

Run the representative cases on the exact installed Linux Hermes/profile/model/settings and record observations without client-sensitive fixture data.

Only after those runs:

```text
native sufficient
or
one dominant residual cost
```

may justify the next decision.

A measured `native_sufficient` outcome closes the issue without further architecture.
