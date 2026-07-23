# Cockpit Runtime Configuration Assistance

Status: candidate support doctrine — minimal runtime-connection assistance boundary — documented non-implemented.
Boundary profile: candidate_support_note.

This document defines the smallest useful configuration-assistance surface for a Pantheon cockpit.

The cockpit does not become a configuration editor, installer, runtime administrator, secret store, policy engine or duplicate of the Pantheon MCP. It exposes only the runtime and connection facts required to understand whether the governed path is present and usable.

## 1. Decision

The selected posture is:

```text
install and maintain through native/operator tooling
-> observe only the minimum runtime and connection state
-> obtain policy, classification and validation from the Pantheon MCP
-> expose the result in the cockpit
-> guide the human to the native surface when a change is required
```

Initial configuration behavior:

```text
read-only observation          -> candidate future adapter
proposal or operator guidance  -> documentation / cockpit card
bounded direct write           -> not selected for the initial scope
arbitrary config-file editing  -> forbidden
```

The cockpit must remain simpler than the runtimes it exposes.

## 2. Responsibility boundary

```text
exposed_by:
  Pantheon MVP Cockpit, OpenWebUI-facing cards or another reviewed display surface.

executed_by:
  Hermes Agent, OpenWebUI, their native administration surfaces, and human/operator tooling.

governed_by:
  Pantheon doctrine and the Pantheon MCP for policy, classification, validation,
  capability status, scope, evidence expectations, activation gates and refusals.

approved_by:
  Human for installation, configuration change, activation, update, restart and rollback.

forbidden:
  General configuration editor, generic YAML/JSON patcher, direct database editing,
  Docker socket access, shell access, secret capture, silent restart, automatic update,
  provider routing, plugin management or policy duplication in the cockpit.
```

## 3. What remains in the Pantheon MCP

The Pantheon MCP remains the preferred bounded interface for:

```text
doctrine consultation
architecture explanation
request classification
capability-status qualification
external-action policy checks
candidate validation
provided-evidence verification
Context Pack planning and validation
status distinctions and refusal reasons
```

The cockpit may render these results. It must not reimplement their rules locally.

```text
cockpit display != policy source
runtime observation != governance decision
MCP result != human approval
runtime success != evidence
```

## 4. Minimum cockpit observation surface

The cockpit should observe only facts needed to understand the active path:

```text
runtime identity
runtime version
reachable / unreachable
bounded health signal
OpenWebUI -> Hermes effective connection target
Hermes API authentication present / absent, without exposing the key
Pantheon MCP binding present / absent
Pantheon MCP reachable / unreachable
Pantheon MCP declared enabled / disabled when observable
configuration compatibility state after an update
last observation time
observation source
```

Optional display-only metadata may include:

```text
instance label
container or host alias
current image or package version reference
restart required / not required / unknown
rollback reference present / absent
```

The initial cockpit does not need to inventory every provider, model, plugin, skill, tool, memory backend, feature flag or internal runtime field. Such inventory may remain in the native Hermes/OpenWebUI surfaces unless a later governed use case proves that it is required.

## 5. Minimum proposal surface

When a connection problem is observed, the cockpit may prepare operator guidance for a narrow set of cases:

```text
correct the OpenWebUI -> Hermes base URL
add the required /v1 suffix when applicable
identify that the Hermes API key is missing or mismatched, without reading it
identify that the Pantheon MCP binding is absent, disabled or unreachable
identify that a runtime configuration migration is required after an update
open or name the relevant native administration surface
show a copyable operator command candidate from reviewed documentation
show the expected post-change checks
show the rollback reference
```

The cockpit should not produce a generic full-file configuration patch.

Preferred proposal forms:

```text
short diagnosis
native setting location
one bounded value or connection change
operator command candidate
expected result
verification checklist
rollback note
```

```text
proposal != execution
operator command candidate != command executed
observed applied != approved activation
```

## 6. Configuration-version drift

Hermes and OpenWebUI configuration formats may change between versions. Field names, nesting, persistence behavior, defaults, environment variables, CLI commands and supported administration interfaces must not be assumed stable.

Therefore:

```text
runtime version must be observed before configuration guidance
configuration guidance must declare the version range it was reviewed against
unknown or unsupported version -> stop and route to native/upstream documentation
field path copied from another version -> not admissible evidence
configuration digest change -> compatibility review required
runtime update -> configuration migration status must be checked separately
```

The cockpit must never use a hard-coded file path or field path as a universal contract.

Forbidden default pattern:

```text
open config.yaml
-> replace arbitrary text
-> restart container
```

Preferred pattern:

```text
observe exact runtime version
-> consult version-matched upstream/native guidance
-> ask the human to apply through the native UI, CLI or operator tooling
-> observe the effective result again
```

When the runtime offers an official validation or migration command, the cockpit may display it as an operator command candidate. Pantheon does not run it.

## 7. Hermes minimum scope

Observable, subject to a reviewed native surface:

```text
Hermes version
API reachability
bounded health response
API authentication present / absent
OpenWebUI-facing API base URL or service identity
Pantheon MCP binding name
Pantheon MCP binding enabled state when exposed
Pantheon MCP call success / failure for a harmless consultation
configuration validation or migration-needed status when exposed
```

Proposal-only:

```text
correct the Hermes API connection used by OpenWebUI
add or restore the reviewed Pantheon MCP declaration
route to the native Hermes configuration or plugin surface
show version-matched config validation or migration commands
reduce an accidental broad API exposure when a reviewed correction is known
```

Not part of the initial cockpit scope:

```text
provider or model management
plugin or skill catalog management
memory-provider selection
browser or messaging credentials
arbitrary MCP inventory management
full toolset administration
config.yaml editing
container recreation
package or model installation
```

These remain owned by Hermes and the operator. Pantheon MCP governs consequential status and admissibility where required.

## 8. OpenWebUI minimum scope

Observable, subject to a reviewed native surface:

```text
OpenWebUI version
application reachability
active Hermes connection name or identifier
Hermes base URL
model discovery through Hermes
connection authentication present / absent, without exposing the key
effective connection observed versus container-environment declaration
```

Proposal-only:

```text
correct the Hermes base URL
replace localhost with the appropriate private-network service name
add the required /v1 suffix
route the human to native secret entry
identify an obsolete duplicate Hermes connection
route the human to Admin Settings when persisted configuration overrides environment values
```

Not part of the initial cockpit scope:

```text
general OpenWebUI settings administration
user or group administration
native RAG administration
web-search administration
provider catalog administration
database editing
feature-flag inventory unrelated to the Pantheon path
```

OpenWebUI may persist configuration in its database. The cockpit must distinguish:

```text
container environment observed
persisted OpenWebUI setting observed
effective connection observed
```

When no supported read surface exists, the state is `to_verify`. When no supported write surface exists, the human uses the native Admin Settings interface.

## 9. Secrets

The cockpit does not store raw runtime secrets.

Allowed:

```text
secret present: true | false | unknown
secret owner
secret reference identifier when externally provided
last rotation time when externally provided
```

Forbidden:

```text
raw API key
raw database password
private SSH key
browser cookie or authenticated profile
unredacted .env file
secret copied into Knowledge, logs or Evidence Packs
```

A secret change always routes to the native secret-entry surface or an external secret manager.

## 10. Updates and compatibility

Update status remains separate from configuration status:

```text
update_available != update_authorized
runtime_updated != configuration_compatible
configuration_migrated != runtime_safe
healthy != safe
rollback_available != rollback_decided
```

After any Hermes or OpenWebUI update, the minimum review is:

```text
observe new version
check upstream release and migration guidance
check effective OpenWebUI -> Hermes connection
check Pantheon MCP binding
run or request native validation/migration checks when applicable
verify a harmless Pantheon MCP consultation
record compatibility as observed_compatible | observed_degraded | migration_required | failed | to_verify
```

## 11. No selected direct-write path

A generic cockpit write adapter is not selected.

```text
bounded direct write -> documented non-implemented
current need          -> not demonstrated
initial posture       -> native/operator application only
```

A future bounded write may be reconsidered only for one concrete, repetitive and low-risk need that cannot be handled acceptably through native guidance. It would require a versioned native interface, exact allowlist, explicit human confirmation, no raw secret handling, readback, health check and rollback.

This possibility must not shape the initial cockpit architecture.

## 12. Cockpit card

A minimal runtime-connection card may show:

```text
runtime
version
reachability
connection status
Pantheon MCP status
configuration compatibility status
last observed
open issue
native action required
verification action
rollback reference
```

Minimal actions:

```text
Inspect
Open native settings
Copy reviewed command candidate
Verify connection again
Consult Pantheon MCP
Show rollback note
```

No card button may install, update, restart, edit arbitrary configuration, expose a port or transmit a secret.

## 13. Initial implementation sequence

```text
Phase A — documentation
  installation guides
  version and migration caveat
  minimum connection contract

Phase B — MCP-backed cockpit projection
  render Pantheon MCP policy and validation results
  no duplicated cockpit policy

Phase C — minimal read-only observations
  Hermes/OpenWebUI version and reachability
  OpenWebUI -> Hermes effective connection
  Pantheon MCP presence and harmless consultation

Phase D — proposal-only assistance when a real problem is observed
  version-matched native guidance
  expected verification
  rollback note
```

No direct-write phase is planned by default.

## 14. Current status

```text
installation documentation              -> implemented as documentation
minimal cockpit observation model        -> implemented as documentation
MCP-backed policy projection              -> documented non-implemented in cockpit
live Hermes/OpenWebUI observation adapter -> documented non-implemented
configuration proposal cards              -> documented non-implemented
configuration write adapter               -> not selected / documented non-implemented
secret store                              -> voluntarily absent
Docker or SSH control                     -> voluntarily absent
automatic activation                      -> voluntarily absent
```
