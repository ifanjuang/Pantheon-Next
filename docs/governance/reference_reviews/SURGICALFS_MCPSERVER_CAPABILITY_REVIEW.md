# SurgicalFS MCP Server Capability Review

Status: external reference / filesystem capability candidate review — documented non-implemented.

Review date: 2026-07-07.

Repository: `wonker007/surgicalfs-mcpserver`.

Reviewed source: `https://github.com/wonker007/surgicalfs-mcpserver`.

This review records a candidate filesystem capability for Pantheon Next and Hermes. It does not adopt, clone, install, execute, configure, expose, approve, mutate files, start an MCP server, create a gateway, create an OpenWebUI plugin, create a Hermes skill or add SurgicalFS as a dependency.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Short assessment

SurgicalFS is a strong candidate for a governed Hermes filesystem binding.

It is not a Pantheon runtime.

It should not be installed, exposed remotely or granted write access by default.

Recommended outcome:

```text
accepted_for_adapter_design
```

Initial sandbox posture:

```text
local stdio only;
read-only mode;
test directory only;
no client data;
no repository write;
no HTTP transport;
no tunnel;
no dashboard exposure;
no analytics file logging;
no mutation tools.
```

## Abstract function

```text
Provide context-efficient, scoped filesystem access for reading, searching, extracting and, only if separately approved, mutating files.
```

Capability Slot:

```yaml
capability_slot:
  id: governed_filesystem_access
  title: Governed Filesystem Access
  abstract_function: read, search, inspect and optionally mutate files inside an allowlisted scope
  professional_use_case: let Hermes inspect project folders, repositories or document workspaces without loading whole files or exposing uncontrolled filesystem access
  expected_inputs:
    - allowed directory
    - Task Contract
    - read-only or write mode
    - enabled tool categories
    - file path or search request
  expected_outputs:
    - File Inspection Candidate
    - Search Result Candidate
    - Document Extraction Candidate
    - Filesystem Mutation Candidate
    - Runtime Status Candidate
    - Capability Gap
  forbidden_outputs:
    - validated proof
    - approved professional fact
    - automatic memory promotion
    - unreviewed file mutation
    - external action authorization
    - repository modification without PR / gate
```

## Candidate bindings

```yaml
candidate_bindings:
  - id: surgicalfs-local-readonly
    runtime_owner: hermes
    transport: stdio
    scope: test_directory_only
    write_access: false
    status: preferred_sandbox_binding

  - id: surgicalfs-sandbox-write
    runtime_owner: hermes
    transport: stdio
    scope: disposable_test_directory_only
    write_access: true
    status: blocked_pending_mutation_gate

  - id: surgicalfs-http-remote
    runtime_owner: external_runtime
    transport: http
    scope: any
    write_access: unknown
    status: blocked_pending_security_review
```

Binding selected does not mean dependency adopted.

## What Pantheon governs

Pantheon governs:

```text
capability status;
filesystem scope;
allowed directory policy;
read-only requirement;
tool-category activation;
mutation approval;
delete / move approval;
repository-write approval;
HTTP exposure gate;
authentication expectation;
logging and analytics admissibility;
runtime health status;
rollback expectation;
Evidence Pack expectation for file changes;
what may become memory or proof.
```

Pantheon must not start the server, host MCP, write config files, hold tokens, expose tunnels, mutate files or route filesystem calls.

## What Hermes executes

Hermes may execute, if separately authorized:

```text
start or call SurgicalFS as an external MCP filesystem binding;
inspect files;
read partial ranges;
search files;
extract PDF / DOCX / XLSX content;
return compact candidates and trace references;
run mutation tools only when a Task Contract and mutation gate allow it.
```

Hermes must not treat runtime success as proof, approval or memory.

## What OpenWebUI exposes

OpenWebUI may expose:

```text
Filesystem Capability Card;
Allowed Directory Card;
Read-only / Write Mode Card;
Tool Category Card;
Runtime Health Card;
Mutation Gate;
Delete / Move Gate;
HTTP Exposure Warning;
Log / Analytics Warning;
Trace Summary Card.
```

OpenWebUI must not turn a card click into filesystem mutation.

## What the human approves

Human approval is required for:

```text
installation;
allowed directories;
switching from read-only to write mode;
activating mutation / manage categories;
file deletion;
file move;
repository writes;
client-data access;
HTTP transport;
public tunnel exposure;
auth token or network-control posture;
file logging;
analytics logging;
production activation;
updates;
rollback plan.
```

## Forbidden by default

