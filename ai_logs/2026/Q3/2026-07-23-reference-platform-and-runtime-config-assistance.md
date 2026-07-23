# 2026-07-23 — Reference platform and runtime configuration assistance

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Request

Document the installation posture for Hermes Agent, OpenWebUI, PostgreSQL/pgvector, the `ai-net` private network, Ollama, SearXNG, Chromium/Browserless and related external services, while continuing the design reflection on whether the Pantheon cockpit may help modify Hermes and OpenWebUI configuration.

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

## Decision recorded

```text
Pantheon Next owns the baseline, installation guidance, status distinctions and gates.
The human and external infrastructure tooling install and maintain the services.
Hermes executes.
OpenWebUI exposes.
Pantheon MVP may later project configuration-assistance cards.
```

The common baseline is now split into:

```text
required foundation
+ conditional services selected by reviewed bindings
```

Required foundation includes the container substrate, private network, persistent storage, backup/rollback posture, Hermes, OpenWebUI and PostgreSQL/pgvector availability. Ollama, embeddings, SearXNG, Browserless, Docling, OCR, observability and external runtime memory are conditional.

## Cockpit posture

The initial cockpit configuration posture is:

```text
observe
-> explain
-> propose
-> human/native application
-> verify
```

The first product target is a Configuration Change Candidate with a diff, rationale, effect classification, secret/restart impact, expected checks and rollback reference.

Direct write behavior remains:

```text
documented non-implemented
default disabled
```

Any future bounded write requires a documented native interface, exact runtime version, allowlisted field, current-value observation, explicit human confirmation, secret isolation, readback, health check and rollback.

## Files changed

```text
docs/install/REFERENCE_PLATFORM_COMPONENTS.md
  new component-by-component operator guide

docs/governance/COCKPIT_RUNTIME_CONFIGURATION_ASSISTANCE.md
  new proposal-first configuration-assistance boundary

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
configuration proposal != execution
observed applied != configuration admitted
healthy != safe
update available != update authorized
```

## Open questions preserved

```text
Which Hermes configuration surfaces are stable and officially supported for writes?
Which OpenWebUI settings have supported administration APIs rather than persisted database-only configuration?
Which low-risk changes justify cockpit application instead of native-UI guidance?
How should stale observations invalidate approval?
Which restart actions should remain operator-only permanently?
How can drift be observed without making Pantheon a monitoring runtime?
```

## Result

The repository now has a coherent documentation-first path for installing the external platform and continuing the cockpit configuration discussion without creating an installer, Docker controller, secret store or runtime administrator.
