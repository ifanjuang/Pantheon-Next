# Pantheon MCP Policy Server — Development Roadmap

Status: candidate development doctrine — documented non-implemented.

This document describes the development sequence for a future Pantheon MCP Policy Server.

It is documentation only. It does not implement an MCP server, Docker service, installer, dashboard, API gateway, connector runtime, scheduler, queue, approval engine, memory engine, provider router, plugin manager or external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

The MCP Policy Server is a proposed read-only / validation / candidate-preparation boundary for Hermes Agent.

It should help Hermes frame work under Pantheon governance without turning Pantheon into the execution runtime.

```text
User request
→ OpenWebUI exposure
→ Hermes execution runtime
→ MCP Policy Server governance check
→ Result Candidate + Evidence Pack Candidate
→ human decision
```

The MCP Policy Server checks the frame. It does not execute the professional task.

## Non-goals

The MCP Policy Server must not become:

```text
runtime
scheduler
queue
approval engine
memory promotion engine
connector gateway
plugin manager
installer
dashboard
provider router
skill installer
tool dispatcher with implicit authority
hidden workflow runner
```

It must not:

```text
send messages
write files
merge code
approve outputs
promote memory
install skills
run shell commands
schedule jobs
select providers autonomously
trigger external actions
```

## Relationship to Pantheon Control

Pantheon Control may later install, display and preflight the MCP Policy Server.

That installation work is separate from this document.

The MCP Policy Server may appear in a future Pantheon Control dashboard as:

```text
installed
connected
authorized for validation
validated for a scope
blocked for external action
```

Those states must remain distinct:

```text
installed != connected != authorized != validated
```

## Development principle

Each development phase must preserve this boundary:

```text
The repo defines governance.
The MCP exposes and validates governance.
Hermes executes under Task Contract.
The Evidence Pack supports review.
The human decides.
```

No phase may silently convert candidate output into validated truth, authorized action or canonical memory.

## Phase 0 — Boundary freeze

Goal: freeze the MCP role before implementation.

The MCP is allowed to be:

```text
policy server
read-only doctrine access layer
validation layer
candidate preparation layer
preflight support layer
```

The MCP is not allowed to be:

```text
runtime
connector gateway
approval authority
memory authority
installation authority
```

Exit criteria:

```text
The boundary is explicit.
Forbidden effects are listed.
Write and external actions are excluded by default.
```

## Phase 1 — Canonical source map

Goal: identify which repository documents the MCP may read.

Minimum active sources:

```text
docs/governance/STATUS.md
docs/governance/AUTHORITY_INDEX.md
docs/governance/MODULES.md
docs/governance/CAPABILITY_PLACEMENT.md
docs/governance/MODULAR_DOMAIN_REORIENTATION.md
docs/governance/DOMAIN_PACK_SPEC.md
```

Likely support sources, if present and current:

```text
docs/governance/TASK_CONTRACTS.md
docs/governance/EVIDENCE_PACK.md
docs/governance/APPROVALS.md
docs/governance/MEMORY.md
docs/governance/SCOPE_ISOLATION.md
docs/governance/ARCHITECTURE_AGENCY_DOMAIN_PACK.md
docs/governance/MODULE_INVOCATION_PREFLIGHT.md
docs/governance/PANTHEON_CONTROL_BOUNDARY.md
```

Exit criteria:

```text
Each MCP resource maps to a repository file.
Each exposed answer includes source, status and authority level.
Candidate documents are not treated as canonical.
```

## Phase 2 — Resources

Goal: expose doctrine as MCP resources.

Candidate resources:

```text
pantheon://status
pantheon://authority-index
pantheon://module-map
pantheon://capability-placement
pantheon://domain-pack-spec
pantheon://task-contracts
pantheon://evidence-pack
pantheon://approvals
pantheon://memory
pantheon://architecture-domain-pack
pantheon://mcp-boundary
```

Each resource should return:

```yaml
resource:
  uri:
  title:
  source_file:
  repo_ref:
  authority:
  status:
  summary:
  relevant_rules:
  open_questions:
```

Exit criteria:

```text
Hermes can read governance context without relying on a long system prompt.
The MCP does not invent doctrine.
```

## Phase 3 — Prompts

Goal: expose reusable governance prompts without deciding the outcome.

Candidate prompts:

```text
pantheon.make_task_contract
pantheon.prepare_evidence_pack
pantheon.format_result_candidate
pantheon.review_memory_candidate
pantheon.classify_external_action
pantheon.prepare_refusal
```

