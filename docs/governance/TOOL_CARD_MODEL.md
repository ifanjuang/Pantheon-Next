# Tool Card Model

Status: candidate support doctrine — documented non-implemented.

Boundary profile: candidate_support_note.

This document defines the detailed cockpit card used to expose tools, skills, plugins, functions, MCP bindings, workflow runtimes and adjacent capability products without turning Pantheon Next into a runtime, installer, plugin manager, skill manager, scheduler, queue, provider router or automatic approval system.

It specializes the common Resource Card from `GOVERNED_RESOURCE_DASHBOARD_MODEL.md` and the capability lifecycle from `COCKPIT_CAPABILITY_MANAGEMENT.md`.

```text
OpenWebUI exposes.
Hermes Agent executes and owns native runtime capability mechanics.
Pantheon Next governs classification, scope, evidence, approval, activation and lifecycle decisions.
The human decides consequential adoption and use.
```

## 1. Purpose

A Tool Card is not a marketing tile and not a flat package-list item.

It answers, at one glance and in a drill-down view:

```text
what is this capability?
what professional function does it serve?
where did Pantheon learn about it?
what runtime owns it?
is it merely known, actually installed, healthy, approved, activated or updateable?
which skills/functions does it expose?
which Capability Slot may it satisfy?
what may it read, write or send?
what evidence can its outputs support?
what still requires a human decision?
```

The cockpit may render a simple card, but the underlying record remains typed and multi-axis.

## 2. Card identity and description

Every Tool Card SHOULD expose the following human-readable fields:

```text
name
short_description
long_description
category
resource_type
provider_or_project
homepage_or_repository
license_when_known
maintainer_or_owner_when_known
primary_use_cases
professional_fit
limitations
known_risks
```

`long_description` is required for a reviewed catalogue entry. It should explain the tool in operational terms rather than repeat upstream marketing copy.

Recommended structure:

```text
What it does
Where it fits in Pantheon / Hermes / OpenWebUI
Typical use cases
What it does not prove or authorize
Important operational or governance risks
```

## 3. Capability placement

Every card maps the concrete product or skill to an abstract Capability Slot.

```text
capability_slot
binding_role: preferred | fallback | watch | candidate | external_only | rejected | not_applicable
runtime_owner
executed_by
exposed_by
governed_by
approved_by
forbidden
```

A single tool may satisfy several slots, but each slot relationship is recorded separately. Pantheon must not infer dependency adoption merely because one product covers several functions.

```text
binding_selected != dependency_adopted
catalogued != installed
installed != approved
healthy != safe
native_enabled != Pantheon scope-activated
update_available != update_authorized
runtime_success != evidence
```

## 4. Provenance and discovery modes

A Tool Card MUST record how the capability entered the cockpit inventory.

```text
provenance_mode:
  hermes_native_inventory
  hermes_dynamic_skill
  runtime_installed
  pantheon_catalog
  external_reference
  operator_declared
  discovered_binding
```

### `hermes_native_inventory`

A native Hermes capability, function, plugin, MCP binding, workflow or profile reported through a reviewed Hermes inventory adapter.

Pantheon may display the observation. Hermes remains source of operational truth for its native state.

### `hermes_dynamic_skill`

A skill or capability package discovered from Hermes-managed skill files, skill directories, manifests or equivalent native metadata.

The dynamic loader belongs to Hermes. Pantheon may read normalized metadata and governance-relevant declarations through the adapter.

```text
skill file discovered != skill reviewed
skill file loaded != skill approved
skill enabled != skill authorized for every project
```

The card SHOULD preserve:

```text
native_identifier
native_manifest_path_or_reference
source_repository_when_known
content_or_version_reference_when_known
discovered_at
observed_at
adapter_contract_version
```

Pantheon must not patch arbitrary Hermes files merely to make the card exist.

### `runtime_installed`

A tool already installed outside Pantheon, whether or not it was installed by Hermes.

Observation does not imply adoption. The user may choose to adopt, keep external, ignore, replace or remove it through the relevant governed lifecycle.

### `pantheon_catalog`

A product, library, repository or capability deliberately added to the Pantheon catalogue for evaluation or future binding.

Catalogue presence is documentary only until a runtime observation or human adoption decision exists.

```text
pantheon_catalog != install instruction
pantheon_catalog != approved dependency
watchlist item != activation
```

