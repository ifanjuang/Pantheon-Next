# Revit Execution Model

Status: support policy candidate — documented non-implemented.

This document consolidates the future Revit plugin execution posture.

It does not implement code, a queue, a scheduler, a Revit add-in, a relay, a schema, tests or runtime behavior.

## Core rule

```text
Hermes may consider broad Revit actions.
Hermes must not execute consequential actions silently.
The Revit plugin observes, preflights, executes local Revit transactions and logs.
Pantheon governs status, scope, proof, approval and memory.
```

## Minimal objects

The first implementation should stay close to these objects:

```text
Task
Action
Dependency
Blocker
WarningLevel
ReversibilityLevel
ValidationState
ResultState
ActionLog
```

## Modes

```text
sandbox_free       -> broad exploration, warnings remain visible
project_guarded    -> real project, guarded writes
production_guarded -> consequential state, higher validation
blocked_by_policy  -> visible but not executable in current mode
```

## Warning levels

```text
W0 read / observe
W1 candidate / preview only
W2 light reversible write
W3 model write with dependencies
W4 destructive or hard-to-reverse action
W5 generated or uncontrolled execution path
```

Tool visibility does not mean approval.

Runtime possibility does not mean governance permission.

## Reversibility levels

```text
R0 no model effect
R1 single transaction rollback
R2 grouped modification rollback
R3 dependent or partially reversible effect
R4 unsafe / blocked by default
```

Any write must disclose its reversibility level before execution.

## Async rule

All future model-changing requests should enter as asynchronous requests.

Actual Revit model changes must still execute only inside a controlled Revit API path and inside a named Revit transaction.

```text
request received
-> request queued
-> preview prepared
-> validation if required
-> request raised to Revit-controlled handler
-> named transaction
-> commit / rollback
-> action log
```

Async orchestration is allowed.

Uncontrolled background Revit writes are not allowed.

## Task and action state

Hermes should track the operational state of each Revit task.

```text
requested
admitted
preparing
preview_ready
awaiting_validation
executing
waiting_user
blocked
failed_recoverable
failed_terminal
completed
finalized
```

Hermes should be able to answer:

```text
what was requested;
what context was used;
what was proposed;
what was validated;
what is pending;
what failed;
why it failed;
what blockers exist;
what alternatives are allowed;
what was finalized;
what should not be retried.
```

This is operational task state, not canonical Pantheon memory.

## Dependencies and non-blocking blockers

A task may contain independent and dependent actions.

A blocker may pause one action without stopping the whole task.

```text
blocked action A
independent action B -> may continue
action C depending on A -> waits
action D sharing the same blocker -> waits or shares the blocker
```

Example:

```text
A1 capture context -> finalized
A2 check annotation family -> waiting_user
A3 create annotation -> blocked_by_dependency
A4 create report -> continues
```

Hermes must not pretend the blocked action succeeded.

## Blockers

Common blocker classes include:

```text
missing_family
pinned_element
worksharing_locked
linked_model_element
grouped_element
missing_target
stale_element_id
category_mismatch
view_not_editable
dependent_element_risk
approval_required
rollback_uncertain
runtime_error
user_cancelled
```

The repository should not exhaustively map all cases. It should define how blockers are represented, surfaced and resumed.

## User dialogue levels

```text
informational_notice
non_blocking_request
blocking_request
validation_required
elevated_validation_required
```

Example:

```text
missing annotation family -> non_blocking_request if other actions can continue
pinned target -> validation_required or elevated_validation_required
worksharing lock -> blocking_request for dependent action
hidden deletion risk -> elevated_validation_required or blocked
```

## Controlled retry loop

Hermes may propose another method after failure, but only as a controlled loop:

```text
attempt
-> observe result
-> classify result
-> update task state
-> propose next method
-> check warning level
-> validate if risk changed
-> retry or stop
```

Stop conditions:

```text
user cancels;
required context is missing;
required user action is pending;
same failure repeats;
warning level escalates beyond validation;
rollback becomes uncertain;
result is accepted and finalized.
```

## Preflight rule

Before any write, the future plugin should check at least:

```text
active document matches the request;
target view exists;
target ElementIds still resolve;
expected categories match;
pinned state is disclosed;
worksharing/editability is checked;
linked/grouped status is disclosed;
dependent element risk is disclosed;
rollback strategy is known.
```

## Finalization rule

A finalized action group must not be repeated accidentally.

Finalization should record:

```text
final status;
created/modified/deleted ids where available;
validation result;
known limitations;
manual follow-up;
do-not-repeat markers.
```

## First prototype scope

The first prototype should support only:

```text
W0 / W1 reads, context and previews;
W2 light review writes;
R0 / R1 / simple R2;
TextNote or DetailLine in sandbox/review views;
local JSONL action logs.
```

W3 should remain preview/elevated-validation.

W4 and W5 should be visible as known danger classes but blocked by default.
