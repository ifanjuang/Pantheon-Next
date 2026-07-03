# Hermes Agent v0.18.0 — Release Boundary Review

Status: external reference / support review — candidate only.

Date: 2026-07-03

External source reviewed:

```text
https://github.com/NousResearch/hermes-agent/releases/tag/v2026.7.1
```

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## What it is

Hermes Agent v0.18.0 is an external execution-runtime release. Its release note frames the version as a reliability and judgment release: zero open P0/P1 at release cut, Mixture-of-Agents as a first-class selectable model, `/goal` completion contracts, verification evidence for coding work, `/learn`, `/journey`, background delegate fan-out, desktop coding projects, gateway lifecycle hardening, auxiliary-model self-review and provider/security improvements.

For Pantheon Next, this is a version-change review event. It does not rewrite the Pantheon kernel by itself.

This review records the release as an external reference. It does not install Hermes, update a Hermes profile, create a skill, create an adapter, create a gateway, create an MCP host, create a scheduler, create an approval engine, promote memory, implement MoA, verify the upstream implementation independently or authorize external execution.

## Source caution

The reviewed material is the upstream release note. The release note is useful for capability classification, but it is not Pantheon proof that every claimed upstream behavior works in a local deployment.

Pantheon should treat the release as:

```text
external reference;
adapter review trigger;
not doctrine;
not implementation evidence for Pantheon;
not approval to use new runtime surfaces in governed workflows.
```

## Initial qualification

Accepted:

```text
Hermes v0.18.0 as an external runtime release worth adapter review;
completion contracts as a useful runtime-side verification pattern;
verification evidence as input to an Evidence Pack Candidate, not approval;
MoA selectable models as candidate-producing model orchestration;
background fan-out as runtime execution under Task Contract;
/learn as possible Skill Candidate generation, not skill approval;
/journey as runtime memory transparency, not Registre Probatoire authority;
gateway drain / scale-to-zero as runtime lifecycle hardening outside Pantheon.
```

Refused:

```text
Hermes v0.18.0 as Pantheon doctrine;
MoA as Pantheon Governance College or Zeus arbitration;
reference-model reasoning blocks as proof, final truth or professional validation;
Hermes verification evidence as self-approving Evidence Pack;
/goal completion as Pantheon approval;
/learn as automatic skill admission;
/journey as canonical memory or Registre Probatoire entry;
background fan-out as permission for scope expansion, unapproved external action or hidden scheduling;
release maturity signals as authorization to bypass capability passports, gates or Task Contracts.
```

To verify:

```text
whether the local Hermes runtime actually exposes the v0.18 surfaces listed upstream;
whether `/goal` verification evidence can be shaped into Pantheon-readable Evidence Pack Candidates;
whether `/learn` outputs can be routed through SKILL_LIFECYCLE.md without becoming automatic skill approval;
whether `/journey` memory items can be displayed as runtime memory candidates without polluting the Registre Probatoire vocabulary;
whether MoA disagreement can be represented in the cockpit as divergence / convergence cards;
whether background delegate fan-out returns enough trace references for governed outcome observation.
```

To arbitrate:

```text
whether HERMES_INTEGRATION.md should later add a formal Hermes 0.18 runtime-surface table;
whether CARD_STACK_MODEL.md should receive new candidate cards for Goal Contract, Verification Evidence, Learned Skill Candidate, Runtime Memory Candidate, MoA Divergence and Delegate Fan-out;
whether a future Hermes adapter document should define a stable v0.18 capability passport set;
whether local deployment review is required before marking any v0.18 surface as usable in Pantheon-governed work.
```

## Placement review

