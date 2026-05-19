# External Agent Pattern Keepers Roadmap Update

Date: 2026-05-19

## Summary

Updated `docs/governance/ROADMAP.md` to record a minimal set of external personal-agent architecture patterns worth preserving as roadmap-level pattern keepers.

The update keeps the patterns as distillation candidates only.

It does not adopt the external architecture.

It does not implement runtime behavior.

## Changed

Added a roadmap subsection titled `External agent pattern keepers` under Phase 1.

The subsection preserves only governance-relevant patterns:

- constitution over prompt;
- negative scope definition;
- capability map before component map;
- reversibility-based approval;
- separation of cache, context, source, evidence and memory;
- Memory Candidate discipline;
- skill `FOR` / `NOT FOR` specification for Hermes-side candidate skills only;
- mandatory dissent and contradiction preservation;
- freshness disclosure;
- correction as specification debt;
- regression review for governance behavior;
- periodic governance audit.

The subsection also explicitly rejects importing:

- persistent personal agent as system center;
- proactive headless jobs or schedulers inside Pantheon;
- unrestricted private-data access;
- self-learning loops or auto-promoted memory;
- automatic skill installation or marketplace behavior;
- hidden council, swarm intelligence or autonomous debate runtime;
- unbounded Hermes browsing of OpenWebUI storage;
- any architecture where Pantheon executes instead of governing.

## Why

The external discussion contains useful operational patterns, but its center of gravity is a persistent personal agent.

Pantheon Next must preserve the opposite boundary:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

The roadmap entry captures the useful patterns while preventing runtime drift.

## Risks and limitations

- The roadmap entry is not an implementation plan.
- The roadmap entry is not an approval to add a scheduler, auto-learning loop, memory promoter, skill marketplace or hidden debate system.
- The external source was treated as inspiration only.
- Future use still requires governed distillation into pattern cards, checklist items or Hermes candidate constraints.

## Files touched

- `docs/governance/ROADMAP.md`
- `ai_logs/2026-05-19-external-agent-pattern-keepers-roadmap.md`