```text
broad filesystem allowlist;
write mode;
mutation tools;
delete / move tools;
repository mutation;
client-data access;
HTTP transport;
remote tunnel;
unauthenticated /mcp exposure;
public control plane;
analytics file logging;
automatic update;
production activation.
```

## Status classification

```yaml
repository_status: active_public_repository
governance_status: capability_candidate_to_verify
runtime_status: not_installed
install_status: absent
health_status: unknown
update_status: unknown
activation_status: unavailable
implementation_status: documented_non_implemented
safe_default: reference_only_until_readonly_sandbox_approved
```

## Positive signals

```text
Rust single-binary posture;
local stdio transport supported;
allowlisted directories required;
symlinks disabled by default;
read-only mode exists;
response budget exists;
partial read operations reduce context load;
structured extraction for JSON / CSV / XLSX / PDF / DOCX;
server-side path validation exists;
atomic write pattern exists;
HTTP authentication option exists;
control plane is intended to remain localhost-only.
```

These signals reduce risk only when configuration matches the safe profile.

They do not authorize use.

## Risk review

| Risk | Classification | Gate |
|---|---|---|
| Broad local filesystem access | critical | filesystem_scope_gate |
| Write or mutation tools enabled | critical | mutation_approval_gate |
| Delete / move tools enabled | critical | delete_move_gate |
| Repository modification without PR | high | repo_write_gate |
| Client documents accessed without scope | high | client_data_gate |
| HTTP / tunnel exposure | critical | http_exposure_gate |
| Empty or weak `/mcp` auth posture | critical | auth_token_gate / network_access_gate |
| Dashboard or control plane exposed | critical | control_plane_gate |
| Full paths in logs or analytics | high | logging_analytics_gate |
| Runtime success treated as evidence | high | evidence_quality_gate |
| File mutation treated as approval | high | external_action_gate |
| Config drift between read-only and write mode | high | runtime_health_gate / config_drift_gate |
| Update changes tool behavior | medium | update_authorization_gate |

## Required gates

```text
filesystem_scope_gate
read_only_gate
mutation_approval_gate
delete_move_gate
repo_write_gate
client_data_gate
http_exposure_gate
auth_token_gate
network_access_gate
control_plane_gate
logging_analytics_gate
runtime_health_gate
config_drift_gate
rollback_gate
evidence_quality_gate
external_action_gate
memory_promotion_gate
update_authorization_gate
```

## Minimum acceptable sandbox

```toml
# Conceptual profile only. Do not treat this as an install instruction.
[server]
transport = "stdio"

[security]
allowed_directories = ["<disposable-test-directory>"]
follow_symlinks = false
read_only = true
max_file_size = 5242880

[tools]
enable = ["inspect", "search", "directory", "utility"]

[logging]
log_dir = ""

[analytics]
log_dir = ""
```

This profile is a governance target, not an executable configuration owned by Pantheon.

## Sandbox test proposal

Allowed test:

```text
Use a disposable folder containing synthetic test files.
Run local stdio only.
Use read-only mode.
Enable inspect / search / directory / utility only.
Verify allowlist denial outside test folder.
Verify symlink denial.
Verify response-budget behavior.
Verify no mutation tools are available.
Record runtime status as candidate only.
Do not use client data.
Do not expose HTTP.
Do not write repository files.
```

Expected result:

```text
Runtime Status Candidate
Filesystem Scope Candidate
Read-only Verification Candidate
Capability Gap list
Gate Recommendation
```

## Future write-mode conditions

Write mode remains blocked until:

```text
Task Contract exists;
mutation target is explicit;
allowed directory is disposable or project-scoped;
backup / rollback expectation is defined;
idempotency key exists;
mutation diff is reviewable;
external effect classification is complete;
User Decision Gate approves;
output returns an Evidence Pack Candidate;
repository writes route through branch / PR discipline.
```

## Decision

```yaml
decision_recommendation: accepted_for_adapter_design
reason: strong context-efficient filesystem capability for Hermes if constrained to local, scoped, read-only operation first
preferred_initial_binding: surgicalfs-local-readonly
default_activation: unavailable
write_activation: blocked
remote_http_activation: blocked
next_allowed_step: documentation review and read-only sandbox design only
```

## Boundary phrase

```text
SurgicalFS may expose the filesystem.
That makes it powerful, not approved.
Hermes may execute only inside a bounded handoff.
OpenWebUI may expose status and gates.
Pantheon governs scope, mutation, evidence and memory.
The human decides.
```
