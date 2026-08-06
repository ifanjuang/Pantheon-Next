# F to J Hermes Convergence Boundary

Status: active support doctrine — human-decided tranche boundary.
Date: 2026-08-06.

This document records the convergence boundary between the current relation tranche
and the later Competence / Tool / Hermes tranche.

It does not implement a runtime, Skill manager, plugin manager, installer, updater,
provider router, workflow engine, scheduler, queue, approval engine, event store,
Cockpit screen, schema, API or Hermes mutation.

```text
Hermes executes and observes its native runtime elements.
Pantheon governs professional Capabilities, scope and consequential change.
pantheon-mvp persists bounded operational records and projections.
The Cockpit presents calculated views and human attention.
The human decides consequential effects.
```

## 1. Decision

The Competence / Tool / Hermes lifecycle is integrated into the existing D–J
programme without inserting a competing tranche.

```text
F
-> provides reusable relation review and ordered-history primitives.

G–I
-> preserve those primitives without introducing Hermes-specific parallel models.

J
-> converges Capabilities, existing Tool Card projections and observed Hermes
   implementations; then adds bounded change management.
```

D–I are not expanded into a Hermes administration project. J remains the first
tranche allowed to decide the identity and projection of Hermes Skills, Toolsets,
Plugins, MCP entries or other native elements.

## 2. Existing primitives to reuse

J must first inventory and reuse, in this order:

```text
Capability / Capability Slot
Tool Card and concrete cockpit tool catalogue
Hermes read-only inventory observations
WorkIssue and WorkIssueScopeLink
DecisionRequest and Decision Record
EntityRef relation carrier and relation review lifecycle
Execution Result and Result Candidate
existing append-only events and provenance records
```

A new concept is justified only when these existing responsibilities cannot cover
the demonstrated need without semantic collision.

```text
reuse
-> extend
-> generalize an existing structure
-> create only for a distinct responsibility
```

## 3. What F must provide

F owns only the reusable relation and history foundations required by later
tranches.

### 3.1 Generic carrier, closed meaning

The relation carrier remains generic in shape and closed in meaning.

```text
EntityRef -> EntityRef
```

A new owner type is admitted only with:

- an authoritative owner;
- a stable identity contract;
- scope resolution;
- refusal behavior;
- projection tests;
- explicit review.

Adding a future owner must not require a second relation table dedicated to Skills,
Tools, Capabilities, Plugins or MCP entries.

### 3.2 Proposal before canonization

Relations use a reviewed lifecycle:

```text
proposed -> canonical -> retired
proposed -> rejected
```

Hermes may propose a relation. Hermes may not canonize, reject or retire one.
This boundary must hold in the schema and executable mutation path, not only in a
prompt.

```text
runtime relation observed != relation proposed
relation proposed != relation canonical
relation canonical != task authorization
```

### 3.3 Ordered append-only history

Events written in one transaction must remain causally orderable. Transaction-start
timestamps are insufficient when several events share the same time.

Every history used for Cockpit reconstruction or Hermes-return tracing must have a
deterministic ordering based on an event time plus a causal discriminator such as
revision or sequence.

### 3.4 Explicit contract drift deferral

A reviewed deferral may pin one exact upstream contract revision.

```text
drift observed != upgrade required
deferral recorded != drift ignored indefinitely
```

If upstream moves beyond the deferred revision, the new drift is unreviewed and
must be raised again.

## 4. What F must not decide

F must not introduce or canonize:

- `HermesElement` as a new backend authority;
- Capability-to-Skill or Capability-to-Tool relation meanings;
- a Skill, Toolset, Plugin or MCP registry owned by Pantheon;
- a general Binding table;
- Skill or Tool version management;
- an upgrade executor;
- autonomy policies for Hermes mutations;
- Skill-specific, Tool-specific or Binding-specific log stores;
- a new Cockpit card family;
- a second backlog or approval path.

The current four Information relation meanings must not be reused artificially to
express future implementation semantics.

```text
répond à / s’appuie sur / remplace / contredit
!= implemented_by / supports / fallback_for / depends_on
```

F supplies the reviewed carrier and lifecycle. J decides whether a demonstrated
new meaning belongs in that carrier or in an already-existing specialized contract.

## 5. Preservation requirements for G–I

G–I must not block the later Competence / Hermes convergence.

Any new durable object introduced before J must be able, when relevant, to:

- be referenced through the canonical cross-domain identity mechanism;
- be scoped by one WorkIssue without creating a dedicated work-link model;
- be the subject of one DecisionRequest without a specialized approval request;
- preserve provenance and append-only history;
- distinguish observation, proposal, adoption and authorization;
- remain projectable without making the Cockpit authoritative.

These are compatibility requirements, not a request to add Hermes-specific fields
to G–I objects.

## 6. J scope

J is the convergence tranche for governed Capabilities and bounded Hermes
implementation links.

### J-alpha — observation and requests

J-alpha must:

1. inventory existing Capability, Tool Card, module-manifest, register-candidate
   and Hermes-observation contracts;
