# Cockpit Runtime Configuration Assistance

Status: candidate support doctrine — runtime configuration assistance boundary — documented non-implemented.
Boundary profile: candidate_support_note.

This document defines how a Pantheon cockpit may observe, explain and propose configuration changes for external runtimes such as Hermes Agent and OpenWebUI without becoming their installer, administrator, secret store or general control plane.

It records a direction for continued design work. It does not create an adapter, API client, write path, approval engine, runtime probe, Docker controller or configuration editor.

## 1. Decision

The initial cockpit posture is:

```text
observe
-> explain
-> propose
-> wait for human application or explicit future bounded adapter
-> verify the resulting observation
```

Direct configuration mutation is not part of the first implementation slice.

```text
observed configuration != approved configuration
proposal != execution
execution success != admitted configuration
admitted configuration != task authorization
healthy != safe
```

## 2. Boundary

```text
exposed_by:
  Pantheon MVP Cockpit, OpenWebUI-facing cards or another reviewed administration surface.

executed_by:
  Hermes native administration surfaces, OpenWebUI Admin Settings, human operator,
  vendor tooling or a separately reviewed bounded adapter.

governed_by:
  Pantheon status distinctions, scope, effect classification, secret handling,
  approval gates, update authorization, health interpretation and rollback visibility.

approved_by:
  Human for every material configuration change, secret change, model/provider binding,
  tool exposure, gateway exposure, update, restart and rollback.

forbidden:
  General shell access, Docker socket access, arbitrary file editing, secret capture,
  silent activation, unrestricted administrator tokens, hidden restart, automatic update,
  provider routing or configuration-to-safety conclusions.
```

## 3. Why the cockpit may assist

Hermes and OpenWebUI expose configuration surfaces that materially affect:

```text
model and provider selection
tool and MCP availability
browser and search access
memory behavior
external communication surfaces
source and dossier access
API exposure
user-facing model availability
runtime restart requirements
```

These are consequential status changes even though execution remains external. Pantheon may therefore govern the review, evidence and approval path without owning the runtime configuration mechanism.

## 4. Capability Slot classification

```text
abstract capability:
  runtime configuration assistance

candidate binding:
  Hermes native dashboard/API/CLI
  OpenWebUI Admin Settings or documented administration API
  operator-run configuration command
  future bounded runtime adapter

installation status:
  external and separately observed

health status:
  observation only

update status:
  shown separately from authorization

activation status:
  default-off for write behavior

Pantheon gates:
  scope, secret, effect, restart, evidence, rollback and human confirmation

human approval:
  required before every material write
```

## 5. Three assistance levels

### 5.1 Level R0 — documentation only

The cockpit or documentation may show:

```text
where the native setting lives
what the setting means
expected values
upstream source reference
known restart requirement
known security consequence
operator command candidate
rollback note
```

No runtime access occurs.

Status:

```text
implemented as documentation
```

### 5.2 Level R1 — observation

A reviewed adapter may read and display a bounded runtime observation:

```text
runtime version
reachable / unreachable
health response
configured provider and model identifiers
configured endpoint identifiers
MCP, plugin or tool names and enabled state
OpenWebUI connection target
configuration digest
last observed change
restart-required indicator when the runtime exposes one
```

The cockpit must show the observation source and time.

```text
read succeeded != complete inventory
runtime reports enabled != Pantheon activation
health response != safe runtime
configuration digest changed != unauthorized change proven
```

No secret value should be returned. Presence, redacted suffix, secret reference or hash may be shown when the runtime supports it safely.

### 5.3 Level R2 — proposal

The preferred first product capability is a Configuration Change Candidate.

The cockpit may prepare:

```text
target runtime and instance
configuration area
current observed value
proposed value
rationale
source reference
change effect class
secret impact
restart impact
expected checks
rollback proposal
human approval request
native application path
```

The candidate may be exported as:

```text
reviewable diff
copyable command candidate
YAML or JSON fragment
link or instructions to the native administration screen
operator checklist
```

The cockpit does not claim the change happened.