| Hermes v0.18 surface | Primary placement | Pantheon classification |
|---|---|---|
| P0/P1 clean sweep | external project maturity signal | useful confidence signal only; not governance evidence or local implementation proof |
| MoA selectable under `moa` provider | execution runtime / model orchestration | Result Candidate source; not Governance College, Zeus or truth authority |
| labelled reference-model outputs | runtime / exposure visibility | divergence evidence candidate; not proof by itself |
| streaming aggregator answer | exposure/runtime UX | usability improvement; no status change |
| `/goal` completion contracts | execution runtime | Task Contract analogue; still candidate-only until Pantheon review |
| coding verification evidence ledger | execution runtime / observability input | Evidence Pack Candidate input; not self-approval |
| `pre_verify` hook | execution runtime | adapter configuration; may support evidence expectations |
| `/learn` skill distillation | execution runtime skill authoring | Skill Candidate only; requires admission, passport and review |
| `/journey` memory timeline | runtime memory transparency | Runtime Memory Candidate / review surface; not Registre Probatoire |
| desktop memory graph | exposure/runtime UX | memory inspection aid; not canonical memory |
| background `delegate_task` fan-out | execution runtime | allowed only under Task Contract; returns consolidated Result Candidate + evidence / trace refs |
| desktop coding projects | runtime cockpit | useful external execution surface; not Pantheon cockpit authority |
| gateway scale-to-zero / drain coordination | runtime operations | lifecycle hardening; no governance status change |
| auxiliary-model self-review | runtime cost / self-improvement mechanic | may propose memory or skill candidates; cannot approve them |
| `/prompt` editor flow | runtime UX | input convenience; no status change |
| Vertex AI provider support | provider adapter | model/provider capability; requires model/capability passport before governed consequential use |
| security hardening | runtime security | useful risk reduction; does not replace governance gates |

## Pantheon translation

The safe translation is:

```text
Hermes v0.18 may produce stronger candidates and better runtime evidence.
Pantheon still governs the admissibility, status, approval, memory and external-effect boundary.
The improved runtime evidence becomes material for review; it does not decide the review.
```

The release reinforces the current split:

```text
The exposure surface exposes.
The execution runtime executes, verifies, learns and fans out under contract.
Pantheon governs truth status, memory status, evidence status, approval, scope and external action.
The human decides. The validated remains.
```

## Candidate adapter implications

### Completion contract mapping

Hermes `/goal` completion contracts are useful when they can be projected into Pantheon terms:

```yaml
goal_completion_candidate:
  origin_runtime: hermes
  hermes_version: v0.18.0
  linked_task_contract:
  declared_done_condition:
  checks_run:
  check_results:
  failed_or_skipped_checks:
  produced_result_candidate:
  produced_evidence_pack_candidate:
  runtime_task_status: success | partial | failed | blocked | unknown
  governance_result_status: candidate | to_verify | approved | rejected | blocked
  trace_refs:
```

The key invariant remains:

```text
runtime done != Pantheon approved
```

### MoA mapping

MoA may improve deliberation quality, but it is not a governance college.

Safe cockpit projection:

```text
reference_model_output -> Viewpoint Candidate
aggregator_output -> Synthesis Candidate
model disagreement -> Divergence Candidate
model convergence -> Convergence Note
Pantheon review -> status assignment
Zeus / human -> arbitration where required
```

Forbidden collapse:

```text
MoA majority = truth
MoA aggregator = Zeus
reference reasoning = Evidence Pack
visible disagreement = automatic escalation result
```

### `/learn` mapping

`/learn` may accelerate Hermes skill creation. It must be routed through the skill lifecycle before governed use.

Safe path:

```text
observed workflow / directory / URL
-> Hermes learned skill draft
-> Skill Candidate
-> source and boundary review
-> capability passport / activation status
-> Task Contract use only if admitted
```

Forbidden collapse:

```text
skill generated = skill approved
skill useful once = reusable competence
skill stored in Hermes = Pantheon Competence
```

### `/journey` mapping

`/journey` makes runtime memory visible and editable. Pantheon should use that visibility to reduce black-box drift, not to grant runtime memory canonical status.

Safe path:

```text
Hermes memory item
-> Runtime Memory Candidate
-> scoped review
-> reject / keep runtime-local / propose Register Candidate
-> Registre Probatoire only after governed validation
```

## Card-stack candidates

If folded into `CARD_STACK_MODEL.md`, the release suggests these candidate cards:

```text
Goal Contract Card
Verification Evidence Card
MoA Divergence Card
MoA Synthesis Card
Learned Skill Candidate Card
Runtime Memory Candidate Card
Delegate Fan-out Card
Gateway Health Card
Capability Passport Gap Card
```

These cards would be display / review grammar only. They would not create UI, renderer, runtime, Hermes skill, provider router, approval engine or memory engine.

## Decision summary

```text
Accepted: Hermes v0.18.0 as an adapter-review reference and runtime capability signal.
Refused: any automatic promotion of Hermes runtime features into Pantheon doctrine, proof, approval, canonical memory or external-action authority.
To verify: local availability, evidence shape, trace shape, skill admission path and memory display path.
To arbitrate: whether to add a formal v0.18 table to HERMES_INTEGRATION.md and whether to project the new surfaces into CARD_STACK_MODEL.md.
```
