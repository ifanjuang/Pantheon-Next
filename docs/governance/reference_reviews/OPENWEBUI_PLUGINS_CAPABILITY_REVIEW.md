# OpenWebUI Plugins Capability Review

Status: active reference review — documented non-implemented.

Reviewed upstream: `Classic298/open-webui-plugins`.

This review qualifies selected OpenWebUI plugins as candidate bindings or pattern sources. It does not install a plugin, approve production use, authorize activation, add a dependency, create an MCP host or make OpenWebUI a governance authority.

```text
OpenWebUI exposes.
Hermes executes.
Pantheon governs.
The human approves consequential transitions.
```

## Decision summary

| Candidate | Capability slot | Placement | Decision | Repository state |
|---|---|---|---|---|
| Inline Visualizer v2 | `governed_rich_ui_renderer` | OpenWebUI display binding | preferred candidate for sandbox review | documented non-implemented |
| MCP App Bridge | `mcp_rich_ui_bridge` | OpenWebUI host bridge to a Hermes-side MCP capability | watchlist / security review required | documented non-implemented |
| Prune | `conversation_retention_control` | OpenWebUI operational utility | deferred | documented non-implemented |
| Keep reasoning_content | `reasoning_metadata_retention` | OpenWebUI message persistence behavior | rejected by default | documented non-implemented |
| Interface Defaults | `deployment_interface_defaults` | OpenWebUI deployment configuration | optional pattern source | documented non-implemented |

## 1. Inline Visualizer v2

### Capability Slot

```text
capability_id: governed_rich_ui_renderer
function: render bounded interactive HTML artifacts and Pantheon status cards inside OpenWebUI
candidate_binding: Classic298/Inline Visualizer v2
owner_layer: OpenWebUI presentation layer
executed_by: OpenWebUI plugin runtime
exposed_by: OpenWebUI
governed_by: Pantheon
binding_status: preferred_candidate
install_status: absent
health_status: unknown
update_status: unknown
activation_status: unavailable
approval_status: not_requested
rollback_status: not_defined
```

### Allowed use

The candidate may render:

- Capability Cards;
- Runtime Cards;
- Evidence Cards;
- Gate Cards;
- Approval Cards;
- Hermes Operation Cards;
- bounded constellation or relationship views;
- non-authoritative developer diagnostics.

Its output remains a view of governed records. The renderer does not create truth, evidence, approval, memory or authorization.

### Risk surfaces

The upstream design uses iframe rendering and accesses browser-side state. Any use of `allow-same-origin`, parent document observation, parent storage, script execution, postMessage or DOM integration creates a privileged trust boundary.

Required review areas:

```text
same-origin exposure;
parent localStorage and session access;
script and event-handler execution;
DOM and style escape;
content-security-policy compatibility;
message origin validation;
artifact provenance;
sanitization and allowlist policy;
resource and network loading;
rollback to native OpenWebUI rendering.
```

### Gate posture

```text
candidate
-> threat-model review
-> fictional-fixture sandbox
-> security test
-> accessibility review
-> human approval for sandbox activation
-> bounded project pilot
```

Production activation is not authorized by this review.

## 2. MCP App Bridge

### Capability Slot

```text
capability_id: mcp_rich_ui_bridge
function: expose MCP application UI inside OpenWebUI while execution remains outside Pantheon
candidate_binding: Classic298/MCP App Bridge
owner_layer: OpenWebUI host bridge
executed_by: OpenWebUI plus external MCP runtime
exposed_by: OpenWebUI
governed_by: Pantheon
binding_status: watch
install_status: absent
health_status: unknown
update_status: unknown
activation_status: unavailable
approval_status: not_requested
rollback_status: not_defined
```

### Boundary

The bridge must not become:

```text
Pantheon MCP host;
Pantheon plugin manager;
Pantheon provider router;
Pantheon runtime;
Pantheon approval engine;
a direct bypass from OpenWebUI to unrestricted tools.
```

Hermes remains responsible for executing bounded MCP capabilities. OpenWebUI may expose the resulting application surface. Pantheon governs scope, binding status, activation, evidence posture, external effects and approval requirements.

### Critical risk

Same-origin application surfaces can potentially access cookies, session data, local storage and authenticated browser context. A bridge that renders third-party or dynamically produced UI therefore requires a stronger trust model than a passive renderer.

Minimum conditions before sandbox installation can be proposed:

- exact upstream commit or release pin;
- origin and iframe isolation review;
- explicit MCP server allowlist;
- tool and resource scope declaration;
- network egress declaration;
- external-write gates;
- secret and session exposure tests;
- visible active binding identity;
- kill switch and rollback procedure;
- fictional-data-only first benchmark.

Current decision: watchlist only. Installation is not proposed.

## 3. Prune

```text
capability_id: conversation_retention_control
candidate_binding: Classic298/Prune
binding_status: to_verify
install_status: absent
activation_status: unavailable
```

This is an operational cleanup utility, not governance. Pantheon may govern retention policy, deletion scope, approval requirements and evidence preservation. OpenWebUI or Hermes performs the actual cleanup.

Defer until Pantheon has explicit rules for:

- conversation retention;
- legal and contractual preservation;
- Evidence Pack references;
- canonical memory references;
- deletion receipts;
- rollback or irreversibility disclosure.

## 4. Keep reasoning_content

```text
capability_id: reasoning_metadata_retention
candidate_binding: Classic298/Keep reasoning_content
binding_status: rejected
install_status: absent
activation_status: rejected
```

Default rejection rationale:

- private or hidden reasoning is not evidence;
- persisted reasoning metadata may expose sensitive context;
- context growth may degrade runtime behavior;
- retained reasoning can be confused with trace, rationale, proof or canonical memory;
- provider-specific fields may be unstable and difficult to govern.

A future review may consider a narrow, explicit `decision_rationale_candidate` artifact. That is not equivalent to retaining provider reasoning content.

## 5. Interface Defaults

```text
capability_id: deployment_interface_defaults
candidate_binding: Classic298/Interface Defaults
binding_status: external_reference
install_status: absent
activation_status: unavailable
```

This may inspire deterministic OpenWebUI deployment defaults. It is not a governance capability. Any default affecting model choice, enabled tools, external access, retention or approval visibility must remain governed through explicit configuration records.

## Human gates

Human approval is required for:

- installation of a plugin with script, storage, session or MCP access;
- activation outside fictional fixtures;
- expansion of network or tool scopes;
- any external-write capability;
- production enablement;
- updates changing permissions or isolation behavior;
- rollback when it may destroy user-visible artifacts or records.

## Forbidden collapses

```text
installed != approved
healthy != safe
update_available != update_authorized
runtime_success != evidence
binding_selected != dependency_adopted
watchlist_item != install_instruction
rendered_card != governed_record
MCP app loaded != MCP action authorized
```

## Implementation status

```text
implemented: no
plugins_installed: no
runtime_added: no
OpenWebUI_configuration_changed: no
schemas_added: no
production_approval: no
repo_state: documented non-implemented
```

## Next governed action

Create a bounded threat model and fictional-fixture test plan for Inline Visualizer v2. Keep MCP App Bridge on the watchlist until browser-origin and session-isolation controls are demonstrated.