### `external_reference`

A referenced technology used for comparison, architecture review or pattern distillation. It does not need to become an installable card.

## 5. Independent state axes

The card MUST NOT collapse lifecycle into one badge.

### Supply / installation

```text
unknown
listed
discovered
selected
install_proposed
install_authorized
installed
external_only
install_failed
removed
retired
```

### Native runtime state

```text
unknown
not_configured
configured
disabled
enabled
degraded
unreachable
not_applicable
```

### Pantheon governance

```text
unreviewed
candidate
approved_for_sandbox
approved_for_project
approved_for_production
suspended
blocked
superseded
rejected
```

### Health

```text
unknown
observed_ready
observed_degraded
observed_unavailable
stale
not_applicable
```

Health is an observation, not a safety verdict.

### Update

```text
update_unknown
up_to_date
update_available
security_update_available
breaking_update_available
update_review_pending
update_authorized
update_applied
rollback_available
rollback_authorized
rollback_applied
not_applicable
```

### Activation

```text
unavailable
not_activated
sandbox_activated
project_activated
production_activated
suspended
blocked
not_applicable
```

## 6. Detailed capability surface

The drill-down view SHOULD show:

```text
skills_exposed
functions_exposed
workflows_exposed
agents_or_profiles_exposed
mcp_servers_or_bindings
connectors_exposed
models_or_providers_touched
observability_surfaces
data_stores_touched
network_surfaces
```

For each exposed capability, retain:

```text
identifier
type
purpose
input_summary
output_summary
side_effect_class
permissions
scope
risk_class
approval_floor
approval_ceiling
evidence_expectation
native_enabled_state
Pantheon_activation_state
last_observation
```

This makes the Tool Card a projection over typed capability records rather than a replacement for them.

## 7. Permissions and effects

Every consequential card SHOULD expose the relevant effect dimensions:

```text
read_files
write_files
execute_commands
network_access
browser_access
external_api_read
external_api_write
send_messages
modify_repository
modify_runtime_configuration
install_packages
manage_credentials
access_private_project_data
write_memory_candidate
produce_external_artifact
```

Unknown permissions are displayed as unknown, never guessed as safe.

## 8. Evidence and receipts

A Tool Card may display:

```text
last_probe
last_native_receipt
last_runtime_trace_reference
last_update_diff
last_installation_receipt
last_rollback_receipt
```

Those are technical observations.

```text
technical receipt != Evidence Pack
trace != proof
successful probe != safe
successful execution != approved result
```

The card separately states the `evidence_expectation` required for consequential use.

## 9. Actions

Actions are conditional projections, not always-visible promises.

Candidate actions include:

```text
inspect source
inspect native manifest
refresh observation
review permissions
propose adoption
propose installation
propose activation
propose suspension
propose update
view update diff
view rollback
propose replacement
keep external
retire catalogue entry
```

An action appears only when a compatible external adapter or operator path exists.

The card never executes itself.

## 10. Dynamic reconciliation with Hermes

The cockpit SHOULD support a reconciliation pass between catalogue and Hermes observations.

Conceptual merge key priority:

```text
1. stable native identifier
2. admitted capability / skill identifier
3. source repository + pinned version or content hash
4. explicit operator mapping
5. otherwise keep records separate and mark possible_duplicate
```

Reconciliation may produce:

```text
catalog_only
runtime_only
matched
version_drift
metadata_drift
possible_duplicate
source_unknown
adapter_incompatible
to_verify
```

Pantheon must not mutate the Hermes source merely to resolve metadata drift. It records the discrepancy and proposes a review or adapter update.

## 11. Catalogue entries added by Pantheon

Tools that are strategically useful but not necessarily exposed by Hermes may be added as `pantheon_catalog` entries.

Initial LangChain ecosystem placement:

### LangChain

```text
name: LangChain
resource_type: external framework / library
provenance_mode: pantheon_catalog
capability_slots:
  - llm_application_composition
  - tool_and_retrieval_integration
binding_role: candidate / external_reference
executed_by: Hermes-side application or external runtime when deliberately adopted
exposed_by: Hermes or OpenWebUI only through an explicit binding
governed_by: Pantheon for capability admission, scope, external effects, evidence and lifecycle decisions
approved_by: human for adoption into governed runtime scopes
```

