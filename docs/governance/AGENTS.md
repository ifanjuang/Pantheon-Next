# Pantheon Roles

Status: canonical — governance roles; not executable agents.

Pantheon Roles are canonical governance roles.

They are not executable agents.
They are not runtime profiles.
They do not install tools.
They do not execute tasks directly.

Hermes profiles may be aligned with Pantheon Roles, but they remain execution profiles and produce candidates only.

## Doctrine

Hermes clients handle runtime interaction.
Hermes Agent executes externally.
Pantheon Cockpit exposes governed projections.
Pantheon Next governs consequential status.

## Naming and compatibility

This file keeps the historical name `AGENTS.md` for repository compatibility.

The canonical concept is `Pantheon Role`.

A Pantheon Role is a governance authority surface.

It is not a runtime identity.

It is not a Hermes profile.

It is not an autonomous actor.

Clarification is preferred over renaming because the file is already referenced by schemas, profiles and governance documents.

## Canonical rule

This document is the canonical role registry for Pantheon Next.

Hermes profile files under `hermes/profiles/` may reference this document, but they must not redefine Pantheon Role authority.

If a Hermes profile conflicts with this document, this document wins.

`GOVERNANCE_COLLEGE.md` defines how these roles interact as a college of separated governance viewpoints, useful tensions and procedural arbitration.

It does not redefine the role registry.

## Role registry

| Pantheon Role | Hermes Profile | Governance Function | Runtime Status |
|---|---|---|---|
| ATHENA | `athena-agent` | Planning, decomposition, workflow strategy | Candidate-only profile |
| ARGOS | `argos-agent` | Source research, evidence and traceability | Candidate-only profile |
| THEMIS | `themis-agent` | Risk, policy compliance, approval boundaries | Candidate-only profile |
| APOLLO | `apollo-agent` | Quality review, completeness, delivery readiness | Candidate-only profile |
| ZEUS | `zeus-agent` | Arbitration when conflict or variant selection is required | Candidate-only profile |
| IRIS | `iris-agent` | Formatting, transmission, clarification and user-facing formulation | Candidate-only profile |
| HEPHAISTOS | `hephaistos-agent` | Build, patch preparation, implementation candidates | Candidate-only profile |
| MNEMOSYNE | — | Memory continuity, historical retrieval framing, current-state/version review and retention-placement proposals | No dedicated profile required |

The absence of a dedicated Hermes profile for a Pantheon Role is valid. Canonizing a governance responsibility does not create an execution profile, install a tool or authorize a runtime capability.

### Name collision: Role versus external memory product

`MNEMOSYNE` in this registry is the Pantheon governance Role.

Some external-memory reviews also mention a third-party product or provider named `Mnemosyne`.

They are unrelated identities.

```text
Pantheon Role MNEMOSYNE
= governance responsibility for memory continuity and placement judgment

external product / provider Mnemosyne
= replaceable candidate binding reviewed outside the Role registry
```

Selecting, installing or using an external memory product does not activate the Pantheon Role, and activating the Pantheon Role does not select any memory provider.

## Universal role constraints

Pantheon Roles may govern through documented policies, approvals and evidence requirements.

Hermes profiles aligned to Pantheon Roles may execute under Task Contract.

Hermes profiles must not:

- approve final actions;
- canonize workflows;
- promote memory;
- mutate doctrine;
- self-authorize code merge or merge without an exact governed authorization;
- bypass approvals;
- become source of truth;
- silently ignore missing capabilities.

The same limits apply when an execution runtime performs retrieval or memory-related work requested from a MNEMOSYNE viewpoint.

## Authority boundaries

Pantheon Roles can review, recommend, request revision or escalate.

Authority belongs to Pantheon governance.

Execution belongs to Hermes Agent under Task Contract.

Runtime interaction belongs to Hermes Web/dashboard or another compatible replaceable Hermes client.

Governed status/navigation/review projection belongs to Pantheon Cockpit and existing Card projection owners.

A selected client or displayed projection does not gain governance authority.

A role output is a candidate unless another governance document explicitly marks the required validation path as complete.

## Inter-role review model

Pantheon Roles may structure disagreement and review.

A task may request several candidate views, such as planning, evidence, risk, quality, memory continuity, arbitration or formulation.

This remains a documentary review model.

It does not create a runtime inside Pantheon Next.

Candidate views can be compared.

Weak evidence can be challenged.

Stale or duplicated memory can be challenged.

Risky proposals can be escalated.

Competing variants can be arbitrated.

Final wording can be reformulated without changing substance.

No role self-promotes its own conclusion into canonical truth or durable memory.

## Governance college model

Pantheon Roles are best understood as a governance college, not as a multi-agent execution team.

The purpose of the college is not to multiply outputs.

The purpose is to separate responsibilities of judgment and preserve useful tension before validation.

A role has value only when it can reveal, preserve or escalate a useful tension.

Examples:

- ATHENA may structure a task while ARGOS challenges missing sources;
- MNEMOSYNE may surface a prior decision while ARGOS challenges whether its source still supports reuse;
- MNEMOSYNE may detect a stale or superseded memory while ZEUS arbitrates the next status or review path;
- APOLLO may make a draft clear while THEMIS blocks delivery because proof is insufficient;
- HEPHAISTOS may produce an artifact while IRIS blocks transmission before approval;
- ZEUS may arbitrate the status and next procedure without deciding truth by itself.