### 5.4 Level R3 — bounded application

Future only. Default status:

```text
documented non-implemented
default disabled
```

A bounded adapter may be considered only when all of the following are true:

```text
native documented API or stable command exists
exact runtime and version are identified
configuration area is allowlisted
current value is read before mutation
write is idempotent or safely repeatable
secret values remain in the native secret boundary
human confirmation is explicit and recent
expected effect is stated
restart behavior is known
post-write readback is available
health check is available
rollback is available
trace can be returned
```

The adapter must refuse unknown fields, ambiguous targets, stale observations, missing rollback and unsupported runtime versions.

## 6. Configuration Change Candidate

Suggested shape:

```yaml
configuration_change_candidate:
  candidate_id:
  created_at:
  target:
    runtime: hermes | openwebui | other
    instance_id:
    version_observed:
    configuration_area:
  observation:
    observed_at:
    source_ref:
    current_value_redacted:
    configuration_digest:
  proposal:
    proposed_value_redacted:
    rationale:
    upstream_reference:
  effect:
    effect_class: display_only | internal_state_change | external_effect | canonical_effect
    secret_change: false
    restart_required: false | true | unknown
    availability_risk: low | medium | high | unknown
    data_exposure_change: none | reduced | increased | unknown
    tool_surface_change: none | reduced | increased | unknown
  checks:
    preconditions: []
    expected_postconditions: []
    stop_conditions: []
  rollback:
    supported: false
    method_ref:
    previous_value_reference:
  application:
    mode: native_ui | operator_command | bounded_adapter | unsupported
    executor: human | hermes_native | openwebui_native | external_adapter
    status: not_executed | declared_executed | observed_applied | observed_failed | unknown
  approval:
    required: true
    status: pending | approved_for_one_attempt | refused | expired
    human_decision_ref:
  evidence_refs: []
```

This is a candidate record. It is not an executable configuration object.

## 7. Initial Hermes scope

### 7.1 Observable candidates

Subject to native surface review:

```text
Hermes version
API server enabled state
API server model name
API reachability and health
active profile identifier
provider and model identifiers without keys
MCP server names and enabled state
plugin names and enabled state
memory provider identifier and readiness state
configured toolsets exposed through the selected API profile
```

### 7.2 Proposal candidates

Potential first proposals:

```text
connect OpenWebUI to the Hermes API URL
change a non-secret model identifier within an approved provider
select a reviewed profile
install or enable an already reviewed Pantheon plugin through the native Hermes flow
add or update a reviewed MCP declaration
reduce exposed toolsets
adjust bounded timeouts or concurrency limits
```

### 7.3 Initially forbidden writes

```text
provider API keys
host shell profile
Docker socket or host mounts
SSH keys
browser session credentials
messaging gateway credentials
unreviewed skill or plugin installation
arbitrary config.yaml fields
system package installation
container recreation
```

Hermes native `config`, plugin and dashboard facilities remain the execution owner. The cockpit may guide the operator to them.

## 8. Initial OpenWebUI scope

### 8.1 Observable candidates

Subject to native surface review:

```text
OpenWebUI version
application reachability
configured OpenAI-compatible connection names and base URLs
whether the Hermes connection includes /v1
model discovery result
selected database type without credentials
enabled feature flags relevant to the governed path
```

### 8.2 Proposal candidates

```text
add or correct the Hermes OpenAI-compatible connection
replace localhost with the correct Docker service name
include the /v1 suffix
align the connection key through native secret entry
remove an obsolete duplicate connection
turn off an unused direct Ollama connection when Hermes is the canonical execution path
turn off unreviewed native RAG or web-search bindings
```

### 8.3 Persistence rule

OpenWebUI may persist connection settings in its database after first launch. A container environment change alone may not change the effective runtime configuration.

The cockpit must distinguish:

```text
container environment observed
OpenWebUI persisted configuration observed
effective connection observed
```

When no supported write API exists, application mode is:

```text
native_ui
```

The cockpit should open or explain the relevant Admin Settings path rather than editing the database.

