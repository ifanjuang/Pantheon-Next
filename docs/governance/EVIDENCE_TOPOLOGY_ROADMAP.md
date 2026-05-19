# Evidence Topology Roadmap Addendum

Status: active roadmap addendum — evidence topology, single-context default and bounded Hermes swarm.

This addendum records the roadmap consequences of `EVIDENCE_TOPOLOGY_GATE.md`.

It exists because the main `ROADMAP.md` was not safely patchable in the current tool pass.

It does not replace `ROADMAP.md`.

It does not implement runtime behavior.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Why this addendum exists

External multi-agent and swarm examples show a recurring failure mode:

```text
specialist workers
-> partial source views
-> summary-only handoffs
-> supervisor synthesis
-> wrong conclusion with high coordination cost
```

Pantheon must prevent this pattern from becoming doctrine.

The correct unit of reasoning is the proof chain, not the number of agents.

## Roadmap status

`EVIDENCE_TOPOLOGY_GATE.md` is active governance doctrine.

It is documentation-level only.

It does not change schemas, operations, tests, platform files, Docker, runtime code or Hermes configuration.

## Keep

Keep these roadmap principles:

- single primary reasoning context by default when decisive evidence must be connected across sources;
- fan-out extraction followed by single synthesis when many sources must be inspected;
- parallel workers only when tasks are genuinely independent;
- routers only for classification, not truth decisions;
- sequential handoff only when each step carries verifiable evidence;
- bounded Hermes swarm only as execution capacity;
- role-team handoff only when each role owns a distinct artifact, boundary or stage;
- source-linked Evidence Items rather than unverifiable worker opinions;
- append-only accumulation where evidence quality is improved across revisions;
- explicit critic or review gates before writer, publisher, deployer or sender stages;
- User Decision Gate when topology affects scope, risk, external effect, cost, delivery or memory;
- Governance College as review of tensions, not distributed execution.

## Reject

Reject these roadmap directions:

- multi-agent by default;
- swarm as intelligence multiplier by default;
- conductor as Zeus;
- role-as-worker confusion;
- hidden debate runtime;
- summary-only handoff for decision-critical work;
- worker checkpoint as approval;
- runtime trace as Evidence Pack;
- Hermes memory as Pantheon Canonical Memory;
- agent memory or auto-captured Knowledge Base as doctrine;
- direct agent-to-agent handoff without governed artifact or source locator;
- tool availability as tool authorization;
- schema field before doctrine stabilizes.

## Persistent role-team pattern

A persistent role-team can work when the roles are stage-bound and artifact-bound.

Example pattern:

```text
research -> strategy brief -> writer draft -> editor review -> SEO packaging
arch review -> backend implementation -> frontend adaptation -> review gate
```

Keep:

- explicit purpose per role;
- explicit handoff destination;
- visible team conversation or canvas;
- durable style or project constraints as candidates for scoped memory;
- handoff artifacts such as API contract, campaign brief, draft, review note or metadata package;
- human visibility before publication, deployment, external transmission or memory promotion.

Reject:

- agent-to-agent chatter as evidence;
- role memory as Canonical Memory;
- auto-captured Knowledge Base as approved doctrine;
- direct handoff as approval;
- editor, reviewer, SEO or arch agents acting as final professional authority;
- hidden scope expansion between product, code, content, marketing and governance work.

Pantheon translation:

```text
Persistent Hermes roles may keep execution continuity.
Pantheon still requires Task Contract scope, Evidence Pack review, approval thresholds and memory discipline.
```

## LangGraph research orchestrator pattern

Keep from the LangGraph clinical research orchestrator example:

- explicit graph edges;
- Researcher -> Critic -> Human Review -> Writer sequencing;
- critic loop before report writing;
- append-only evidence accumulation across revisions;
- human-in-the-loop interrupt before the writer stage;
- structured state over informal handoff;
- refusal to let a Writer act on thin or contradictory evidence.

Reject from Pantheon:

- LangGraph as Pantheon runtime;
- clinical report generation as professional advice without review;
- Critic approval as final approval;
- in-memory checkpoint as Canonical Memory;
- tool search result as Evidence Item without selection and source qualification.

Pantheon translation:

```text
Researcher may collect.
Critic may challenge sufficiency.
Human review may gate writing.
Writer may draft.
Pantheon governs the status of every step.
```

## Hermes Workspace pattern distillation

Keep from Hermes Workspace:

- SwarmBrief as an inspiration for a derived Hermes execution brief;
- proof-bearing checkpoints;
- explicit blockers;
- review lane;
- Greenlight Gate;
- role-based worker routing;
- skill-as-procedure discipline;
- Reports and Inbox as exposure surfaces.

Reject from Pantheon:

- Hermes Workspace as Pantheon cockpit;
- Conductor as governance;
- swarm as judgment;
- editable agent memory as Canonical Memory;
- skill marketplace as approval;
- MCP, terminal, dashboard, jobs, scheduler or tool runtime inside Pantheon.

## Task Contract implications

Future Task Contract examples may include a non-runtime topology declaration such as:

```yaml
reasoning_topology:
  selected: single_primary_reasoning_context
  reason: cross_source_reasoning_required
  handoff_policy: no_summary_only_handoff
  evidence_policy: source_linked_evidence_items_required
```

This is a governance expectation.

It is not a dispatch instruction.

The current schemas are unchanged.

Any future schema update is protected work.

## Evidence Pack implications

Future Evidence Pack examples may record:

- selected topology;
- why the topology was chosen;
- worker outputs treated as Evidence Items;
- summary-only handoffs rejected or blocked;
- contradictions preserved;
- synthesis limitations;
- unresolved evidence gaps;
- User Decision Gate impact.

Evidence Packs must not become runtime traces or chain-of-thought archives.

## Read-only Doctor implications

Future read-only checks may eventually flag:

- docs claiming multi-agent improves reliability by default;
- role profiles being treated as Pantheon authority;
- summary-only handoffs in examples;
- Hermes swarm described as approval authority;
- runtime state described as memory;
- topology fields described as executable dispatch instructions.

These checks must remain read-only.

They must not execute workflows or dispatch workers.

## Example sequence before schema work

Recommended next sequence:

1. Add a fictional Task Contract example using `single_primary_reasoning_context`.
2. Add a fictional Task Contract example using `fanout_extract_then_single_synthesis`.
3. Add a fictional Task Contract example using `persistent_role_team_handoff` for artifact-bound work.
4. Add a fictional Evidence Pack example showing Evidence Items from workers.
5. Add a User Decision Gate example where topology choice affects risk or cost.
6. Only then consider schema changes under the protected-file rule.

## Final rule

```text
Swarm for collection.
Role-team handoff for bounded artifact stages.
Single context for inference when evidence must connect.
Governance College for review.
User Decision Gate for unresolved stakes.
Human decision for consequential approval.
```
