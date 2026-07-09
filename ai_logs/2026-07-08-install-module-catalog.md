# Install module catalog grammar

Date: 2026-07-08

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

- Added: `docs/governance/INSTALL_MODULE_CATALOG.md`.
- Updated: `docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md`.
- Updated: `docs/governance/WHAT_RUNS.md`.
- Removed: none.

## External catalog patterns reviewed

The candidate grammar distills useful fields from:

- Portainer templates: title, description, categories, platform, image, ports, volumes, environment.
- Helm charts: package version, appVersion, dependencies, platform constraints, annotations, deprecation.
- Backstage catalog descriptors: apiVersion, kind, metadata, spec, owner, lifecycle, system, tags, links.
- Home Assistant integration manifests: domain, name, documentation, requirements, integration type, local/cloud class.
- Homebrew formulae: source URL, checksum, livecheck, dependencies, conflicts, caveats and tests.

## Pantheon-specific additions

The external patterns were not imported as-is. The new candidate grammar adds:

```text
approval gates
activation gates
source trust
version policy
preset classification
conflict classes
dependency roles
secret policy
health status
rollback posture
update policy
non-equivalence rules
```

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none.
Authority impact: candidate support doctrine indexed; no promotion to canonical doctrine.
Schema/test/CI impact: none.
External action: none.
Memory behavior: none.
Approval behavior: none.

## Local distinctions

```text
module_listed != module_authorized
module_installed != module_activated
preset_selected != preset_approved
latest_detected != update_authorized
dependency_installed != dependency_adopted
conflict_detected != conflict_resolved
health_green != safe
trace != doctrine
```
