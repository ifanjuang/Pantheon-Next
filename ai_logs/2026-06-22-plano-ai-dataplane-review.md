# AI Log — Plano AI dataplane review

Date: 2026-06-22

Actor: ChatGPT

## Context

The user asked to distill `https://github.com/katanemo/plano` after discussing Hermes on Termux as a mobile runtime pattern.

Plano was reviewed as a current external reference. The repository describes Plano as an AI-native proxy and data plane for agentic applications, with agent orchestration, model routing, agentic signals, OpenTelemetry traces, filter chains, safety/moderation and memory hooks.

Relevant Pantheon context:

- Pantheon remains governance-first.
- Hermes executes.
- OpenWebUI / Pantheon Control exposes.
- Gateways, provider routers, traces, filters, schedulers, queues and runtime memory must not become Pantheon governance.

No existing Plano-specific issue or PR was found in Pantheon Next before creating the review.

## Change made

Created:

- `docs/governance/reference_reviews/PLANO_AI_DATAPLANE_REVIEW.md`

The document classifies Plano as:

- external AI gateway / data-plane reference;
- runtime routing and observability adapter candidate;
- possible filter-chain PEP carrier, subject to later review;
- possible NUC/server-side component for Hermes traffic;
- not Pantheon runtime, proof authority, approval engine, Registre Probatoire, canonical memory, scheduler, queue or autonomous orchestration authority.

## Boundary preserved

The change is documentation only.

No Plano dependency was installed.
No gateway was configured.
No data plane was created.
No model routing was enabled.
No filter chain was created.
No provider key or `.env` file was touched.
No Docker, operations, platform, schema, test or runtime file was modified.
No Hermes profile or Kanban board was changed.

## Repo state

Documented non-implemented.

## Decision status

Accepted:

- Plano as external AI gateway / data-plane reference.
- Plano as possible runtime routing and observability adapter candidate.
- Plano as possible filter-chain PEP carrier, subject to later review.
- Plano as possible NUC-side component for Hermes traffic, not Pantheon kernel.

Refused:

- Plano as Pantheon runtime.
- Plano as approval engine.
- Plano as Evidence Pack authority.
- Plano as Registre Probatoire or canonical memory.
- Plano as autonomous orchestration authority.
- Plano as hidden scheduler, queue, workflow authority or external-action authorizer.

To verify:

- Self-hosting requirements.
- Provider key handling.
- Trace export and retention.
- Filter-chain fail behavior.
- Memory hook disablement / candidate-only behavior.
- Hermes profile / Kanban compatibility.
- Local-only or private-network deployment.

To arbitrate:

- Whether Plano should be tested before or after Hermes local stack stabilization.
- Whether Plano overlaps with Langfuse, Nango, MCP policy-server or future bridge candidates.
- Whether filter chains are allowed as PEP candidates.
- Whether memory hooks are categorically disabled until Registre Probatoire implementation exists.
