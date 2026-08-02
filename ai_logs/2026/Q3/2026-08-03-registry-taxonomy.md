# Registry taxonomy

Date: 2026-08-03

Status: candidate support clarification — validation-only.

## Decision

Retain `Registry` as the generic technical mechanism. Do not rename the family to `Vocabulary`, because navigation and visual materials are not vocabularies.

Admit three initial Registry families only:

```text
vocabulary
projection_config
presentation
```

The technical index keeps the reserved `registry_index` kind.

## Classification

```text
tag registry        -> vocabulary
navigation registry -> projection_config
materials registry  -> presentation
status registry     -> presentation candidate pending axis audit
```

## Exclusions

Roles, Rites, governed Spaces, Capabilities, Capability Slots, Bindings, Providers and other governed business objects keep their existing owner doctrines and schemas. A Registry may later reference their stable identities without becoming their owner.

## Boundaries

```text
registry != business object model
registry != lifecycle owner
registry != runtime router
registry != authorization source
projection_config != workflow
presentation != semantic authority
capability visible != task authorized
```

No runtime, API, scheduler, queue, plugin manager, provider router, approval engine or memory promotion is introduced.
