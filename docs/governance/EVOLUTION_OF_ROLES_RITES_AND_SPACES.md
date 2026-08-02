# Evolution of Roles, Rites and Spaces

Status: candidate support doctrine — documented non-implemented.
Boundary profile: candidate_support_note.

This document coordinates how Pantheon Roles, Rites and Spaces may be introduced, changed, reviewed, deprecated or superseded without creating duplicate ontology, hidden runtime authority or UI-driven semantics.

It does not replace the owner documents for Roles, Rites or the Card Stack.

```text
Roles judge.
Rites structure method.
Spaces expose bounded context and deliberation.
Hermes executes.
Pantheon governs.
The human decides.
```

## 1. Purpose

Pantheon may evolve, but not every new need justifies a new Role, Rite or Space.

Before adding one of these forms, reconcile the need against existing concepts:

```text
Context
Trace
Knowledge
Evidence
Claim
ChangeCandidate
Competence
Method
Role
Rite
Scene
Deck
Constellation
Agora
```

The objective is convergence:

```text
one recurring responsibility
-> one stable owner

one recurring methodological tension
-> one governed rite

one review purpose
-> one bounded projection space
```

## 2. Definitions and semantic owners

### Role

A Role is a standing responsibility of judgment.

A Role is not an agent, runtime worker, tool router, prompt profile or executable module.

Owner references:

- `GOVERNANCE_COLLEGE.md`;
- `docs/domain-packs/architecture/ROLE_FACETS.md`;
- `docs/domain-packs/architecture/ROLE_ACTIVATION_MODEL.md`;
- `docs/domain-packs/architecture/ROLE_REFLEX_COORDINATION.md`.

### Facet or quality

A facet is a stable quality by which a Role perceives, warns, orients, proposes, consults or limits itself around its jurisdiction.

A facet is not a new Role and does not create execution authority.

### Rite

A Rite is a governed method coordinating several role viewpoints around a recurring methodological tension.

A Rite is not an agent, workflow engine, scheduler, queue, approval loop or runtime.

Owner references:

- `docs/governance/rites/README.md`;
- `docs/governance/rites/RITE_INVOCATION_POLICY.md`;
- `docs/governance/rites/RITE_MODES.md`;
- `docs/governance/rites/RITE_EXIT_CRITERIA_AND_CONFLICTS.md`.

### Space

A Space is a bounded environment of reference, deliberation, project review or projection.

A Space does not own the underlying object lifecycles unless an owner document explicitly says so.

Examples:

```text
Governance Reference Space
Project Space
Agora
Scene
Deck
Constellation
```

Owner references:

- `CARD_STACK_MODEL.md` for Scene, Deck, Constellation, Reference Space and Project Space;
- Agora doctrine for visible deliberation;
- underlying domain owner documents for the objects projected inside a Space.

## 3. What should remain stable

### Roles

The jurisdiction of a Role should change rarely.

A Role may be changed only when an observed responsibility cannot be safely covered by:

- an existing jurisdiction;
- a new or clarified facet;
- a Method;
- a Competence;
- a Rite;
- a consultation between existing role qualities.

```text
new subject != new Role
new tool != new Role
new document type != new Role
new workflow step != new Role
```

### Rites

The purpose, trigger boundary, anti-triggers, expected outputs and closure conditions of an active Rite should remain stable enough to be reviewed and compared over time.

Operational guides and Hermes bindings may evolve more quickly than the governed Rite.

```text
Rite doctrine != execution binding
Rite revision != new Rite by default
binding change != semantic change
```

### Spaces

A Space should have one clear review or deliberation purpose.

A new visual arrangement, filter, card family or navigation state does not automatically justify a new Space.

```text
new screen != new Space
new card != new Space
new filter != new Space
new route != new Space
```

## 4. What may evolve progressively

