# AI intervention trace — Hermes Paperless intake binding

Date: 2026-07-23
Reconciled against current repositories: 2026-07-25
Status: validation-only trace
Boundary profile: validation_only_trace.

## Human direction

After the Paperless Capability Slot and initial-installation work, the repository owner asked to continue implementation. Before the deployment step, the owner explicitly warned that repository updates had landed and requested that current state be checked first.

This trace records the resulting binding work, later repository advances, rebase and review hardening. It is not authority, installation evidence, activation or professional approval.

## Current external implementation

The external implementation has now been merged in:

```text
repository: ifanjuang/pantheon-mvp
Paperless source adapter: #56 merged
human-decision signing producer: #66 merged
Hermes Paperless binding/PEP: #59 merged after rebase and review hardening
binding: pantheon-document-intake
```

Candidate implementation includes:

```text
AgentSkills-compatible Hermes skill
transport-only skill script
Hermes -> bounded Paperless gateway path
governed exact-version Project Document intake
Task Contract perimeter enforcement
existing Docling/store.ingest reuse
PEP -> PDP request normalization
PEP-owned decision expectation binding
PEP-owned known external-effect facts
metadata-effect digest binding
metadata live-source revalidation
malformed Task Contract refusal normalization
```

Repository merge establishes implementation only.

```text
implemented != installed
```

## Finding 1 — preflight transport mismatch

The external MVP PEP had originally passed runtime-specific candidate fields directly to the Pantheon preflight endpoint.

The active Pantheon HTTP contract expects:

```text
request
+ gate_signals
```

The external implementation now strips product-specific fields from the policy body and translates runtime effects into the generic policy contract.

```text
runtime adapter vocabulary != Pantheon policy vocabulary
```

## Finding 2 — decision expectation ownership

A caller-controlled `decision` plus caller-controlled matching `expectation` is insufficient effect binding.

The external PEP derives:

```text
required ceiling
required scope
object identity
expected digest
```

from the Task Contract, exact source and requested operation, then uses those PEP-owned facts for decision validation.

## Repository update — authenticated issuer implementation

The earlier version of this trace classified human-decision issuer authentication as not implemented. That statement became obsolete after later repository work.

Pantheon Next #473 added optional cryptographic issuer verification to the PDP when an operator-provided read-only issuer registry is configured. External `pantheon-mvp#66` added the matching HMAC decision-signing producer.

Current classification:

```text
issuer signature verification implementation -> implemented in PDP
matching signing producer                    -> implemented externally
live target issuer registry                  -> not established
signed decision delivery on target           -> not established
issuer_authenticated round-trip              -> not proven
```

Preserved distinctions:

```text
asserted decided_by != authenticated issuer
issuer verification implemented != target issuer configured
issuer_authenticated != approval
valid decision verdict != effect authorization
```

The unresolved item is now deployment proof, not absence of architecture.

## Finding 3 — current PDP V0 does not authorize external effects

The active Pantheon preflight contract keeps:

```text
external_effect_allowed = false
canonical_effect_allowed = false
```

Therefore an eligible candidate-work disposition and a valid decision — signed or not — do not authorize a native Paperless PATCH/upload.

Current intended behavior:

```text
Project Document candidate intake
  external_effect = false
  writes_state = true
  -> may continue as candidate work when the remaining gates validate

Paperless PATCH/upload
  external_effect = true
  -> blocked under current PDP V0
```

A future reviewed Pantheon policy version may change authorization semantics. Hermes cannot infer that change itself.

## Review hardening before #59 merge

The rebased external #59 received three actionable review findings. All were fixed and the full CI passed before merge.

### External-effect downgrade refusal

Known Paperless external executors now supply PEP-owned effect facts after caller normalization. A caller cannot bypass `external_effect_allowed=false` with a nested `request.external_effect=false`.

```text
caller request flag != executor fact
```

### Live-source revalidation before metadata mutation

Paperless stores non-content metadata on the root document while bytes may have versions. The external gateway now re-reads the selected exact version immediately before a future metadata PATCH and, for the real Paperless client, compares current/latest bytes with the approved capture digest.

```text
source changed after decision -> metadata PATCH refused
```

A new capture and decision are required.

### Malformed Task Contract refusal

YAML/read/encoding failures are normalized to `ContractError`, so malformed Task Contract input returns the bounded client refusal path rather than an internal 500.

## Skill secret boundary

The Hermes skill receives only:

```text
PANTHEON_PAPERLESS_GATEWAY_URL
MVP_HERMES_API_KEY
```

It does not receive:

```text
PAPERLESS_API_TOKEN
PANTHEON_POLICY_API_KEY
PANTHEON_DECISION_ISSUER_KEYS_PATH
issuer signing secret
Paperless database credentials
```

The complete skill package contains both `SKILL.md` and its bundled transport script. Installation must retain the package, not only copy the prose.

## Preserved separation

```text
Paperless stores source bytes/versions and executes native DMS operations.
Docling executes structured extraction.
Hermes executes the skill/orchestration.
The external gateway acts as PEP adapter.
Pantheon supplies policy/preflight/decision-validation data, optionally verifies configured issuer signatures, and governs status.
OpenWebUI exposes.
The human decides consequential effects and activation.
```

## Status after reconciliation

```text
external skill implementation           merged candidate
PEP request normalization               merged candidate
PEP-owned effect expectation            merged candidate
PEP-owned external-effect facts         merged candidate
exact-version Project Document intake   merged candidate
metadata source revalidation            merged candidate
Paperless external mutation path        implemented but blocked by current PDP V0
issuer signing producer                 merged / not connected to target
PDP issuer verification                 implemented / target registry not proven
skill target installation               not established
Paperless target installation           not established
live Hermes -> gateway -> PDP proof      not established
live signed-decision issuer proof        not established
target health                            not established
adoption                                 not decided
activation                               not authorized
real-dossier production                 forbidden pending review
```

No target runtime installation or activation is claimed by this trace.
