# Hermes Runtime Surface Review

Status: candidate external-runtime review — reviewed release, not installed, activated or task-authorized.
Boundary profile: external_reference_review.
Current reviewed target: Hermes Agent 0.20.0.

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
| OpenAI-compatible chat surface | external conversation transport | OpenWebUI may use Hermes as its agent backend. OpenWebUI memory, retrieval and tool configuration remain separate runtime inputs and must not silently widen a governed task. `X-Hermes-Session-Key` is an opt-in long-term-memory scope and is forbidden for the governed profile. |
| MCP and plugin surfaces | replaceable execution bindings | tool discovery or plugin availability does not select, activate or authorize a binding. Exact tool names remain allowlisted per admitted run. |
| External memory provider system | optional runtime-memory layer | the reviewed 0.20 documentation lists external provider plugins, allows one external provider at a time and keeps built-in `MEMORY.md` / `USER.md` available alongside it. Provider activation may inject context, prefetch recall, synchronize turns, extract memories, mirror writes and expose provider tools. These effects are forbidden by default for the governed Pantheon profile. |
| Built-in memory controls | profile-local runtime configuration | `hermes memory off` disables the external provider only. Hermes separately reports built-in memory injection, user-profile injection and memory-tool state. All three must be disabled for `pantheon-governed`; stored files may remain present but must not enter the prompt or tool surface. |
| Observability plugin surface | external trace layer | Langfuse may remain the preferred candidate observability binding, but plugin presence does not prove hook delivery from API-server, OpenWebUI or Runs paths. A live synthetic trace is required before qualification. |

## Runtime profile separation

The runtime must use separate operational profiles rather than one profile with
all convenience features enabled.

```text
profile: pantheon-governed
external_memory_provider: off
built_in_memory_injection: off
built_in_user_profile_injection: off
memory_tool: off
session_memory_key: forbidden
automatic_runtime_recall: forbidden
automatic_runtime_memory_write: forbidden
OpenWebUI_memory_injection: forbidden
OpenWebUI_automatic_RAG: forbidden
allowed_tools: explicit per Task Contract
provider_and_model_override_in_run_payload: omitted
consequential_effects: human-gated

profile: assistant-personal
external_memory_provider: optional_one_only
built_in_memory_posture: user_selected
runtime_recall_and_write: user-scoped convenience
Pantheon_authority: none
professional_task_authorization: none
canonical_memory_promotion: none
```

Disabling only the external provider is insufficient. The governed posture must
also disable built-in `MEMORY.md` injection, `USER.md` profile injection and the
memory tool. The files may remain stored as Hermes runtime data, but they must
not influence a Pantheon-admitted run.

Profile separation is a deployment and runtime-configuration requirement. It
creates no new Pantheon runtime, identity or approval object.

```text
profile created != scope governed
hermes memory off != built-in memory injection off
provider absent != memory context absent
memory tool absent != memory injection disabled
provider selected != memory admitted
memory recalled != source verified
conversation synchronized != Register Candidate accepted
```

## Ecosystem compatibility decisions

These decisions reuse existing Capability Slots and adapter boundaries. They do
not add components to the standard distribution lock.

| System | Candidate placement with Hermes | Decision at this review |
|---|---|---|
| OpenWebUI | conversation and cockpit exposure through the Hermes OpenAI-compatible surface | compatible as UI; governed profile must suppress hidden memory or retrieval enrichment |
| Langfuse | external observability binding | preferred candidate; synthetic API-server and Runs-path trace still required |
| Docling | `document_structural_analysis` binding through a bounded service, MCP or API | preferred document-analysis candidate; output remains a source-linked derivation candidate |
| Paperless-ngx | optional `document_source_management` binding | compatible and already independently classified; not required for core local/NAS ingestion |
| Mem0 | official Hermes external-memory provider candidate | optional for the personal assistant profile; refused as canonical or governed-task memory |
| Mnemosyne | third-party Hermes/MCP memory adapter candidate | sandbox candidate for local-first personal memory; not bundled or selected by Pantheon |
| Haystack | bounded `knowledge_retrieval_pipeline` candidate | compare only when a concrete governed corpus requires a retrieval service |
| LlamaIndex / LangChain | component libraries inside a bounded adapter | watch or compare; refuse as the global execution or provider abstraction layer |
| Langflow | visual workflow laboratory exposed as one bounded tool if needed | sandbox/prototype only; refuse as a second production orchestrator |
| LangGraph | specialized external workflow behind one capability contract | refuse as Pantheon or default Hermes runtime; use only for a demonstrated stateful workflow gap |
| RAGFlow | integrated external RAG product | watch/reference only by default; refuse as a replacement for Hermes, Docling, Paperless, OpenWebUI or Pantheon governance |

## Adapter decision

```text
runtime_target: 0.20.0
kernel_change_required: false
run_binding_change_required: false
observer_contract_change_required: true
standard_distribution_components_change_required: false
real_instance_observation_required: true
runtime_artifact_digest_required_before_observed: true
composed_acceptance_required_before_qualified: true
installation_effect: none
activation_effect: none
task_authorization_effect: none
```

The observer contract requires a bounded extension because `/v1/toolsets` alone
cannot prove that built-in prompt injection is disabled. The extension must
consume an explicit read-only profile-memory observation; it must not inspect
arbitrary host files, mutate Hermes configuration or infer safety from absent
tool names.

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
2. observe the explicit named `/p/<profile>/v1/capabilities` and `/v1/toolsets` route when profile multiplexing is used;
3. verify the active tool allowlist;
4. verify that the Pantheon run-binding payload contains no `model`, `provider`
   or `model_options` override;
5. record a read-only profile memory-status observation proving:
   - external provider is absent;
   - built-in memory injection is disabled;
   - built-in user-profile injection is disabled;
   - memory tool is disabled;
   - no `X-Hermes-Session-Key` is supplied by the governed client;
6. verify that OpenWebUI adds no hidden memory or automatic RAG enrichment;
7. execute one admitted read-only run and one one-shot reconciliation;
8. if Langfuse is selected, emit one synthetic trace from the actual API-server
   and Runs path and verify redaction, correlation and retention;
9. confirm that no A2A, webhook, voice, messaging or provider-routing surface
   was activated by the composition;
10. retain runtime and observability traces as technical observations, not Evidence.

## Non-equivalences

```text
release reviewed != release installed
version target updated != artifact observed
Runs API documented != live instance compatible
profile route answered != governed profile qualified
trusted peer != approved actor
webhook configured != external effect authorized
citation present != Evidence admitted
voice command received != human approval recorded
hermes memory off != built-in memory injection off
provider absent != memory context absent
memory tool absent != memory injection disabled
provider selected != memory admitted
memory recalled != truth
trace recorded != Evidence
runtime success != Evidence
```
