# Converge MVP governed loop client and retrieval ownership

Date: 2026-08-27
Issue: #666
Role: architecture convergence
Rite: compatibility retirement
Space: MVP governed task loop
Change level: semantic

## Objective

Remove historical OpenWebUI and mandatory-pgvector assumptions from the governed MVP loop while preserving the useful nine-step governance behavior.

## Observed state

After #770 and #771, `MVP_GOVERNED_TASK_LOOP.md` still defined the loop as OpenWebUI + Hermes Agent + pgvector, assigned authentication/display responsibilities to the historical client, and referenced `OPENWEBUI_INTEGRATION.md` as an active surface owner.

PR #772 review then exposed three additional active-contract mismatches: canonical `AGENTS.md` still assigned exposure to OpenWebUI; the loop wording had weakened the implemented requirement for a conforming Evidence Pack Candidate; and the retention step no longer stated that `approve` is required in addition to separate retention authorization.

## Change

- runtime interaction is owned by Hermes Web/dashboard or another compatible replaceable Hermes client;
- Hermes Agent remains external execution owner;
- retrieval is optional/provider-agnostic, with direct source/context access valid when sufficient;
- pgvector is retained only as a possible demonstrated binding, not an architectural requirement;
- Pantheon Cockpit and existing Card owners cover governed review/status projection where useful;
- canonical `AGENTS.md` is aligned to the same Hermes client / Hermes Agent / Pantheon Cockpit / Pantheon governance boundary;
- client/session authentication remains distinct from Pantheon Decision Record authority;
- the loop requires a conforming Evidence Pack Candidate, preserving the implemented decision-record digest contract;
- Register Candidate proposal requires both a reviewed `approve` decision and explicit `retention_authorization`;
- the existing Task Contract, Evidence Pack, decision, Register and `pantheon_contracts` schema seam remain unchanged;
- add regression tests for the current responsibility split, Evidence/retention transitions and non-equivalences.

Historical earlier `ai_logs/` and dated audits are unchanged.

## Invariants

```text
retrieved != truth
runtime success != authorization
projection != persistence
provider selected != authority transfer
memory != Evidence
```

## Next

Continue the remaining active OpenWebUI incoming-link convergence. Long governance files must be edited only from complete content or bounded safe transformations; do not replace them from truncated reads.
