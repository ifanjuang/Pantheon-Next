# Document Runtime Live Observations

Status: candidate support doctrine — generic observation boundary; OpenWebUI adapter removed — implementation partial.
Boundary profile: candidate_support_note.

This document owns the bounded observation semantics for the document vertical. It does not own Cockpit product topology, service installation, activation, authorization, source truth, Knowledge publication or Evidence admission.

Current executable candidate observation seams remain under `implementation/mvp_vertical/`. The former OpenWebUI projection tool has been removed.

## Boundary

```text
technical observer -> source-attributed observation
Pantheon Cockpit   -> governed projection
Pantheon governance -> status meaning and gates
human              -> consequential activation/use decision
```

Hermes and selected external tools may expose native read-only observations. Their runtime state does not become Pantheon authority.

## Required non-equivalences

```text
reachable != healthy
healthy != safe
installed != approved
activated != task-authorized
PDP ready != effect authorized
issuer_authenticated != approval
runtime success != Evidence
runtime observation != activation decision
synthetic check pass != production adoption
```

No aggregate global green/red health score is authoritative.

## Observation record minimum

```yaml
source:
observation_source:
observed_at:
reachability_status:
```

Where a field is not observed, keep that state explicit rather than inferring it from another service.

## Core document path

The target core document path is product-independent:

```text
bounded local/NAS source root
-> Task Contract declared-source check
-> path containment
-> source digest / provenance
-> reviewed extraction binding when needed
-> Project Document candidate
```

```text
source reachable != source admitted
extraction result != source truth
Project Document candidate != Knowledge
Knowledge != Evidence
```

## Residual Paperless compatibility

The co-located implementation still contains Paperless-aware observer/gateway/Compose/skill code pending its separate protected consumer audit.

A configured compatibility value such as `MVP_DOCUMENT_SOURCE_BINDING=paperless_ngx` is an implementation observation, not target selection or architecture authority.

```text
Paperless absent != Pantheon degraded
Paperless absent != core document ingestion unavailable
binding string != dependency adoption
Paperless reachable != binding activated
```

The next cleanup slice must preserve the generic local/NAS path and source/provenance checks while removing Paperless-specific code with no surviving target consumer.

## Policy observations

Policy service readiness or metadata may be observed independently from a concrete effect decision.

```text
PDP reachable != effect authorized
configured issuer registry != issuer authenticated
issuer_authenticated != approval
```

Authorization remains effect-time and contract-bound.

## Extraction observations

A selected extraction service may expose a technical health observation. That observation does not establish extraction quality, professional validation, source truth or Evidence status.

## Hermes observations

Hermes-native inventory or runtime observations remain external runtime facts. A skill/tool being visible or loaded does not establish Pantheon activation or task authorization.

```text
runtime item listed != capability approved
capability activated != task authorized
```

## Secret boundary

Observation and Cockpit projection surfaces must not expose backing service tokens, database credentials, policy secrets, issuer signing material or source-system administrative credentials.

## Current qualification

```text
generic document observer seams      -> co-located executable candidate
OpenWebUI projection adapter         -> removed
core local/NAS ingestion             -> co-located candidate / live target proof external
Paperless compatibility observations -> residual / cleanup pending
live target deployment               -> not established
production adoption                  -> not decided
```

## Convergence path

After Paperless compatibility removal, retain this document only if the document vertical still needs observation semantics not already owned by generic Cockpit/control-plane doctrine. Otherwise absorb the remaining invariants into those owners and remove this file.
