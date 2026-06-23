# Hermes Multi-Profile Kanban Execution Patterns

Status: candidate / to verify — tool-specific execution-pattern note for Hermes profiles, Kanban and delegation.

This document classifies external Hermes Agent multi-agent patterns for Pantheon Next.

It is not canonical doctrine.

It is not a Hermes installation guide, runtime specification, dispatcher configuration, queue design, scheduler, approval mechanism, memory mechanism or implementation artifact.

It does not install Hermes Agent, configure profiles, create Kanban boards, start workers, define cron jobs, route Telegram topics, install plugins, execute swarm graphs or grant inter-agent authority.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

A recent external pattern describes Hermes Agent as a multi-profile execution surface: isolated profiles, durable Kanban board, task rows, parent links, idempotent task creation, dispatcher-driven workers, short-lived delegation and optional channel routing.

The useful part for Pantheon is not the claim that Hermes becomes an autonomous team.

The useful part is narrower:

```text
Hermes profiles can specialize external execution.
Hermes Kanban can coordinate durable runtime work.
Hermes delegation can support short-lived reasoning.
Pantheon governs what any of those outputs are allowed to mean.
```

This document records which ideas are admissible as execution patterns, which are refused as governance claims, and what must be verified before local use.

## Distillation scope

Source material reviewed:

```text
Hermes Agent multi-agent / profiles megathread dated 2026-06-21.
Official Hermes documentation should still be checked before local configuration, because CLI and gateway behavior are version-sensitive.
```

Distilled into Pantheon:

```text
profiles as execution identities;
Kanban as durable runtime coordination;
delegate_task as synchronous short-lived helper;
channel routing as exposure / transport;
community plugins as adapter candidates only;
anti-loop and anti-autonomy guardrails.
```

Not distilled into Pantheon:

```text
Reddit anecdotes;
raw CLI recipes;
Telegram bot setup instructions;
plugin installation instructions;
agent-team marketing language;
claims that runtime coordination equals governance;
claims that agents can approve, validate, remember, send, merge or decide.
```

## Classification

| Item | Decision | Reason |
|---|---|---|
| Hermes profiles | Accepted as execution identities | Profiles isolate Hermes state and can specialize work, but do not create Pantheon Role authority. |
| Profile-specific memory / sessions / skills | Accepted as runtime state | Useful for execution continuity; not Registre Probatoire memory. |
| Durable Kanban task board | Accepted as execution coordination | A durable board can carry task state and handoff material outside Pantheon. |
| Named Hermes profile assignees | Accepted as execution routing | Useful for task specialization; profile identity remains runtime identity only. |
| Parent / child task gates | Accepted as execution sequencing | Useful for research, extraction, review and synthesis dependencies. |
| Kanban comments | Accepted as runtime handoff notes | They may support an Evidence Pack Candidate when summarized, scoped and linked. |
| Idempotency key for automation | Accepted as safety pattern | Prevents duplicate scheduled, retried or webhook-triggered work. |
| Max runtime / retry limits | Accepted as execution guardrail | Limits worker storms and stuck tasks at runtime level. |
| delegate_task | Accepted for short-lived reasoning | Useful for parallel research, code review or comparison when the parent needs immediate results. |
| delegate_task for durable work | Refused | It is not the right carrier for restart-safe, auditable or human-interruptible work. |
| Telegram / Discord topic routing | Accepted as channel routing only | Channel proximity does not lower approval requirements. |
| Multiple bot tokens | Accepted as runtime isolation pattern | Useful for cleaner gateway separation; still not OS sandboxing or governance authority. |
| Constitution pattern | Accepted as adapter routing note | It can describe which profile handles which runtime work; it must not redefine Pantheon roles. |
| Shared memory / context bus plugins | Candidate only | Useful for context transfer, but high risk if they bypass scope, approval or memory rules. |
| Direct agent-to-agent chat | Candidate only / high risk | Useful only with mention-required mode, loop guards and explicit Task Contract boundaries. |
| Swarm topology | Accepted as candidate fan-out pattern | Useful only when the task genuinely decomposes into parallel tracks. |
| Hermes verifier profile | Accepted as pre-review | It can detect gaps, contradictions or insufficient evidence; it does not validate. |
| Hermes synthesizer profile | Accepted as candidate assembler | It may assemble a Result Candidate and Evidence Pack Candidate. |
| Hermes profiles as Pantheon Roles | Refused | Profile identity is not Pantheon Role authority. |
| Hermes Kanban as governance | Refused | Coordination is not authority. |
| Hermes done status as approval | Refused | Runtime completion does not create legitimacy. |
| Hermes comments as a Registre Probatoire entry | Refused | Runtime state and comments are not governed memory. |
| Automatic external action after worker success | Refused without explicit approval | Execution success is not delivery, sending, merge or filing authorization. |
| Self-organizing agent team | Refused as governance claim | A self-generated intention is not a scoped Task Contract. |

