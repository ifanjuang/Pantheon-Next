# Governance Status

Status: external executable candidate — implemented and tested / not adopted.

This repository is not Pantheon Next.

It is an external executable candidate intended to host the MVP vertical slice and bounded runtime adapters for governed task-loop testing.

## Boundary

```text
executed_by: this external repository and Hermes, only when explicitly installed/run
exposed_by: terminal decision stand-in, read-only OpenWebUI Document Card, Paperless Source Inbox, Document Runtime Status and Document Runtime Live Status candidates, mobile Knowledge editor candidate; not installed
governed_by: Pantheon Next doctrine and adoption gates
approved_by: human decision only; authenticated issuer verification is available when the PDP registry and signed decision path are configured
forbidden: self-approval, external send bypass, memory promotion, provider routing by Pantheon, scheduling by Pantheon, unrestricted source access
```

## Current status

```text
implementation_status: blocks_1_2_3_plus_work_issues_and_document_vertical_complete_as_candidates
# The executable candidate remains aligned to the vendored Pantheon governed-loop
# schema at UPSTREAM_COMMIT f8bc3bde142d1e105b7c9a966d8e0d62b39918c4.
# Newer upstream commits are drift signals and do not silently change this contract.
binding_status: candidate
installation_status: not installed by Pantheon Next
activation_status: not activated
health_status: acceptance_tests_pass    # test_pass != adoption
ci_status: green_on_pr_80_candidate
production_status: forbidden
knowledge_publication_status: candidate_implemented_and_schema_validated
mobile_editor_status: candidate_implemented_not_installed
hermes_intelligent_edit_binding: polling_seam_implemented_not_connected

policy_chokepoint_seam: implemented_not_connected
# policy_gate normalizes runtime effects to the Pantheon request+gate_signals HTTP
# contract, fails closed and binds decision validation to PEP-derived effect facts.

policy_client_http: implemented_not_connected
capability_management_slice: implemented_not_connected
knowledge_update_chokepoint: wired_not_connected
capability_executor_http: implemented_transport_requires_verified_binding
# HermesCapabilityExecutor no longer invents /v1/capabilities:operate as a default.
# A caller must provide an explicitly reviewed native capability-operation endpoint.
# The verified Hermes Runs API is work execution, not install/enable/update semantics.

hermes_runs_api_observer: implemented_candidate_merged_not_connected
# Reads only Hermes /v1/capabilities and /v1/toolsets. It checks the public Runs API
# feature contract and compares concrete active tools to an explicit reviewed
# allowed/required tool policy. It never submits/stops/approves a run or changes
# activation. reachable != safe; Runs API available != run authorized.

hermes_run_launch_reservation: implemented_candidate_merged_not_connected
# One immutable reservation and bounded Launch Context Snapshot per admitted run.
# The candidate adds admitted -> launch_reserved -> consumed with lazy
# launch_expired projection. Reservation performs no runtime submission and creates
# no queue, scheduler or retry worker.

hermes_runs_external_binding: implemented_candidate_merged_not_connected
# The external Run Binding requires compatible Runs API + qualified concrete tool
# surface, reserves one launch, POSTs exactly one /v1/runs request and records the
# real run_id. Ambiguous network outcomes are never retried automatically. Model
# and provider routing remain inside Hermes.

hermes_active_context_bridge: implemented_candidate_merged_not_connected
# Resolves the exact running run server-side from the admission/session identity and
# delegates to Scoped Hermes Data Access. Caller/model supplies no run_id and gains
# no global Agency Data access.

hermes_context_plugin: implemented_candidate_merged_not_installed
# Candidate native Hermes plugin exposes only pantheon_context_manifest and
# pantheon_context_entity. Tool schemas contain no admission_id/run_id. Host task_id
# is used as the admission identity and must be admission-*. Upstream source maps a
# supplied Runs session_id to run_conversation task_id, but target behavior remains
# to verify before installation, enablement or activation.

hermes_run_launch_junction_ci: green_on_merged_candidate
# Runs observer and launch junction are merged in current main. Contract tests,
# current Paperless contracts and the full PostgreSQL suite pass. test_pass != adoption.

hermes_live_binding_acceptance: implemented_candidate_not_run
# Operator-only helper. Default mode is read-only Runs/toolset observation. A live
# run requires --ack SYNTHETIC_ONLY plus a pre-created synthetic admission whose
# question/root are explicitly synthetic and require both Pantheon context tools.
# PASS requires session echo, context-tool events, out-of-scope refusal, terminal
# reconciliation and active-context closure. Ambiguous launch states are preserved
# as inconclusive and never trigger automatic retry/stop/approval.

human_issuer_signing: implemented_not_connected
# decision_signing.py produces the HMAC signature matching Pantheon PDP issuer
# authentication. Signing authenticates who decided; it does not approve or
# authorize the effect. Key registry and live target wiring remain operator-side.

paperless_document_adapter: implemented_not_deployed
paperless_gateway: implemented_not_deployed
paperless_source_inbox: implemented_not_installed

document_runtime_status: implemented_read_only_not_installed
# First card: bounded Paperless gateway observation only; unrelated dimensions
# stay not_observed.

document_runtime_live_observations: implemented_read_only_not_deployed
# Independent Paperless, PDP, Docling and Hermes skill-inventory observations
# retain their own source/timestamp. The original co-located CLI observer remains
# available; the network-native observer uses Hermes' authenticated read-only
# /v1/skills endpoint and is the preferred multi-container deployment candidate.
# No synthetic global health is computed and no observation changes authority.

document_runtime_network_observer: implemented_candidate_not_deployed
# Uses server-side MVP_COCKPIT_API_KEY, PANTHEON_POLICY_API_KEY and
# HERMES_API_SERVER_KEY only inside the observer service. It projects bounded
# status and never exposes those credentials to the Cockpit response.

synthetic_document_runtime_check: implemented_candidate_not_run
# Operator-only helper. Default mode is read-only. Optional synthetic intake uses
# the installed Hermes skill transport. It can sign a synthetic human decision
# and perform a separate PDP issuer-validation proof using the PEP-returned
# expectation. Operator PDP/signing secrets are stripped from the skill subprocess.

phase_b_portainer_compose: implemented_candidate_not_deployed
# compose.phase-b.yaml is an additive external deployment candidate using the
# shared external ai-net network. It does not replace an existing OpenWebUI or
# SearXNG stack, publishes no DB/Docling/gateway/Cockpit/Hermes/observer host
# ports, and keeps backing Paperless/PDP secrets out of Hermes and the Cockpit.

paperless_runtime_profile: implemented_candidate_not_installed
hermes_pantheon_document_intake_skill: implemented_candidate_not_installed

human_decision_issuer_authentication: implementation_available_not_connected
# Pantheon PDP can verify issuer signatures when a read-only issuer key registry is
# configured, and this repo contains the matching decision-signing producer. The
# target path has not yet proven registry configuration + signed decision delivery.
```

