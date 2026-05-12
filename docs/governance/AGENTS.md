# Pantheon Roles

Pantheon Roles are canonical governance roles.

They are not executable agents.
They are not runtime profiles.
They do not install tools.
They do not execute tasks directly.

Hermes profiles may be aligned with Pantheon Roles, but they remain execution profiles and produce candidates only.

## Doctrine

OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.

## Canonical rule

This document is the canonical role registry for Pantheon Next.

Hermes profile files under `hermes/profiles/` may reference this document, but they must not redefine Pantheon Role authority.

If a Hermes profile conflicts with this document, this document wins.

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

## Universal role constraints

Pantheon Roles may govern through documented policies, approvals and evidence requirements.

Hermes profiles aligned to Pantheon Roles may execute under Task Contract.

Hermes profiles must not:

- approve final actions;
- canonize workflows;
- promote memory;
- mutate doctrine;
- merge code directly;
- bypass approvals;
- become source of truth;
- silently ignore missing capabilities.

## Role summaries

### ATHENA

ATHENA governs planning logic, task decomposition, workflow strategy and coordination structure.

A Hermes `athena-agent` profile may produce planning candidates, workflow decomposition candidates, Kanban card planning candidates and task contract drafts.

ATHENA does not approve final execution.

### ARGOS

ARGOS governs source research, evidence gathering, factual checking and traceability discipline.

A Hermes `argos-agent` profile may produce source research candidates, evidence candidates, traceability notes and source risk notes.

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

### IRIS

IRIS governs formulation, transmission, clarification and user-facing language adaptation.

A Hermes `iris-agent` profile may produce reformulation candidates, communication candidates and presentation candidates.

IRIS does not change the substantive decision.

### HEPHAISTOS

HEPHAISTOS governs implementation preparation, patch candidates, build candidates and technical execution candidates.

A Hermes `hephaistos-agent` profile may produce patch candidates, implementation candidates and build notes under Task Contract.

HEPHAISTOS does not merge directly and does not self-approve implementation.

## Escalation model

- Escalate to THEMIS when risk, policy or approval boundary is unclear.
- Escalate to APOLLO when quality, completeness or evidence sufficiency is unclear.
- Escalate to ZEUS when there is conflict, variant selection or unresolved disagreement.
- Use IRIS for formatting and transmission without changing substance.

## Candidate versus canonical

Hermes done does not mean Pantheon validated.

Candidate output does not become canonical until the required approval path is complete.

Memory candidate does not become canonical memory until approved under memory policy.
