# Common installation baseline and self-review

Status: validation-only trace — no authority effect.

## User decision

The user selected one common installation baseline for all supported deployments and explicitly retired alternative Pantheon installation compositions.

The common component presence includes Hermes, OpenWebUI, PostgreSQL, pgvector, embeddings, Docling, SearXNG, a pinned read-only Pantheon checkout, the Pantheon policy MCP and the Pantheon Modules dashboard plugin.

Required presence does not silently select or activate every binding.

## Repository changes

PR #437 adds or aligns:

- `docs/governance/COMMON_INSTALLATION_BASELINE.md`;
- `docs/install/COMMON_BASELINE_RUNBOOK.md`;
- `templates/openwebui/pantheon_common.env.template`;
- a corrected versioned Hermes MCP fragment;
- a module-only installation catalog;
- authority and runtime-status indexing;
- Hermes template navigation.

The former installation-composition model and its declarative examples are classified obsolete. They remain historical only and must not determine, render or install an environment.

No Docker stack, installer, database schema, migration, secret, provider binding, runtime, public exposure or activation is added.

## Self-review findings

The first draft had five material problems:

1. commands using `/opt/data/...` and `hermes plugins ...` did not state clearly that they run inside the Hermes container;
2. omitting `platform_toolsets.api_server` would restore Hermes' broad native API-server toolset;
3. the new installation direction was missing from `WHAT_RUNS.md` and from the intervention trace;
4. the dashboard plugin command followed the remote default branch instead of the audited Pantheon commit;
5. the old installation-composition model remained visible as a parallel grammar despite the decision to use one common baseline.

The branch now:

- separates host SSH commands from `docker exec` commands;
- retains `platform_toolsets.api_server: [pantheon-policy]`;
- records the possible Hermes 0.18.2 static warning without weakening the runtime allowlist;
- requires runtime verification that native API toolsets are absent and the Pantheon MCP remains callable;
- installs the dashboard plugin from the pinned local read-only checkout;
- uses one shared component baseline;
- retains only independent module records for status, dependencies, gates, health, updates and rollback;
- classifies historical installation-composition documents, schemas and examples as obsolete.

## Boundary

```text
documented baseline != installed stack
required presence != active binding
service present != binding selected
binding selected != dependency adopted
runtime success != evidence
acceptance passed != professional validation
```

Pantheon governs the baseline and status vocabulary. The operator executes through SSH, Docker Compose, Portainer or vendor tooling. Hermes executes after installation. OpenWebUI exposes. The human approves consequential changes.

## Validation posture

Previous reviewed heads passed:

```text
Governance CI                    -> success
MCP server unit and stdio tests -> success
Packaging and release contract  -> success
Obsolete authority consistency  -> success
```

The PR remains draft. CI must confirm the final reviewed head, and the generated `ai_logs/INDEX.md` must be regenerated before the PR is marked ready. CI success does not install or authorize the documented stack.
