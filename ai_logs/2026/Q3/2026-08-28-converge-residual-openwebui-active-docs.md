# Residual OpenWebUI active-document convergence — 2026-08-28

## Objective

Audit remaining active repository documents after #666/#780/#781/#783 and remove residual OpenWebUI ownership only where it still described current architecture. Preserve historical ai_logs and dated implementation provenance.

## Revalidated base

Pantheon-Next `main`: `f6fda6f20b31e35447a28ddd8ad45e79a2c5f812`.

Open issue search found no active issue assigning `OpenWebUI exposes`. Broad repository search still returned many historical ai_logs plus active doctrine carrying present-tense OpenWebUI ownership.

## Classification

Left unchanged:

- `ai_logs/**` other than this current intervention log: historical provenance;
- dated implementation history such as `implementation/docs/architecture/2026-08-03-stable-openwebui-projection-routes.md`: historical implementation provenance unless a current owner points to it as authority;
- product comparisons or explicit refusal/history statements that do not assign current authority;
- `templates/README.md`: already client-agnostic and explicitly protects retirement of `templates/openwebui/`.

Initial active drift included the HTTP pointer/contract, Approval, Run Trace, Evidence Pack, Task Contract, Governance College, public introduction and Agent Plugins review.

A review-driven executable sweep then found 30 additional present-tense ownership hits across active doctrine, including workflow, Knowledge, Context Packs, visual language, request coordination, product differentiation, repository simplification, Role Signals, execution discipline, Hermes integration, User Decision Gate, Scope Isolation and rite policy surfaces.

## Hermes WebUI clarification

During the slice, `nesquena/hermes-webui` was explicitly identified as an available Hermes web/mobile surface that should remain proposed/optional rather than mandatory.

Upstream revalidation on 2026-08-28 observed:

- public repository `nesquena/hermes-webui`;
- MIT licence;
- active upstream development;
- near-CLI web/mobile interaction positioning;
- chat runs Hermes Agent in-process by default, with an optional Gateway-backed chat mode documented separately.

Therefore Hermes WebUI must not be collapsed into a generic mandatory `Hermes Web/dashboard` owner. If selected, it is a replaceable external runtime/client surface requiring its own deployment/security qualification.

```text
Hermes WebUI available != Hermes WebUI selected
Hermes WebUI selected != Pantheon authority transferred
Hermes WebUI runtime approval card != Pantheon human approval
web interaction success != Evidence
```

## Current split

```text
optional runtime client / Hermes WebUI candidate = possible runtime interaction
Hermes Agent                                      = external execution
runtime PEP                                       = consequential-effect enforcement
Pantheon Cockpit                                  = governed projections / Cards / decisions / status
Pantheon Next                                     = governance / PDP authority
human                                             = consequential decision
```

No capability is removed. Client interaction, execution, policy enforcement, approval, Task Contract, Evidence, Run Trace, rites, Knowledge, scope and Cockpit projection remain with their existing owners.

## Review-driven widening

PR review correctly identified two initial problems:

1. the stable HTTP pointer had been corrected while its protected contract still carried the old OpenWebUI/PEP wording;
2. a hand-maintained five-file regression allowed other active doctrine to keep assigning current ownership to OpenWebUI.

Corrections:

- protected HTTP contract corrected alongside its stable pointer while preserving runtime PEP responsibility;
- Task Contracts and Governance College corrected;
- regression changed into an executable active-doctrine inventory of retired ownership phrases;
- the resulting 30 hits were corrected systematically rather than replaced with another mandatory WebUI;
- PR body expanded with Role/Rite/Space context, overlap, consumers, rollback, authority and runtime impact.

The sweep intentionally distinguishes current ownership statements from historical provenance. The objective is not lexical deletion of `OpenWebUI` from Git history.

## Active-doctrine sweep

Current ownership was made client-agnostic in:

