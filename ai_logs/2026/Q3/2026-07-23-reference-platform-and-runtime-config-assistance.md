# 2026-07-23 — Reference platform and minimal runtime configuration assistance

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Request

Document the installation posture for Hermes Agent, OpenWebUI, PostgreSQL/pgvector, the `ai-net` private network, Ollama, SearXNG, Chromium/Browserless and related external services, while keeping cockpit configuration assistance as small as possible.

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
docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md
```

Official upstream installation and integration documentation was reviewed for Docker networking, Hermes Agent, OpenWebUI, Ollama, pgvector, SearXNG and Browserless/Chromium.

## Installation decision

```text
Pantheon Next owns the baseline, installation guidance, status distinctions and gates.
The human and external infrastructure tooling install and maintain the services.
Hermes executes.
OpenWebUI exposes.
Pantheon MVP may later project a minimal runtime-connection card.
```

The common baseline is split into:

```text
required foundation
+ conditional services selected by reviewed bindings
```

Required foundation includes the container substrate, private network, persistent storage, backup/rollback posture, Hermes, OpenWebUI and PostgreSQL/pgvector availability. Ollama, embeddings, SearXNG, Browserless, Docling, OCR, observability and external runtime memory are conditional.

## Refined cockpit decision

The cockpit remains deliberately small:

```text
install and maintain through native/operator tooling
-> observe the minimum connection state
-> obtain policy, classification and validation from the Pantheon MCP
-> expose the result
-> guide the human to the native surface when change is required
```

The minimum observation surface is limited to:

```text
runtime identity and version
reachability and bounded health
OpenWebUI -> Hermes effective connection
Hermes API authentication present / absent without the key
Pantheon MCP binding present / absent and reachable / unreachable
configuration compatibility after update
observation source and time
```

The cockpit does not need to inventory or manage every model, provider, plugin, skill, tool, memory backend or feature flag.

## MCP boundary

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

The cockpit renders these results and must not duplicate their rules.

```text
cockpit display != policy source
runtime observation != governance decision
MCP result != human approval
```

## Configuration-version drift

Hermes and OpenWebUI configuration formats may change between versions. Field names, nesting, persistence behavior, environment variables, defaults, CLI commands and administration interfaces must not be assumed stable.

Recorded rules:

```text
observe exact runtime version before guidance
bind guidance to a reviewed version range
unsupported version -> stop and use native/upstream documentation
runtime update != configuration compatibility
configuration migration status must be checked separately
hard-coded file or field path != stable contract
```

The cockpit must not implement a generic YAML/JSON patcher or arbitrary configuration-file editor.

## Direct writes

A generic cockpit write adapter is not selected.

```text
bounded direct write -> documented non-implemented
current need          -> not demonstrated
initial posture       -> native/operator application only
```

A future bounded write may be reconsidered only for one concrete, repetitive and low-risk need that cannot be handled acceptably through native guidance. It must not shape the initial architecture.

## Files changed

```text
docs/install/REFERENCE_PLATFORM_COMPONENTS.md
  component-by-component operator guide

docs/governance/COCKPIT_RUNTIME_CONFIGURATION_ASSISTANCE.md
  minimal MCP-backed runtime-connection assistance boundary

docs/governance/COMMON_INSTALLATION_BASELINE.md
  required foundation separated from conditional services

docs/install/COMMON_BASELINE_RUNBOOK.md
  manual sequence aligned with the revised baseline

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
secret stored: no
external action: GitHub documentation branch and draft PR only
memory behavior: none
approval behavior: none
```

## Explicit non-equivalences

```text
installation guide != installer
command candidate != command executed
service present != binding selected
binding selected != dependency adopted
cockpit observation != policy decision
configuration proposal != execution
runtime updated != configuration compatible
healthy != safe
update available != update authorized
```

## Result

The repository now documents the external platform without creating a universal installer. The cockpit scope is reduced to minimum connection visibility and operator guidance, while policy, classification and validation remain in the Pantheon MCP. Configuration-version drift is an explicit stop condition for any unsupported guidance or future write path.
