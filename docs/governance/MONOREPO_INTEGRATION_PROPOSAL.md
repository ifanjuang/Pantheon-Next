# Monorepo Integration Proposal — MCP server and verification dashboard in-repo

Status: validation-only proposal — doctrine amendment. Requires explicit approval before the modules are built. It changes the founding boundary in `CLAUDE.md`; it adds no module code.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Intent

The maintainer wants two surfaces to live inside the Pantheon Next repository:

- an **MCP server** as the simplest, standard way to connect the governance to **Hermes Agent** (and OpenWebUI);
- a **dashboard** whose purpose is to **verify that Pantheon Next is correctly installed and answering** (liveness / health), including on a NAS.

Both are useful and, scoped this way, both are *read-only verification or candidate-preparation surfaces* — not a runtime. This proposal records the boundary that lets them live in-repo without Pantheon Next becoming the agent runtime its doctrine forbids.

## The decision taken

```text
Structure: monorepo with a hard internal boundary (not a separate repo, not a full fusion).
Doctrine:  amend CLAUDE.md first, before any module code.
```

Boundary validated by the maintainer (2026-06-09), with scope refinements:

```text
- no runtime anywhere; both modules stay light.
- dashboard: verify installs from their LOGS, view evidence logs, and prepare
  proposed evidence-log edits; every edit is a governed candidate through the
  chokepoint, never a direct write.
- mcp-server: centered on the capability passport (serve/validate passports,
  scope and approval checks, return the policy decision as data).
```

## The boundary

```text
governance core  doctrine, schemas, validation, read-only checks. Pure.
                 Depends on nothing in the other zones.
mcp-server/      read-only policy / validation MCP surface. Connection point to Hermes.
                 Depends on the core. Never the reverse.
dashboard/       thin install + liveness verification surface. Shows state. Decides nothing.
                 Depends on the core. Never the reverse.
```

One-way dependency. The boundary moves from the repo edge to the module edge: Pantheon still **governs and does not execute**. Exposure (MCP) and verification (dashboard) are modules around the core, not inside it.

## What each module may and may not do

### `mcp-server/` — centered on the capability passport

```text
MAY  serve and validate capability passports; expose governance doctrine and
     read-only checks as MCP resources/prompts/tools; check scope, check approval
     ceiling, run doctor checks, return a policy decision as data, prepare candidates.
MUST NOT execute a capability, route an LLM provider, send to an external party,
     schedule, queue, or promote memory. It returns decisions; it never enforces them.
```

The passport is the unit of work: each capability carries one (data), the MCP server reads it, checks it and returns a decision. Hermes Agent is the consumer (the enforcement point) and speaks to it over a standard protocol — which is why it is the simplest connection path.

### `dashboard/` — light, log-based verification + evidence-log proposal surface

```text
MAY  verify installs from their LOGS and check liveness (is it installed, does it
     answer, are the checks green), including a NAS view;
     view the evidence logs (Registre Probatoire) organized by scope/project;
     prepare a proposed evidence-log edit — but the proposal is a governed
     CANDIDATE that routes through the chokepoint and the User Decision Gate
     before it lands.
MUST NOT become a heavy admin dashboard, an automatic skill installer, an
     orchestrator, an approval engine or any runtime. It writes no evidence directly
     and bypasses no gate. It shows and proposes; the gate decides.
```

This is the `installed != connected != authorized != validated` distinction made visible, plus a governed proposal surface over the Registre Probatoire. Viewing is read-only; editing is a candidate proposal through the chokepoint — so the dashboard still decides nothing.

## CLAUDE.md amendment (this PR)

```text
- Doctrine: the GOVERNANCE CORE (not "Pantheon Next" as a whole) must not become a runtime;
  the repo may host the two bounded modules.
- New section "Repository structure (monorepo with hard boundary)": the three zones and the
  one-way dependency rule.
- Non-negotiable boundaries: the forbidden runtime list now scopes to the governance core;
  "heavy dashboard" and "automatic skill installer" become constraints on the dashboard
  module (what it must not grow into), not a blanket ban on having a dashboard.
- Repository migration policy: the modules are new bounded code, not bulk-copied runtime.
```

The chokepoint rule is unchanged: a consequential effect still routes through the governance check; no module bypasses it.

## What this proposal does NOT do

```text
No mcp-server/ or dashboard/ code, scaffold, package, Docker stack, .env or installer is added.
No schema, test or other protected path is changed.
The modules are built only after this doctrine amendment is approved.
```

## Approval checklist

```text
[ ] confirm monorepo with hard one-way boundary (not separate repo, not full fusion)
[ ] confirm the governance core stays pure (depends on neither module)
[ ] confirm mcp-server/ is read-only / validation only (no execution, routing, sending, promotion)
[ ] confirm dashboard/ is install + liveness verification and evidence-edit proposal only (no heavy dashboard, no auto-installer)
[ ] approve the CLAUDE.md amendment in this PR
[ ] only then: a separate PR may scaffold the modules under the boundary
```

## Current repo state

Documented non-implemented. The doctrine amendment is proposed in this PR (draft until approved). No module code exists. Built only after approval, under the boundary above.
