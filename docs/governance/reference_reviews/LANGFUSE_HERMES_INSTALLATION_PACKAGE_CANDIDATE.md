# Langfuse / Hermes Installation Package Candidate

Status: candidate / to verify — installation package proposal, documented non-implemented.

This document defines a bounded installation package for using Langfuse beside Hermes and exposing it from the Dashboard.

It does not deploy Langfuse, modify a host, start a container, create secrets, change `.env`, create `operations/`, create `platform/`, add runtime code, add a Dashboard route, add a Hermes SDK integration, create an approval engine, create a memory engine or authorize external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Why this package exists

PR #147 established Langfuse as an external observability reference candidate.

This package is the next controlled step: prepare installable templates and decision points before any real deployment.

The goal is to avoid turning a product choice into hidden runtime authority.

```text
Langfuse observes.
Hermes executes.
The Dashboard exposes.
Pantheon governs status, evidence, approval, scope and memory.
```

## External source basis

Current Langfuse v3 self-hosting documentation describes Docker Compose as the simplest way to run Langfuse locally or on a VM for initial deployment. Production high-availability or high-throughput deployments require a more deliberate deployment path such as Kubernetes/Helm or equivalent infrastructure.

Current Langfuse Docker Compose examples include `langfuse-web`, `langfuse-worker`, Postgres, ClickHouse, Redis and object storage such as MinIO/S3-compatible storage. Official examples include multiple `CHANGEME` placeholders for secrets and recommend restricting inbound host traffic.

Reference URLs:

```text
https://langfuse.com/self-hosting/deployment/docker-compose
https://langfuse.com/self-hosting/configuration
https://langfuse.com/self-hosting/deployment/infrastructure/clickhouse
https://github.com/langfuse/langfuse/blob/main/docker-compose.yml
```

## Placement

| Component | Layer | Role | Authority |
|---|---|---|---|
| Langfuse service | Observability layer | stores and displays traces | no governance authority |
| Hermes | Execution runtime | emits traces and metadata | no approval or memory authority |
| Dashboard | Exposure surface | shows link, health and read-only trace refs | display only |
| Pantheon | Governance layer | defines status, evidence, approval, scope and memory rules | governance authority |

## Accepted package scope

Accepted as candidate package content:

- compose template for local / single-host Langfuse test;
- env example with placeholders only;
- Dashboard module manifest candidate for link/status/read-only access;
- Hermes trace metadata contract candidate;
- preflight checklist;
- redaction and retention questions;
- healthcheck expectations;
- explicit boundary that traces are not proof.

## Refused in this package

Refused:

- real secrets;
- `.env` with values;
- Docker modification in the active runtime;
- `operations/` runbook before this package is validated;
- `platform/` deployment code;
- schema or tests;
- Dashboard implementation;
- Hermes code integration;
- automatic trace-to-Evidence-Pack promotion;
- automatic approval, memory or external action.

## Candidate file set

This work package proposes templates only:

```text
docs/governance/reference_reviews/LANGFUSE_HERMES_INSTALLATION_PACKAGE_CANDIDATE.md
templates/langfuse-hermes/README.md
templates/langfuse-hermes/docker-compose.langfuse.example.yml
templates/langfuse-hermes/langfuse.env.example
templates/langfuse-hermes/dashboard-module.langfuse.example.yaml
templates/langfuse-hermes/hermes-trace-metadata.example.yaml
ai_logs/2026-06-15-langfuse-hermes-installation-package-candidate.md
```

No `operations/`, `platform/`, `.env`, schema, tests or runtime code are created.

## Deployment posture

Recommended first posture:

```text
local_or_single_host_test
```

Not production.

Not high availability.

Not exposed publicly without reverse proxy, TLS, authentication policy and retention policy.

A production package would need a separate review for:

```text
TLS
identity and access policy
backup / restore
retention
redaction
resource sizing
upgrade path
network exposure
storage persistence
incident response
```

## Selected first-test posture

The first-test posture is now selected as candidate direction:

```text
network_exposure: LAN_or_VPN_only
public_exposure: refused
Dashboard_posture: link_only
embedded_view: refused_for_first_test
trace_payload: synthetic_only
client_dossier_traces: refused_until_redaction_review
trace_retention: 7_days
Langfuse_prompt_management: disabled_initially
Langfuse_datasets: disabled_initially
first_test_goal: health + one synthetic Hermes trace
```

This selection is not an installation. It only fixes the intended safe posture for the next implementation package.

The posture may be promoted to an operations runbook only after host, secret handling, backup and rollback are named.

## Dashboard projection candidate

The Dashboard may expose only:

```text
module: observability.langfuse
state: unconfigured | configured | reachable | degraded | unavailable
ui_url: configured external link
health_endpoint: /api/public/health or deployment-specific health URL
trace_refs: linked identifiers only
open_ui_action: external_link
embedded_view: false by default
```

The default is link-only.

Embedded read-only views remain `to_verify` because they raise authentication, clickjacking, redaction and client-data visibility questions.

For the selected first test, embedded view is refused. Only an external link and health state may be exposed.

## Hermes trace metadata candidate

Hermes may attach the following metadata to Langfuse traces when available:

```text
task_contract_id
dossier_id
case_id
run_id
result_candidate_id
evidence_pack_candidate_id
approval_gate_id
requested_effect
approval_ceiling
memory_behavior
scope
source_policy_ref
redaction_profile
```

The metadata is trace context, not governance status.

For the selected first test, Hermes must emit only synthetic, non-client data.

## Minimum preflight before real deployment

Before any real install:

```text
1. decide host: local machine, internal VM, NAS/container host or dedicated server;
2. decide exposure: LAN or VPN only for the first test;
3. decide auth: admin user, user creation policy, project keys, rotation;
4. decide retention: 7 days for first test unless explicitly changed;
5. decide redaction: synthetic-only until client-data rules are reviewed;
6. decide backup: Postgres, ClickHouse and object storage volumes;
7. decide Dashboard posture: link-only first;
8. decide first Hermes path: which skill/run emits traces first;
9. keep prompt management and datasets disabled initially;
10. record Capability Gap if any prerequisite is missing.
```

## Safe first installation shape

The safe first shape is intentionally modest:

```text
Langfuse runs locally or on an internal host.
Dashboard stores only URL and health state.
Hermes emits one test trace with non-client synthetic data.
No client dossier trace is emitted before redaction policy is reviewed.
No trace becomes Evidence Pack automatically.
No trace becomes memory.
No external action depends on Langfuse success.
```

## Exit criteria for promoting this package

This package can move from candidate to approved implementation package only when:

```text
- deployment host is named;
- exposure model is chosen;
- secret handling is defined;
- retention is defined;
- backup posture is defined;
- redaction rule is defined;
- first Hermes integration path is named;
- Dashboard posture is limited to link/status/read-only;
- rollback procedure exists;
- one synthetic trace test is planned;
- issue #146 records the decision.
```

## Boundary phrase

```text
Installing Langfuse may improve observation.
It does not validate truth, approve action, canonize memory or govern the dossier.
```
