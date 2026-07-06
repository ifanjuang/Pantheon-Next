# Hermes Templates

Status: non-executable Hermes template scaffold.

This directory contains candidate templates for future Hermes execution handoffs, returns and skill candidates.

They are not installed Hermes profiles, skills, tools or toolsets.

They do not execute.

## Placement

Hermes may execute under Task Contract and return candidates.

Hermes must not approve, canonize memory, mutate doctrine, merge directly or bypass approvals.

## First template classes

```text
handoffs/   future Task Contract and Context Pack input envelopes
returns/    future candidate return envelopes
skills/     future skill candidate declarations
```

## Loop candidate templates

Loop candidate templates apply `docs/governance/LOOP_GOVERNANCE_MODEL.md` to Hermes-side handoffs and returns.

```text
handoffs/loop_contract_candidate.json
returns/loop_result_candidate.json
```

They are governance-readable examples, not executable schemas.

Runnable loop mechanics, retry state, queues, checkpoints and tool calls remain in Hermes or another execution runtime.

Pantheon governs admissibility, scope, evidence, blockers, gates and status.

## Rule

Hermes done does not mean Pantheon validated.
