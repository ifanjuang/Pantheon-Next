# Document Runtime Status

Status: external executable candidate — read-only projection implemented / not installed.

This surface gives the Cockpit a bounded document-runtime status view without turning reachability into health, health into safety or observation into activation.

Implementation:

```text
openwebui/pantheon_document_runtime_status.py
```

The first slice reads only the bounded Paperless gateway `/health` projection.

## Displayed areas

```text
Paperless-ngx
  reachability status
  health explicitly not established by reachability
  safety explicitly not inferred

Paperless gateway
  service status
  Project Document intake surface
  native write surface

Pantheon PDP
  reachability not observed by this surface
  authorization not inferred

Docling
  reachability not observed by this surface
  extraction health not established

Hermes skill
  expected skill name: pantheon-document-intake
  installation status not observed by gateway
  native Hermes inventory identified as the observation source

Pantheon activation
  no activation/status mutation performed
```

## Non-equivalence rules

```text
reachable != healthy
healthy != safe
skill name known != skill installed
skill installed != approved
gateway healthy != PDP reachable
PDP reachable != effect authorized
runtime success != Evidence
runtime observation != activation decision
```

## Why some fields remain `not_observed`

The gateway is not the authority for Hermes native inventory, Docling health or Pantheon policy status.

The first status card therefore refuses to manufacture a global green state from partial evidence.

```text
Paperless observation source -> bounded Paperless gateway
Hermes skill installation     -> Hermes native skill inventory
Pantheon PDP status           -> Pantheon policy service observation
Docling health                -> reviewed Docling runtime observation
activation/adoption           -> Pantheon governance + human decision
```

A later aggregation layer may combine these independent observations, but each field must retain its observation source and timestamp rather than becoming one synthetic `healthy=true` flag.

## Security posture

The OpenWebUI Tool receives only the Cockpit read key and bounded gateway URL.

```text
MVP_COCKPIT_API_KEY
paperless-gateway URL
```

It does not require:

```text
PAPERLESS_API_TOKEN
PANTHEON_POLICY_API_KEY
MVP_HERMES_API_KEY
Paperless database credentials
```

The read key is sent only in the Authorization header, never in the URL.

## Current status

```text
OpenWebUI status tool          implemented candidate
Paperless reachability card   implemented candidate
health/safety separation      implemented
Hermes skill live inventory   not connected
Pantheon PDP live observation not connected
Docling live observation      not connected
Cockpit installation          not established
activation                    unchanged / not authorized
production                    forbidden pending separate review
```
