# Document Runtime Live Observations

Status: candidate support doctrine — external implementation merged / target deployment not established.
Boundary profile: candidate_support_note.

This document governs the live-observation layer of the document vertical after the first read-only status card.

Current external implementation:

```text
repository: ifanjuang/pantheon-mvp
historical slice: #62
clean current-main replacement: #73 merged
observer: mvp_vertical.document_runtime_observer
Cockpit projection: openwebui/pantheon_document_runtime_live_status.py
synthetic helper: scripts/document_runtime_synthetic_check.py
```

The implementation being merged does not establish that any target host runs it.

## Boundary

```text
OpenWebUI exposes source-attributed observations.
The external observer reads bounded technical surfaces.
Hermes reports its native skill inventory when explicitly observed.
Paperless reports source-runtime reachability through the bounded gateway.
Docling reports its own health endpoint.
Pantheon PDP reports policy readiness/meta and validates bounded decisions.
Pantheon governs status semantics, gates and activation.
The human decides consequential activation and use.
```

Pantheon does not run the probes, schedule them, restart services or turn observations into automatic approvals.

## Required non-equivalences

```text
reachable != healthy
healthy != safe
installed != approved
skill listed != skill activated for scope
PDP ready != effect authorized
issuer verification implemented != issuer authenticated on target
issuer_authenticated != approval
Docling health endpoint responds != extraction quality established
runtime success != Evidence
runtime observation != activation decision
synthetic check pass != production adoption
```

A runtime observation set must not collapse these dimensions into one global green/red health score.

## Observation record minimum

Each source observation retains at least:

```yaml
source:
observation_source:
observed_at:
reachability_status:
```

Source-specific fields may be added without changing their meaning.

The aggregate projection declares:

```yaml
synthetic_global_health: not_computed
authority_effect: none
write_effect: false
activation_changed: false
```

## Paperless / bounded gateway

Observation source:

```text
GET <PANTHEON_PAPERLESS_GATEWAY_URL>/health
```

This may establish gateway reachability and the gateway's observed Paperless reachability. It does not establish Paperless safety, backup validity, restore readiness, professional suitability or activation.

## Pantheon PDP

Candidate observation surfaces:

```text
GET /readyz
GET /v1/meta
```

The policy credential stays server-side. `/readyz` is readiness of the policy projection, not authorization of a concrete effect.

Current effect authorization remains evaluated by the PEP from the exact preflight response. The V0 posture remains conservative:

```text
external_effect_allowed = false
canonical_effect_allowed = false
```

Issuer authentication is also decision-time data. It must not be inferred from PDP readiness, from the presence of `PANTHEON_DECISION_ISSUER_KEYS_PATH`, or from the existence of signing code.

```text
configured registry != issuer authenticated
issuer_authenticated != approval
valid decision verdict != effect authorized
```

## Docling

Observation source:

```text
GET <DOCLING_SERVE_URL>/health
```

A responding health endpoint does not establish extraction/OCR quality, professional validation, source truth or Evidence status.

## Hermes native inventory

The authoritative candidate source for whether `pantheon-document-intake` is listed in an observed Hermes installation is Hermes native inventory:

```text
hermes skills list
```

The external observer executes this fixed command only when explicitly configured on the Hermes host or an equivalent reviewed environment. It accepts no caller-provided shell fragments.

Statuses:

```text
installed_observed
not_listed_observed
not_observed
```

Without co-location/configuration, use `not_observed`, not `not_installed`.

```text
skill listed != approved
skill listed != activated
skill listed != normal Hermes model/agent invocation proven
```

## Cockpit secret boundary

OpenWebUI receives only:

```text
bounded observer URL
Cockpit read credential
```

The Cockpit must not receive:

```text
PAPERLESS_API_TOKEN
PANTHEON_POLICY_API_KEY
MVP_HERMES_API_KEY
PANTHEON_DECISION_ISSUER_KEYS_PATH
PANTHEON_DECISION_ISSUER_SIGNING_SECRET
DOCLING_SERVE_API_KEY
Paperless database credentials
```

The observer exposes no install, update, activation, mutation, approval, Knowledge-publication or Evidence-admission operation.

## Synthetic acceptance relationship

The external helper may consume the independent observations to determine only:

```text
candidate_ready_for_synthetic_intake = true | false
```

This is a technical prerequisite classification, not a safety or production verdict.

A synthetic intake remains explicitly operator-triggered and must use the installed Hermes skill transport plus the existing PEP/PDP path.

When authenticated issuer proof is explicitly required, the current external helper may additionally:

```text
operator signs the supplied synthetic human decision
-> installed skill receives a temporary signed decision
-> gateway/PEP derives the actual decision expectation
-> helper performs separate read-only PDP decision validation
   using that exact returned expectation
-> receipt records verdict + issuer_authenticated
```

Proof is valid only when:

```text
verdict = valid
issuer_authenticated = true
```

This proof does not authorize a Paperless external mutation and does not alter the current PDP V0 effect-denial posture.

## Operator-secret isolation

Issuer-signing and PDP secrets belong to the operator helper, not the Hermes skill.

The external implementation strips from the skill subprocess environment:

```text
PAPERLESS_API_TOKEN
PANTHEON_POLICY_API_KEY
PANTHEON_DECISION_ISSUER_KEYS_PATH
PANTHEON_DECISION_ISSUER_SIGNING_SECRET
```

The skill retains only its normal bounded runtime inputs such as the gateway URL and Hermes gateway credential.

```text
operator can prove issuer != skill owns issuer secret
```

## Responsibility split

### Pantheon governs

- status vocabulary and non-equivalence rules;
- Task Contract scope;
- preflight/decision-validation semantics;
- configured issuer-signature verification;
- adoption/activation state;
- Knowledge/Evidence boundaries.

### Hermes executes

- the installed document skill externally;
- native inventory observation when explicitly configured;
- no Pantheon authority function.

### OpenWebUI displays

- source-attributed observations;
- timestamps and `not_observed` states;
- no global health/safety verdict.

### Human approval remains required for

- target installation/adoption;
- activation;
- real-dossier use;
- target issuer-key provisioning;
- any future Paperless external mutation once policy permits it.

### Forbidden

- Pantheon running/scheduling the probes;
- observer installing/restarting/updating runtimes;
- `reachable -> healthy -> safe -> approved` promotion;
- fabricated Hermes installation from gateway status;
- fabricated policy authorization from `/readyz`;
- fabricated issuer authentication from registry configuration;
- treating synthetic receipts as Evidence;
- using the synthetic helper on a real client dossier.

## Current status

```text
external observer code                  merged candidate in pantheon-mvp #73
Paperless observation                   implemented candidate
Pantheon PDP readiness/meta observation implemented candidate
Docling health observation              implemented candidate
Hermes native inventory observation     implemented candidate / co-location required
OpenWebUI live projection               implemented candidate
synthetic read-only assessment          implemented candidate
optional synthetic intake helper        implemented candidate / not run on target
optional issuer-auth proof helper        implemented candidate / not run on target
target deployment                       not established
live target observations                not established
Hermes normal agent skill invocation    not proven
target issuer-authenticated decision    not proven
adoption                                not decided
activation                              not authorized
production                              forbidden pending separate review
```
