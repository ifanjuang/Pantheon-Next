# Nango Reference Review

Status: support review only — external connector gateway, Hermes candidate boundary and forbidden-import record.

Observed date: 2026-05-29

Reviewed sources:

- `https://nango.dev/docs/getting-started/intro-to-nango`;
- `https://nango.dev/docs/guides/auth/auth-guide`;
- `https://nango.dev/docs/getting-started/quickstart`;
- `https://nango.dev/docs/guides/functions/functions-guide`;
- `https://nango.dev/docs/getting-started/use-cases/tool-calling`;
- `https://nango.dev/docs/guides/platform/self-hosting`;
- `https://github.com/NangoHQ/nango`.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Review scope

This review evaluates Nango as an external API integration, auth and connector gateway that may support bounded Hermes-side calls to third-party APIs.

This document does not approve installation.

This document does not add a dependency.

This document does not create a Pantheon runtime, tool runtime, provider router, scheduler, queue, MCP layer, plugin manager, connector marketplace, automatic approval system, automatic memory system, OpenWebUI function, OpenWebUI tool, OpenWebUI pipe, OpenWebUI filter, OpenWebUI action or OpenWebUI pipeline.

## External project summary

Nango presents itself as an integration platform for connecting applications and agents to external APIs.

Its official documentation describes two core primitives:

```text
Auth      -> user authorization, credential storage, refresh and validation
Functions -> provider-specific integration logic executed with connected-account credentials
```

The documentation also describes action functions that may be exposed to agents through tool schemas and MCP, and functions that may be called from a backend or triggered through schedules and webhooks.

Pantheon interpretation:

```text
Nango is useful because it centralizes API auth and integration execution.
Nango is risky because it combines credentials, external effects and executable functions.
```

## Technical characterization

Nango should be classified as:

```text
external_api_integration_gateway
credential_broker
connector_proxy
external_function_execution_surface
agent_tool_calling_surface
```

It is not:

```text
Pantheon governance
Pantheon memory
Pantheon approval
Pantheon runtime
OpenWebUI cockpit
Hermes profile
Hermes skill by itself
```

A Nango connection is a credential handle for one external provider context.

A Nango action function is an external executable capability.

A Nango log is runtime trace material.

None of these objects is Canonical Memory, proof, approval or doctrine.

## Layer mapping

| Layer | Classification |
|---|---|
| Pantheon Next | governance policy, scope, approval and evidence requirements |
| Hermes Agent | optional external runtime caller under Task Contract |
| Nango | external auth, credential and connector gateway |
| OpenWebUI | cockpit exposure of consent, scope, approval, result and Evidence Pack Candidate |
| Third-party APIs | external systems with read or write effects |

## Recommended classification

```text
name: nango
classification: External Connector Gateway
pantheon_status: reference_review_only
hermes_status: optional_connector_gateway_candidate
openwebui_status: consent_and_result_exposure_candidate
memory_status: non_canonical
approval_status: not_approved_for_installation
runtime_status: external_only
```

## Valuable patterns to distill

The following patterns are useful for Pantheon if stripped of runtime authority:

```text
centralized OAuth and token refresh as external capability
connection identity separated from Pantheon memory
provider scopes declared before execution
read/write distinction at connector level
action function as Task Contract-bound capability
connector logs as Evidence Pack input, not evidence by themselves
consent screen as OpenWebUI exposure pattern
credential handles never copied into governance artifacts
```

## Forbidden imports

Pantheon must not import:

```text
Nango Functions as Pantheon workflow runtime
Nango schedules as Pantheon scheduler
Nango webhooks as Pantheon event bus
Nango MCP exposure as internal Pantheon MCP layer
Nango connector catalog as plugin marketplace
Nango logs as Evidence Pack by themselves
Nango connection state as Canonical Memory
Nango action availability as approval
Nango dashboard state as governance truth
direct OpenWebUI-to-Nango execution bypassing Hermes and Task Contract
credential handling inside Pantheon governance documents
```

## Risk classification

| Capability surface | Default risk class | Reason |
|---|---:|---|
| Read-only connector retrieval | T1 | retrieves external private or public data |
| Candidate artifact generation from retrieved data | T2 | transforms retrieved content into output candidates |
| Repository or project mutation candidate through an external API | T3/T4 | may change external project state |
| External write action such as create, update, send, publish or delete | T4 | creates third-party effect |
| OAuth setup, token handling, provider configuration or self-hosting | T5 | touches credentials, trust boundary or runtime configuration |
| Schedules, webhooks or MCP tool exposure | T5 | may create hidden execution paths |

Final approval remains governed by `APPROVALS.md` and `EXTERNAL_TOOLS_POLICY.md`.

## Task Contract requirement

A Nango-mediated action requires a Task Contract when it touches:

- private data;
- credentials or OAuth scopes;
- third-party accounts;
- external writes;
- repository mutation;
- professional dossier material;
- protected governance areas;
- memory-sensitive output;
- schedules, webhooks or MCP/tool-calling surfaces.

Minimum Task Contract checks:

```text
provider
connection handle or environment label
intended action
read/write effect
scope of accessible data
excluded providers and resources
approval level
expected Evidence Pack
credential handling rule
memory rule
rollback or correction path when relevant
```

## Evidence interpretation

Nango output may support an Evidence Pack Candidate as:

```text
Source Reference
Tool Output
External Action Trace
Connector Log Summary
Capability Gap
Risk Note
```

It must not become:

```text
Canonical Memory
Approval
Proof by itself
Doctrine
Runtime State owned by Pantheon
```

Credential values, access tokens, refresh tokens, client secrets, API keys and raw private payloads must not be stored in Evidence Packs.

## User Decision Gate triggers

Use a User Decision Gate when Nango involvement affects:

- external write actions;
- OAuth scopes or credential handling;
- provider configuration;
- self-hosting or deployment posture;
- schedules or webhooks;
- MCP/tool exposure;
- broad connector catalog activation;
- memory promotion from external data;
- repository mutation;
- professional, contractual, legal, financial, medical or safety-sensitive material;
- cross-project or cross-dossier data access.

## Decision

```text
Adopt the pattern.
Do not adopt the runtime into Pantheon.
Keep Nango external.
Route eligible execution through Hermes under Task Contract.
Expose consent, status and results through OpenWebUI only.
Represent outputs as candidates until reviewed.
```

## Final rule

```text
Nango may hold the connector keys.
Hermes may call the connector under contract.
Pantheon decides whether the call is legitimate.
OpenWebUI shows the decision surface.
```
