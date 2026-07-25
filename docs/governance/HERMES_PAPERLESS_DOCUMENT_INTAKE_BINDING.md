# Hermes Paperless Document Intake Binding

Status: candidate support doctrine — external implementation candidate exists / not installed / not activated.

This document records the governed placement of the external Hermes skill `pantheon-document-intake` and its Paperless gateway binding.

It does not install a Hermes skill, create a runtime, authorize a Paperless write, create a scheduler/queue, store a secret, authenticate a human decision issuer by itself or promote any document to Knowledge or Evidence.

```text
OpenWebUI / Cockpit exposes.
Hermes Agent executes the skill.
Paperless-ngx executes native document operations.
Docling executes structured analysis.
The external MVP gateway is the Policy Enforcement Point adapter.
Pantheon Next PDP governs/preflights/validates and may authenticate configured issuer signatures.
The human decides consequential effects.
```

## Capability placement

```text
abstract capability
  document_source_management

preferred source runtime
  paperless_ngx

higher-level Hermes binding
  pantheon-document-intake

analysis binding
  document_analysis -> docling
```

The skill composes reviewed capabilities. It does not make Paperless or Docling part of Pantheon itself.

## External implementation candidate

Observed external implementation candidate:

```text
repository: ifanjuang/pantheon-mvp
PR: #59
skill package: pantheon-document-intake directory in the external PR
gateway: mvp_vertical.paperless_gateway
PEP seam: mvp_vertical.policy_gate
policy adapter: mvp_vertical.policy_request
intake adapter: mvp_vertical.paperless_ingestion
issuer-signing producer: mvp_vertical.decision_signing (merged separately in #66)
```

Repository status alone does not establish installation, health, activation, adoption or production suitability.

## Skill surface

Candidate read operations:

```text
search
inspect
capture exact Paperless version
task observation
```

Candidate governed operations:

```text
intake exact version as Project Document candidate
update Paperless operational metadata mirror
```

Explicitly absent from this first binding:

```text
free upload
source deletion
version replacement
permission mutation
Knowledge publication
Evidence admission
memory promotion
Paperless AI activation
remote OCR activation
outgoing webhook activation
scheduler or background retry loop
```

## Secret boundary

The Hermes skill may receive only the bounded gateway endpoint and Hermes gateway credential:

```text
PANTHEON_PAPERLESS_GATEWAY_URL
MVP_HERMES_API_KEY
```

The Hermes skill must not receive:

```text
PAPERLESS_API_TOKEN
PANTHEON_POLICY_API_KEY
Paperless database credentials
issuer signing key
```

Those remain server-side/operator runtime secrets.

```text
skill can call gateway != skill owns backing credentials
secret reference != secret value
```

## Exact-version intake

The Project Document intake candidate follows:

```text
Paperless exact document/version
-> Source Capture candidate + SHA-256
-> Task Contract declared-source check
-> PEP derives effect requirements
-> Pantheon preflight
-> human decision validation against PEP-owned requirements
-> optional issuer-signature authentication when registry is configured
-> existing external store.ingest
-> Docling/direct extraction
-> Project Document candidate
-> paperless_source_bindings
```

The source read occurs before policy consultation only to identify the exact proposed object and digest. State mutation occurs after the chokepoint.

The Task Contract must already declare the generated Paperless `source_ref`.

```text
Paperless visibility != Task Contract scope
source readable != source admitted
```

A mismatch stops before persistence.

## PEP-to-PDP request contract

The external PEP must translate runtime-specific effects to the generic internal policy contract before consulting Pantheon.

Preflight body:

```text
request
  intent
  external_effect
  writes_state
  transmission_requested
  memory_promotion_requested
  professional_position
  financial_or_contractual_effect
  scope

gate_signals
  task_contract_ref
  evidence_pack_candidate_ref
  human_decision_ref
  human_decision_level
```

Paperless-specific implementation keys are runtime trace data and must not be treated as policy vocabulary.

Known runtime effect facts are PEP-owned. A caller may add trace/context but may not downgrade a known Paperless upload or metadata PATCH to `external_effect=false`.

```text
caller request flag != executor fact
external Paperless executor -> external_effect = true
```

## Decision expectation ownership

A runtime caller must not be able to define both a decision and the expectation against which that decision is checked.

For this binding the PEP derives:

```text
required_ceiling <- Task Contract
required_scope    <- Task Contract
object_identity   <- operation + exact Paperless identity + Task Contract
expected_digest   <- operation + Task Contract digest + exact source digest + effect payload
```

The caller may provide the human decision record, but caller-supplied expectation values do not override these effect requirements.

```text
caller expectation != effect requirement
matching fabricated decision+expectation != valid effect binding
```

## Human issuer authentication — implementation available, target proof open

Binding the decision to exact PEP-owned object/digest/scope/ceiling establishes effect integrity. It does not, by itself, prove who issued the decision.

