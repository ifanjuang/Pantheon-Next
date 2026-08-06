# F to J Hermes convergence boundary

Date: 2026-08-06.
Decision owner: human.
Status: recorded architecture decision; documentation-only.

## Context

The D–J programme has reached the beginning of F. Recent review of the current
Pantheon-Next and pantheon-mvp state, together with the current Hermes extension
model, showed that the repositories already provide the principal primitives for
future Competence / Tool / Hermes lifecycle work:

- Capability and Capability Slot;
- Tool Card and concrete catalogue projection;
- read-only Hermes inventory observations;
- WorkIssue with multi-EntityRef scopes;
- DecisionRequest separated from Decision Record;
- reviewed generic EntityRef relations;
- Execution Results and append-only histories.

The remaining risk is no longer absence of concepts. It is premature creation of
parallel Skill, Tool, Binding, upgrade, log and approval models before J inventories
what already exists.

## Human decision

The Competence / Tool / Hermes lifecycle is integrated into the existing D–J
programme without adding a competing tranche.

```text
F
-> reusable relation proposal/review and deterministic-history foundations.

G–I
-> compatibility preservation only; no Hermes-specific parallel model.

J-alpha
-> observation, Capability-to-implementation visibility, Cockpit requests and
   read-only correlated history.

J-beta
-> bounded Hermes diagnosis, isolated candidate changes, rollback and
   consequential human decisions.
```

F does not decide the identity of Skills, Toolsets, Plugins, MCP entries, Bindings
or runtime instances in Pantheon. It must only make the generic reviewed carrier
and history reusable.

J must begin by inventorying and reusing Capability, Tool Card, WorkIssue,
DecisionRequest, EntityRef, Execution Result and existing event contracts before a
new object is proposed.

## Invariants

```text
runtime relation observed != relation proposed
relation proposed != relation canonical
Capability candidate != Hermes Skill implemented
Hermes Skill implemented != Capability admitted
installed != approved
healthy != safe
enabled != task authorized
Execution Result != Evidence
Cockpit projection != runtime persistence
Hermes proposal != human decision
```

Hermes may propose relations and bounded technical changes. It may not canonize a
relation, admit a Capability, expand permissions or approve its own consequential
change.

## Repository effect

Added:

- `docs/governance/F_TO_J_HERMES_CONVERGENCE_BOUNDARY.md`
- this decision log.

No schema, API, test, runtime, Cockpit code, adapter, installation, Hermes mutation
or production activation is changed.

## Closure

The architectural boundary is decided and documented. F may proceed using the
recorded constraints. The concrete identity/projection decision for Hermes-native
elements remains intentionally open until the J inventory.
