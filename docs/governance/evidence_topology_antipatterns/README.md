# Evidence Topology Anti-patterns

Status: active support cards — documentation-level governance support.

These cards support `EVIDENCE_TOPOLOGY_GATE.md` (removed; git history) and `EVIDENCE_TOPOLOGY_CHECKLIST.md` (removed; git history).

They are not runtime rules.

They are not schemas.

They are not tests.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Evidence topology failures often look productive from the outside.

They may show many agents, many messages, many summaries, a visible canvas or an apparently active swarm.

That activity does not prove the result.

These cards define recurring failure patterns and the correction expected by Pantheon.

## Cards

| Card | Risk |
|---|---|
| [`ANTI_PATTERN_SUMMARY_ONLY_HANDOFF.md`](ANTI_PATTERN_SUMMARY_ONLY_HANDOFF.md) | Decisive details are destroyed at handoff. |
| [`ANTI_PATTERN_SWARM_AS_AUTHORITY.md`](ANTI_PATTERN_SWARM_AS_AUTHORITY.md) | Distributed execution is mistaken for decision authority. |
| [`ANTI_PATTERN_ROLE_MEMORY_AS_CANONICAL_MEMORY.md`](ANTI_PATTERN_ROLE_MEMORY_AS_CANONICAL_MEMORY.md) | Runtime continuity is mistaken for governed memory. |
| [`ANTI_PATTERN_CONDUCTOR_AS_ZEUS.md`](ANTI_PATTERN_CONDUCTOR_AS_ZEUS.md) | A runtime orchestrator is mistaken for procedural governance. |
| [`ANTI_PATTERN_CANVAS_AS_EVIDENCE_PACK.md`](ANTI_PATTERN_CANVAS_AS_EVIDENCE_PACK.md) | Visibility is mistaken for proof structure. |

## Correction pattern

Use this correction sequence:

```text
identify topology drift
recover source-linked evidence
restore approval boundary
separate runtime state from governance state
escalate to User Decision Gate if stakes remain unresolved
```

## Final rule

```text
Activity is not evidence.
Continuity is not authority.
Visibility is not validation.
```