| Element | Normal evolution | Higher-threshold change |
|---|---|---|
| Role | clarify facets, jurisdiction wording, consultation boundaries | split, merge, create or retire a Role |
| Facet | refine expression threshold, tactics and limits | move responsibility to another Role |
| Rite | refine modes, examples, observations and closure guidance | change purpose, authority boundary or retained outputs |
| Space | refine projection, navigation, density and labels | create, merge, rename or remove a governed Space |
| Hermes binding | implementation, tools, transport and verification technique | broaden capability, scope, data exposure or external effects |
| Cockpit projection | layout, grouping and progressive disclosure | introduce a new semantic object or status axis |

## 5. Addition test

Before proposing a new Role, Rite or Space, answer:

```text
What observed problem is not covered?
Which existing owner documents were checked?
Why is extension insufficient?
What is the smallest new semantic commitment?
Who owns the meaning?
What does the proposal explicitly not do?
How can it be removed or superseded?
```

A proposal must be rejected or reduced when it mainly provides:

- a more attractive metaphor;
- a duplicate name for an existing responsibility;
- a UI grouping without semantic need;
- a runtime convenience;
- a prompt persona;
- a tool-specific abstraction;
- an automatic approval shortcut.

## 6. Role evolution procedure

```text
observed recurring responsibility
-> reconcile against existing jurisdictions
-> test facet extension
-> test Method, Competence or Rite coverage
-> document the uncovered responsibility
-> define jurisdiction, limits and consultations
-> test on representative cases
-> review overlap and authority risk
-> candidate status
-> active promotion only after explicit governance review
```

A Role proposal should include:

```text
role_id
purpose
standing jurisdiction
facets or qualities
expression thresholds
allowed consultations
allowed rite requests
limits
forbidden drift
overlap analysis
examples
lifecycle status
```

### Role split

Split a Role only when one Role contains two responsibilities that:

- require materially different evidence;
- create recurring conflicts of judgment;
- have different approval or escalation boundaries;
- cannot remain understandable through facets.

### Role merge

Merge Roles when their jurisdictions are indistinguishable in practice and separation only creates repeated consultation, duplicated doctrine or UI noise.

### Role retirement

A retired Role must identify where each retained responsibility moves. Historical references may remain, but no active Task Contract or projection should depend on an undefined Role.

## 7. Rite evolution procedure

The existing Rite lifecycle remains authoritative:

```text
proposed
active
under_review
deprecated
rejected
superseded
```

A new or revised Rite should follow:

```text
observed recurring methodological tension
-> check existing Rite catalogue
-> test mode or guide extension
-> define triggers and anti-triggers
-> define role viewpoints and retained outputs
-> define closure and next allowed action
-> test with fictional and real bounded cases
-> review cost, proof value and chaining risk
-> candidate review
-> activation, rejection or supersession
```

A Rite revision does not justify a new Rite when the original purpose and closure remain unchanged.

Create a distinct Rite only when the tension, review sequence or required retained output is materially different.

### Rite review criteria

A Rite should be placed `under_review` when:

- it is repeatedly invoked without changing decisions;
- it creates proof theatre;
- it is commonly chained with other Rites;
- it duplicates another Rite;
- its outputs are not retained or reviewable;
- its execution binding silently expands scope;
- users cannot distinguish its result from approval.

A Rite may be deprecated or superseded, but its past Review Cards and traces remain historically attributable to the exact Rite identity and revision used.

## 8. Space evolution procedure

A Space exists to make a class of review, reference or deliberation understandable.

Before creating a Space, first test whether the need is only:

- a Scene;
- a Deck;
- a card projection;
- a filter;
- a mode of progressive disclosure;
- a project selector;
- a bounded Agora discussion.

A Space proposal should define:

```text
space_id
purpose
scope
underlying objects projected
entry and exit conditions
navigation relation to existing Spaces
owner documents
what the Space may expose
what the Space may not decide or execute
retirement or merge path
```

### Space creation

