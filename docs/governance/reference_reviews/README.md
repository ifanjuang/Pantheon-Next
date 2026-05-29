# External Reference Reviews

Status: support doctrine index — reference review navigation only.

This directory contains detailed reviews of external systems before any Pantheon distillation, Hermes candidate use or OpenWebUI exposure pattern.

It does not approve dependencies.

It does not approve integrations.

It does not define runtime behavior.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Review rule

Every external reference should be reviewed across three layers:

```text
Pantheon   -> governance distillation and forbidden imports
Hermes     -> execution candidate only, if useful and bounded
OpenWebUI  -> cockpit exposure only, not runtime authority
```

## Reviews

| Reference | File | Status | Pantheon posture | Hermes posture | OpenWebUI posture |
|---|---|---|---|---|---|
| LangGraph | `LANGGRAPH.md` | support review only | governance vocabulary and boundary stress-test | optional runtime candidate only | run state and user decision exposure only |
| Understand-Anything | `UNDERSTAND_ANYTHING.md` | support review only | structural-evidence boundary and forbidden-import record | optional structural-analysis skill candidate only | graph, result and Evidence Pack Candidate exposure only |

## Non-adoption rule

A review may recommend:

- watch;
- distill;
- reject;
- keep as Hermes candidate;
- expose as OpenWebUI template;
- archive.

A review must not be treated as:

- dependency approval;
- implementation approval;
- runtime migration;
- skill installation;
- provider choice;
- memory promotion;
- approval shortcut.

## Final rule

```text
Review first.
Distill only what survives the boundary.
Install nothing by implication.
```