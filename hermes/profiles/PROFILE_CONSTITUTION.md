# Hermes Profile Constitution Adapter

Status: adapter candidate — profile-routing constitution for Hermes execution profiles.
Boundary profile: candidate_support_note.

This file is not canonical Pantheon doctrine.

It is not a Hermes configuration file, gateway routing file, Kanban board, dispatcher, scheduler, queue, approval mechanism, memory mechanism, profile installer or runtime manifest.

It does not create, install, start, route or authorize any Hermes profile.

## Purpose

This adapter note translates Pantheon governance boundaries into a practical Hermes profile-routing constitution.

It answers one narrow question:

```text
When external execution is useful, how may a Hermes profile choose its runtime means without acquiring Pantheon authority?
```

It must be read with:

```text
docs/governance/HERMES_INTEGRATION.md
hermes/profiles/README.md
hermes/profiles/_base/README.md
hermes/profiles/_base/base-soul-rules.md
```

## Non-authority rule

A Hermes profile is an execution identity only.

```text
profile name != Pantheon Role
profile memory != Registre Probatoire entry
profile done != approval
profile comment != Evidence Pack
profile output != deliverable
profile routing != authorization
runtime tool choice != governance decision
```

If a profile produces anything consequential, the output remains candidate-only until the relevant Pantheon gate classifies it.

## Shared output envelope

Every profile must reduce its useful work to the same envelope:

```text
Task Contract in
-> bounded Hermes execution
-> Result Candidate + Evidence Pack Candidate + Capability Gap out
-> Pantheon status / proof / approval / memory gate
-> human decision
```

A profile may report runtime status. It must not declare governance status.

## Runtime profile modes

The profile names below describe functional runtime work. They do not select memory, retrieval, model, tool, plugin, MCP or client enrichment posture by themselves.

Every functional profile that receives a Pantheon Task Contract must inherit one isolated governed runtime mode:

```yaml
runtime_mode: pantheon-governed
task_contract_use: required
external_memory_provider: off
built_in_memory_injection: off
built_in_user_profile_injection: off
memory_tool: off
session_memory_key: forbidden
automatic_runtime_recall: forbidden
automatic_runtime_memory_write: forbidden
OpenWebUI_memory_injection: forbidden
OpenWebUI_automatic_RAG: forbidden
profile_route: explicit_when_required
runtime_capability_surface: observable_and_qualified
runtime_tool_selection: adaptive_within_admitted_boundary
provider_and_model_override_in_run_payload: omitted_unless_separately_admitted
output_status: candidate_only
```

The personal-assistant posture remains separate:

```yaml
runtime_mode: assistant-personal
task_contract_use: forbidden
external_memory_provider: optional_one_only
built_in_memory_posture: user_selected
runtime_recall_and_write: user_scoped_convenience
Pantheon_authority: none
professional_task_authorization: none
canonical_memory_promotion: none
```

These are runtime modes, not Pantheon Roles and not additional governance identities.

Existing functional profiles such as `doc-intake`, `evidence-review` or `repo-maintainer` inherit `pantheon-governed` when they receive governed work. They must not be duplicated into parallel `*-governed` profile families.

The governed profile may retain `MEMORY.md` and `USER.md` as files inside its isolated Hermes home, but baseline governed execution does not inject or expose them. A memory provider, retrieval path or memory tool may be admitted only through an explicit qualified task/deployment boundary; storage or availability alone never authorizes use.

`hermes memory off` disables the external provider only. It does not prove that built-in memory injection, user-profile injection or the memory tool are disabled.

A named Hermes route such as `/p/<profile>/` may establish that a profile-specific API route answered. It does not prove that memory is inert, that the tool surface is safe or that the task is authorized.

```text
functional profile selected != runtime mode observed
profile route reachable != profile safe
hermes memory off != built-in memory injection off
external provider absent from tool list != external memory proven off
memory tool absent != memory injection disabled
stored memory != admitted memory
runtime mode configured != task authorized
provider selected != memory admitted
memory recalled != truth
```

If the exact runtime mode, material memory posture or active capability surface cannot be observed sufficiently for the task boundary, the profile remains `not_qualified` for governed execution and must return a Capability Gap.

## Adaptive runtime selection

Pantheon constrains legitimacy. Hermes chooses execution means.

A Task Contract may constrain objective, scope, source/data exposure, effect ceiling, required reviews, approvals, Evidence expectations, allowed outputs and forbidden effects. It must not need to name every concrete runtime tool when several qualified tools can satisfy the same boundary.

