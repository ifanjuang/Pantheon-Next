# Install Module Catalog

Status: candidate support doctrine — installable module catalog and preset grammar. Repository state: documented non-implemented.
Boundary profile: candidate_support_note.

## Purpose

This document defines a governance-readable catalog shape for installable modules and stack presets.

It is inspired by external catalog patterns, but it is not a clone of any of them:

```text
Portainer templates -> deployment-facing fields such as title, description, category, platform, image, ports, volumes and environment.
Helm charts -> package metadata, dependencies, chart version, appVersion and platform constraints.
Backstage catalog entities -> apiVersion/kind/metadata/spec envelope and ownership/lifecycle/system metadata.
Home Assistant integration manifests -> domain, name, documentation, requirements, integration type and local/cloud class.
Homebrew formulae -> pinned source, checksum, livecheck, dependencies, conflicts, caveats and tests.
```

Pantheon adds the missing governance layer:

```text
approval gates
activation gates
secret policy
conflict classes
preset classifications
health status
rollback posture
source trust
non-equivalence rules
```

This document does not create a live module registry, installer, Portainer stack, Docker file, SSH runner, package manager, plugin marketplace, provider router, scheduler, queue, approval engine or memory engine.

## Boundary

```text
exposed_by:
  OpenWebUI or Pantheon Control may expose module cards, preset cards, dependency maps, conflict warnings, version status, update status and activation gates.

executed_by:
  A bounded provisioner, Portainer, Docker, SSH bootstrapper, package manager or external runtime executes installation outside Pantheon.

governed_by:
  Pantheon governs classification, status vocabulary, gates, source trust, dependency adoption, conflict review, activation, evidence expectations and rollback visibility.

approved_by:
  The human approves installation, module adoption, update, public exposure, provider binding, secret handling, external action and rollback.

forbidden:
  The catalog must not become a plugin marketplace, dependency adoption engine, auto-installer, secret store, provider router, update runner, shell runner, approval shortcut, activation shortcut or memory promotion path.
```

## External pattern distillation

### Portainer-like deployment surface

Useful fields:

```text
display name
description
categories
platform
container image
ports
volumes
environment variables
```

Pantheon adjustment:

```text
ports and volumes are not just technical fields; they also create exposure, persistence, backup and rollback questions.
```

### Helm-like package surface

Useful fields:

```text
api version
chart/package version
application version
dependencies
repository
maintainers
platform/version constraints
deprecation
annotations
```

Pantheon adjustment:

```text
module_version != application_version
version_detected != version_authorized
constraint_satisfied != installation_approved
```

### Backstage-like catalog envelope

Useful fields:

```text
apiVersion
kind
metadata
spec
owner
lifecycle
system
links
annotations
tags
```

Pantheon adjustment:

```text
owner must be a governance owner or human decision owner, not only a technical team.
lifecycle must distinguish catalog maturity, install status and activation status.
```

### Home Assistant-like integration manifest

Useful fields:

```text
domain
name
documentation
requirements
integration_type
local/cloud class
code owners
config flow
```

Pantheon adjustment:

```text
local != safe
cloud != forbidden
requirement_available != capability_authorized
configuration_possible != configuration_approved
```

### Homebrew-like formula metadata

Useful fields:

```text
description
homepage
source URL
checksum
license
livecheck
dependencies
conflicts
caveats
tests
```

Pantheon adjustment:

```text
checksum_verified != source_approved
conflict_detected != conflict_resolved
test_passed != safe_activation
latest_detected != update_authorized
```

## Catalog files

Recommended repository shape for future implementation:

```text
install_catalog/
  modules.json
  presets.json
  conflict_rules.json
  source_trust.json
  update_policies.json
```

Current status: documented non-implemented.

These files should not be added as implementation artifacts without schema and protected review. Until then, this document is the candidate grammar only.

## Module record shape

A module record should use a stable envelope:

```json
{
  "apiVersion": "pantheon.next/v1alpha1",
  "kind": "InstallModule",
  "metadata": {
    "module_id": "postgres",
    "display_name": "Postgres",
    "description": "Relational database for data, observability, RAG and checkpoint-capable modules.",
    "family": "data",
    "roles": ["primary_relational_database"],
    "tags": ["database", "persistent", "critical"],
    "owner": "human_admin",
    "maturity": "stable"
  },
  "spec": {
    "classification_default": "recommended",
    "source": {},
    "provisioning": {},
    "dependencies": {},
    "conflicts": [],
    "presets": {},
    "gates": {},
    "health": {},
    "rollback": {},
    "updates": {},
    "forbidden": []
  },
  "status": {
    "catalog_status": "candidate",
    "install_status": "not_installed",
    "health_status": "not_checked",
    "activation_status": "disabled",
    "adoption_status": "not_adopted"
  }
}
```

The envelope keeps Pantheon close to established catalog practice while preserving its own governance status fields.

## Module classifications

Use classifications inside a preset, not as global absolutes unless the module is part of bootstrap itself.

