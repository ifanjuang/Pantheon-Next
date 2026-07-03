# CogniCore Runtime Review

Status: external reference — candidate / to verify.

Review date: 2026-07-03.

Subject: `https://github.com/cognicore-dev/cognicore-my-openenv`

Reviewed source signals:

- `README.md` — runtime cognition layer, memory, reflection, adaptive execution, RL environments, CLI and optional extras.
- `pyproject.toml` — package metadata, alpha classifier, optional integration extras.
- `cognicore/runtime.py` — callable wrapper, memory context, reflection hints, retries, runtime stats and persistence.
- `cognicore/middleware/memory.py` — episodic runtime memory grouped by key, success/failure retrieval and JSON persistence.
- `cognicore/middleware/reflection.py` — failure-pattern analysis, natural-language hints and optional action override suggestion.
- `cognicore/integrations/langchain.py` — example integration exposing repair context and memory storage as LangChain tools.

This review is an external reference. It does not adopt CogniCore, install a dependency, create a Hermes skill, create an OpenWebUI tool, create a runtime, create a memory backend, create an approval path or promote any Pantheon doctrine by itself.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Boundary conclusion

CogniCore may inspire runtime-side adaptive execution and runtime memory signals.

It must not be treated as Pantheon memory, evidence, approval, truth, scope authority or Zeus arbitration.

Any future integration belongs to Hermes adapter territory and must preserve the shared envelope:

```text
Task Contract in
-> Hermes-side CogniCore-wrapped skill or runtime experiment
-> Result Candidate + Evidence Pack Candidate out
```

The output remains candidate material until Pantheon gates classify it and the human decision path validates it where required.

## What CogniCore is

CogniCore is positioned as a runtime cognition layer for agents.

Its central pattern is not governance. Its central pattern is adaptive execution:

```text
agent function
+ runtime context
+ episodic memory
+ reflection hint
+ evaluator / retry loop
+ execution stats
```

The runtime stores past execution outcomes, retrieves similar successes and failures, generates reflection hints, and may suggest a different action when a proposed action matches repeated failures.

That is useful runtime intelligence. It is not proof, approval or professional validation.

## What differs from Pantheon Next

| Axis | Pantheon Next | CogniCore |
|---|---|---|
| Primary function | Governs consequential decisions: truth status, scope, evidence, approval, memory, external action. | Improves runtime behaviour through memory, reflection, retries and adaptive execution. |
| Layer | Governance kernel plus adapters. | Execution/runtime layer. |
| Runtime posture | Pantheon is not a runtime and must not become one. | Runtime wrapping is the core product. |
| Memory | Canonical memory requires scoped validation; runtime recall is not Pantheon memory. | Episodic runtime memory stores successes/failures and can persist to JSON. |
| Evidence | Evidence Pack / Evidence Pack Candidate must qualify claims, provenance, limits and contradictions. | Memory and reflection provide hints, stats and patterns; they are not evidence by default. |
| Approval | Approval levels and gates classify consequential effects before validation or external action. | No Pantheon-equivalent approval model. |
| Roles / gods | Roles guard jurisdictions and expose tensions; Zeus states procedure and status. | No governance college; reflection is an analytical mechanism, not a role. |
| Human decision | Human decision remains final for validation, external action and professional responsibility. | Runtime success can be computed by an evaluator or absence of crash. |
| External action | Requires effect classification, scope and approval path. | A wrapped callable may do whatever the integrated agent function does unless guarded externally. |
| Status language | Candidate, to verify, approved, rejected, canonical, blocked. | Success, failure, hint, recommendation, override, stats. |

The main difference is therefore structural:

```text
Pantheon decides what status an output may carry.
CogniCore helps a runtime produce a better output candidate.
```

## What can inspire Pantheon Next

### 1. Runtime failure memory for Hermes

CogniCore's success/failure memory can inspire a Hermes-side pattern for remembering operational mistakes without converting them into Pantheon memory.

Candidate use cases:

- failed extraction tactics;
- brittle prompt formats;
- bad parser choices;
- OCR or PDF handling failures;
- recurring connector errors;
- invalid schema-shape attempts;
- poor code-repair tactics;
- weak evidence-pack assembly patterns.

Pantheon rule:

```text
Runtime memory may suggest.
Runtime memory must not canonize.
```

### 2. Reflection Candidate cards

CogniCore's reflection hints can inspire cockpit cards such as:

- `Runtime Pattern Candidate`;
- `Failed Tactic Candidate`;
- `Successful Tactic Candidate`;
- `Reflection Hint Candidate`;
- `Evaluator Warning Candidate`.

These cards would be displayed as operational signals, not as proof.

They fit the card-stack model only if they remain subordinate to Evidence, Action and Gate cards.

### 3. Cleaner return-path separation

CogniCore records runtime success, failure, duration, memory context and hint.

Pantheon can use this as a reminder that return objects should separate:

```text
transport / handoff status
runtime task status
candidate result status
evidence candidate status
governance result status
```

This reinforces the existing rule:

```text
Runtime completion is not governance approval.
Task success is not truth.
Retrieval is not evidence.
```

### 4. Capability Passport fields for adaptive runtimes

CogniCore suggests that adaptive runtimes need explicit passport fields before admission.

Potential future review fields:

```text
runtime_memory: none | volatile | persistent | externalized
memory_scope: task | session | dossier | organization
memory_payload_policy: minimized | redacted | raw_forbidden
reflection_output: hidden | visible_candidate | blocked
reflection_override: forbidden | candidate_only | allowed_for_low_risk
human_review_required: true | false
```

These are not schema changes here. They are possible future distillation candidates.

### 5. Benchmark and harness discipline

CogniCore includes environment and benchmark vocabulary. That can inspire test fixtures for Hermes-side capabilities:

- repeat a task family;
- record failure modes;
- compare strategies;
- test whether a refusal fixture stays refused;
- test whether a candidate output carries its required evidence state.

Pantheon must not import the benchmark as doctrine. At most, it can inspire validation-only examples or Hermes-side experiments.

### 6. UX language for runtime learning

A useful cockpit distinction:

```text
Pattern observed by runtime
not
validated lesson
```

That wording prevents false authority. A pattern may help a professional or assistant revise an approach, but it does not become agency doctrine or a Registre Probatoire entry until reviewed.

## How to distill this into Pantheon Next if needed

Distillation should be staged. The goal is not to import CogniCore. The goal is to extract durable governance distinctions that remain true if CogniCore is replaced.

### Level 0 — keep as external reference

Default posture.

Use the review only as a comparative note when discussing runtime memory, reflection hints, adaptive execution or Hermes-side learning.

No repo change is required beyond this review.

Status:

```text
external reference
candidate / to verify
documented non-implemented
```

### Level 1 — distill a tool-agnostic rule

Do this only if the same pattern appears across several external runtimes, not because CogniCore alone exists.

Candidate distillation target:

```text
docs/governance/EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md
```

Possible distilled rule:

```text
Runtime memory, reflection and adaptive retries may improve candidate production,
but they must remain scoped runtime signals unless promoted through Pantheon memory gates.
```

Allowed content:

- runtime memory classes;
- reflection output status;
- override limits;
- persistence scope;
- sensitive payload exclusion;
- return-path status separation;
- evidence and memory non-equivalence.

Forbidden content:

- CogniCore-specific API dependency;
- install instructions;
- Hermes profile configuration;
- code snippets that imply adoption;
- schema changes without explicit approval;
- runtime, scheduler, queue or memory engine behaviour.

### Level 2 — add a capability placement note

Do this if a concrete Hermes-side experiment is being considered.

Candidate document:

```text
docs/governance/COGNICORE_HERMES_ADAPTER_CANDIDATE.md
```

Status should be:

```text
candidate / to verify
documented non-implemented
```

Minimum sections:

```text
1. Purpose
2. Allowed Hermes-side use
3. Forbidden Pantheon effects
4. Task Contract input shape
5. Result Candidate output shape
6. Evidence Pack Candidate expectation
7. Runtime memory scope
8. Reflection hint visibility
9. Override prohibition / candidate-only rule
10. Data minimization
11. Approval ceiling
12. Capability Gap conditions
13. Deletion and persistence review
14. Test fixture expectations
```

This document must not create the adapter. It only defines the admissibility conditions for a future adapter.

### Level 3 — prototype outside the kernel

Only after explicit arbitration.

The prototype, if ever created, should live outside Pantheon kernel doctrine, preferably Hermes-side or in an adapter/prototype area explicitly classified as implementation or external runtime experiment.

Pantheon-side artifact should remain limited to:

```text
Task Contract
Capability Passport
governed execution handoff
Result Candidate expectation
Evidence Pack Candidate expectation
Capability Gap rules
```

The prototype must not write Pantheon memory, approve outputs, decide truth, send externally or mutate canonical doctrine.