```text
WORKFLOW_SCHEMA.md
KNOWLEDGE_TAXONOMY.md
CONTEXT_PACKS.md
VISUAL_LANGUAGE.md
REQUEST_ORCHESTRATION.md
PRODUCT_DIFFERENTIATION.md
REPOSITORY_SIMPLIFICATION_PLAN.md
ROLE_SIGNALS.md
EXECUTION_DISCIPLINE.md
USER_DECISION_GATE.md
SCOPE_ISOLATION.md
rites/RITE_MODES.md
rites/RITE_SELECTION_MATRIX.md
rites/RITE_EXIT_CRITERIA_AND_CONFLICTS.md
rites/README.md
rites/RITE_INVOCATION_POLICY.md
rites/RITE_ANTI_PATTERNS.md
```

These documents now use a generic optional runtime-client boundary. Hermes WebUI appears only where a concrete optional/proposed client example materially helps.

## Semantic owner consolidation

Two active owners were fully read through EOF before modification and were found to contain large absorbed historical/candidate catalogues in addition to their current responsibility.

### `HERMES_INTEGRATION.md`

The prior file mixed:

- the stable Pantheon/Hermes integration boundary;
- historical Hermes 0.17/0.19 surface reviews;
- absorbed simulation/evaluation material;
- absorbed Kanban/multi-profile patterns;
- absorbed Page-Agent adapter design;
- historical OpenWebUI Knowledge and exposure assumptions.

The active owner is now reduced to its stable responsibility:

```text
Pantheon/Hermes boundary
PDP/PEP chokepoint
Task Contract / admission
candidate return discipline
Evidence
source/retrieval
runtime memory
Roles/profiles
subagents/deliberation
skills/tools/MCP/plugins
messaging/external effects
repository mutation
Capability Gaps
runtime currentness ownership
optional Hermes WebUI qualification boundary
```

Release-specific review remains with `HERMES_RUNTIME_SURFACE_REVIEW.md`. Other candidate patterns remain with their dedicated owners or Git/ai_log provenance.

### `EXTERNAL_TOOLS_POLICY.md`

The prior file mixed the real tool policy with absorbed framework/method/repository catalogues.

The retained policy owner keeps:

```text
T0-T5 effect/risk classes
authorization questions
least capability
Evidence discipline
read/write/repository/communication rules
MCP/gateway/plugin/provider boundaries
installation/configuration
memory/secrets
external-runtime review record
host-control classification
untrusted-content and prompt-injection posture
permission granularity
exposure posture
runtime-client/Hermes WebUI review
PDP/PEP relationship
safe defaults
revocation/rollback
```

Framework and repository comparison belongs to watchlist, distillation, reference-review and placement owners rather than this policy.

Both large reductions are explicitly acknowledged in `.github/scripts/truncation_ack.txt`; they are deliberate convergence, not partial-read truncation.

## Preserved invariants

```text
runtime display != governance authority
runtime output != Evidence
Evidence Pack Candidate != admitted Evidence
projection != persistence
projection != approval
optional client selected != authority transfer
runtime PEP enforcement != Pantheon governance authority
PDP decision != PEP execution
retrieved != true
runtime memory != Registre Probatoire
runtime success != Evidence
```

## Test

`tests/test_openwebui_integration_owner_retirement.py` protects the corrected core surfaces and scans `Status: active doctrine` documents for present-tense retired ownership phrases while continuing to allow historical/retirement provenance elsewhere.

The test is used as an executable inventory: a failing path is treated as a real review target, not silenced merely to make CI green.

## Finish criteria

- no prohibited OpenWebUI ownership phrase remains in active doctrine;
- Hermes WebUI is optional/proposed, not required;
- no replacement client becomes governance authority;
- protected HTTP PDP/PEP responsibility remains explicit;
- `HERMES_INTEGRATION.md` and `EXTERNAL_TOOLS_POLICY.md` each own one clear responsibility instead of absorbed catalogues;
- historical provenance remains available in Git/ai_logs;
- Governance CI, Architecture Audit and Obsolete Authority green on exact PR head;
- no unresolved review finding.