## Boundary

Hermes profiles, Kanban and delegation may be treated as external execution carriers.

Pantheon governs the status of the output, not the internal worker mechanics.

```text
Task Contract in
-> Hermes profile / Kanban task / delegate_task / skill
-> Result Candidate + Evidence Pack Candidate out
-> Pantheon status / proof / approval / memory gate
-> human decision
```

A Hermes Kanban task may finish.

That means only:

```text
runtime work completed or stopped
```

It does not mean:

```text
source validated
claim proven
approval granted
memory promoted
action authorized
document delivered
patch merged
```

## Profile placement

Hermes profiles are useful when execution behavior should remain stable across sessions.

Candidate local profile map:

| Runtime profile | Possible execution purpose | Forbidden interpretation |
|---|---|---|
| `pantheon-dispatcher` | Read bounded task requests and assign runtime work | Not a hidden orchestrator, scheduler or approval engine. |
| `doc-intake` | Inventory corpus, classify source types, surface missing material | Not source validation. |
| `evidence-review` | Compare sources, identify contradictions, prepare Evidence Pack Candidate | Not proof authority. |
| `architecture-domain` | Apply architecture-domain method to produce Result Candidates | Not professional validation. |
| `repo-maintainer` | Prepare documentation patches, diffs and ai_logs | Not merge authority. |
| `governance-review` | Detect doctrine tension, scope issues and approval gaps | Not Zeus. |

These names are implementation examples, not Pantheon doctrine.

If a local install uses other names, the same placement test applies:

```text
Does this profile only execute bounded work and return candidates?
```

If yes, it may remain runtime-side.

If no, the profile is attempting to produce truth, memory, approval or external action and must stop at a visible Pantheon gate.

## Profiles are not sandboxes

Hermes profile isolation must not be overstated.

For Pantheon purposes:

```text
profile state isolation != OS isolation
profile memory != Registre Probatoire entry
profile config != governance approval
profile tool access != capability authorization
```

If filesystem or client separation is required, that belongs to the execution environment: Docker, VM, separate machine, restricted user, mounted workspace or another external isolation mechanism.

Pantheon records the required boundary and effect class. It does not provide host sandboxing.

## Kanban task posture

A Hermes Kanban task is an execution record.

It may carry references to Pantheon objects, but it must not become those objects.

Minimum safe shape for a governed Kanban item:

```yaml
kanban_task:
  title:
  assignee_profile:
  workspace:
  pantheon_refs:
    task_contract:
    context_pack:
    evidence_expectation:
    approval_ceiling:
  requested_effect: read_only | internal_state_change | external_effect | canonical_effect
  allowed_outputs:
    - Result Candidate
    - Evidence Pack Candidate
    - Capability Gap
  forbidden_outputs:
    - approval
    - Registre Probatoire entry
    - external send
    - merge
    - doctrine mutation
  idempotency_key:
  return_expected:
    - runtime_task_status
    - produced_candidates
    - evidence_refs
    - approval_gap
    - memory_impact
```

