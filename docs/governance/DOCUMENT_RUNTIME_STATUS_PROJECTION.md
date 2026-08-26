# Document Runtime Status Projection

Status: candidate support doctrine — generic status-projection boundary; OpenWebUI adapter removed — implementation partial.
Boundary profile: candidate_support_note.

This document owns only the document-runtime observation-to-Cockpit projection boundary. It does not own service lifecycle, installation, health truth, capability activation, task authorization, Evidence or runtime execution.

The former OpenWebUI status tool has been removed. Current product display responsibility belongs to the Pantheon Cockpit and its existing projection owners.

## Core rule

```text
technical observation -> qualified observed field
Pantheon governance    -> status meaning / non-equivalence
Pantheon Cockpit       -> projection
human                  -> consequential decision
```

No layer may infer a stronger state than its source demonstrates.

```text
reachable != healthy
healthy != safe
installed != approved
activated != task-authorized
PDP ready != effect authorized
runtime success != Evidence
projection != persistence
```

## Observation contract

A projected field should retain, where applicable:

```text
source
observation_source
observed_at
observed value/status
explicit unknown or not_observed state
```

`not_observed` is a valid result. Missing evidence must not be converted into a positive or negative claim.

## Product boundary

The current target does not require a product-specific status adapter.

```text
OpenWebUI adapter -> removed
Pantheon Cockpit  -> governed status projection owner
```

The removed adapter carried no independent source/persistence authority; therefore its deletion does not delete document identity, source provenance, Knowledge or Cockpit Card capabilities.

## Residual Paperless compatibility

Paperless-specific observer/gateway code still exists pending its own protected consumer audit. Any Paperless observation is compatibility data only and cannot restore Paperless as a selected binding.

```text
Paperless reachable != Paperless selected
Paperless absent != core ingestion unavailable
Paperless observation != architecture dependency
```

Generic local/NAS document ingestion remains distinct from optional DMS compatibility.

## Policy and security boundary

Status projection must not expose backing secrets or infer authorization from technical probes.

```text
policy service reachable != proposed effect allowed
issuer authenticated != approval
source readable != source admitted
```

Credentials, source-system tokens, database credentials and signing material remain outside display projections.

## Current implementation qualification

```text
generic Cockpit projection foundations -> executable candidate
OpenWebUI document status tool          -> removed
Paperless compatibility observation    -> residual; cleanup pending
live target deployment                  -> not established by repository state
production adoption                     -> not decided
```

## Convergence path

If removal of the remaining Paperless compatibility leaves no document-specific status rule beyond generic Cockpit/control-plane semantics, absorb these remaining rules into the existing Cockpit/control-plane owners and delete this document rather than preserving a parallel doctrine.
