# Pantheon MVP

> Executable candidate implementation for the Pantheon ecosystem.

[Governance repository](https://github.com/ifanjuang/Pantheon-Next) · [Pantheon runtime status](https://github.com/ifanjuang/Pantheon-Next/blob/main/docs/governance/WHAT_RUNS.md) · [Package configuration](pyproject.toml)

```text
implementation: external candidate
adoption: not adopted
activation: not activated
production use: forbidden
```

`pantheon-mvp` implements operational candidates around PostgreSQL, APIs, Cockpit projections and adapters. It executes bounded workflows defined by Pantheon contracts; it does not own governance or professional authority.

## System boundary

| Component | Responsibility |
|---|---|
| **Pantheon Next** | Canonical doctrine, schemas, status, Evidence, scope and approval boundaries. |
| **pantheon-mvp** | Candidate implementation, persistence, APIs, projections and integration seams. |
| **Hermes** | External task execution, tools, skills and model/runtime bindings. |
| **Cockpit / OpenWebUI** | Review and interaction surfaces. A rendered status is not authorization. |
| **Human** | Consequential validation, rejection and authorization. |

This repository may produce candidates, observations and refusals. It must not approve truth, admit Evidence automatically, promote memory, send externally, schedule work or route providers.

## Implemented candidate surfaces

- Task Contract ingestion and SQL-scoped retrieval;
- deterministic candidate and refusal paths;
- PostgreSQL / pgvector persistence;
- Work Issues, comments, Runs and append-only material events;
- Project Document and Knowledge projections;
- structured document extraction through an optional Docling binding;
- Cockpit API, mobile Markdown editor and schema-driven card navigation;
- optional OpenWebUI and Paperless adapters;
- vendored Pantheon schemas with structural drift monitoring.

Implementation does not imply installation, health, adoption, activation or production authorization.

## Quickstart

Requirements: Python 3.11+ and Docker Compose.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[test,cockpit]"

docker compose up -d
pytest -q
```

Run the bounded synthetic example:

```bash
mvp-vertical ingest --contract dossiers/devis_reprise/task_contract.yaml

mvp-vertical run \
  --contract dossiers/devis_reprise/task_contract.yaml \
  --question "le devis correspond-il au périmètre du CCTP pour le lot 06 ?" \
  --output out/candidates.yaml
```

The runner must refuse sources and questions outside the declared Task Contract scope.

## Optional profiles

| Profile | Purpose | Status boundary |
|---|---|---|
| default | PostgreSQL + pgvector development store. | Local service availability is not adoption. |
| `documents` | Self-hosted Docling document conversion. | Extraction is derived data, not Evidence. |
| `cockpit` | API, document/knowledge surfaces and mobile editor. | UI and API success are not authorization. |
| `paperless` | Optional Paperless document-source binding. | Optional adapter; not a source of truth. |

Start the Cockpit candidate with separate development credentials:

```bash
export MVP_COCKPIT_API_KEY='dev-read-key'
export MVP_EDITOR_API_KEY='dev-editor-key'
export MVP_HERMES_API_KEY='dev-hermes-key'
export MVP_DOCUMENT_ROOT='./dossiers'

docker compose --profile cockpit up -d --build
curl http://127.0.0.1:8081/health
```

The document mount is read-only. Real credentials, real dossier access and runtime activation require a separate reviewed deployment decision.

## Repository map

| Path | Purpose |
|---|---|
| [`mvp_vertical/`](mvp_vertical/) | Python implementation, APIs, persistence and domain projections. |
| [`mvp_vertical/cockpit/`](mvp_vertical/cockpit/) | Cockpit frontend and projection modules. |
| [`mvp_vertical/vendor/pantheon/`](mvp_vertical/vendor/pantheon/) | Vendored governance schemas and upstream commit marker. |
| [`mvp_vertical/sql/`](mvp_vertical/sql/) | Additive PostgreSQL schema and migrations. |
| [`openwebui/`](openwebui/) | Optional reviewed OpenWebUI tools. |
| [`tests/`](tests/) | Contract, boundary and acceptance tests. |
| [`dossiers/`](dossiers/) | Synthetic fixtures and Task Contracts. |
| [`tools/`](tools/) | Drift, inventory and architecture-audit utilities. |

## Development rules

- Keep server contracts authoritative; Cockpit cards are projections.
- Use registries and schemas for editable fields, navigation, tags and statuses.
- Keep source data, derived structure, Knowledge, Evidence and UI projections distinct.
- Changes with consequences should use provenance, base revision, diff, idempotency and human review.
- Vendored Pantheon schemas are references with drift detection, not duplicated governance authority.
- Do not remove compatibility or apparently unused modules without checking imports, routes, scripts, deployments and tests.

## Invariants

```text
external_repo != Pantheon runtime
retrieved != truth
indexed != Evidence
runtime_success != Evidence
result_candidate != approved_result
healthy != safe
activated != task_authorized
UI status != authorization
```

## License

MIT — see [`LICENSE`](LICENSE).
