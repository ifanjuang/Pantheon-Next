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

Direct current-SHA verification initially identified:

- `DECISION_SURFACE_SPEC.md` still owned an OpenWebUI-facing decision surface;
- `AI_LEARNING_REPOS_DISTILLATION.md` still contained an active destination link to `OPENWEBUI_INTEGRATION.md` and product-specific exposure language;
- `.github/workflows/governance-ci.yml` still required the integration file to exist;
- the obsolete index still described former OpenWebUI sub-documents as merged into the integration owner;
- the governance authority index still described the Decision Surface as OpenWebUI-facing.

GitHub code search was used only for candidate discovery because its index lagged behind current `main`; all changed owners were fetched directly at the exact current SHA before modification.

Review then found an additional active owner that filename-link search could not detect: `CAPABILITY_PLACEMENT.md` still assigned user visibility/decision capture and the cockpit surface directly to OpenWebUI and repeated that ownership in its placement matrix and future phases. That is an active architecture rule, not historical provenance, so the slice was expanded to converge this owner too.

## Change

- make Decision Surface a client-agnostic governed review projection;
- make the AI learning distillation client-agnostic and route Pantheon-facing UX through existing Cockpit/Card owners;
- make `CAPABILITY_PLACEMENT.md` client-agnostic: replace OpenWebUI ownership with replaceable runtime clients plus Pantheon Cockpit/Card governed projection, while retaining Hermes/Langflow/LangGraph/Langfuse/GraphRAG boundaries;
- remove the integration file from the mandatory Governance CI baseline;
- record `OPENWEBUI_INTEGRATION.md` itself as removed/refused in `OBSOLETE_AND_ABSENT_INDEX.md` and reroute the former domain/plugin-policy rows;
- align the Decision Surface authority-index row;
- delete `OPENWEBUI_INTEGRATION.md` from the working tree;
- add regression tests that forbid active governance references to the removed owner and the former explicit OpenWebUI ownership assertions;
- acknowledge the deliberate reduction of `AI_LEARNING_REPOS_DISTILLATION.md` in `.github/scripts/truncation_ack.txt` after the anti-truncation guard correctly flagged the shrink.

The existing truncation acknowledgment for the deleted integration owner remains during this deletion pass so the deliberate removal is review-visible.

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
- optional compatibility with OpenWebUI as a replaceable client;
- historical provenance in Git and dated `ai_logs`.

## Exit criteria

- `OPENWEBUI_INTEGRATION.md` no longer exists;
- Governance CI does not require it;
- no active governance document depends on it, except the obsolete index recording its removal;
- active placement doctrine does not assign cockpit/governance ownership to OpenWebUI;
- Decision Surface and AI learning support remain useful without client-specific ownership;
- current authority/obsolete indexes agree with the retirement;
- CI and review are green on the exact PR head before merge.
