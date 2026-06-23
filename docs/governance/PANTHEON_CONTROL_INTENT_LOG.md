# Pantheon Control — Intent Log

Status: candidate — to verify.

Date: 2026-06-21

Related issue:

```text
https://github.com/ifanjuang/Pantheon-Next/issues/192
```

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

The Intent Log is a cockpit surface for displaying Intent Candidates before they become tasks.

It exists because a runtime, module, skill or workflow may detect a next step, a missing capability, a workflow branch or a useful follow-up. That proposal must remain visible and bounded. It must not silently become a scoped task, a memory promotion, a truth claim, an approval or an external action.

## Status

Accepted:

```text
Expose Intent Candidates in Pantheon Control.
Show admissibility status, affected truth/memory/external/canonical flags, evidence requirement and approval requirement.
Let a human inspect, reject, revise or route the candidate to a Task Contract later.
```

Refused:

```text
No runtime loop.
No self-authorized task.
No automatic approval.
No automatic memory promotion.
No external action.
No schema promotion.
No operations, platform, Docker or dependency changes.
```

To verify:

```text
whether the display remains readable once fed by real Hermes workflows;
whether the statuses align cleanly with governed_execution_handoff preflight outcomes;
whether the page should be linked from the main Pantheon Control navigation once nav structure is stabilized.
```

To arbitrate:

```text
whether Intent Candidate later deserves a formal schema under schemas/;
whether the cockpit should support decision capture buttons;
whether rejected candidates should be retained, archived or periodically summarized.
```

## Display boundary

The cockpit may show:

```text
intent id;
origin runtime;
origin module;
observed context;
proposed intention;
proposed task;
target scope;
affected truth claims;
affected memory;
possible external effect;
possible canonical effect;
evidence required;
approval required;
admissibility status;
decision owner;
created / resolved dates;
trace refs.
```

The cockpit must not:

```text
execute the proposed task;
turn the candidate into a Task Contract by itself;
promote memory;
validate truth;
grant approval;
send, publish, file, notify or mutate an external system;
write a Registre Probatoire entry;
create a schema or runtime event without separate review.
```

## Candidate status vocabulary

Initial display statuses:

```text
candidate      — visible proposal, not yet reviewed;
to_verify      — plausible, needs evidence or compatibility check;
needs_approval — cannot proceed without a Decision Gate or approval path;
rejected       — refused and retained for traceability if useful;
blocked        — forbidden, out of scope or protected-path change without approval.
```

## Static cockpit implementation

A static candidate page is exposed at:

```text
docs/assets/pantheon-control/intent-log.html
```

Supporting files:

```text
docs/assets/pantheon-control/intent-log-data.js
docs/assets/pantheon-control/intent-log-ui.js
```

This is a static documentation asset. It is not a runtime, connector, database view, scheduler, queue, workflow engine or approval engine.

The sample data is fictional / illustrative and must not be treated as operational state.

## Future admission criteria

Before connecting this page to real Hermes or cockpit state, require:

```text
1. a Task Contract or workflow source that produces Intent Candidates explicitly;
2. provenance and trace refs for every candidate;
3. a visible boundary between candidate, to verify, needs approval, rejected and blocked;
4. no automatic conversion to Task Contract;
5. no automatic memory write;
6. no external effect without User Decision Gate;
7. explicit retention / deletion behavior for rejected or expired intents.
```

## Repository state

Documented and statically exposed.

Implemented only as a static cockpit asset under `docs/assets/`.

Not implemented as runtime, schema, test, operation, platform code, Docker, connector, queue, scheduler, memory engine or approval engine.
