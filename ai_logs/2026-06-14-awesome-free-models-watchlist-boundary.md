# AI Log — awesome-free-models external tooling watchlist boundary

Date: 2026-06-14

## Context

The user reviewed `12britz/awesome-free-models` as a possible resource for Pantheon Next tooling discovery.

The repository is a curated list of free AI models, API tiers, local inference tools, chatbot UIs, RAG/vector databases, agentic frameworks, fine-tuning tools, datasets, hosting platforms and learning resources.

The useful question was not whether Pantheon should import the catalogue, but where such a catalogue belongs and what must be verified before any item becomes usable in professional work.

## Repository reading

The active governance documents were reviewed before the change:

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`

Additional repository material checked:

- `docs/governance/AUTHORITY_INDEX.md`
- `docs/governance/EXTERNAL_TOOLS_POLICY.md`
- `docs/governance/EXTERNAL_TOOL_PLACEMENT_REGISTER.md`
- `docs/governance/CAPABILITY_REGISTRY.md`
- `docs/governance/OPENWEBUI_INTEGRATION.md`
- Issue #41 process note on PR preference and doctrine sprawl

External source checked:

- `https://github.com/12britz/awesome-free-models`

## Decision

Accepted with constraints:

```text
awesome-free-models may be used as an external tooling watchlist source.
```

Refused:

```text
awesome-free-models as approved model catalogue.
awesome-free-models as approved provider list.
awesome-free-models as approved install source.
awesome-free-models as license authority.
awesome-free-models as privacy authority.
awesome-free-models as benchmark authority.
awesome-free-models as Pantheon capability registry.
awesome-free-models as Hermes skill registry.
```

To verify for each discovered item:

```text
exact upstream source;
pinned version or retrieval date;
license and commercial-use status;
data retention and training policy;
local / cloud processing boundary;
required permissions;
quota or free-tier volatility;
professional-domain benchmark result;
forbidden outputs and effects;
owner and review date.
```

To arbitrate later:

```text
Whether the dashboard should expose a Tooling Watchlist view.
Whether candidates should later be promoted into the candidate Capability Registry.
Whether any specific model or API can be admitted for IFJ architecture dossiers.
```

## Change made

Updated:

- `docs/governance/EXTERNAL_TOOL_PLACEMENT_REGISTER.md`

Added `12britz/awesome-free-models` as:

```text
external tooling watchlist source only; may seed candidates, never approve them.
```

The register now clarifies that a dashboard `Tooling Watchlist` may display and qualify reviewed candidates, but must not authorize, install, route, benchmark, approve or treat free availability as professional suitability.

## Boundary state

Documented non implemented.

No runtime, dashboard implementation, Hermes skill, provider configuration, model configuration, connector, schema, test, Docker, operations file or dependency was added.

## Process note

Issue #41 prefers PR-based work and warns against doctrine sprawl. This intervention stayed minimal by updating the existing external tool placement register instead of creating a new doctrine document.

The change was applied directly to `main` because it was limited to allowed governance Markdown plus this AI log. A future structural dashboard or capability-registry change should use a PR.
