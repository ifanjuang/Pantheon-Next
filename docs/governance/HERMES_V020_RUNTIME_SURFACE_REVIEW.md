# Hermes 0.20 Runtime Surface Review

Status: candidate external-runtime review — reviewed release, not installed, activated or task-authorized.
Boundary profile: external_reference_review.

## Observed release

Official upstream state reviewed on 2026-08-04:

```text
repository: NousResearch/hermes-agent
version: 0.20.0
release_date: 2026.8.3
release_commit: 3c27eb6234bf91b8ceee9e9071591b31e9b148cb
release_name: The Herald Release
```

The official release commit describes voice, A2A v1.0, outbound webhooks,
grounded citations and the desktop platform wave. The release source also
reports `hermes_cli.__version__ = "0.20.0"`.

External release metadata informs adapter review only. It does not govern
Pantheon and does not prove that any local Hermes installation runs this
artifact.

## Existing bridge compatibility

The Hermes 0.20.0 API-server documentation at the release commit still exposes:

```text
GET  /v1/capabilities
GET  /v1/toolsets
POST /v1/runs
GET  /v1/runs/{run_id}
GET  /v1/runs/{run_id}/events
POST /v1/runs/{run_id}/stop
```

`/v1/capabilities` continues to advertise the run-submission, run-status,
run-events and run-stop features used by the candidate MVP observer.

The existing Pantheon run binding may therefore remain the candidate binding
for 0.20.0, subject to a real-instance observation and acceptance run. This
review does not claim wire compatibility on an unobserved installation.

## Surface mapping

| Hermes 0.20 surface | Placement | Pantheon rule |
|---|---|---|
| A2A v1.0, streaming and orchestration | external execution and delegation runtime | A2A peers are runtime endpoints, not Pantheon Roles. Each consequential delegation remains bounded by Task Contract, scope, return status and human gates. Runtime anti-loop limits narrow execution but do not grant legitimacy. |
| Trusted A2A peers | runtime trust configuration | trusted peer does not mean approved capability, admissible source or authorized task. Peer identity and permitted effects remain explicit. |
| Push notifications and outbound webhooks | external-effect transport | every consequential delivery requires an approved destination, payload scope, idempotency, trace and revocation path. Runtime delivery success is not acceptance or Evidence. |
| Grounded citations | provenance-bearing runtime output | citations may become source references or Evidence candidates after verification. Retrieved or cited does not mean true, admissible or sufficient. |
| Streaming voice, barge-in and wake words | runtime input/output surface | microphone access, wake-word listening, recording, retention and external TTS processing require explicit deployment and user decisions. A spoken instruction is not by itself a Pantheon approval signal. |
| Desktop platform and multiple UI surfaces | runtime exposure surface | additional windows and controls expose runtime state only. UI state does not create authorization, canonical status or Evidence. |
| Per-request `model`, `provider` and `model_options` on `/v1/runs` | runtime provider-routing surface | the Pantheon candidate binding continues to omit these fields. Provider/model selection remains external runtime configuration and must not be silently inferred from a Task Contract. |
| Existing smart approvals | runtime approval mechanic inherited from 0.19 | an in-runtime model assessment remains distinct from human approval and must not authorize consequential effects. |

## Adapter decision

```text
runtime_target: 0.20.0
kernel_change_required: false
run_binding_change_required: false
observer_contract_change_required: false
real_instance_observation_required: true
runtime_artifact_digest_required_before_observed: true
composed_acceptance_required_before_qualified: true
installation_effect: none
activation_effect: none
task_authorization_effect: none
```

The distribution example and candidate operational lock may target `0.20.0`.
They must retain:

```text
artifact_digest: null
installation_state: not_observed
activation_state: not_activated
task_authorization_state: not_authorized
acceptance_state: not_run
```

until an operator observes the exact installed artifact and executes the
bounded acceptance procedure.

## Required live checks

Before any 0.20.0 distribution is marked `observed` or `qualified`:

1. record the installed Hermes package or image digest;
2. run the read-only `/v1/capabilities` and `/v1/toolsets` observation;
3. verify the active tool allowlist;
4. verify that the Pantheon run-binding payload contains no `model`, `provider`
   or `model_options` override;
5. execute one admitted read-only run and one one-shot reconciliation;
6. confirm that no A2A, webhook, voice, messaging or provider-routing surface
   was activated by the composition;
7. retain the runtime trace as a technical observation, not Evidence.

## Non-equivalences

```text
release reviewed != release installed
version target updated != artifact observed
Runs API documented != live instance compatible
trusted peer != approved actor
webhook configured != external effect authorized
citation present != Evidence admitted
voice command received != human approval recorded
runtime success != Evidence
```
