# Stable document observation route

Date: 2026-08-03

Status: architecture convergence validation trace.

## Scope

The local-CLI and network-native document runtime observers are alternative bindings that produce the same read-only observation envelope.

Both now expose:

```text
GET /documents/observations
```

The former route is removed from both applications:

```text
GET /v1/document-runtime/observations
```

No compatibility alias is retained.

## Binding distinction

```text
local observer
  -> bounded gateway/PDP/Docling probes
  -> optional local Hermes CLI inventory

network observer
  -> selected document-source binding observation
  -> bounded gateway/PDP/Docling probes
  -> authenticated Hermes skills API observation
```

These are deployment alternatives, not separate semantic owners. They retain the same observation-set contract and the same non-equivalences.

## Preserved envelope

```text
object_type = document_runtime_observation_set
synthetic_global_health = not_computed
authority_effect = none
write_effect = false
activation_changed = false
```

Each source retains its own timestamp and status dimensions.

```text
reachable != healthy
healthy != safe
installed != approved
runtime success != Evidence
runtime observation != activation decision
```

## Baseline reduction

```text
generation-named active artifacts:     0
internal versioned route files:        7 -> 5
internal versioned route declarations: 24 -> 22
```

## Boundaries

The route reads observations only. It does not install, activate, approve, update, execute, schedule, route providers, promote memory, create Evidence or compute a global health verdict.

The upstream Hermes and Pantheon policy APIs keep their own external protocol paths, including `/v1/skills` and `/v1/meta`. Those external adapter details are not internal Pantheon route generations.

## Deferred slices

```text
OpenWebUI capability/resource projections
Paperless gateway
Hermes handoff, admission, active-context and return routes last
```
