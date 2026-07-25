# Live observer deployment note

Status: candidate operator note — no deployment or activation performed.

The `mvp_vertical.document_runtime_observer` service is intended to run on the private runtime network. This repository does not claim that it is deployed.

Required server-side inputs:

```text
MVP_COCKPIT_API_KEY
PANTHEON_PAPERLESS_GATEWAY_URL
PANTHEON_POLICY_API_URL
PANTHEON_POLICY_API_KEY
DOCLING_SERVE_URL
DOCLING_SERVE_API_KEY              optional
MVP_HERMES_INVENTORY_MODE          disabled by default
HERMES_CLI_PATH                    hermes by default
```

Recommended default:

```text
MVP_HERMES_INVENTORY_MODE=disabled
```

Enable `local_cli` only when the observer is intentionally placed on the Hermes host (or another reviewed environment where the native Hermes CLI represents the target runtime). Otherwise the Hermes skill status remains `not_observed`.

The service exposes only:

```text
GET /health
GET /v1/document-runtime/observations
```

The observation endpoint requires the Cockpit read key. It has no write, install, update, activation, restart or approval route.

The service should not be internet-published. It is a private read projection for the Cockpit and synthetic operator checks.

Deployment success would establish only that this observer process and its configured probes can run. It would not establish safety, adoption, professional readiness or production authorization.
