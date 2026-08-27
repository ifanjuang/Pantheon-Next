# Retire OpenWebUI integration owner

Date: 2026-08-27
Issue: #666
Role: architecture convergence
Rite: compatibility retirement
Space: runtime-client interaction + Pantheon governed projection
Change level: semantic

## Objective

Remove `docs/governance/OPENWEBUI_INTEGRATION.md` after converging its active responsibilities and structural consumers to current owners, without treating every historical or non-objective OpenWebUI mention as an active dependency.

## Verified state before change

`main` was verified at `e18e7672ef2e6a25e8ee7e48063ceb6425a04d98` after PR #779.

The retired integration owner already declared itself refused and stated that it could be deleted once compatibility code/templates and live incoming links were removed.

Direct current-SHA verification identified:

- `DECISION_SURFACE_SPEC.md` still owned an OpenWebUI-facing decision surface;
- `AI_LEARNING_REPOS_DISTILLATION.md` still contained an active destination link to `OPENWEBUI_INTEGRATION.md` and product-specific exposure language;
- `.github/workflows/governance-ci.yml` still required the integration file to exist;
- the obsolete index still described former OpenWebUI sub-documents as merged into the integration owner;
- the governance authority index still described the Decision Surface as OpenWebUI-facing.

GitHub code search was used only for candidate discovery because its index lagged behind current `main`; all changed owners were fetched directly at the exact current SHA before modification.

## Change

- make Decision Surface a client-agnostic governed review projection;
- make the AI learning distillation client-agnostic and route Pantheon-facing UX through existing Cockpit/Card owners;
- remove the integration file from the mandatory Governance CI baseline;
- record `OPENWEBUI_INTEGRATION.md` itself as removed/refused in `OBSOLETE_AND_ABSENT_INDEX.md` and reroute the former domain/plugin-policy rows;
- align the Decision Surface authority-index row;
- delete `OPENWEBUI_INTEGRATION.md` from the working tree;
- add a regression test that forbids active governance references to the removed owner except the historical obsolete index.

The existing truncation acknowledgment remains during this deletion pass so the deliberate removal is review-visible.

## Invariants

```text
client selected != governance authority
projection != persistence
UI display != approval
runtime success != authorization
retrieval != Evidence
historical mention != active dependency
removed owner != removed capability
```

## Preserved capabilities

The retirement does not remove:

- Hermes/runtime-client conversation or execution interaction;
- Pantheon Cockpit/Card governed projections;
- Decision Surface semantics;
- Knowledge/retrieval/review displays;
- Task Contract, Evidence, approval or memory boundaries;
- historical provenance in Git and dated `ai_logs`.

## Exit criteria

- `OPENWEBUI_INTEGRATION.md` no longer exists;
- Governance CI does not require it;
- no active governance document depends on it, except the obsolete index recording its removal;
- Decision Surface and AI learning support remain useful without client-specific ownership;
- current authority/obsolete indexes agree with the retirement;
- CI and review are green on the exact PR head before merge.