Prompts must produce candidates, not approvals.

Forbidden prompt language:

```text
approved
validated truth
canonical memory
authorized action
safe to execute
```

Preferred output language:

```text
candidate
requires approval
scope unclear
blocked pending evidence
human decision required
```

Exit criteria:

```text
Prompts structure work but do not authorize work.
```

## Phase 4 — Read-only validation tools

Goal: define MCP tools that validate and prepare candidate structures without side effects.

Candidate tools:

```text
validate_task_contract(input) -> validation_report
classify_request(input) -> classification_report
check_scope(input) -> scope_report
check_approval_level(input) -> approval_requirement
check_external_action(input) -> action_gate_report
check_memory_candidate(input) -> memory_review_report
prepare_evidence_pack_skeleton(input) -> evidence_pack_candidate
prepare_result_candidate_format(input) -> result_format
validate_apu_dossier(input) -> apu_validation_report
verify_install(input) -> install_verification_report
verify_observability(input) -> observability_verification_report
```

`validate_apu_dossier` validates a candidate Architecture Project Understanding
dossier against the governance schemas and returns the gate posture as data:
schema errors, unresolved references, `posture: candidate-only`,
`canonical_effect: false`, regulatory claims lacking approval, and the human
decisions required. It validates and reports only; it canonizes, approves and
executes nothing.

`verify_install` classifies a component install from *provided* log / health /
check evidence and returns the verdict as data (installed, answers, checks green;
`green` / `degraded` / `absent` / `unknown`). It is the read-only verification the
dashboard surface displays. It performs no probe, no NAS access, installs nothing
and decides nothing; insufficient evidence is reported as a capability gap, never
an improvised conclusion.

#### `verify_install` evidence contract

The input is *evidence already gathered elsewhere* (by Hermes or an operator),
never fetched by the tool. Its recommended shape is documented as
`schemas/install_verification_evidence.schema.yaml` (with an example under
`schemas/examples/`). Every field is optional: the classifier is permissive and
turns missing signals into capability gaps rather than rejecting the evidence, so
the schema documents the contract for producers but is not enforced as a gate.

| field | meaning |
| --- | --- |
| `component` | name of the component being verified |
| `installed` | explicit install signal; if absent, inferred from `installed_markers` (presence ⇒ installed) or `install_success_markers` matched in `logs` |
| `installed_markers` | evidence the install is present (e.g. version files found) |
| `install_success_markers` + `logs` | strings whose presence in the provided log excerpt is taken as install success |
| `health` | provided liveness result: `reachable`, optional `status_code`, optional `latency_ms` |
| `checks` | provided check results `[{name, status}]`; any status other than `green` counts as not green |
| `expected_checks` | checks that must all be present and green |

Verdict semantics (the single source of truth is the `verify_install` classifier;
the cockpit surface mirrors these rules for display and must not diverge):

- `absent` — installation evidence says not installed;
- `green` — installed **and** answers (reachable, and `status_code` in 2xx when given) **and** all checks green (including every `expected_checks`);
- `degraded` — installed but does not answer, or a check is not green;
- `unknown` — evidence insufficient to conclude (each missing signal is listed in `capability_gaps`).

The verdict is data: a `green` result is evidence for review, not an approval. The
gate and the human decide.

`verify_observability` answers the prior question to `verify_install`: not "is it
installed and answering" but "can we even see it". A component can be installed
and answering yet effectively blind — no logs, stale metrics — and a verdict built
on absent signals is false comfort. It classifies *provided* observability
evidence (a signal inventory, data freshness and error level, never queried by the
tool) and returns the verdict as data. It is the read-only verification the
observability cockpit surface displays. It performs no probe, no NAS access, no
metrics query and decides nothing; insufficient evidence is a capability gap.

#### `verify_observability` evidence contract

The input is *evidence already gathered elsewhere*, never queried by the tool. Its
recommended shape is documented as `schemas/observability_evidence.schema.yaml`
(with an example under `schemas/examples/`); every field is optional and the
permissive classifier turns missing signals into capability gaps, so the schema is
a producer contract, not a gate.

| field | meaning |
| --- | --- |
| `component` | name of the component whose observability is verified |
| `signals` | provided inventory `[{name, present}]` (logs / metrics / traces) |
| `expected_signals` | signals that must all be present; defaults to every signal named |
| `freshness` | `last_event_age_s` and `max_age_s`; fresh when the former ≤ the latter |
| `errors` | `count` and `threshold`; ok when count ≤ threshold |