2. decide whether the existing Tool Card projection can represent observed Hermes
   Skills, Skill Bundles, Toolsets, Plugins, MCP entries and Profiles while
   preserving their native kind;
3. relate governed Capabilities to observed implementations without turning
   runtime availability into adoption;
4. expose the existing `Compétences` and `Outils` spaces as two projections of
   distinct responsibilities;
5. provide one user action, `Demander une modification`, creating a WorkIssue;
6. expose read-only, correlated operational history without creating per-object
   log authorities.

J-alpha performs no native installation, activation, update or deletion.

### J-beta — bounded management

Only after J-alpha is verified may J-beta introduce:

- Hermes diagnosis of a WorkIssue;
- isolated tests and candidate Skill or Plugin changes;
- compatibility and version-drift reporting;
- reversible rollback under an admitted policy;
- DecisionRequest creation for consequential effects;
- application by Hermes or another admitted native executor after authorization;
- fresh post-change observation.

Pantheon must not execute these native operations itself.

## 7. UX boundary

The accepted root spaces remain:

```text
Pantheon
Décisions
Affaires
Connaissances
Compétences
Outils
```

```text
Compétences
= what the system is governed to know how to do professionally.

Outils
= replaceable technical means and observed Hermes-native elements.
```

The primary user request is outcome-oriented:

```text
Demander une modification
```

The user describes the problem and expected result. The system may later qualify
the WorkIssue as add, improve, fix, adapt, upgrade, replace, review, deprecate or
remove. The user is not required to identify a Skill, Tool, Binding or Provider in
advance.

Native Hermes detail remains progressively disclosed for diagnosis and technical
administration.

## 8. Hermes autonomy boundary

Hermes may, within admitted scope:

- inventory its native Skills, Toolsets, Tools, Plugins, MCP entries and Profiles;
- observe availability and exact versions;
- diagnose failures;
- create or modify a candidate Skill;
- prepare a candidate Plugin or adapter;
- test in isolation;
- compare variants;
- prepare a rollback;
- propose a WorkIssue, relation or DecisionRequest context.

Hermes may not infer from technical success that it may:

- admit a Capability;
- canonize a governed relation;
- expand permissions or scope;
- adopt a new sensitive dependency;
- activate a production change;
- delete a governed element;
- promote an Execution Result to Evidence;
- approve its own consequential proposal.

```text
technical and reversible under an admitted policy
-> may be managed by Hermes.

new authority, permission, destination, dependency or consequential effect
-> human decision required.
```

The initial autonomy vocabulary remains deliberately small:

```text
observed
managed
governed
```

It must not become a general automatic approval engine.

## 9. Change and attention flow

The target flow reuses existing authorities:

```text
Capability or Tool Card
-> Demander une modification
-> WorkIssue with EntityRef scopes
-> bounded Hermes inspection / test / proposal
-> Execution Result and correlated events
-> DecisionRequest only when consequential
-> human Decision Record
-> admitted native executor applies
-> fresh observation
-> WorkIssue verification and closure
```

No specialized `SkillUpgradeRequest`, `PluginInstallRequest`,
`ToolImprovementRequest` or parallel backlog is introduced.

## 10. Observability boundary

Operational events form one correlated history. Skill, Toolset, Tool, Plugin,
Capability, WorkIssue, run and project views are filters over that history.

```text
one event != incident
incident != WorkIssue
WorkIssue != DecisionRequest
runtime success != Evidence
```

Repeated or blocking events may support an Incident or WorkIssue proposal, but no
single runtime error automatically creates governed work or human attention.

## 11. Required invariants

```text
Capability candidate != Hermes Skill implemented
Hermes Skill implemented != Capability admitted
Tool catalogued != runtime element discovered
runtime element discovered != installed
installed != approved
approved != activated for a scope
healthy != safe
enabled != task authorized
binding selected != dependency adopted
relation proposed != relation canonical
Execution Result != Evidence
Cockpit projection != runtime persistence
Hermes proposal != human decision
```

## 12. Completion criteria

This boundary is respected when:

1. F closes with a reusable reviewed relation lifecycle and deterministic history;
2. F creates no Hermes-specific authority or vocabulary prematurely;
3. G–I introduce no second graph, backlog, decision system or event authority;
4. J begins with an inventory of existing contracts rather than a new model;
5. Capability, Tool Card, WorkIssue, DecisionRequest, EntityRef, Execution Result and
   existing events are reused before new concepts are considered;
6. Hermes retains native ownership of Skills, Toolsets, Tools, Plugins and MCP;
7. the Cockpit remains a calculated human-facing projection;
8. consequential changes remain human-decided;
9. optional adapters remain replaceable;
10. authoritative professional data survives disabling or replacing Hermes.

## 13. Non-goals

This document does not:

- select PinchTab, Playwright, Docling or another provider;
- add a Capability relation vocabulary;
- install or configure Hermes;
- modify the active F implementation branch;
- authorize a Hermes run or mutation;
- prescribe storage before the J inventory;
- make Tool Card the final answer before verification;
- promote runtime observations to Pantheon authority.

```text
boundary documented != tranche implemented
future reuse enabled != future concept admitted
```
