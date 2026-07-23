# Platform Phase B — Deployment Runbook

Status: candidate operator artifact — documented non-implemented.
Boundary profile: candidate_support_note.

This runbook is the operator handoff for Phase B of
`docs/roadmaps/PLATFORM_IMPLEMENTATION_ROADMAP.md`: deploy the policy PDP and the
reference stack, then wire the already-implemented client so a consequential
effect really routes through the chokepoint.

It documents commands; it runs none of them. It stores no secret, changes no
host and authorizes no production use. Deployment is a reviewed operator action;
adoption Gate 8 remains a separate human decision.

```text
OpenWebUI exposes.
Hermes Agent executes and enforces.
Pantheon Next governs.
The human decides consequential effects.
```

## What already exists (do not rebuild)

```text
PDP capability          Pantheon mcp-server: preflight + validate_decision (implemented)
PDP container candidate  Dockerfile.policy-api, compose.policy-api.yaml (not activated)
PEP seam                 pantheon-mvp policy_gate: enforce_consequential (implemented)
real client              pantheon-mvp policy_gate.HttpPolicyClient (implemented)
capability lifecycle     pantheon-mvp capability_manager (implemented)
reference components      docs/install/REFERENCE_PLATFORM_COMPONENTS.md
baseline handoff          docs/install/COMMON_BASELINE_RUNBOOK.md
```

Phase B installs and connects these. It writes no new application code.

## Prerequisites

```text
a Docker host the operator controls (SSH / Portainer)
the external network `ai-net` created:  docker network create ai-net
a pinned Pantheon Next checkout mounted read-only
a secret manager holding PANTHEON_POLICY_API_KEY and stack credentials
the reference components reviewed (REFERENCE_PLATFORM_COMPONENTS.md)
```

Secrets are referenced from the operator's secret manager, never committed.

## Step 1 — Deploy the policy PDP

Bring up `pantheon-policy-api` on `ai-net` from the hardened candidate. It
publishes no host port, mounts the repository read-only, drops capabilities and
receives no Docker socket.

```bash
export PANTHEON_POLICY_API_KEY="$(op read op://pantheon/policy-api/key)"   # example
docker compose -f compose.policy-api.yaml up -d
```

Acceptance (from another container on `ai-net`; the API has no host port):

```bash
curl -fsS http://pantheon-policy-api:8000/livez
curl -fsS http://pantheon-policy-api:8000/readyz
curl -fsS -H "Authorization: Bearer $PANTHEON_POLICY_API_KEY" \
  http://pantheon-policy-api:8000/v1/meta
```

`readyz` confirms the checkout is readable; it does not establish safety
(`ready != safe`).

## Step 2 — Deploy the reference stack

Deploy the components of `REFERENCE_PLATFORM_COMPONENTS.md` on `ai-net`, each
pinned: PostgreSQL/pgvector, Ollama, Hermes Agent 0.19, OpenWebUI, SearXNG,
Browserless/Chromium and any conditional extraction service a reviewed binding
selects. Follow `COMMON_BASELINE_RUNBOOK.md` for the SSH/Docker/Portainer
handoff, and its §13 acceptance — treat `/health` as an optional, version-guarded
probe and `GET /v1/models` as the authoritative Hermes check.

## Step 3 — Configure the Hermes Policy Enforcement Point

On the Hermes host, adapt the connection blueprint
`templates/hermes/connection/pantheon_policy_http.template.yaml`:

```text
base_url: http://pantheon-policy-api:8000
api_key_env: PANTHEON_POLICY_API_KEY
consequential_unavailable: fail_closed
always_block_effects_when_false: [external_effect_allowed, canonical_effect_allowed]
```

Required for Hermes 0.19 (see `HERMES_INTEGRATION.md`, Hermes 0.19 review):
**disable smart-approvals for consequential effects** so an in-runtime model
review never substitutes for the human gate. Re-verify the MCP tool names
(`mcp__server__tool`) and the `platform_toolsets.api_server` restriction against
the observed 0.19 install before enabling.

## Step 4 — Point the cockpit client at the PDP

In the `pantheon-mvp` deployment, install the `cockpit` extra (which now includes
`httpx`) and inject the real client instead of the stand-in:

```python
from mvp_vertical.policy_gate import HttpPolicyClient, governed_effect

policy = HttpPolicyClient(
    base_url="http://pantheon-policy-api:8000",
    api_key=os.environ["PANTHEON_POLICY_API_KEY"],
)
# a consequential effect now routes through the live PDP, fail-closed:
governed_effect(policy, candidate=candidate, decision_payload=decision, effect=apply)
```

The same client backs `capability_manager.governed_execute` for capability
lifecycle actions.

## Step 5 — Verify the chokepoint end to end

Use the read-only verifications the repository already ships:

```text
mcp-server verify_install / verify_exposure / run_doctor_checks on the deployment evidence
a preflight round-trip: POST /v1/policy/preflights:evaluate returns a disposition
a decision round-trip:  POST /v1/policy/decisions:validate returns a verdict
a blocked case: with the PDP stopped, a consequential effect fails closed (does not run)
```

The last check is the important one: stopping the PDP must block the effect, not
let it through.

## Rollback

```text
docker compose -f compose.policy-api.yaml down       # remove the PDP
revert the Hermes connection fragment to no policy binding
the cockpit falls back to refusing consequential effects (fail-closed), never to
  running them unchecked
```

## Boundary

```text
deployed != adopted
installed != approved
healthy != safe
PDP reachable != effect authorized
green acceptance != production authorization
```

Phase B connects reviewed candidates in one operator environment. It does not
close adoption Gate 8, authorize real-dossier use or make Pantheon a runtime.
The human decides consequential effects and any activation.
