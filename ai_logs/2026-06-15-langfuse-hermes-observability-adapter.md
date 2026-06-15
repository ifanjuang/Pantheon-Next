# AI Log — Langfuse / Hermes observability adapter review

Date: 2026-06-15

## Trigger

User asked whether an existing repository could be reused, installed near Hermes and accessed or displayed from the Dashboard. Langfuse was selected as the preferred candidate.

## Doctrine read first

Read path followed before writing:

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`
- `docs/governance/AUTHORITY_INDEX.md`

Relevant repository discussion checked:

- issue `#128` — AgentCanvas as trace-visualization reference.

## External check

Official Langfuse sources reviewed:

- `https://langfuse.com/self-hosting/deployment/docker-compose`
- `https://github.com/langfuse/langfuse`
- `https://github.com/langfuse/langfuse/blob/main/docker-compose.yml`

Useful current facts retained:

- Langfuse is an open-source AI engineering / LLM observability platform.
- Docker Compose is the simplest first self-host deployment path.
- High-availability / high-throughput deployments should not rely on Docker Compose alone.
- Langfuse integrates with common LLM observability and tracing ecosystems, including OpenTelemetry and several LLM frameworks / SDKs.

## Change

Added:

- `docs/governance/reference_reviews/LANGFUSE_HERMES_OBSERVABILITY_ADAPTER.md`

The document is placed under `reference_reviews/` because it names a specific product. This follows the tool-naming rule: generic governance documents stay abstract; product names belong in bindings, adapters, integration notes or reference reviews.

## Classification

```text
Accepted:
- Langfuse as external observability layer candidate.
- Hermes emitting trace metadata to Langfuse.
- Dashboard exposing link/status/read-only trace summary.
- Pantheon retaining authority over status, evidence, approval, scope and memory.

Refused:
- Langfuse as Pantheon runtime.
- Langfuse as approval engine.
- Langfuse as canonical memory.
- Langfuse trace as Evidence Pack or Registre Probatoire entry.
- Langfuse success as validation.

To verify:
- First Hermes trace path.
- Metadata keys.
- Redaction and visibility rules.
- Link-only versus embedded Dashboard display.
- Need for a generic Trace Candidate contract.

To arbitrate:
- Deployment mode.
- Auth/access policy.
- Trace retention.
- Whether prompt management/datasets stay disabled initially.
```

## Boundary

Documentation only.

No Docker files, `.env`, `operations/`, `platform/`, schema, test, runtime code, connector, SDK integration, service deployment, approval engine, memory engine or Dashboard implementation was added.

## Verification

Repository diff should show one governance reference-review document plus this ai_log only.
