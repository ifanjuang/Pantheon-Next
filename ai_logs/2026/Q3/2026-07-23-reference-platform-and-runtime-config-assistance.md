# 2026-07-23 — Reference platform, raw configuration boundary and cockpit capability management

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Request

Document the installation posture for Hermes Agent, OpenWebUI, PostgreSQL/pgvector, the `ai-net` private network, Ollama, SearXNG, Chromium/Browserless and related external services.

The cockpit should remain simple around unstable raw configuration, but it must manage the lifecycle of skills, functions, workflows, runtime agents, plugins and MCP bindings.

## Repository reading

The change was framed against the current repository status spine and relevant owners:

```text
docs/governance/README.md
docs/governance/STATUS.md
docs/governance/WHAT_RUNS.md
docs/governance/AUTHORITY_INDEX.md
docs/governance/MODULES.md
CONTRIBUTING.md
docs/governance/STATUS_HEADER_RULES.md
docs/governance/COMMON_INSTALLATION_BASELINE.md
docs/install/COMMON_BASELINE_RUNBOOK.md
docs/governance/HERMES_INSTALLATION_ASSISTANCE.md
docs/governance/HERMES_INTEGRATION.md
docs/governance/GOVERNED_RESOURCE_DASHBOARD_MODEL.md
docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md
```

Official upstream installation and integration documentation was reviewed for Docker networking, Hermes Agent, OpenWebUI, Ollama, pgvector, SearXNG and Browserless/Chromium.

## Installation decision

```text
Pantheon Next owns the baseline, installation guidance, status distinctions and gates.
The human and external infrastructure tooling install and maintain the services.
Hermes executes.
OpenWebUI exposes.
Pantheon MVP projects cockpit cards and decisions.
```

The common baseline is split into:

```text
required foundation
+ conditional services selected by reviewed bindings
```

Required foundation includes the container substrate, private network, persistent storage, backup/rollback posture, Hermes, OpenWebUI and PostgreSQL/pgvector availability. Ollama, embeddings, SearXNG, Browserless, Docling, OCR, observability and external runtime memory are conditional.

## Corrected cockpit decision

The earlier reduction was too broad. It incorrectly treated plugin and skill management as raw configuration editing.

The corrected distinction is:

```text
Raw runtime configuration
  -> narrow, version-sensitive, native or operator-managed

Capability lifecycle management
  -> central cockpit function

Policy, classification and validation
  -> Pantheon MCP

Native operation
  -> Hermes or another admitted runtime adapter
```

The cockpit must manage:

```text
skills
functions and tools
workflows
runtime agents / profiles
plugins
MCP servers and bindings
connectors where admitted
```

Management includes inventory, inspection, candidate authoring, source/provenance review, installation proposal, native install where admitted, enable/disable, scope activation, health, update status, update authorization, rollback, suspension, replacement and retirement.

## Capability action flow

```text
Cockpit observes current native state and exact runtime version
-> creates one Capability Action Candidate
-> Pantheon MCP validates type, source, effect, status, scope, gate and rollback
-> human approves one action, target, version and scope
-> Hermes adapter performs the native operation
-> technical receipt and fresh observation return to the cockpit
-> activation, task authorization, evidence and professional acceptance remain separate
```

The cockpit button does not become the plugin manager or runtime. It requests one bounded native operation from the external executor.

## MCP boundary

The Pantheon MCP remains the governance interface for:

```text
doctrine consultation
architecture explanation
request classification
capability identity and status qualification
source/provenance review
permission and effect classification
scope and activation gates
external-action policy checks
candidate validation
provided-evidence verification
update and rollback admissibility
receipt consistency and refusal reasons
```

The MCP does not install, enable, execute, update or remove capabilities.

## Runtime-agent distinction

An Agent card refers to an external runtime agent or profile executed by Hermes.

```text
Pantheon Role or god != runtime agent
```

Pantheon Roles remain governance viewpoints. Hermes owns runtime-agent creation and execution.

## Configuration-version drift

Hermes and OpenWebUI configuration formats may change between versions. Field names, nesting, persistence behavior, environment variables, defaults, CLI commands and administration interfaces must not be assumed stable.

Recorded rules:

```text
observe exact runtime version before guidance or mutation
adapter declares a supported version range
unsupported version -> preserve safe read-only visibility and disable mutations
runtime update != configuration compatibility
refresh capability inventory after update
hard-coded file or field path != stable contract
```

Capability management must use native APIs, CLI surfaces or plugin endpoints matched to the observed runtime version. It must not rely on generic YAML/JSON patching.

## Files changed

```text
docs/install/REFERENCE_PLATFORM_COMPONENTS.md
  component-by-component operator guide

docs/governance/COMMON_INSTALLATION_BASELINE.md
  required foundation separated from conditional services

docs/install/COMMON_BASELINE_RUNBOOK.md
  manual sequence aligned with the revised baseline

docs/governance/COCKPIT_RUNTIME_CONFIGURATION_ASSISTANCE.md
  narrow raw-configuration and compatibility boundary

docs/governance/COCKPIT_CAPABILITY_MANAGEMENT.md
  unified cockpit lifecycle management for skills, functions, workflows,
  runtime agents, plugins and MCP bindings

docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md
  new documents indexed without promotion
```

## Runtime and protected-path impact

```text
runtime impact: none
protected paths touched: no
schemas/tests/CI impact: none
installation executed: no
configuration modified: no
capability mutation executed: no
secret stored: no
external action: GitHub documentation branch and draft PR only
memory behavior: none
approval behavior: none
```

## Explicit non-equivalences

```text
installation guide != installer
capability card != runtime capability
listed != authorized
installed != approved
enabled != activated for a scope
workflow selected != workflow authorized
runtime agent != Pantheon Role
MCP decision != human approval
runtime updated != adapter compatible
healthy != safe
update available != update authorized
technical receipt != evidence
```

## Result

The repository now documents the external platform and the correct cockpit split: minimal raw-configuration handling, central capability lifecycle management, MCP-backed policy and validation, and external Hermes-native execution. The design supports managing skills, functions, workflows, runtime agents, plugins and MCP bindings without turning Pantheon into their runtime or native package manager.