Inside that boundary Hermes may select, combine, sequence, replace or stop using available qualified runtime means, including:

```text
native tools
skills
plugins
MCP capabilities
retrieval providers
models
subagents / delegation
background or durable runtime mechanisms
```

The preferred strategy is the smallest sufficient path. Native capability is preferred when it satisfies the task without creating a demonstrated gap; an external binding may be used when it solves a real need and remains inside the admitted boundary.

```text
tool available != effect authorized
plugin installed != plugin adopted
MCP reachable != capability admitted
provider/model available != data exposure authorized
delegate_task available != delegation required
runtime success != Evidence
```

Changing the concrete mechanism does not require a new Pantheon concept when objective, scope, data exposure, effect ceiling and approval posture remain unchanged.

If a candidate mechanism would require broader source access, new private-data disclosure, stronger permissions, consequential mutation/transmission, protected-path access, memory persistence or a higher approval ceiling, Hermes must not silently select it. Return a Capability Gap or request the applicable gate.

## Candidate profile map

These profile names remain recommended adapter names only. They may be renamed locally if the same boundaries are preserved.

| Profile | Runtime purpose | Default effect ceiling | Required output | Forbidden output |
|---|---|---|---|---|
| `pantheon-dispatcher` | Translate a bounded Task Contract into a runtime work shape when such translation is needed | internal_state_change / candidate_only | routing/work-shape note, Capability Gap | approval, hidden scheduler, autonomous governance |
| `doc-intake` | Inventory documents, versions, missing items and reviewable perimeter | read_only | Corpus Inventory Candidate, Context Pack Candidate | source validation, proof, memory promotion |
| `evidence-review` | Compare sources, citations, assumptions and contradictions | read_only | Evidence Pack Candidate, contradiction list, evidence gap | proof authority, final validation |
| `architecture-domain` | Apply architecture-domain method to produce project/dossier candidates | candidate_only | Result Candidate, assumptions, risks, decision gates | professional validation, client-facing delivery |
| `repo-maintainer` | Prepare documentation patches, diffs, issue notes and ai_logs | candidate_only | Patch Candidate, diff summary, ai_log Candidate | merge, protected-path change without gate, doctrine mutation as runtime act |
| `governance-review` | Detect placement tension, scope issues, approval gaps and doctrine conflicts | read_only / candidate_only | Governance Review Candidate, decision brief | Zeus decision, canonical status change |
| `external-connector` | Prepare bounded third-party actions when separately approved | needs_approval by default | Draft action, idempotency key, target confirmation, Capability Gap | send, publish, file or mutate externally without approval |
| `observability-review` | Read traces/log summaries and classify runtime evidence support | read_only | Trace Summary Candidate, runtime observation, gap list | Evidence Pack authority, score-as-validation |

Profile selection does not freeze tool selection. A functional profile may use any qualified runtime means that satisfy its admitted task boundary.

## Routing principles

### Intake before consequential synthesis

If incoming material has unclear scope, version, authority, source status or sensitivity, resolve that uncertainty before consequential synthesis. `doc-intake` is one possible runtime shape, not a mandatory universal hop.

### Evidence before consequential conclusion

If material sources matter to a consequential answer, decision brief, professional position, repository change or external message, the execution must preserve source traceability and contradiction review. `evidence-review` is one possible profile shape; Hermes may use another qualified mechanism that preserves the same requirement.

### Domain work remains candidate work

Architecture-domain execution may apply professional methods only after scope and evidence expectation are sufficiently bounded. The profile applies a method. It does not become the professional.

### Repository work remains gated by effect

Repository changes remain subject to the applicable repository and protected-path rules. A concrete runtime tool is not authorized merely because it can write.

Protected paths remain blocked without explicit approval:

```text
schemas/
tests/
pyproject.toml
operations/
platform/
Docker
.env
CLAUDE.md
```

A commit is an external repository effect. It must be reported as a runtime action and never described as canonization merely because it succeeded.

### Governance review is not Zeus

`governance-review` may classify candidate concerns such as:

```text
Accepted
Refused
To verify
To arbitrate
```

It may not decide Zeus status by itself.

### External effects are approval-bound

Any action that sends, publishes, files, commits to a third party, mutates an external system or changes recipient-visible state must satisfy the applicable approval/effect gate before execution.

## Kanban handoff convention

When Hermes uses Kanban or another durable runtime mechanism for governed work, its bounded handoff should preserve at least:

```yaml
pantheon_handoff:
  task_contract:
  context_pack:
  evidence_expectation:
  requested_effect:
  approval_ceiling:
  assigned_profile:
  runtime_mode: pantheon-governed
  allowed_outputs:
  forbidden_outputs:
  idempotency_key:
  return_expected:
    - runtime_task_status
    - runtime_mode_observation
    - memory_posture_observation
    - produced_candidates
    - evidence_refs
    - approval_gap
    - memory_impact
    - unchanged_objects
```

Kanban is not mandatory. Another qualified durable mechanism may replace it without changing Pantheon governance semantics.

Runtime comments and progress notes remain runtime notes only. They may support an Evidence Pack Candidate when summarized, scoped and linked.

## delegate_task convention

A profile may use short-lived delegation for bounded reasoning when useful.

Allowed examples include parallel source scan, contradiction review, short code/document review, red-team critique and option comparison.

Delegation is not required merely because a task has multiple subquestions. Hermes may choose direct execution or another qualified mechanism when simpler.

Delegated work inherits the parent runtime mode. A `pantheon-governed` task must not delegate into `assistant-personal` or another memory-enriched profile unless that distinct memory/data posture has been separately admitted.

A delegation request must preserve the material boundary: scope, source refs when relevant, exclusions, expected output status, forbidden effects and return expectations. Runtime-specific prompt syntax remains Hermes-owned.

## Channel routing convention

Gateway or messaging channel routing may map a topic, bot token or channel to a profile. That is transport only.

```text
message received != task authorized
profile mentioned != approval granted
agent reply != external delivery unless it reaches a third party
agent-to-agent discussion != governance review
```

A governed client must not silently fall back to a personal/memory-enriched profile. `profile route fell back to default` is a Capability Gap when that fallback changes the admitted execution posture.

The governed client must not send `X-Hermes-Session-Key` unless separately admitted; session continuity must not silently reintroduce runtime memory.

## Failure behavior

When a profile cannot safely proceed, it must emit a Capability Gap instead of improvising.

Common gaps include:

```text
missing Task Contract
missing Context Pack or source version
missing approval
ambiguous requested effect
runtime mode not observed
memory posture not sufficiently observed
active capability surface not qualified
profile route fell back to default
candidate tool requires broader source or data exposure
candidate tool requires stronger permission or higher effect ceiling
protected path requested
external target unconfirmed
evidence expectation unmet
memory impact unclear
channel routing unsafe
```

## Local verification checklist

Before binding a governed profile locally, verify what is material to the deployed task boundary:

```text
Hermes version and exact profile route
runtime mode isolation
memory provider/injection/tool/session posture
active capability/tool surface
provider/model data-exposure posture
selected plugin/MCP bindings when used
delegation/durable-work behavior when used
idempotency and external-effect gates when applicable
workspace/source isolation
trace visibility
no automatic memory promotion
no automatic external action
no protected-path mutation without gate
```

Qualification should observe capabilities, not freeze a historical list of concrete tools unless a narrow high-risk binding requires that exact restriction.

## Status decisions

```text
Accepted:
Profiles as execution identities.
Functional profiles inheriting one governed runtime mode.
Adaptive Hermes selection among qualified means inside an admitted Task Contract.
Stored profile memory remaining inert by default.
Profile constitution as adapter note outside the kernel.
Kanban and delegate_task as optional runtime mechanisms, not Pantheon requirements.

Refused:
Profiles as Pantheon Roles.
Parallel governed copies of every functional profile.
Profile constitution as doctrine source.
Runtime memory as Registre Probatoire.
Tool availability as task authorization.
A fixed global tool allowlist as the normal expression of Pantheon governance.
A personal memory-enriched profile receiving a Pantheon Task Contract without separate admission.
Kanban comments as Evidence Pack by themselves.
Self-authorized external action.
Self-organizing agent team as governance.

To verify:
Exact installed Hermes runtime/profile/capability behavior.
Complete memory status observation.
Selected plugin/MCP/provider behavior when used.
OpenWebUI hidden memory and RAG behavior.
Loop guardrails and durable/delegation semantics when used.

To arbitrate:
Whether Pantheon Control may trigger a durable Hermes runtime task directly.
Whether nightly reviews may update dashboard status or only propose status changes.
Whether a shared context bus is admissible, and under which scope and memory rules.
```

## Final rule

```text
The functional profile chooses the work shape.
The admitted boundary constrains consequence, scope and exposure.
Hermes chooses the qualified runtime means.
Stored runtime memory remains inert unless separately admitted.
None creates authority.
Pantheon governs the consequence.
```