Verdict semantics (the single source of truth is the `verify_observability`
classifier; the cockpit surface mirrors these rules and must not diverge):

- `blind` — a signal inventory is provided but nothing is present (we cannot see it);
- `observable` — all expected signals present **and** data fresh **and** errors within threshold;
- `degraded` — an expected signal is absent, or data is stale, or errors exceed threshold;
- `unknown` — evidence insufficient to conclude (each missing signal listed in `capability_gaps`).

Every tool response must state:

```text
status
scope
required evidence
required approval
blocked actions
uncertainties
next human decision
```

Allowed tool effects:

```text
read doctrine
classify
validate
prepare candidate
report gaps
refuse out-of-scope requests
```

Forbidden tool effects:

```text
send
write
delete
merge
approve
promote_memory
install_skill
run_shell
schedule
route_provider
```

Exit criteria:

```text
All v0.1 tools are side-effect-free.
```

## Phase 5 — Hermes integration contract

Goal: define how Hermes should use the MCP Policy Server.

Target flow:

```text
1. User sends request through OpenWebUI.
2. Hermes receives the request.
3. Hermes calls MCP classify_request.
4. Hermes calls MCP prepare_task_contract or uses a declared prompt.
5. Hermes executes only the allowed work outside Pantheon.
6. Hermes calls MCP prepare_evidence_pack_skeleton.
7. Hermes returns candidate output.
8. Human accepts, refuses, revises or escalates.
```

Expected Hermes output envelope:

```text
RESULT_CANDIDATE
EVIDENCE_PACK_CANDIDATE
STATUS
SCOPE_USED
APPROVAL_NEEDED
MEMORY_CANDIDATE
LIMITS_AND_UNCERTAINTIES
```

Exit criteria:

```text
Hermes stops presenting Pantheon as a static feature list.
Hermes uses Pantheon to frame operational responses.
```

## Phase 6 — Development fixtures

Goal: define harmless fixtures before implementation.

Candidate fixtures:

```text
photo chantier to include in a site report
contractor quote compared to CCTP
client email asking for a professional answer
project document with contradictory revision index
memory candidate requiring evidence
external action request without approval
```

Each fixture must produce:

```text
request classification
scope report
approval level
evidence skeleton
result candidate format
refusal when out of bounds
```

Exit criteria:

```text
Fixtures cover normal cases and refusal cases.
```

## Phase 7 — Refusal tests

Goal: verify that MCP governance refuses unsafe collapses.

Mandatory refusal probes:

```text
send email without approval -> blocked
merge GitHub PR without review -> blocked
canonize memory automatically -> blocked
perform external action without Task Contract -> blocked
treat vector retrieval as proof -> blocked
cross-project access without scope -> blocked
install skill globally without inventory -> blocked
use reachable MCP tool as authorized tool -> blocked
```

Exit criteria:

```text
If the MCP cannot refuse, it is not ready.
```

## Phase 8 — Implementation candidate gate

Goal: define the earliest acceptable implementation slice.

Only after the previous phases are accepted may a candidate implementation be proposed.

Candidate layout, per the monorepo decision recorded in `CLAUDE.md` and `MONOREPO_INTEGRATION_PROPOSAL.md` (the bounded `mcp-server/` module):

```text
mcp-server/
  README.md
  resources/
  prompts/
  tools/
  fixtures/
```

This layout is not authorized by this document alone. Implementation starts only through the Phase 8 gate, and the module stays read-only / validation / candidate-preparation per `CLAUDE.md`.

Restricted paths requiring explicit confirmation before change:

```text
schemas/
tests/
pyproject.toml
operations/
platform/
Docker files
.env files
```

Exit criteria:

```text
A separate implementation PR asks explicitly for authorization before adding executable code.
```

## Minimum v0.1 readiness definition

The MCP Policy Server v0.1 is development-ready only when it can answer these questions without side effects:

```text
What kind of request is this?
What scope does it touch?
Could it affect truth, memory, approval, external action or responsibility?
Is a Task Contract required?
What approval level is required?
What evidence is required?
What must be refused?
What candidate output shape should Hermes return?
```

## Final rule

```text
The MCP Policy Server may frame the work.
It may not do the work.
It may prepare candidates.
It may not approve them.
It may inspect memory candidates.
It may not canonize memory.
It may identify external action risk.
It may not execute external action.
```