```text
mandatory
  Required by the selected preset or capability.

recommended
  Recommended for the selected preset, but removable with warning.

optional
  Available but not required.

experimental
  Testable under sandbox/review conditions only.

blocked
  Known but currently disallowed.

deprecated
  Still recognized but should be replaced.
```

Rule:

```text
mandatory_for_preset != mandatory_for_pantheon
recommended != approved
optional != harmless
experimental != unavailable
blocked != unknown
```

## Source trust

A source block should make freshness and trust explicit:

```json
{
  "source": {
    "type": "official_image | official_repo | internal_repo | community_repo | postgres_extension | package_manager",
    "repo": "docker.io/library/postgres",
    "homepage": "https://www.postgresql.org/",
    "release_channel": "stable",
    "version_policy": "pinned",
    "recommended_version": "16",
    "selected_version": "16.4",
    "digest_or_checksum": "sha256:...",
    "allow_latest": false,
    "source_trust": "official",
    "license": "to_verify"
  }
}
```

Rules:

```text
repo_exists != source_trusted
latest_exists != latest_authorized
official_source != no_review_required
checksum_present != source_approved
```

## Provisioning

A provisioning block should describe who executes and how:

```json
{
  "provisioning": {
    "provisioner": "portainer | ssh_provisioner | docker_compose | package_manager | manual",
    "install_mode": "docker_stack | compose_stack | shell_manifest | postgres_extension | package_install",
    "requires_bootstrap": true,
    "requires_privilege": "user | sudo | root | unknown",
    "writes_files": true,
    "network_access": true,
    "secret_inputs": ["postgres_password"],
    "public_exposure_default": false
  }
}
```

Rules:

```text
provisioner_available != execution_authorized
stack_generated != stack_approved
portainer_running != portainer_governed
ssh_available != free_shell_authorized
```

## Dependencies

Dependencies should be typed:

```json
{
  "dependencies": {
    "requires": ["docker", "portainer"],
    "recommends": ["backup_service"],
    "optional": ["pgvector"],
    "provides": ["primary_relational_database"],
    "requires_roles": ["container_runtime"],
    "provides_roles": ["primary_relational_database"]
  }
}
```

Rules:

```text
dependency_installed != dependency_adopted
role_available != role_selected
binding_selected != dependency_adopted
```

## Conflicts

Conflict entries should carry class, severity and reason:

```json
{
  "conflicts": [
    {
      "with": "external_postgres",
      "type": "role_conflict",
      "severity": "soft",
      "reason": "Only one primary Postgres binding should be selected for a data role unless explicitly configured."
    }
  ]
}
```

Conflict types:

```text
hard_conflict
soft_conflict
role_conflict
port_conflict
resource_conflict
data_conflict
governance_conflict
version_conflict
security_conflict
lifecycle_conflict
```

Rules:

```text
conflict_detected != conflict_resolved
soft_conflict != safe_combination
hard_conflict != impossible_forever
```

## Gates

Every module needs at least install and activation gates:

```json
{
  "gates": {
    "install": "human_required",
    "activate": "human_required",
    "adopt_for_project": "human_required",
    "expose_public": "blocked_by_default",
    "provide_secret": "external_secret_store_or_runtime_prompt",
    "major_update": "human_required",
    "delete_volume": "elevated_approval_required"
  }
}
```

Rules:

```text
install_approved != activation_approved
secret_present != secret_governed
public_port_open != exposure_authorized
major_update_available != major_update_authorized
```

## Health and rollback

Health should be observed, not over-interpreted:

```json
{
  "health": {
    "check_kind": "container_health | http | command | postgres_extension | manual",
    "check_command": "pg_isready",
    "expected_result": "ready",
    "last_result": "not_checked"
  },
  "rollback": {
    "required": true,
    "strategy": "snapshot | previous_image | volume_backup | manual",
    "last_verified": "never"
  }
}
```

Rules:

```text
health_green != safe
service_ready != data_policy_safe
rollback_defined != rollback_tested
backup_configured != backup_verified
```

## Updates

Update policy should be separate from source freshness:

```json
{
  "updates": {
    "check_latest": true,
    "policy": "manual | auto_patch | security_patch_only | pinned_only",
    "patch": "policy_allowed",
    "minor": "human_required",
    "major": "human_required",
    "breaking": "blocked_until_review",
    "rollback_required": true
  }
}
```

Rules:

```text
update_available != update_authorized
update_downloaded != update_applied
update_applied != update_activated
patch != harmless
```

## Preset record shape

A preset record composes modules without silently activating capabilities:

```json
{
  "apiVersion": "pantheon.next/v1alpha1",
  "kind": "InstallPreset",
  "metadata": {
    "preset_id": "pantheon_agence",
    "display_name": "Pantheon Agence",
    "description": "Private agency stack with interface, execution, data base, RAG base and observability candidate modules.",
    "maturity": "candidate"
  },
  "spec": {
    "modules": [
      { "module_id": "docker", "classification": "mandatory" },
      { "module_id": "portainer", "classification": "mandatory" },
      { "module_id": "pantheon_control", "classification": "mandatory" },
      { "module_id": "openwebui", "classification": "mandatory" },
      { "module_id": "hermes", "classification": "mandatory" },
      { "module_id": "postgres", "classification": "recommended" },
      { "module_id": "pgvector", "classification": "recommended" },
      { "module_id": "langfuse", "classification": "recommended" },
      { "module_id": "searxng", "classification": "optional" },
      { "module_id": "langgraph", "classification": "optional" },
      { "module_id": "langchain", "classification": "optional" }
    ],
    "forbidden_defaults": [
      "public_gateway_exposure",
      "provider_auto_activation",
      "secret_storage_in_pantheon",
      "external_action_auto_enablement",
      "experimental_module_auto_include"
    ]
  }
}
```

Rules:

```text
preset_selected != preset_approved
preset_installed != preset_activated
module_included != module_authorized_for_use
pack_installed != capability_authorized
```

## Example modules

### Postgres

```json
{
  "apiVersion": "pantheon.next/v1alpha1",
  "kind": "InstallModule",
  "metadata": {
    "module_id": "postgres",
    "display_name": "Postgres",
    "family": "data",
    "roles": ["primary_relational_database"],
    "maturity": "stable"
  },
  "spec": {
    "classification_default": "recommended",
    "source": {
      "type": "official_image",
      "repo": "docker.io/library/postgres",
      "version_policy": "pinned",
      "allow_latest": false
    },
    "provisioning": {
      "provisioner": "portainer",
      "install_mode": "docker_stack",
      "public_exposure_default": false
    },
    "dependencies": {
      "requires": ["docker", "portainer"],
      "recommends": ["backup_service"],
      "provides_roles": ["primary_relational_database"]
    },
    "conflicts": [
      {
        "with": "external_postgres",
        "type": "role_conflict",
        "severity": "soft",
        "reason": "Only one primary relational database binding should be selected per role unless explicitly configured."
      }
    ],
    "gates": {
      "install": "human_required",
      "adopt_for_pantheon": "human_required",
      "delete_volume": "elevated_approval_required",
      "expose_public": "blocked_by_default"
    }
  }
}
```

### pgvector

```json
{
  "apiVersion": "pantheon.next/v1alpha1",
  "kind": "InstallModule",
  "metadata": {
    "module_id": "pgvector",
    "display_name": "pgvector",
    "family": "data_extension",
    "roles": ["vector_extension"],
    "maturity": "stable"
  },
  "spec": {
    "classification_default": "recommended",
    "source": {
      "type": "postgres_extension",
      "repo": "pgvector/pgvector",
      "version_policy": "pinned",
      "allow_latest": false
    },
    "provisioning": {
      "provisioner": "portainer | ssh_provisioner",
      "install_mode": "postgres_extension"
    },
    "dependencies": {
      "requires": ["postgres"],
      "provides_roles": ["vector_extension"]
    },
    "conflicts": [
      {
        "with": "alternative_vector_db_primary",
        "type": "role_conflict",
        "severity": "soft",
        "reason": "A preset should avoid multiple primary vector stores unless explicit multi-store routing is reviewed."
      }
    ],
    "gates": {
      "install": "human_required",
      "activate_memory_use": "human_required",
      "promote_to_project_memory": "human_required"
    }
  }
}
```

### SearXNG

```json
{
  "apiVersion": "pantheon.next/v1alpha1",
  "kind": "InstallModule",
  "metadata": {
    "module_id": "searxng",
    "display_name": "SearXNG",
    "family": "retrieval_search",
    "roles": ["web_retrieval"],
    "maturity": "stable"
  },
  "spec": {
    "classification_default": "optional",
    "source": {
      "type": "official_repo_or_image",
      "repo": "searxng/searxng",
      "version_policy": "pinned",
      "allow_latest": false
    },
    "provisioning": {
      "provisioner": "portainer",
      "install_mode": "docker_stack",
      "public_exposure_default": false
    },
    "dependencies": {
      "requires": ["docker", "portainer"],
      "optional": ["redis"]
    },
    "conflicts": [
      {
        "with": "unrestricted_web_search_gateway",
        "type": "governance_conflict",
        "severity": "hard",
        "reason": "Search retrieval must not bypass source review, evidence rules or external query gates."
      }
    ],
    "gates": {
      "install": "human_required",
      "external_queries": "human_required",
      "use_as_evidence": "blocked_by_default",
      "public_exposure": "blocked_by_default"
    }
  }
}
```

## Final rule

```text
A module catalog may describe installable components.
A preset may recommend or require components.
A conflict rule may warn, block or require arbitration.
A source check may detect available versions.
A provisioner may execute after approval.

Neither a module nor a preset may silently authorize consequential activation.
```

## Review status

```text
review_result: candidate / to_verify
runtime_impact: none
protected_paths_touched: no
schema_test_ci_impact: none
external_action: none
memory_behavior: none
approval_behavior: none
```
