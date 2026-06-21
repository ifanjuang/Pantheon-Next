# AI log — Intent Log cockpit exposure

Date: 2026-06-21

Status: static cockpit exposure, documented non-runtime.

## Trigger

User said: `On expose` after the Intent Candidate placement review.

Interpretation:

```text
Decision Zeus: expose Intent Candidates in the cockpit.
```

## Source documents read

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`

## Related discussions checked

- PR #67 comments around Pantheon Control dashboard, machine inventory, logs, metrics and display-only boundaries.
- GitHub issue search for cockpit / intent / Pantheon Control / Intent Candidate.

## Issue created

- #192 — `Expose Intent Candidate log in Pantheon Control`

Accidental placeholder issues were created during connector use and immediately closed as not planned:

- #193
- #195
- #196
- #197
- #198

These placeholders contain no doctrine, no action and no implementation.

## Decision

Accepted:

```text
Expose Intent Candidates as a Pantheon Control display-only surface.
Show admissibility status, affected truth/memory/external/canonical flags, required evidence and required approval.
Use fictional/static data until a real Hermes workflow produces candidate state.
```

Refused:

```text
No runtime loop.
No self-authorized task.
No automatic approval.
No automatic memory promotion.
No external action.
No schema promotion.
No operations, platform, Docker, dependency, tests or MCP changes.
```

To verify:

```text
readability with real Hermes workflow data;
alignment with governed_execution_handoff preflight outcomes;
whether the page should be linked from the main Pantheon Control nav once nav structure is stable.
```

To arbitrate:

```text
formal schema under schemas/;
decision capture buttons in cockpit;
retention / archiving behavior for rejected or expired intents.
```

## Files added

- `docs/governance/PANTHEON_CONTROL_INTENT_LOG.md`
- `docs/assets/pantheon-control/intent-log.html`
- `docs/assets/pantheon-control/intent-log-data.js`
- `docs/assets/pantheon-control/intent-log-ui.js`
- `ai_logs/2026-06-21-intent-log-cockpit-exposure.md`

## Repo state

Static cockpit exposure exists under `docs/assets/`.

This is not a runtime implementation. It does not connect to Hermes, OpenWebUI, a database, an API, a queue, a scheduler, a memory engine, an approval engine or a connector.

The displayed sample data is illustrative only.
