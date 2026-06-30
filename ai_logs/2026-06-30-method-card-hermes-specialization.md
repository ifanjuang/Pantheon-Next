# AI Log — Method Card Hermes handoff specialization

Date: 2026-06-30

Actor: ChatGPT

Scope:

- Created `docs/governance/METHOD_CARD_HERMES_HANDOFF_SPECIALIZATION.md`.
- Replaced the broader #240 proposal with a short specialization that does not duplicate `CAPABILITY_PLACEMENT.md`.
- Commented on and closed PR #240 as superseded without merge.

Status:

```text
validation-only / trace
```

Modified paths:

```text
docs/governance/METHOD_CARD_HERMES_HANDOFF_SPECIALIZATION.md
ai_logs/2026-06-30-method-card-hermes-specialization.md
```

PR decision:

```text
#240 — accepted as direction, superseded as implementation.
Closed without merge.
```

Rationale:

```text
CAPABILITY_PLACEMENT.md already owns the canonical governed execution handoff.
The new file records only what Method Cards add to an already valid handoff.
```

Boundary:

```text
No runtime.
No Hermes skill.
No OpenWebUI function.
No bridge.
No connector.
No schema.
No test.
No approval engine.
No memory engine.
No queue.
No scheduler.
No provider router.
No external action.
```

Decision position recorded:

```text
Accepted:
- Method Card -> Hermes specialization is useful.
- It must remain candidate support doctrine / documented non-implemented / to verify.
- It must not redefine generic handoff doctrine.

To verify:
- AUTHORITY_INDEX.md indexing by Claude or later controlled pass.
- Relationship to #245 compact architecture method run tests.
```