Create a Space only when the user must maintain a stable mental distinction between two kinds of activity, such as:

```text
reusable governance reference
!=
project-specific work

visible human deliberation
!=
bounded procedural review
```

### Space merge

Merge Spaces when users cannot explain their distinction, objects are duplicated between them without a review reason, or navigation exists only because of historical implementation structure.

### Space rename

A rename must preserve underlying identities and relations. A new label does not create a new Space or migrate authority.

### Space removal

Removing a Space removes a projection or navigation environment, not the governed objects it displayed. Those objects must remain accessible through their owner-defined projections or archival references.

## 9. Relations between Roles, Rites and Spaces

```text
Role
-> carries a standing responsibility of judgment

Rite
-> temporarily structures several relevant viewpoints

Space
-> exposes the relevant objects, tensions, status and next review action
```

Allowed relation:

```text
Role quality observes a tension
-> proposes a Rite
-> ZEUS authorizes or rejects
-> Hermes may execute an admitted binding
-> outputs return as candidates and observations
-> a Space exposes the result
-> human or governed status closes the consequence
```

Forbidden collapse:

```text
Role visible in UI
-> Role executed

Rite selected
-> Rite authorized

Rite completed
-> output approved

Space displays status
-> Space owns status

Agora discussion
-> decision recorded
```

## 10. Evidence and change discipline

Changes to Roles, Rites or Spaces should identify:

- observed need;
- current owner documents;
- overlap analysis;
- examples or usage evidence;
- affected Task Contracts, schemas or projections;
- migration requirements;
- rollback or supersession path;
- authority impact;
- implementation impact, if any.

Consequential semantic changes should use a reviewed ChangeCandidate where the current implementation supports it.

```text
documented proposal != active doctrine
active doctrine != runtime implementation
runtime implementation != task authorization
usage observation != Evidence promotion
```

## 11. Promotion criteria

A candidate may become active only when:

- its owner and boundaries are explicit;
- no existing concept adequately covers it;
- overlap and terminology have been reviewed;
- examples demonstrate usefulness;
- anti-patterns and failure modes are stated;
- the change does not create runtime authority in Pantheon;
- required human-decision and ZEUS boundaries remain intact;
- documentation, schemas, implementation and projection statuses are not conflated.

## 12. Deprecation and supersession

Deprecation must be explicit and non-destructive.

```text
deprecated element
-> remains identifiable historically
-> names its successor or reason for rejection
-> stops receiving new references
-> preserves past traces and decisions
-> removes active projections only after consumers migrate
```

Supersession must state:

```text
superseded_id
successor_id
scope of supersession
effective date
retained historical meaning
migration impact
```

## 13. Anti-patterns

Do not:

- create a god for each professional topic;
- turn facets into sub-agents;
- turn Rites into workflows or automatic chains;
- turn Spaces into backend domains solely because they are visible in navigation;
- let Cockpit cards define backend schemas;
- make a runtime binding canonical doctrine;
- preserve obsolete identities through permanent compatibility aliases without a removal condition;
- use mythology to conceal ownership or authority;
- treat repeated use as approval;
- infer implementation from documentation status.

## 14. Compact decision rule

```text
Need a new judge?
-> consider a Role only after facet and consultation tests fail.

Need a recurring discipline?
-> consider a Rite only after existing Rite and mode tests fail.

Need a distinct mental environment?
-> consider a Space only after Scene, Deck, filter and projection tests fail.

Need execution?
-> it belongs to Hermes or another approved runtime, not to Role, Rite or Space.
```

## 15. Final rule

```text
Roles evolve by rare jurisdiction change and careful facet clarification.
Rites evolve through governed methodological review and explicit lifecycle status.
Spaces evolve as bounded projections and deliberation environments without acquiring hidden authority.

Extend before multiplying.
Supersede before duplicating.
Observe before promoting.
Keep execution outside Pantheon.
Keep consequential decisions human.
```
