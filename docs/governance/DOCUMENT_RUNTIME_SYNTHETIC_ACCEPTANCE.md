# Document Runtime Synthetic Acceptance

Status: candidate support doctrine — external helper merged / no target run observed.
Boundary profile: candidate_support_note.

A synthetic document-runtime check is a bounded acceptance procedure for a non-production fixture. It is not production readiness, Evidence admission, approval, health authority or activation.

Current external implementation:

```text
repository: ifanjuang/pantheon-mvp
historical slice: #62
clean current-main replacement: #73 merged
helper: scripts/document_runtime_synthetic_check.py
```

## Read-only prerequisite assessment

The helper may consume independently sourced observations for:

```text
Paperless source path
Pantheon PDP readiness
Docling health endpoint
Hermes native skill inventory
```

A technical pass may be represented only as:

```text
candidate_ready_for_synthetic_intake = true
```

It must not be represented as:

```text
safe = true
approved = true
production_ready = true
activated = true
```

## Optional synthetic Project Document candidate

An operator may explicitly request a synthetic candidate intake only when:

- the Paperless source is synthetic/non-production;
- exact document and version are identified;
- exact Source Capture precedes intake;
- the Task Contract is explicitly synthetic and contains the exact `source_ref`;
- a human decision payload is supplied rather than invented by the helper;
- the installed Hermes skill transport is used;
- the existing PEP/PDP gate path is used;
- Knowledge publication and Evidence admission remain false.

The helper must not perform Paperless upload, metadata mutation, deletion or version replacement.

## Optional authenticated-issuer proof

The current repository architecture can now prove the identity of the synthetic decision issuer when the operator explicitly requests that proof and the target PDP is configured with the reviewed issuer registry.

Required operator-side inputs include the signing secret and PDP consultation credential. They are not given to the Hermes skill.

Sequence:

```text
human-supplied decision
-> operator helper signs bounded decision fields
-> temporary signed decision passed to installed Hermes skill
-> gateway/PEP derives actual effect expectation
-> synthetic intake returns that decision_expectation
-> operator helper calls PDP decisions:validate read-only
   with signed decision + exact PEP-returned expectation
-> receipt records verdict + issuer_authenticated
```

The helper may classify issuer proof as `proven` only when:

```text
verdict = valid
issuer_authenticated = true
```

It may otherwise report `not_attempted`, `not_observed` or `not_proven`.

```text
asserted decided_by != authenticated issuer
issuer_authenticated != approval
valid decision verdict != effect authorization
```

The current PDP V0 still blocks external Paperless effects regardless of a valid authenticated decision.

## Secret isolation

Before the installed skill subprocess starts, the operator helper strips:

```text
PAPERLESS_API_TOKEN
PANTHEON_POLICY_API_KEY
PANTHEON_DECISION_ISSUER_KEYS_PATH
PANTHEON_DECISION_ISSUER_SIGNING_SECRET
```

This prevents the skill transport from inheriting operator-only backing/runtime credentials.

```text
operator proof secret != skill secret
```

## Receipt semantics

Every technical receipt retains:

```text
technical_receipt_is_evidence = false
production_authorization = false
activation_changed = false
```

When the operator invokes the installed skill transport directly:

```text
agent_skill_selection_proven = false
```

because transport execution is not proof that a normal Hermes model/agent conversation selected the skill.

Issuer proof is a separate field:

```text
human_issuer_authentication_status = not_attempted | not_observed | not_proven | proven
human_issuer_authentication_proven = false | true
```

## Open proof gaps

Even a successful synthetic intake plus authenticated-issuer proof does not close:

- normal Hermes model/agent skill-selection behavior;
- real-dossier authorization;
- production adoption;
- current external Paperless mutation denial under PDP V0;
- professional extraction quality;
- human approval for activation.

## Forbidden interpretation

```text
synthetic check pass != production adoption
runtime success != Evidence
issuer_authenticated != approval
valid decision verdict != effect authorized
installed skill != approved capability
```

## Current status

```text
synthetic prerequisite helper        merged candidate in pantheon-mvp #73
synthetic Project Document intake    implemented candidate / not run on target
issuer-auth proof helper             implemented candidate / not run on target
target issuer registry               not established
target signed-decision round-trip    not established
normal Hermes agent invocation       not proven
real-dossier use                     not authorized
activation                           not authorized
production adoption                  not decided
```