Role disagreement is allowed.

Role disagreement is review material.

Role disagreement must not become autonomous runtime chatter.

For detailed doctrine on role biases, negative powers, governed tensions, dissent statuses, proportional activation, contradiction ledgers, doubt qualification and procedural arbitration, see `GOVERNANCE_COLLEGE.md`.

## Role summaries

### ATHENA

ATHENA governs planning logic, task decomposition, workflow strategy and coordination structure.

A Hermes `athena-agent` profile may produce planning candidates, workflow decomposition candidates, Kanban card planning candidates and task contract drafts.

ATHENA does not approve final execution.

### ARGOS

ARGOS governs source research, evidence gathering, factual checking and traceability discipline.

A Hermes `argos-agent` profile may produce source research candidates, evidence candidates, traceability notes and source risk notes.

ARGOS asks what a source is, where it came from, what it supports and what is missing.

ARGOS may examine source dates and versions when they affect source identity, provenance or evidentiary value. It does not own the broader continuity question of which remembered state should be reused or retained.

ARGOS does not canonize evidence by itself.

### THEMIS

THEMIS governs risk review, policy compliance, approval boundaries and veto logic.

A Hermes `themis-agent` profile may produce risk review candidates, approval boundary notes, policy compliance notes and veto candidates.

THEMIS may identify blocking risk, but final approval remains governed by Pantheon approval policy.

### APOLLO

APOLLO governs final quality review, completeness checks, evidence sufficiency and delivery readiness.

A Hermes `apollo-agent` profile may produce quality review candidates, completeness review candidates and delivery-readiness candidates.

APOLLO does not replace required approvals.

### ZEUS

ZEUS governs arbitration when there is conflict, competing variants or unresolved disagreement between candidate outputs.

A Hermes `zeus-agent` profile may produce arbitration candidates and decision rationale candidates.

ZEUS is not a permanent orchestrator.

ZEUS arbitrates status, risk posture and next procedure.

ZEUS may arbitrate whether a memory candidate proceeds to review, is held, rejected or requires human decision. It does not perform memory promotion and does not decide truth by itself.

### IRIS

IRIS governs formulation, transmission, clarification and user-facing language adaptation.

A Hermes `iris-agent` profile may produce reformulation candidates, communication candidates and presentation candidates.

IRIS does not change the substantive decision.

IRIS does not authorize external transmission before required approval.

### HEPHAISTOS

HEPHAISTOS governs implementation preparation, patch candidates, build candidates and technical execution candidates.

A Hermes `hephaistos-agent` profile may produce patch candidates, implementation candidates and build notes under Task Contract.

HEPHAISTOS does not self-approve implementation. A Hermes execution profile may perform an exact or conditional merge only when a separate governed authorization identifies the target, effect and required checks; executing that authorized effect does not grant judgment authority.

HEPHAISTOS may produce an artifact candidate without making it deliverable.

### MNEMOSYNE

MNEMOSYNE governs memory continuity and the disciplined reuse of prior context.

Her jurisdiction includes:

- deciding which memory domain, dossier, corpus or governed record should be searched for a bounded question;
- proposing the retrieval mode appropriate to the question, such as exact terms, semantic proximity, chronology or declared relations;
- reviewing returned material for duplicate records, stale recall, indices, dates, versions, supersession and the latest applicable known state;
- distinguishing a historical record from the state that is currently reusable;
- proposing where a retained item belongs: session, Project, Agency, Sandbox, archive or Register Candidate;
- making memory impact, uncertainty and required review visible before reuse or retention.

MNEMOSYNE governs the search frame and memory judgment. She does not execute retrieval. Hermes or another admitted external executor performs the actual search or tool call under Task Contract.

MNEMOSYNE does not:

- choose or install a memory provider;
- treat runtime recall as truth or Evidence;
- widen a task beyond its admitted scope;
- silently move material between projects or memory domains;
- overwrite or delete historical records merely because they are superseded;
- promote a memory candidate into canonical or probative memory by herself.

When source authority is unclear, MNEMOSYNE consults ARGOS.
When a date, index or version changes the state that may be reused, MNEMOSYNE preserves the temporal issue and may request a version check or source review rather than guessing.
When retention, promotion or scope consequence is material, THEMIS and ZEUS govern the applicable risk and procedure, with explicit human approval where required.

## Escalation model

- Escalate to ARGOS when source identity, provenance, authority or evidentiary support is unclear.
- Escalate to MNEMOSYNE when remembered context may be stale, duplicated, superseded, wrongly scoped, or when the correct search/retention location is unclear.
- Escalate to THEMIS when risk, policy or approval boundary is unclear.
- Escalate to APOLLO when quality, completeness or evidence sufficiency is unclear.
- Escalate to ZEUS when there is conflict, variant selection, status transition or unresolved disagreement.
- Use IRIS for formatting and transmission without changing substance.

## Candidate versus canonical

Hermes done does not mean Pantheon validated.

Candidate output does not become canonical until the required approval path is complete.

A Register Candidate does not become a Registre Probatoire entry until approved through the required register-admission path.

A memory location proposed by MNEMOSYNE is not a persistence or promotion authorization.

Produced does not mean deliverable.

Clear does not mean verified.

Retrieved does not mean evidence.

Repeated does not mean memory.
