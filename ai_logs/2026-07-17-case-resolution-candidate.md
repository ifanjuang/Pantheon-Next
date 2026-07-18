# Explainable Case resolution candidate

Date: 2026-07-17

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

- Updated `DOSSIER_SITUATION_INTAKE.md` with an explainable `Case Resolution Candidate`, signal families, statuses and clarification policy.
- Updated `WORKFLOW_FORGING_PROTOCOL.md` so project-specific workflow candidates depend on visible Case resolution status.
- Updated `TRIPARTITE_INTERFACE_SPEC.md` with the cross-layer candidate object, confirmation gate and Context Pack admission boundary.
- Updated `CARD_STACK_MODEL.md` so Case resolution remains independent of cards and never creates a Project record by implication.
- Added no schema, test, runtime, MCP tool, Hermes Skill or OpenWebUI component.

## Why

Professional requests often identify an Affaire indirectly through aliases, location, participants, companies, topics, phases or distinctive situations. The existing intake already required project identity and clarification, but it did not define a multi-candidate, explainable resolution object or distinguish a probable match from a confirmed Case.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none.
Authority impact: active support doctrine clarified; no canonical promotion.
Schema/test/CI impact: none.
External action: none.
Memory behavior: none; Case resolution does not admit Register content or durable scope automatically.

## Local distinctions

```text
confidence != confirmation
candidate_case != active_case
shared_company_or_topic != Case_identity
temporary_resolution_card != Project_card
select_existing_case != create_new_case
documented_contract != implemented_resolver
```

## Remaining work

- Review the qualitative signal ordering and confirmation policy.
- Decide whether a protected-path schema proposal is justified later.
- Implement any resolver only as an external Hermes-side binding.
- Design the OpenWebUI selection surface only after the interface grammar is accepted, preserving the no-card fallback.
