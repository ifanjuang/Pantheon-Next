# AI Log — Langfuse / Hermes installation package candidate

Date: 2026-06-15

## Trigger

User approved continuing after the Langfuse / Hermes observability adapter review was merged in PR #147.

## Doctrine read first

Read path followed before continuing:

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`
- `docs/governance/reference_reviews/LANGFUSE_HERMES_OBSERVABILITY_ADAPTER.md`

Important boundary retained:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

`CAPABILITY_PLACEMENT.md` states that no `operations/` content should be created before a governing documentation spec has been explicitly validated. Therefore this pass creates a candidate installation package and templates only.

## External check

Current Langfuse sources reviewed:

- `https://langfuse.com/self-hosting/deployment/docker-compose`
- `https://langfuse.com/self-hosting/configuration`
- `https://langfuse.com/self-hosting/deployment/infrastructure/clickhouse`
- `https://github.com/langfuse/langfuse/blob/main/docker-compose.yml`

Useful facts retained:

- Langfuse v3 self-hosting can be started with Docker Compose for local / VM first deployment.
- Production / HA posture requires more deliberate deployment design.
- Langfuse v3 examples include Langfuse Web, Langfuse Worker, Postgres, ClickHouse, Redis and object storage.
- Official examples include secret placeholders and recommend constrained network exposure.

## Change

Added / updated:

```text
docs/governance/reference_reviews/LANGFUSE_HERMES_INSTALLATION_PACKAGE_CANDIDATE.md
templates/langfuse-hermes/README.md
templates/langfuse-hermes/docker-compose.langfuse.example.yml
templates/langfuse-hermes/langfuse.env.example
templates/langfuse-hermes/dashboard-module.langfuse.example.yaml
templates/langfuse-hermes/hermes-trace-metadata.example.yaml
ai_logs/2026-06-15-langfuse-hermes-installation-package-candidate.md
```

## Direct-main note

The intended branch creation path failed in the connector. A first Markdown file was committed directly to `main`, then completed and accompanied by templates. The affected paths are within the allowed documentation/template/ai_log perimeter. No protected runtime path was touched.

## Classification

```text
Accepted:
- Candidate installation package for Langfuse beside Hermes.
- Template-only Docker Compose example.
- Template-only env example with CHANGEME placeholders.
- Dashboard link/status/read-only manifest candidate.
- Hermes trace metadata candidate.

Refused:
- Real deployment.
- Real `.env`.
- `operations/` runbook.
- `platform/` service.
- Runtime code.
- Dashboard implementation.
- Hermes SDK integration.
- Schema or tests.
- Automatic trace-to-proof, approval or memory promotion.

To verify:
- deployment host;
- exposure model;
- authentication policy;
- secret handling;
- trace retention;
- redaction profile;
- first Hermes trace path;
- Dashboard link-only versus embedded view.

To arbitrate:
- whether this candidate package may be promoted into an actual `operations/` runbook;
- whether real compose files live in a separate runtime repo or in this repository under an explicitly approved protected path.
```

## Boundary

Documentation and templates only.

No Langfuse service was installed.

No container was started.

No secret was created.

No Docker, `.env`, `operations/`, `platform/`, schema, test, runtime code, Dashboard implementation, Hermes integration, approval engine or memory engine was added.