### Distillation gates

Before any move beyond this review, require the following gates:

| Gate | Question | Safe outcome |
|---|---|---|
| G1 — repeated pattern | Is this a general adaptive-runtime issue, not only a CogniCore feature? | Distill abstract rule only. |
| G2 — placement | Is the effect runtime production or governance status? | Runtime production stays Hermes-side. |
| G3 — memory | Could stored data become false memory or leak dossier material? | Candidate-only, scoped, minimized, deletion policy required. |
| G4 — evidence | Could hints be mistaken for proof? | Label as runtime signal, never Evidence Pack. |
| G5 — override | Could reflection change a consequential action? | Override forbidden except candidate-only low-risk internal revision. |
| G6 — approval | Could the runtime bypass Zeus or human decision? | Block; open gate or return Capability Gap. |
| G7 — implementation | Does the change touch schemas, tests, platform, operations, Docker or runtime code? | Explicit approval required before change. |

### Distillation sequence

Recommended order if needed:

```text
1. Keep CogniCore as external reference.
2. Compare with at least two other runtime-memory systems.
3. Extract the tool-agnostic invariant.
4. Update EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md, not the kernel directly.
5. If a concrete experiment is wanted, create COGNICORE_HERMES_ADAPTER_CANDIDATE.md.
6. Create test fixtures as documentation first.
7. Only after approval, consider implementation outside Pantheon kernel.
```

### Best distilled output

The highest-value extraction is probably not CogniCore itself.

The durable Pantheon concept is:

```text
Runtime Recall Signal
```

A `Runtime Recall Signal` is a runtime-produced candidate signal derived from execution history. It may help an execution runtime avoid repeating operational failures. It is not evidence, memory, approval or truth.

Possible abstract shape:

```text
runtime_recall_signal:
  source_runtime:
  task_family:
  scope:
  signal_type: failure_pattern | success_pattern | reflection_hint | retry_warning
  payload_minimized: true
  confidence:
  derived_from:
  forbidden_uses:
    - evidence
    - approval
    - canonical_memory
    - external_action_authority
  expiry:
  review_status: candidate | ignored | promoted_to_register_candidate
```

This shape should remain documentary until a schema or test is explicitly approved.

## What should not be imported

Do not import CogniCore as Pantheon core.

Do not treat repeated runtime success as proof.

Do not allow reflection override for consequential external action.

Do not let runtime memory store raw private, client, contractual or professional dossier material without scope, minimization and approval rules.

Do not treat a LangChain tool wrapper as an approved connector.

Do not let an evaluator function replace Evidence Pack review, Zeus status or human decision.

Do not use CogniCore terminology to rename Pantheon concepts. Pantheon should keep its own controlled vocabulary:

```text
candidate
Evidence Pack Candidate
Register Candidate
Gate
approval
scope
external effect
canonical memory
```

## Risks and limitations

The reviewed package metadata marks the project as alpha.

The repository URL and package metadata appear partially inconsistent: the reviewed repository is under `cognicore-dev/cognicore-my-openenv`, while package metadata still references `Kaushalt2004/cognicore-my-openenv`.

The runtime stores and persists execution memory. Before any real use with professional data, review is required for:

- data minimization;
- local versus external persistence;
- deletion policy;
- scope isolation;
- sensitive payload exclusion;
- auditability;
- test coverage;
- license and ownership clarity;
- interaction with Hermes logs and profiles.

## Placement decision

Accepted:

- External reference review.
- Inspiration for Hermes-side adaptive execution patterns.
- Inspiration for visible runtime-signal cards.
- Inspiration for stricter adaptive-runtime passport fields.

Refused:

- Pantheon kernel integration.
- CogniCore as source of truth.
- CogniCore as approval engine.
- CogniCore as canonical memory.
- CogniCore as Zeus arbitration.
- CogniCore as default Hermes dependency.

To verify:

- maturity;
- tests;
- security posture;
- persistence behaviour;
- data minimization;
- connector/tool boundaries;
- license and repository ownership clarity.

To arbitrate:

- whether a future Hermes-side prototype should be created as a bounded adapter experiment.
- whether `EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md` should later distill a generic pattern from this review and similar runtime-memory systems.

## Short doctrine distillation candidate

```text
Adaptive runtime memory may improve candidate production.
It must remain runtime-local, scoped, minimized and reviewable.
It never becomes Pantheon memory, evidence, approval or truth by itself.
```
