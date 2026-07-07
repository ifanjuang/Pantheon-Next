# Rite — External Repo Qualification

Status: candidate support rite — bounded method for reviewing external repositories before capability-candidate placement.

Runtime status: non-executable.

This rite defines a review sequence for an external repository, product, tool, library or local application that may become a Capability Candidate.

It does not clone, install, execute, scan, sandbox, benchmark, configure, update, approve, reject by automation, create a Hermes skill, create an adapter, create a connector, create an OpenWebUI plugin, promote memory or authorize external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

External repositories often arrive as links, examples or recommendations.

This rite prevents link review from turning into dependency adoption.

It produces a governed classification:

```text
external repository
-> abstract function
-> Capability Slot
-> candidate binding
-> installation / health / update posture
-> risk and gate map
-> decision recommendation
```

## Entry conditions

Use this rite when a repository or tool may affect:

```text
professional output;
source interpretation;
document preparation;
retrieval or RAG;
meeting capture;
external communication;
file mutation;
repository mutation;
long-lived memory;
provider selection;
runtime installation;
updates or rollback.
```

A light review is enough when the repository is pure inspiration.

A full review is required when the repository could become a binding, adapter, connector, runtime dependency, skill projection or privileged local tool.

## Roles

Recommended role sequence:

| Step | Role | Function |
|---:|---|---|
| 1 | ATHENA | define the abstract function and likely use case |
| 2 | ARGOS | identify sources, repository facts, license, provenance and version signals |
| 3 | THEMIS | review risk, data exposure, approval and legal/professional boundaries |
| 4 | HEPHAISTOS | identify possible binding, runtime needs and implementation boundary |
| 5 | APOLLO | make the review readable and decision-ready |
| 6 | ZEUS | arbitrate status, gates and next procedure |

These roles are review functions, not agents.

The rite is a method, not a workflow runtime.

## Steps

### 1. Identify the repository

Record:

```yaml
repository_review:
  repository_name:
  repository_url:
  owner:
  default_branch:
  license:
  reviewed_ref:
  reviewed_date:
  public_or_private:
```

If repository identity is ambiguous, stop at `to_verify`.

### 2. Extract the abstract function

Do not begin with the product name.

Begin with the function:

```text
prepare documents for RAG
capture and transcribe meetings
manage external connectors
compare quotes against CCTP
serve local models
visualize provenance
```

This becomes the Capability Slot.

### 3. Classify placement

Use the placement rule:

```text
what Pantheon governs;
what Hermes executes;
what OpenWebUI exposes;
what the human approves;
what remains forbidden.
```

If the repository mainly executes, it belongs outside Pantheon.

If the repository mainly displays, it belongs in the exposure surface or adapter layer.

If the repository creates consequential status, evidence, approval, memory or external effect, Pantheon governs that consequence only.

### 4. Review capability surface

Record whether the tool can:

```text
read private material;
write durable material;
send or publish externally;
call providers or cloud APIs;
store, index or recall long-lived data;
record audio or screen content;
execute commands;
install or update itself;
change repository or project files;
produce professional output.
```

Each positive answer must map to a gate or safe default.

### 5. Determine candidate binding

A binding candidate names how the abstract capability could be executed.

Examples:

```text
chunky-local-docker under Hermes
meetily-desktop-local outside Pantheon, visible only as candidate source
cadastre-api-query through Hermes connector gateway
openwebui-display-card for cockpit exposure
```

A binding candidate does not mean dependency adoption.

### 6. Classify status

Use the following classification blocks.

Repository status:

```text
active
archived
unknown
renamed_or_migrated
to_verify
```

Capability status:

```text
external_reference
capability_candidate
accepted_for_sandbox
approved_for_sandbox
approved_for_project
blocked
refused
```

Runtime status:

```text
not_installed
installed_elsewhere
unknown
sandbox_only
to_verify
```

Implementation status:

```text
implemented
documented_non_implemented
partial
to_verify
obsolete
non_applicable
```

### 7. Define gates

Choose gates proportionally.

Common gates:

```text
license_review_gate
source_review_gate
sandbox_approval_gate
external_provider_gate
data_exit_gate
client_data_gate
analytics_gate
update_authorization_gate
runtime_health_gate
rollback_gate
evidence_quality_gate
indexation_approval_gate
recording_consent_gate
external_action_gate
memory_promotion_gate
```

A gate blocks or authorizes a status.

It does not run the repository.

### 8. Produce decision recommendation

Allowed outcomes:

```text
reject
watchlist
reference_only
capability_candidate
accepted_for_sandbox
needs_more_evidence
needs_adapter_design
blocked_pending_review
```

The recommendation must state:

```text
why;
what may be tested;
what must not be tested;
which human decision is required next.
```

## Output shape

```yaml
external_repo_qualification_result:
  repository:
  reviewed_ref:
  reviewed_date:
  abstract_function:
  capability_slot:
  candidate_binding:
  pantheon_governs:
  hermes_executes:
  openwebui_exposes:
  human_approves:
  forbidden:
  status:
    repository_status:
    capability_status:
    runtime_status:
    implementation_status:
  risks:
  required_gates:
  safe_default:
  decision_recommendation:
  trace_refs:
```

## Safe defaults

If the rite is incomplete:

```text
no installation;
no client data;
no external provider call;
no production use;
no memory promotion;
no external effect;
no approval claim;
no dependency adoption;
status: to_verify.
```

## Card projection

The result may appear in the Card Stack as:

```text
Capability Candidate Card
Binding Candidate Card
Risk Card
Gate Card
Sandbox Test Proposal Card
Capability Gap Card
```

Those cards expose status.

They do not execute the repository.

## Boundary phrase

```text
A repository can inspire.
A capability can be named.
A binding can be proposed.
The gate decides status.
The human decides use.
Pantheon does not become the runtime.
```
