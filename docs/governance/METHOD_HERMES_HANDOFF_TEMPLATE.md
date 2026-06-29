# Method Hermes Handoff Template

Status: candidate support template — bounded handoff template for projecting Method Cards into Hermes execution.

Runtime status: non-executable.

This document defines a reviewable template for handing a Method Card or Method Proposal Candidate from Pantheon to Hermes.

It does not implement a Hermes skill, profile, router, queue, scheduler, workflow engine, approval engine, memory engine, connector, schema, test or external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

A Method Card structures work. Hermes executes only a bounded task. Pantheon keeps status, proof, memory, scope, approval and external-action boundaries.

This template answers:

```text
Why is Hermes being called?
Which Method Card structures the call?
Which sources may enter?
Which outputs may return?
Which outputs are forbidden?
Where must Hermes stop?
Which gate appears if the result becomes consequential?
```

The template is a governance artifact, not an executable configuration.

## Relationship with existing doctrine

This document does not replace Task Contracts, Capability Placement or the general governed execution handoff boundary.

It specializes the handoff for one use case:

```text
A Role has proposed or selected a Method Card for a Task,
and Hermes may execute a bounded candidate-producing step.
```

## Final invariant

```text
A Method Hermes Handoff lets Hermes work.
It does not let Hermes decide.
It does not let Hermes validate.
It does not let Hermes remember.
It does not let Hermes act externally.
```

The validated remains.
