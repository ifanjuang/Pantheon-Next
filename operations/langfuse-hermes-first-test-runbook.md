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

- `docs/governance/HERMES_RUNTIME_SURFACE_REVIEW.md`
- `docs/governance/HERMES_CAPABILITY_BINDINGS.md`
- `docs/governance/EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md`
- `docs/governance/EXTERNAL_TOOLS_POLICY.md`
- `templates/langfuse-hermes/`
- historical issue `#146`

The former one-shot Langfuse review files were removed during governance cleanup. Their strategic residue is carried by the current documents above and by `docs/governance/reference_reviews/README.md`.

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
first_test_goal: health + one synthetic Hermes trace from each selected live path
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
exact_hermes_version:
exact_hermes_artifact_digest:
selected_trace_paths: api_server | runs | openwebui_chat
Langfuse_plugin_or_adapter_path:
```

Safe defaults if not otherwise decided:

```text
target_host: internal VM or local container host, not public
public_dns: none
reverse_proxy: none for first test
retention: 7 days
Dashboard: external link only
trace_data: synthetic only
selected_trace_paths: api_server, runs
```

If any required field is absent, stop and record a Capability Gap.

```text
plugin present != plugin loaded
plugin loaded != selected path instrumented
trace emitted != complete or safely redacted trace
```

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

```text
Langfuse reachable != Hermes instrumented
```

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

## Step 9 — Verify the actual Hermes instrumentation path

Before emitting a trace, verify the exact Hermes artifact and selected plugin or adapter path.

Required observations:

```text
Hermes version and artifact digest recorded
Langfuse plugin or adapter detected
plugin or adapter enabled only in the intended profile
selected path documented: api_server | runs | openwebui_chat
no client data configured
no prompt-management or dataset mutation enabled
```

The test must not infer hook delivery from repository presence, plugin discovery or a successful Langfuse health endpoint.

If the selected Hermes path cannot demonstrate that the observability hook is loaded, stop and record:

```text
capability_gap: langfuse_hook_path_not_observed
```

## Step 10 — Hermes synthetic traces

Emit one synthetic trace for each selected live path. At minimum, cover the Pantheon Runs path. Cover the OpenWebUI chat path only if it is part of the target deployment.

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
trace_path: api_server | runs | openwebui_chat
```

Forbidden in the first traces:

```text
client name
real project address
real dossier reference
real contract text
real mail body
real document extract
personal data
professional secret
hidden reasoning or unrestricted environment data
```

For each trace, verify:

```text
trace received
trace path identifiable
Task Contract / run correlation preserved when applicable
secrets absent
client data absent
tool names and statuses sufficient for technical review
retention policy applied
```

A trace that reaches Langfuse but lacks its runtime path or run correlation is a partial result, not a successful acceptance.

## Step 11 — Result classification

Classify outcome separately:

```text
handoff_delivery_status: not_sent | sent | refused | failed | timeout
runtime_task_status: not_started | success | partial | failed | blocked | unknown
governance_result_status: candidate | to_verify | approved | rejected | blocked
```

For a technically successful first test, the only valid governance status is:

```text
governance_result_status: candidate
```

A successful trace is not validation.

## Step 12 — Retention and cleanup

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

After execution, record:

```text
host:
exact_hermes_version:
exact_hermes_artifact_digest:
exposure:
health_status:
selected_trace_paths:
observed_trace_paths:
synthetic_traces_emitted:
trace_contains_client_data: false
trace_contains_secret: false
run_correlation_verified:
Dashboard_link_configured: true | false
embedded_view_enabled: false
retention_policy:
rollback_tested: true | false
capability_gaps:
```

Do not reopen or update historical issue `#146` merely to record a new runtime acceptance. A current implementation issue or acceptance record should own the execution result.

## Boundary phrase

```text
The runbook may test observation.
It does not validate truth, approve action, canonize memory or govern the dossier.
```