# 2026-08-09 — I9 Capability Passport owner convergence

Parent: #620
Audit: #645

## Finding

I5 introduced the canonical exact-binding `CapabilityActivation` owner while the existing Capability Passport still carried historical `governance.activation_state` and `governance.task_authorization` fields.

The Passport validator already returned zero activation/authorization effect, but the schema still allowed `task_authorized`, creating an unnecessary semantic overlap with Task Contract / Execution Admission.

## Consumer check

Current direct consumers use the Passport for schema validation, exact implementation/release provenance and read-only eligibility qualification. No executable task/run seam requires a positive Passport task-authorization value.

## Convergence

The Capability Passport remains the governed Capability classification and exact-release eligibility surface.

```text
Capability Passport
= capability classification + risk/interface/result rules + exact release provenance

CapabilityActivation
= scoped governance activation for one exact CapabilityBinding

Task Contract / Execution Admission
= task/run legitimacy
```

Historical Passport fields remain accepted only for compatibility:

- `activation_state` is optional, deprecated and explicitly non-authorizing;
- `task_authorization` is optional, deprecated and may only be `unauthorized`.

A Passport that claims `task_authorized` is schema-invalid rather than merely carrying a warning.

## Boundaries

```text
Passport reviewed != activated
Passport reviewed != task authorized
legacy activation hint != CapabilityActivation
exact release eligible != task authorized
Execution Admission remains the sole task/run legitimacy seam
```

No runtime, activator, installer, persistence owner, provider router, scheduler, queue, Evidence admission or H source/adapter qualification is added.