Detailed description: framework ecosystem for composing LLM applications, prompts, retrieval, tool integrations and model/provider abstractions. In Pantheon Next it is not a governance dependency and must not become a provider router or hidden orchestration layer by implication. It is useful primarily as an external implementation option or pattern source behind Hermes.

Primary risks: abstraction drift, hidden provider/tool routing, dependency sprawl, tool side effects, retrieval output treated as truth.

### LangGraph

```text
name: LangGraph
resource_type: external workflow / agent graph runtime library
provenance_mode: pantheon_catalog
capability_slots:
  - bounded_workflow_runtime
  - stateful_agent_graph_execution
binding_role: candidate / watch
executed_by: Hermes-side or another admitted external runtime
governed_by: Pantheon for graph eligibility, scope, effects, evidence and activation
approved_by: human for consequential activation
```

Detailed description: stateful graph runtime for long-running, branching or multi-step agent workflows. It may implement execution topology outside Pantheon, but Pantheon Workflow Manifests, gates and evidence rules remain governance artifacts. A LangGraph state/checkpoint is not canonical Pantheon memory.

Primary risks: Pantheon workflow doctrine being confused with executable graph semantics, checkpoint state promoted to memory, autonomous loops, hidden retries or external actions.

### LangFlow

```text
name: LangFlow
resource_type: visual workflow builder / external runtime surface
provenance_mode: pantheon_catalog
capability_slots:
  - workflow_visualization
  - external_flow_authoring
binding_role: candidate / watch
executed_by: external LangFlow runtime when adopted
exposed_by: LangFlow UI or a reviewed OpenWebUI/Hermes bridge
governed_by: Pantheon for adoption, capability scope, external effects and activation
approved_by: human
```

Detailed description: visual builder for composing LLM, retrieval, tool and workflow components. It can be useful for authoring or inspecting execution flows, but its canvas is not Pantheon doctrine and a visually connected flow is not an authorized Workflow Manifest.

Primary risks: visual configuration treated as governance authority, embedded credentials/connectors, auto-execution assumptions, flow drift from reviewed manifests.

### LangSmith

```text
name: LangSmith
resource_type: observability / evaluation surface
provenance_mode: pantheon_catalog
capability_slots:
  - observability
  - evaluation_and_trace_review
binding_role: fallback_candidate / candidate
executed_by: external observability service and Hermes-side instrumentation when adopted
exposed_by: LangSmith UI and optional cockpit summaries
governed_by: Pantheon for trace handling, retention, evidence classification and lifecycle status
approved_by: human for data exposure and governed-project adoption
```

Detailed description: tracing, debugging, dataset/evaluation and monitoring platform for LLM applications. It may help observe Hermes-side or LangChain/LangGraph executions. Its traces, scores and evaluator outputs remain operational observations and candidates; they do not become proof, approval or canonical memory by themselves.

Primary risks: prompt/client-data leakage, external telemetry retention, evaluator score treated as professional validation, trace data mistaken for Evidence Pack.

These four records remain catalogue candidates until exact source, version, deployment mode, data handling and runtime binding are reviewed.

## 12. Relationship to existing registries

```text
HERMES_CAPABILITY_BINDINGS.md
  -> which concrete products are candidate bindings for abstract slots

CAPABILITY_REGISTRY.md
  -> which governed capabilities exist and what they may do

COCKPIT_CAPABILITY_MANAGEMENT.md
  -> lifecycle and human action surface

GOVERNED_RESOURCE_DASHBOARD_MODEL.md
  -> common Resource Card projection

TOOL_CARD_MODEL.md
  -> detailed product/tool/skill card grammar and provenance reconciliation
```

The Tool Card does not replace these registries.

## 13. Implementation posture

```text
implemented: no
runtime_added: no
installer_added: no
scheduler_added: no
plugin_manager_added: no
provider_router_added: no
schema_added: no
protected_paths_touched: no
repo_state: documented non-implemented
```

Future implementation should prefer data-driven card generation from normalized inventory/catalogue records rather than hard-coded React product lists.

A reviewed adapter may supply live Hermes observations. A static catalogue may supply known candidate tools. The cockpit merges their projections without changing native runtime ownership.

## Final rule

```text
The catalogue describes.
Hermes reports and executes its native capabilities.
The cockpit reconciles and displays.
Pantheon governs consequential status and decisions.
The human adopts, activates, updates or refuses.
```
