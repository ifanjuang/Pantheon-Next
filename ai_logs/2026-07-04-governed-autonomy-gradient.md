# AI Log — Governed Autonomy Gradient

Date: 2026-07-04

## Scope

Created a general autonomy-gradient doctrine for governed AI use.

File created:

```text
docs/governance/GOVERNED_AUTONOMY_GRADIENT.md
```

## User decision

The user asked whether Pantheon could allow more freedom and AI autonomy.

Decision captured:

```text
Yes, but autonomy must be graduated.
AI should be free in reversible, internal, candidate and traceable zones.
AI must stop at consequential thresholds: truth, memory, approval, transmission, external action, irreversible effect and professional responsibility.
```

## Doctrine added

The document defines autonomy levels:

```text
A0 — Assisted reading
A1 — Autonomous exploration
A2 — Autonomous candidate production
A3 — Local reversible action
A4 — Consequential action with human gate
A5 — Forbidden or out-of-scope action
```

It also defines:

```text
freedom zones;
gate zones;
profiles;
Revit projection;
relationship to Governed Method Standard;
relationship to Task Contract;
minimum trace by autonomy level;
anti-patterns.
```

## Boundary

Documentation only.

No agent loop, runtime, queue, scheduler, approval engine, memory engine, connector gateway, OpenWebUI plugin, Hermes skill, Revit add-in, permission system, schema, test or external action was created.

## Relationship to existing documents

This document complements:

```text
docs/governance/GOVERNED_METHOD_STANDARD.md
docs/governance/CAPABILITY_PLACEMENT.md
docs/governance/DOMAIN_PACK_SPEC.md
docs/governance/PANTHEON_REVIT_GATE.md
```

It does not replace them.

## Authority index note

`AUTHORITY_INDEX.md` should receive a row for:

```text
docs/governance/GOVERNED_AUTONOMY_GRADIENT.md
```

Suggested row:

```text
| `docs/governance/GOVERNED_AUTONOMY_GRADIENT.md` | active support doctrine | documented non-implemented | Autonomy gradient for governed AI use: A0 assisted reading, A1 exploration, A2 candidate production, A3 local reversible action, A4 consequential action with human gate, A5 forbidden/out-of-scope. Defines freedom zones, gate zones, profiles, Revit projection and trace expectations without creating an agent, runtime, permission system, approval engine, memory engine, schema, test or external action. |
```

If `AUTHORITY_INDEX.md` has concurrent changes, avoid overwriting it without a clean full-file diff.
