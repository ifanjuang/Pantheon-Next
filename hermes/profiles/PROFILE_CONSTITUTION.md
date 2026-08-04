# Hermes Profile Constitution Adapter

Status: adapter candidate — profile-routing constitution for Hermes execution profiles.

This file is not canonical Pantheon doctrine.

It is not a Hermes configuration file, gateway routing file, Kanban board, dispatcher, scheduler, queue, approval mechanism, memory mechanism, profile installer or runtime manifest.

It does not create, install, start, route or authorize any Hermes profile.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

This adapter note translates Pantheon governance boundaries into a practical Hermes profile-routing constitution.

It answers one narrow question:

```text
When external execution is useful, which kind of Hermes profile should carry the runtime work?
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

A profile may report runtime status.

It must not declare governance status.

## Runtime profile modes

The profile names below describe functional runtime work. They do not select the memory, retrieval or OpenWebUI enrichment posture by themselves.

Every functional profile that receives a Pantheon Task Contract must inherit one isolated governed runtime mode:

```yaml
runtime_mode: pantheon-governed
task_contract_use: required
external_memory_provider: off
automatic_runtime_recall: forbidden
automatic_runtime_memory_write: forbidden
OpenWebUI_memory_injection: forbidden
OpenWebUI_automatic_RAG: forbidden
profile_route: explicit
tool_allowlist: explicit
provider_and_model_override_in_run_payload: omitted
output_status: candidate_only
```

The personal-assistant posture remains separate:

```yaml
runtime_mode: assistant-personal
task_contract_use: forbidden
external_memory_provider: optional_one_only
runtime_recall_and_write: user_scoped_convenience
Pantheon_authority: none
professional_task_authorization: none
canonical_memory_promotion: none
```

These are runtime modes, not Pantheon Roles and not additional governance identities.

Existing functional profiles such as `doc-intake`, `evidence-review` or `repo-maintainer` inherit `pantheon-governed` when they receive governed work. They must not be duplicated into parallel `*-governed` profile families.

A named Hermes route such as `/p/<profile>/` may establish that a profile-specific API route answered. It does not prove that external memory is off, that the tool surface is safe or that the task is authorized.

Absence of provider-specific tools is not sufficient proof that automatic provider context injection, recall or writes are disabled.

```text
functional profile selected != runtime mode observed
profile route reachable != profile safe
external provider absent from tool list != external memory proven off
runtime mode configured != task authorized
provider selected != memory admitted
memory recalled != truth
```

If the exact runtime mode, external-memory posture or active tool surface cannot be observed, the profile remains `not_qualified` for governed execution and must return a Capability Gap.

## Candidate profile map

These profile names are recommended adapter names only. They may be renamed locally if the same boundaries are preserved.

| Profile | Runtime purpose | Default effect ceiling | Required output | Forbidden output |
|---|---|---|---|---|
| `pantheon-dispatcher` | Convert a bounded Task Contract into assigned runtime work | internal_state_change / candidate_only | Kanban Task Candidate, routing note, Capability Gap | approval, autonomous task creation, hidden scheduler |
| `doc-intake` | Inventory documents, sources, versions, missing items and reviewable perimeter | read_only | Corpus Inventory Candidate, Context Pack Candidate | source validation, proof, memory promotion |
| `evidence-review` | Compare sources, citations, assumptions and contradictions | read_only | Evidence Pack Candidate, contradiction list, evidence gap | proof authority, final validation |
| `architecture-domain` | Apply the architecture domain method to produce project/dossier candidates | candidate_only | Result Candidate, assumptions, risks, decision gates | professional validation, client-facing delivery |
| `repo-maintainer` | Prepare documentation patches, diffs, issue notes and ai_logs | candidate_only | Patch Candidate, diff summary, ai_log Candidate | merge, protected-path change, doctrine mutation as runtime act |
| `governance-review` | Detect placement tension, scope issues, approval gaps and doctrine conflicts | read_only / candidate_only | Governance Review Candidate, decision brief | Zeus decision, canonical status change |
| `external-connector` | Prepare bounded third-party connector actions when separately approved | needs_approval by default | Draft action, idempotency key, target confirmation, Capability Gap | send, publish, file or mutate externally without approval |
| `observability-review` | Read traces/log summaries and classify runtime evidence support | read_only | Trace Summary Candidate, runtime observation, gap list | Evidence Pack authority, score-as-validation |

## Routing rules

### 1. Intake before execution

If the incoming material has unclear scope, version, authority, source status or sensitivity, route first to `doc-intake`.

Do not route directly to `architecture-domain`, `repo-maintainer` or `external-connector` when the perimeter is unclear.

### 2. Evidence before conclusion

If the task asks for a consequential answer, decision brief, professional position, repo change or external message, route to `evidence-review` before synthesis when sources are material.

Retrieval alone is not evidence.

### 3. Domain method before drafting

If the task belongs to architecture practice, route to `architecture-domain` only after the task has an admitted scope and known evidence expectation.

The profile applies a method. It does not become the professional.

### 4. Repo change through candidate path

If the task modifies allowed repository documentation paths, `repo-maintainer` may prepare and apply documentation-only changes when those paths are already authorized by standing instruction.

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

A commit is an external repository effect. It must be reported as a runtime action and never described as canonization unless the changed document already has that status and the content preserves its authority.

### 5. Governance review is not Zeus

`governance-review` may classify:

```text
Accepted
Refused
To verify
To arbitrate
```

It may not decide Zeus status by itself.

Where ambiguity touches doctrine, approval, Registre Probatoire, external action or protected paths, the profile must stop with a `To arbitrate` candidate.

### 6. External connector path is approval-first

Any action that sends, publishes, files, commits to a third party, mutates an external system or changes recipient-visible state must route through an approval gate before execution.

The connector profile may prepare:

```text
draft;
target confirmation;
idempotency key;
expected effect;
rollback / unchanged objects note;
Capability Gap.
```

It may not execute the external effect without approval.

## Kanban handoff convention

When a Hermes Kanban task is created from this constitution, its description should include:

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

A Kanban task may include comments and progress notes.

Those comments are runtime notes only. They may support an Evidence Pack Candidate when summarized, scoped and linked.

## delegate_task convention

A profile may use short-lived delegation for bounded reasoning.

Allowed:

```text
parallel source scan;
short contradiction review;
short code or document review;
red-team critique;
comparison of options.
```

Forbidden:

```text
durable work;
human-interruptible workflow;
approval;
memory promotion;
external action;
canonization;
protected-path mutation;
merge authority.
```

Every delegation prompt must include:

```text
scope;
source paths or source refs;
exclusions;
expected output status;
forbidden effects;
return format;
```

Delegated work inherits the parent runtime mode. A `pantheon-governed` task must not delegate into `assistant-personal` or another memory-enriched profile.

## Channel routing convention

Gateway or messaging channel routing may map a topic, bot token or channel to a profile.

That is transport only.

```text
message received != task authorized
profile mentioned != approval granted
agent reply != external delivery unless it reaches a third party
agent-to-agent discussion != governance review
```

Direct agent-to-agent channels require loop guards and mention-required behavior before local use.

A channel or OpenWebUI model route intended for governed work must target the explicit governed profile route. Falling back silently to a default or personal profile is refused.

## Failure behavior

When a profile cannot safely proceed, it must emit a Capability Gap instead of improvising.

Common gaps:

```text
missing Task Contract;
missing Context Pack;
missing source version;
missing approval;
ambiguous requested effect;
profile lacks permission;
runtime mode not observed;
external memory posture not observed;
active tool surface not qualified;
profile route fell back to default;
protected path requested;
external target unconfirmed;
evidence expectation unmet;
memory impact unclear;
channel routing unsafe;
loop risk detected.
```

## Local verification checklist

Before installing or binding any profile locally, verify:

```text
Hermes version;
profile command surface;
profile home isolation behavior;
profile token boundaries;
explicit named profile route;
no fallback to default or personal profile;
external memory provider state;
automatic recall and write state;
OpenWebUI memory and RAG enrichment state;
active tool allowlist;
Kanban command surface;
Kanban worker assignment behavior;
Gateway / dispatcher behavior;
delegate_task behavior and limits;
idempotency behavior;
workspace behavior;
loop guardrails;
log / trace visibility;
no automatic memory promotion;
no automatic external action;
no protected-path mutation.
```

## Status decisions

```text
Accepted:
Profiles as execution identities.
Functional profiles inheriting one governed runtime mode.
Profile constitution as adapter note outside the kernel.
Kanban handoff convention as runtime coordination aid.
delegate_task convention as short-lived helper discipline.

Refused:
Profiles as Pantheon Roles.
Parallel governed copies of every functional profile.
Profile constitution as doctrine source.
Runtime memory as Registre Probatoire.
A personal memory-enriched profile receiving a Pantheon Task Contract.
Kanban comments as Evidence Pack by themselves.
Self-authorized external action.
Self-organizing agent team as governance.

To verify:
Installed Hermes profile and Kanban behavior.
Named profile route behavior under API multiplexing.
Actual profile home and token isolation.
External memory provider state observation.
OpenWebUI hidden memory and RAG behavior.
Loop guardrails.
Community plugin behavior.

To arbitrate:
Whether Pantheon Control may trigger Hermes Kanban tasks directly.
Whether nightly reviews may update dashboard status or only propose status changes.
Whether a shared context bus is admissible, and under which scope and memory rules.
```

## Final rule

```text
The functional profile chooses the work shape.
The runtime mode constrains the execution context.
Neither creates authority.
Pantheon governs the consequence.
```