## 9. Secret handling

The cockpit must not store raw runtime secrets.

Allowed display patterns:

```text
secret present: true | false
secret owner
secret reference identifier
last rotation time when externally provided
redacted suffix when the native system returns it safely
```

Forbidden:

```text
raw API key
raw database password
private SSH key
browser cookie or authenticated profile content
unredacted .env file
secret copied into a Knowledge item, log or Evidence Pack
```

A change that requires a secret should route the human to the native secret-entry surface or an external secret manager.

## 10. Restart and availability

A change candidate must say whether a restart is:

```text
not required
required for one runtime
required for dependent runtimes
unknown
```

The cockpit must not restart a container merely because a configuration candidate was approved.

For an initial implementation, restart application mode remains:

```text
operator action outside Pantheon
```

Future restart adapters would require a separate high-risk review and must not imply Docker socket access is acceptable.

## 11. Verification after human application

After the human declares a native change applied, the cockpit may perform or request bounded read-only checks:

```text
read the effective setting again
compare configuration digest
check runtime health
check expected model discovery
check expected MCP or plugin state
check that no additional tool or port exposure appeared
record mismatch or partial result
```

Possible result:

```text
observed_applied
observed_partial
observed_not_applied
observed_failed
to_verify
```

The result remains an observation. It does not approve activation or professional use.

## 12. Update and rollback relationship

Configuration assistance does not replace runtime update governance.

```text
configuration proposal != update authorization
runtime update != configuration migration verified
rollback available != rollback decided
```

Every candidate with material availability or exposure impact must cite a rollback method or remain blocked.

## 13. Cockpit card behavior

Suggested card states:

```text
not_observed
observed
proposal_ready
waiting_human_decision
approved_for_one_attempt
waiting_native_application
observed_applied
observed_partial
observed_failed
blocked
expired
```

Suggested actions:

```text
Inspect source
Show diff
Copy command candidate
Open native settings
Record human decision
Declare applied
Verify again
Show rollback
```

No button may silently install, enable, update, restart, expose a port or transmit a secret.

## 14. Human decision requirements

Human approval is required before:

```text
changing provider or model
changing tool or MCP exposure
installing or enabling a plugin or skill
changing browser, search, memory or messaging bindings
changing a secret
changing a published port or CORS origin
restarting a consequential runtime
updating or rolling back
```

Approval should be scoped to one candidate, one instance, one expected value and one attempt. It should expire when the observed configuration digest changes.

## 15. Initial implementation sequence

Recommended order for future work:

```text
Phase A — documentation
  component installation guide
  configuration candidate grammar
  native-surface inventory

Phase B — read-only observation
  Hermes version, health, provider/model identifiers, MCP/plugin state
  OpenWebUI version, Hermes connection target and model discovery

Phase C — proposal-only cockpit
  diff, rationale, risk, native application path and rollback

Phase D — bounded write experiment
  one low-risk, non-secret, reversible field
  explicit human confirmation
  readback and rollback proof

Phase E — broader adapter decision
  continue, narrow or refuse based on evidence
```

No phase is authorized by this document.

## 16. Open questions for continued reflection

```text
Which Hermes configuration surfaces are stable and officially supported for write access?
Which OpenWebUI settings have a supported administration API rather than database-only persistence?
Which configuration changes are consequential enough to require Pantheon gating?
Which low-risk changes genuinely benefit from cockpit application rather than native-UI guidance?
How should identity and project scope be attached to runtime observations?
How should stale configuration observations invalidate an approval?
Which restart actions can remain operator-only permanently?
How should configuration drift be detected without creating a monitoring runtime inside Pantheon?
```

## 17. Current status

```text
documentation and proposal model       -> implemented as documentation
live Hermes observation adapter         -> documented non-implemented
live OpenWebUI observation adapter       -> documented non-implemented
configuration write adapter              -> documented non-implemented / default disabled
secret store                              -> voluntarily absent
Docker or SSH control                     -> voluntarily absent
automatic activation                      -> voluntarily absent
```
