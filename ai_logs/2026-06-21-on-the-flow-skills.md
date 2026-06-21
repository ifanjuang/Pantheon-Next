# AI log — On-the-flow skill lifecycle clarification

Date: 2026-06-21
Repository: `ifanjuang/Pantheon-Next`

## Request

User clarified that a workflow may be composed of several skills: Hermes skills, custom skills and on-the-flow skills. On-the-flow skills that work well may later be upgraded into custom skills.

## File updated

- `docs/governance/SKILL_LIFECYCLE.md`

## Change

Added an explicit on-the-flow skill path:

```text
on-the-flow use
-> workflow trace
-> post-task review
-> candidate pattern
-> manifest draft
-> validation
-> admission
-> per-task authorization
```

Also added workflow composition guidance: a workflow is not a monolith; it is a sequence or graph of bounded steps with different authorization states.

## Boundary preserved

No protected path changed.
No schema changed.
No test changed.
No runtime created.
No skill installer created.
No custom skill builder created.
No automatic skill distiller created.
No automatic admission or promotion created.
No workflow engine created.

## Doctrine retained

```text
on-the-flow != candidate != declared != admitted
custom != approved unless admitted and task-authorized
runtime success != lifecycle promotion
repeated use != admission
```
