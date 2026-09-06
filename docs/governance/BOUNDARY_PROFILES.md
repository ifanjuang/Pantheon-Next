# Boundary Profiles

Status: active support doctrine — boundary profile vocabulary and deduplication rule.

This document defines reusable boundary profiles for Pantheon Next documents and templates.

It does not create a runtime, schema, test, CI workflow, operation, platform component, Docker configuration, environment setting, approval engine, memory engine, scheduler, queue, provider router, plugin manager, installer, updater or external action.

## Purpose

Many repository documents need to say that they do not execute, approve, remember, send, schedule, route providers or install tools.

Repeating that whole disclaimer in every document creates noise.

Use a `Boundary profile` line when a document can inherit a standard boundary.

## Rule

A boundary profile reduces repeated boilerplate.

It does not reduce responsibility.

If a document touches a protected path, proposes an external action, changes execution status, changes memory behavior, changes approval behavior or changes a runtime surface, the specific boundary must still be explicit.

## Inherited role separation

`docs/governance/ARCHITECTURE.md` (active doctrine) owns the role separation, and every profile inherits it:

```text
Hermes-compatible clients handle runtime interaction.
Hermes Agent executes externally.
Pantheon Cockpit exposes governed projections.
Pantheon Next governs consequential status.
The human decides.
```

A document that declares a `Boundary profile` therefore does not need to restate it, and should not.

Restating it is not false. It is duplication, and duplication is what makes a change to the separation expensive: retiring one named client required sweeping the same sentence out of documents one by one, because each held its own copy instead of inheriting the owner's.

Inheritance covers the generic separation only. A document that names a specific exposure, execution, governance or approval surface is making a concrete claim about that surface and must state it with the fields below.

## Boundary fields

For concrete capabilities, repos, skills, connectors, workflows or runtime changes, prefer explicit fields:

```text
exposed_by
executed_by
governed_by
approved_by
forbidden
```

Use these fields when the answer must classify who displays, who executes, who governs, who approves and what remains forbidden.

## Profiles

### `documentation_only`

Use for explanatory Markdown that states or explains an idea without proposing implementation.

Means:

```text
runtime: false
schema: false
test: false
ci: false
external_action: false
memory_promotion: false
approval_change: false
```

### `candidate_support_note`

Use for notes that propose, explore or frame a candidate direction.

Means:

```text
binding_doctrine: false
implementation: false
runtime: false
external_action: false
memory_promotion: false
automatic_approval: false
```

Candidate support can inform a later decision. It cannot promote itself.

### `active_support_doctrine`

Use for documents that clarify, coordinate or operationalize already accepted doctrine.

Means:

```text
canonical_override: false
runtime: false
implementation: false
external_action: false
memory_promotion: false
automatic_approval: false
```

Active support doctrine must remain compatible with canonical doctrine and `AUTHORITY_INDEX.md`.

### `validation_only_trace`

Use for ai_logs, reconciliation notes, local reports or audit traces.

Means:

```text
doctrine_creation: false
runtime: false
approval: false
external_action: false
memory_promotion: false
```

A trace may support a later review. It is not doctrine by itself.

### `non_executable_template`

Use for prompt, handoff, return, form, profile, flow, trace or policy templates that are not deployed.

Means:

```text
installed: false
deployed: false
executed: false
runtime_config: false
skill_installation: false
external_action: false
memory_promotion: false
automatic_approval: false
```

A template may frame future use. It does not prove that the tool, skill, flow or action exists.

### `schema_contract`

Use for declarative schema files or schema notes.

Means:

```text
validation_contract: true
runtime: false
approval: false
truth_validation: false
external_action: false
memory_promotion: false
```

Schema validity is structural only.

### `read_only_verification_surface`

Use for bounded checkers or status surfaces that report but do not act.

Means:

```text
read_only: true
runtime_execution: false
write_action: false
approval: false
external_action: false
memory_promotion: false
```

A read-only pass is not approval, truth, memory admission or runtime safety.

## Minimal usage

Recommended header pattern:

```text
Status: candidate support note — documented non-implemented.
Boundary profile: candidate_support_note.
```

or:

```text
Status: candidate support note — non-executable prompt template — documented non-implemented.
Boundary profile: non_executable_template.
```

## Required local override

Add a local boundary section when the document introduces any of these:

```text
protected path change
schema or test change
CI or workflow change
runtime status claim
external tool or connector adoption
installation proposal
update proposal
health status
rollback status
external send or write action
memory admission
approval behavior
```

## Non-equivalence reminders

Boundary profiles preserve non-equivalence rules.

Use `docs/governance/NON_EQUIVALENCE_RULES.md` as the canonical reference for recurring distinctions such as:

```text
template != implementation
schema_valid != approved
runtime_success != evidence
installed != approved
trace != doctrine
```

Do not copy the full non-equivalence list into every document. Repeat only the distinctions that are locally material.

## Forbidden use

Do not use a boundary profile to hide a consequential change.

If the change has an operational effect, name the effect.

If the effect is not approved, state that it is not approved.