`canonical_effect` should not be dispatched as runtime work. It must be routed to the governed validation path.

## delegate_task posture

`delegate_task` is useful when the parent execution needs immediate reasoning results and the work is short-lived.

Allowed uses:

```text
parallel source scan;
independent contradiction review;
short code review;
comparison of two approaches;
quick extraction from bounded material;
red-team critique of a draft candidate.
```

Forbidden uses:

```text
durable multi-day work;
human-interruptible work;
work requiring restart recovery;
approval;
memory promotion;
external action;
canonical doctrine change;
merge authority.
```

Critical rule:

```text
Subagents do not inherit conversation context safely.
```

A delegation request must carry explicit scope, paths, sources, exclusions, expected output status and forbidden effects.

## Channel routing posture

Telegram, Discord or another gateway may expose different profiles through topics, bots or channels.

Pantheon classification:

```text
channel routing = exposure / transport
profile selection = runtime routing
message received = not approved
message sent by runtime = external effect if it reaches a third party
```

Direct agent-to-agent chat is high-risk because loops, token waste and false coordination are predictable failure modes.

Minimum guardrails before considering such a pattern locally:

```text
mention-required mode;
bot-to-bot response limits;
hard loop stop;
explicit Task Contract reference;
no self-created tasks without admissibility review;
no external action from agent discussion;
no memory promotion from chat transcript.
```

## Community plugin posture

Community patterns such as context buses, shared memory, A2A protocols, NAS logs or third-party Kanban integrations are not refused by default.

They are adapter candidates.

They require admission review before local use:

```text
What state do they store?
Can they create or modify tasks?
Can they send messages externally?
Can they read or write memory?
Can they bypass scope isolation?
Can they trigger tools?
Can they create loops?
Can they survive restart without losing provenance?
Can their output be reduced to Result Candidate + Evidence Pack Candidate?
```

If a plugin cannot keep truth, memory, approval and external action outside runtime authority, it is refused for Pantheon use.

## Admissible patterns

### 1. Research-to-draft relay

Use when two or more research or extraction tracks can run independently before a synthesis step.

Allowed output:

```text
Research Candidate
Evidence Pack Candidate
Draft Candidate
Capability Gap
Risk Escalation
```

Required Pantheon gate:

```text
source sufficiency
contradiction review
scope fit
approval expectation
memory impact
```

Forbidden interpretation:

```text
The final writer card does not produce a deliverable by itself.
```

### 2. Scheduled nightly review

Use for routine monitoring tasks such as repository status review, open PR review, issue triage, dashboard status preparation or integration drift detection.

Required execution guardrails:

```text
idempotency key
runtime cap
explicit assignee profile
candidate-only output
no external mutation by default
```

Allowed output:

```text
Review Note
Risk Escalation
Capability Gap
Status Candidate
Next Action Candidate
```

Forbidden interpretation:

```text
A scheduled review must not update doctrine, move approval status, promote memory, merge code or send anything externally without a separate governed approval.
```

### 3. Swarm with verifier and synthesizer

Use only when the work naturally decomposes into parallel viewpoints.

Examples:

```text
source audit + contradiction review + synthesis
repository scan + doctrine compatibility review + patch candidate
multi-domain review + risk classification + decision brief
```

Required structure:

```text
bounded Task Contract
explicit worker purposes
shared scope limit
verifier output as pre-review only
synthesizer output as candidate only
Evidence Pack Candidate
User Decision Gate when consequential
```

Forbidden interpretation:

```text
A swarm is not a Governance College.
A verifier profile is not Zeus.
A synthesizer profile is not final authority.
```

### 4. Orchestrator plus specialists

Use when stable runtime specialization is useful but governance must remain outside the runtime.

Allowed structure:

```text
exposure surface receives request;
Pantheon-bound Task Contract qualifies scope and effect;
dispatcher profile creates or assigns runtime work;
specialist profile executes;
review profile prepares contradictions / gaps;
human gate decides.
```