None of these statuses establishes a live Paperless instance, target health, installed Hermes skill/plugin, live PDP/PEP enforcement, authenticated target issuer, adopted Runs binding, activation or real-dossier authorization.

## Stand-in rule

```text
runner.py -> stand_in_runner != Hermes Agent
terminal_gate_standin.py -> terminal_gate != OpenWebUI cockpit
```

The actual `pantheon-document-intake` artifact is a Hermes skill candidate, not a stand-in for Pantheon policy or human approval.

## Required non-equivalence rules

```text
runtime_success != evidence
test_pass != adoption
candidate != approval
retrieved != truth
Knowledge != Evidence
offline replay != overwrite permission
queued edit request != Hermes proposal
source_declared != path_safe
reachable != healthy
healthy != safe
Runs API available != run authorized
toolset configured != toolset approved
Hermes API observation != runtime execution
launch reservation != dispatch
launch reservation != Hermes run
session_id correlation != memory promotion
plugin installed != approved
plugin enabled != activated
Paperless metadata != canonical business classification
Paperless OCR != source truth
Paperless task success != professional validation
Paperless exact capture != Evidence
unsigned_or_asserted_decision_fields != authenticated_human_issuer
issuer_authenticated != approval
Hermes skill installed != capability approved
Hermes /v1/skills listing != task authorization
runtime observation != activation decision
synthetic check pass != production adoption
live binding acceptance pass != production adoption
compose present != target deployed
stand_in_runner != Hermes Agent
terminal_gate != OpenWebUI cockpit
external_repo != Pantheon runtime
```

## Adoption gates

```text
Task Contract schema alignment               -> met as candidate evidence
source path boundary                         -> met as candidate evidence
fixture-independent drafting seam            -> met as candidate evidence
human gate decision semantics                -> met as candidate evidence
system-signer refusal                        -> met as candidate evidence
external-send refusal                        -> met as candidate evidence
CI result after code push                    -> met on PR #80 candidate
Hermes Runs API observation                  -> implementation merged / live target proof OPEN
reviewed restricted Hermes tool surface      -> OPEN / deployment-owned
Hermes launch reservation + snapshot         -> implementation merged / live target proof OPEN
Hermes external /v1/runs binding             -> implementation merged / live target proof OPEN
Hermes context plugin                        -> implementation merged / install + live target proof OPEN
Hermes live acceptance helper                -> implemented / target run OPEN
handler task_id == submitted session_id      -> upstream source reviewed / live target proof OPEN
network-native Hermes skill observation      -> implemented candidate / live proof OPEN
Phase B Portainer composition                -> implemented candidate / live deployment OPEN
live Paperless + PDP + Hermes synthetic path -> OPEN
target issuer registry + signed decision     -> OPEN / implementation available, live proof absent
human approval for activation                -> OPEN
```

## Final rule

```text
This repository may execute an external proof loop.
Pantheon Next governs the status of that loop.
The human decides.
```