The repository has now advanced beyond the earlier architecture gap:

```text
Pantheon PDP (#473)
  optional read-only issuer key registry
  verifies HMAC signature over bounded decision fields
  surfaces issuer_authenticated

pantheon-mvp (#66)
  decision_signing.py producer
  emits the matching HMAC signature
```

Therefore the current classification is:

```text
decision field validation             implemented/available in PDP
PEP-owned expectation binding         external implementation candidate
issuer-signature verification         implemented in PDP when registry configured
matching signature producer           implemented in external MVP
live target issuer registry           not established
signed decision delivery to this path not established
issuer_authenticated round-trip       not proven
```

A caller-provided `decided_by` string without a verified signature remains insufficient when authenticated issuer proof is required.

```text
asserted decided_by != authenticated issuer
issuer verification implemented != target issuer configured
issuer_authenticated != approval
valid decision verdict != effect authorization
```

## Current Pantheon PDP V0 effect limit

The current bounded Pantheon policy preflight is deliberately conservative.

For V0:

```text
external_effect_allowed = false
canonical_effect_allowed = false
```

Therefore:

### Project Document candidate intake

The candidate intake request is represented as:

```text
external_effect = false
writes_state = true
memory_promotion_requested = false
```

It may proceed only as candidate work when the remaining preflight and human-decision requirements are satisfied.

```text
Project Document candidate write != canonical truth mutation
Project Document candidate != Knowledge
Project Document candidate != Evidence
```

### Native Paperless metadata/update/upload effects

A Paperless PATCH/upload is an external runtime effect.

Under the current PDP V0:

```text
external_effect_allowed = false
```

so the external PEP must block the native effect even when the decision fields and issuer signature validate.

The implementation may expose the governed command and test its future authorization branch with a deterministic stand-in, but deployment must treat the current live PDP response as authoritative.

```text
implementation present != external effect authorized
valid decision != override of PDP denial
issuer_authenticated != override of PDP denial
```

A future policy version may add or change effect authorization semantics only through a reviewed Pantheon change. Hermes may not infer that authorization itself.

## Operational metadata mirror

The candidate metadata path binds the exact change payload into the expected digest:

```text
Task Contract digest
+ exact Paperless source hash
+ requested metadata changes
```

Changing tags, custom fields, document type or another allowlisted field changes the effect digest.

Because Paperless keeps non-content metadata on the root document while file bytes are versioned, the external PEP also revalidates the source immediately before a metadata PATCH. The exact selected version is re-read and the real Paperless client compares the current/latest document bytes to the approved capture hash. A newer/different source requires a new capture and decision.

```text
approved historical capture != authority to classify changed live bytes
source changed after decision -> PATCH refused
```

The Classification Candidate remains trace/context only:

```text
Classification Candidate != decision expectation
Paperless tag != Project Document Link
Paperless custom field != canonical business classification
```

## Knowledge boundary

The skill intentionally stops after Project Document candidate intake.

```text
Paperless Source Capture
-> Project Document candidate
-> derived extraction/projection
-> optional later Knowledge publication under the existing governed Knowledge path
```

It does not call Knowledge publication automatically.

```text
Source Capture != Knowledge
Project Document != Knowledge Item
Knowledge != Evidence
```

## Installation posture

Hermes supports skills with `SKILL.md` plus supporting `scripts/`, `references/` and templates. The reviewed installation mechanism must retain the complete skill directory, not only recreate its prose manually.

Installation remains an operator/Hermes action:

```text
skill package available != installed
installed != enabled
visible in /skills != capability approved
skill loaded != task authorized
```

The exact source commit/URL must be pinned or recorded before installation.

## Capability Slot state

```text
capability: document_source_management
binding: paperless_ngx + pantheon-document-intake
external implementation: implemented candidate in pantheon-mvp PR #59
installation: not established
health: not established
update: source version available / authorization not implied
activation: not authorized
real dossier scope: not authorized
production adoption: not decided
```

## Responsibility map

```text
Pantheon governs
  capability status
  Task Contract scope
  preflight classification
  decision validation contract
  configured issuer-signature verification
  Knowledge/Evidence boundaries
  activation/update/rollback status

Hermes executes
  skill procedure
  bounded gateway calls
  candidate orchestration

Paperless executes
  native source reads/search/tasks
  native metadata mutation only when explicitly authorized by policy and source revalidation passes

Docling executes
  structured extraction

OpenWebUI exposes
  source inbox and Project Document views

Human approves
  consequential decisions
  installation/adoption/activation
  target issuer key provisioning

Forbidden
  Hermes self-approval
  direct Paperless secret exposure to the skill
  direct Paperless database mutation
  PDP-denial override
  issuer-authentication bypass
  scope widening
  automatic Knowledge/Evidence promotion
  Pantheon-owned runtime/scheduler/queue/plugin manager
```
