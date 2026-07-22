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

The former installation-composition document, manifests and schema are removed from the working tree and retained only in Git history. Their schema fields, fixtures, validators and static projections are migrated to reviewed configuration references.

No Docker stack, installer, database migration, secret, provider binding, runtime, public exposure or activation is added.

## Self-review findings

The first draft had five material problems:

1. commands using `/opt/data/...` and `hermes plugins ...` did not state clearly that they run inside the Hermes container;
2. omitting `platform_toolsets.api_server` would restore Hermes' broad native API-server toolset;
3. the new installation direction was missing from `WHAT_RUNS.md` and from the intervention trace;
4. the dashboard plugin command followed the remote default branch instead of the audited Pantheon commit;
5. the old installation-composition model remained visible and loadable as a parallel catalog grammar despite the decision to use one common baseline.

The branch now:

- separates host SSH commands from `docker exec` commands;
- retains `platform_toolsets.api_server: [pantheon-policy]`;
- records the possible Hermes 0.18.2 static warning without weakening the runtime allowlist;
- requires runtime verification that native API toolsets are absent and the Pantheon MCP remains callable;
- installs the dashboard plugin from the pinned local read-only checkout;
- uses one shared component baseline;
- retains only independent module records for status, dependencies, gates, health, updates and rollback;
- removes the retired installation-composition files and reader;
- binds handoff decisions to the exact reviewed `InstallationCandidate` through `configuration_ref`;
- acknowledges the deliberate reduction of `INSTALL_MODULE_CATALOG.md` in the repository truncation guard.

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

The final branch must pass:

```text
Governance CI
Capability Catalog CI
Provisioner Handoff CI
Handoff Decision CI
Current Decision Resolver CI
MCP server unit and stdio tests
Packaging and release contract
Obsolete authority consistency
```

The generated `ai_logs/INDEX.md` was regenerated deterministically to 662 entries and includes this trace. The PR may move to human review once the final CI on the resulting tree is green. CI success does not install or authorize the documented stack.
