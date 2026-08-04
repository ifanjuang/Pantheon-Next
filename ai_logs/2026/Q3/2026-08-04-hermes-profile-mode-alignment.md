# Hermes profile mode alignment — 2026-08-04

Status: completed repository change candidate. No Hermes profile was installed, configured, activated or authorized.

## Objective

Align the existing functional Hermes profile constitution with the runtime-mode separation established by the Hermes ecosystem adaptability review.

## Existing state verified

```text
hermes/profiles/README.md
hermes/profiles/PROFILE_CONSTITUTION.md
hermes/profiles/_base/base-soul-rules.md
tests/test_hermes_ecosystem_adaptability.py
```

The repository already distinguished functional profiles such as `doc-intake`, `evidence-review` and `repo-maintainer`. The merged runtime review separately introduced `pantheon-governed` and `assistant-personal` as runtime postures.

Creating parallel `*-governed` functional profile folders would have duplicated the existing profile model.

## Decision

```text
functional profile
+ pantheon-governed runtime mode
+ admitted Task Contract
+ explicit tool allowlist
= candidate execution posture
```

All functional profiles used for Pantheon work inherit `pantheon-governed`.

`assistant-personal` remains a separate non-governed runtime mode and must not receive Pantheon Task Contracts or professional task authorization.

## Required governed posture

```text
external memory provider off
automatic runtime recall forbidden
automatic runtime memory writes forbidden
hidden OpenWebUI memory injection forbidden
hidden OpenWebUI automatic RAG forbidden
explicit named profile route
explicit tool allowlist
no silent provider/model override
candidate-only output
```

## Observation boundary

A named Hermes API route may show that a profile-specific endpoint answered. It does not prove that external memory is disabled or that the profile is safe.

```text
profile route reachable != profile safe
provider-specific tool absent != external memory proven off
runtime mode configured != task authorized
```

An unobserved runtime mode, memory posture or tool surface leaves the profile `not_qualified` and produces a Capability Gap.

## Files changed

```text
hermes/profiles/README.md
hermes/profiles/PROFILE_CONSTITUTION.md
hermes/profiles/_base/base-soul-rules.md
tests/test_hermes_ecosystem_adaptability.py
```

## Non-effects

```text
no runtime
no profile installation
no profile configuration
no memory provider selection
no OpenWebUI configuration
no distribution-lock change
no task authorization
no governance authority change
```