Forbidden interpretation:

```text
The dispatcher is not Pantheon.
The specialist is not the profession.
The reviewer is not Zeus.
The team is not autonomous governance.
```

## Command posture

Pantheon must not canonize Hermes CLI syntax.

Hermes command shape can change across versions. Before using a workflow locally, verify the installed surface:

```bash
hermes --version
hermes profile --help
hermes kanban --help
hermes kanban create --help
```

Minimum checks before treating a Hermes multi-agent workflow as locally usable:

```text
profiles exist;
profile home / config / token boundaries are understood;
board exists;
gateway or dispatcher behavior is understood for the installed version;
create command accepts the intended flags;
worker assignment behavior is verified;
delegate_task behavior is verified;
idempotency behavior is verified;
runtime cap behavior is understood;
workspace behavior is understood;
channel routing behavior is understood if a gateway is used.
```

If the installed CLI differs from an external post, local `--help` wins.

If local behavior conflicts with Pantheon doctrine, Pantheon doctrine wins and the Hermes workflow must be reduced, blocked or reframed.

## Required Evidence Pack summary

For a governed Hermes multi-profile / Kanban run, the returned Evidence Pack Candidate should summarize:

```text
Task Contract id or summary;
Hermes board or task references;
profiles involved;
worker purposes;
source references used;
assumptions;
contradictions;
runtime-level actions relevant to governance;
outputs produced;
capability gaps;
risks left open;
approval gap;
memory impact;
external-effect status;
unchanged objects.
```

Raw runtime logs are not Evidence Pack by themselves.

Kanban comments are not Evidence Pack by themselves.

Gateway transcripts are not Evidence Pack by themselves.

They may support an Evidence Pack Candidate when summarized, scoped and linked.

## Relation to open work

This pattern must stay compatible with:

```text
Pantheon Control dashboard candidate doctrine;
module invocation and connectivity preflight doctrine;
governed composition / capability registry candidate doctrine;
external runtime memory adapter doctrine;
capability placement doctrine.
```

The dashboard may display Hermes profile, Kanban or runtime status.

Preflight may check that a module, profile, board, command surface or connector is available.

Governed composition may propose the task graph shape.

None of those makes Hermes profiles, Kanban, delegation, plugins or channels a Pantheon runtime or a governance authority.

## Status decisions

```text
Accepted:
Hermes profiles as execution identities.
Hermes Kanban as external execution coordination.
delegate_task as short-lived reasoning support.
Parent gates, idempotency and runtime caps as useful execution guardrails.
Verifier and synthesizer as candidate-producing execution profiles.
Channel routing as exposure / transport only.

Refused:
Hermes profiles as Pantheon Role authority.
Hermes Kanban as governance authority.
Hermes done as approval.
Hermes comments, profile memory or runtime state as Registre Probatoire entries.
Automatic external action after worker success.
Self-authorized agent teams.
Shared memory or context bus as canonical memory.

To verify:
Installed Hermes CLI syntax.
Profile isolation behavior in the local stack.
Dispatcher / gateway behavior in the local stack.
Kanban worker assignment behavior.
delegate_task behavior and limitations in the installed version.
Idempotency behavior against the local board.
Profile availability and scope.
Channel routing behavior if Telegram / Discord is used.
Community plugin behavior before any installation.

To arbitrate:
Whether nightly reviews may update dashboard status automatically, or only propose status changes.
Whether Pantheon Control may trigger Hermes Kanban tasks directly, and under which Task Contract / approval level.
Whether any shared context bus is admissible, and if so under which scope and memory rules.
Whether a local profile constitution should be maintained as an adapter file outside the governance kernel.
```

## Final rule

```text
Hermes profiles specialize execution.
Hermes Kanban coordinates durable runtime work.
delegate_task supports short-lived reasoning.
Pantheon governs status, proof, approval, memory, scope and external action.
```
