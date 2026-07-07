# Langfuse / Hermes First-Test Runbook

Status: candidate operations runbook — documented non-implemented, not executed.

This runbook translates the validated first-test posture into a controlled manual procedure.

It does not install Langfuse by itself. It does not create secrets, start containers, modify a host, change `.env`, configure Dashboard, modify Hermes, send traces or authorize external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Governing references

- `docs/governance/reference_reviews/LANGFUSE_HERMES_OBSERVABILITY_ADAPTER.md`
- `docs/governance/EXTERNAL_TOOLS_POLICY.md`
- `templates/langfuse-hermes/`
- issue `#146`

## Selected first-test posture

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

## Preconditions

Before execution, a human operator must fill and validate:

```text
target_host:
access_model: LAN_or_VPN_only
operator:
secret_storage_location:
backup_location:
rollback_owner:
first_hermes_trace_path:
```

Safe defaults if not otherwise decided:

```text
target_host: internal VM or local container host, not public
public_dns: none
reverse_proxy: none for first test
retention: 7 days
Dashboard: external link only
trace_data: synthetic only
```

If any required field is absent, stop and record a Capability Gap.

## Step 1 — Prepare runtime folder outside Pantheon

Create a runtime folder outside the Pantheon repository.

Example:

```bash
mkdir -p ~/pantheon-runtime/langfuse-hermes
cd ~/pantheon-runtime/langfuse-hermes
```

Do not run Langfuse from inside the Pantheon governance repo.

## Step 2 — Copy templates

Copy, do not symlink, the candidate templates from the repo:

```bash
cp /path/to/Pantheon-Next/templates/langfuse-hermes/docker-compose.langfuse.example.yml ./docker-compose.yml
cp /path/to/Pantheon-Next/templates/langfuse-hermes/langfuse.env.example ./langfuse.env
```

Then compare `docker-compose.yml` against the current official Langfuse compose before use.

## Step 3 — Generate secrets outside Git

Replace every `CHANGEME` value in `langfuse.env` with generated secrets.

Example helpers:

```bash
openssl rand -base64 32
openssl rand -hex 32
```

Never commit `langfuse.env`.

Never paste generated secrets into Notion, GitHub issues, AI logs, prompts or chat.

## Step 4 — Bind to LAN/VPN only

For first test, keep ports bound to localhost or a LAN/VPN interface only.

Refused for first test:

```text
0.0.0.0 public exposure
public DNS
public reverse proxy
embedded Dashboard iframe
client dossier traces
```

## Step 5 — Start local stack manually

Only after secrets and exposure are reviewed:

```bash
docker compose --env-file ./langfuse.env up -d
```

Observe services:

```bash
docker compose ps
docker compose logs --tail=100 langfuse-web
docker compose logs --tail=100 langfuse-worker
```

## Step 6 — Health check

Check health from the runtime host:

```bash
curl -fsS http://localhost:3000/api/public/health
```

Expected result: reachable health response.

If health fails, do not continue to Hermes trace emission. Record runtime_task_status as `failed` or `blocked` and open a Capability Gap.

## Step 7 — Create or confirm test project keys

Use synthetic project keys only.

Do not use client dossier names, addresses or project references.

Record only the existence of keys, never the secret key itself.

## Step 8 — Dashboard posture

Dashboard may record only:

```text
module: observability.langfuse
state: reachable | degraded | unavailable
ui_url: internal link
open_ui_action: external_link
embedded_view: false
```

Dashboard must not embed Langfuse during first test.

Dashboard must not interpret trace success as proof, approval or memory.

## Step 9 — Hermes synthetic trace

Emit one synthetic trace from a deliberately non-client path.

Synthetic trace payload must use fake data only:

```text
dossier_id: synthetic-demo
case_id: synthetic-langfuse-health
run_id: generated-test-run-id
requested_effect: read_only
approval_ceiling: C0
memory_behavior: none
scope: local_test
redaction_profile: synthetic_only
```

Forbidden in the first trace:

```text
client name
real project address
real dossier reference
real contract text
real mail body
real document extract
personal data
professional secret
```

## Step 10 — Result classification

Classify outcome separately:

```text
handoff_delivery_status: not_sent | sent | refused | failed | timeout
runtime_task_status: not_started | success | partial | failed | blocked | unknown
governance_result_status: candidate | to_verify | approved | rejected | blocked
```

For a successful first test, the only valid governance status is:

```text
governance_result_status: candidate
```

A successful trace is not validation.

## Step 11 — Retention and cleanup

First-test retention target:

```text
7_days
```

After the test, either:

```bash
docker compose down
```

or, if deleting all local test data is intended and approved:

```bash
docker compose down -v
```

Volume deletion destroys local Langfuse test data. Do not run `down -v` unless the human operator confirms no audit material must be kept.

## Rollback

Safe rollback for non-production first test:

```bash
docker compose down
```

Full cleanup, if approved:

```bash
docker compose down -v
rm -f ./langfuse.env
```

Do not delete backups or exported evidence without separate approval.

## Completion report

After execution, record in issue `#146`:

```text
host:
exposure:
health_status:
synthetic_trace_emitted: true | false
trace_contains_client_data: false
Dashboard_link_configured: true | false
embedded_view_enabled: false
retention_policy:
rollback_tested: true | false
capability_gaps:
```

## Boundary phrase

```text
The runbook may test observation.
It does not validate truth, approve action, canonize memory or govern the dossier.
```
