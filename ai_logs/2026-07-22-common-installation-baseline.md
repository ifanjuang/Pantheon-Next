# Common installation baseline and self-review

Status: validation-only trace — no authority effect.

## User decision

The user selected one common installation baseline for all supported deployments. Pantheon presets are not the active installation path.

The common component presence includes Hermes, OpenWebUI, PostgreSQL, pgvector, embeddings, Docling, SearXNG, a pinned read-only Pantheon checkout, the Pantheon policy MCP and the Pantheon Modules dashboard plugin.

Required presence does not silently select or activate every binding.

## Repository changes

PR #437 adds:

- `docs/governance/COMMON_INSTALLATION_BASELINE.md`;
- `docs/install/COMMON_BASELINE_RUNBOOK.md`;
- `templates/openwebui/pantheon_common.env.template`;
- a corrected versioned Hermes MCP fragment;
- authority and runtime-status indexing;
- Hermes template navigation.

No Docker stack, installer, database schema, migration, secret, provider binding, runtime, public exposure or activation is added.

## Self-review findings

The first draft had four material problems:

1. commands using `/opt/data/...` and `hermes plugins ...` did not state clearly that they run inside the Hermes container;
2. omitting `platform_toolsets.api_server` would restore Hermes' broad native API-server toolset;
3. the new installation direction was missing from `WHAT_RUNS.md` and from the intervention trace;
4. the dashboard plugin command followed the remote default branch instead of the audited Pantheon commit.

The branch now:

- separates host SSH commands from `docker exec` commands;
- retains `platform_toolsets.api_server: [pantheon-policy]`;
- records the possible Hermes 0.18.2 static warning without weakening the runtime allowlist;
- requires runtime verification that native API toolsets are absent and the Pantheon MCP remains callable;
- installs the dashboard plugin from the pinned local read-only checkout;
- indexes the candidate baseline and runbook in the repository status maps.

## Boundary

```text
documented baseline != installed stack
service present != binding selected
binding selected != dependency adopted
runtime success != evidence
acceptance passed != professional validation
```

Pantheon governs the baseline and status vocabulary. The operator executes through SSH, Docker Compose, Portainer or vendor tooling. Hermes executes after installation. OpenWebUI exposes. The human approves consequential changes.

## Validation posture

The reviewed content before the final pinning correction passed:

```text
Governance CI                    -> success
MCP server unit and stdio tests -> success
Packaging and release contract  -> success
Obsolete authority consistency  -> success
```

The PR remains draft. CI must confirm the final reviewed head, and the generated `ai_logs/INDEX.md` must be regenerated before the PR is marked ready. CI success does not install or authorize the documented stack.
