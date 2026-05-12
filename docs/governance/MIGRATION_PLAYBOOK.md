# Migration Playbook (Phase C)

Status: canonical — Phase C migration doctrine.

This document is the canonical playbook for migrating governance Markdown from `ifanjuang/Pantheon-OS` into the existing stubs of `ifanjuang/Pantheon-Next` during Phase C.

## Doctrine

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

Pantheon Next is governance-first.

Migration must not reintroduce execution runtime, scheduler, queue, message bus, provider router, automatic memory promotion, automatic Hermes installation or automatic skill installation.

## Scope

Phase C migrates governance Markdown only.

Phase C does not migrate code, schemas, tests, operations tooling, runtime configuration, Docker files or environment files. Those phases come later under separate plans.

## Source of truth

Pantheon-OS is the historical source repository.

For Phase C, a single SHA snapshot of `ifanjuang/Pantheon-OS@main` is taken at the start of Phase C and recorded in `ai_logs/migration-mapping.md`. All migration PRs reference that single snapshot SHA. Later OS evolution is out of scope for Phase C and is handled as delta PRs after Phase C completes.

## Access channel

The chosen channel is **C-1**: `ifanjuang/Pantheon-OS` is added as a read-only repository to the Claude session permissions. Claude reads OS source files directly via the GitHub MCP tools. Claude does not push to Pantheon-OS.

If C-1 is not yet active when a migration PR begins, the migration waits. Migration content is never pasted blind without the snapshot SHA.

## Per-PR ritual

```
1. Identify the OS source file and confirm the snapshot SHA
2. Read the OS source fully
3. Apply the doctrinal filter (see below)
4. Diff: stub → migrated content
5. Verify the per-PR invariants (see below)
6. Cross-check every Markdown link
7. Write the ai_log with OS source path, OS SHA, transformations applied
8. Push a branch claude/migrate-<FILE>
9. Open a PR draft
10. Owner reviews and merges
11. ChatGPT reconciles STATUS, index and CHANGELOG after merge
```

One PR migrates exactly one stub. Migrations are never grouped.

## Doctrinal filter

Apply line by line during the diff. If a line matches any pattern below, transform or remove before it lands in Pantheon-Next.

| Pattern in OS source | Action in Pantheon-Next |
|---|---|
| runtime, scheduler, queue, message bus, provider router, installer | reformulate as policy or remove |
| version, endpoint, port, environment variable, Docker path, command | generalize or remove; mark `À vérifier` if truly version-dependent |
| renamed term: Authorities, Capability Contracts, HEPHAESTUS | rewrite using Pantheon Next vocabulary (Pantheon Role, Pantheon Skill, HEPHAISTOS) |
| central orchestrator assumption inside Pantheon | reformulate as Hermes-side execution or remove |
| auto-promotion memory, auto-merge, auto-installer, self-evolution | invert with the explicit Pantheon Next decision; record the reversal in the ai_log |
| diagrams, images, assets | defer to Lot 8; not migrated alongside doctrine |

## Per-PR invariants

A migration PR is valid only if every invariant holds.

- The `Status: stub — Non implémenté — à migrer depuis Pantheon-OS` header is replaced by `Status: migrated from Pantheon-OS @ <SHA>`.
- No Python code, YAML schema, Dockerfile, environment file or installation script appears in the diff.
- No file is added or modified under `schemas/`, `tests/`, `operations/`, `platform/`, repository root, `pyproject.toml`, `.env*`, `docker*`.
- Every Markdown link resolves to an existing file in Pantheon-Next.
- No simultaneous modification of `STATUS.md`, `ROADMAP.md`, `CHANGELOG.md`, root `README.md` or `docs/governance/README.md`. ChatGPT reconciles those after merge.
- The migrated doc does not contradict any already-migrated Pantheon-Next doctrine document.
- Document length stays around three hundred lines or less. Longer source content is condensed by default.
- The ai_log cites OS source path, OS SHA and lists every doctrinal transformation applied.
- HEPHAISTOS canonical spelling enforced. HEPHAESTUS appears only as an explicit non-canonical warning if needed.

## Arbitration rules (D1 to D6)

The following rules are canonical for Phase C.

### D1 — OS doc better than current Next doctrine

If the OS source carries content that is genuinely better than the existing Pantheon-Next doctrine, the migration PR does not silently integrate the improvement. The improvement is first proposed as a separate Pantheon-Next doctrine update for arbitration. Migration resumes only after the doctrine update is decided.

### D2 — Obsolete or contradictory OS doc

If the OS source is obsolete or directly contradicts Pantheon-Next doctrine, the default action is not to migrate. The corresponding stub is closed with status `Voluntarily not migrated` and a short justification is recorded in the ai_log. Canonizing a contradiction is forbidden.

### D3 — Oversized OS doc

If the OS source exceeds the per-doc length guideline, the default action is to condense. Splitting into multiple Pantheon-Next Markdown files is allowed only if condensation would destroy doctrine integrity or produce an unreadable document. The split decision is recorded in the ai_log.

### D4 — Broken link to a moved or removed file

If the OS source references a file that has moved or been removed between OS and Next, the migration PR fixes the link and records a migration note in the ai_log explaining the redirect. Silent rewrites are forbidden.

### D5 — Pantheon-OS drift during Phase C

A single OS SHA snapshot is taken at the start of Phase C. Later OS evolution is ignored during Phase C. Delta migrations against newer OS SHAs are handled in a separate post-Phase-C pass.

### D6 — Diagrams and images

Diagrams and images are deferred to Lot 8. They are not migrated inline with doctrine content. Lot 8 will produce `docs/assets/` content under a dedicated review pass.

## Special rule for GLOSSARY in Lot 1

Pantheon Next already has an active `GLOSSARY.md`. During Lot 1, the OS source for the glossary is compared against the Next version. The migration PR touches `GLOSSARY.md` only if the OS diff brings real terminological clarification that is missing from Next.

If no real clarification is added, the migration PR records a `no-op` decision in the ai_log and does not modify `GLOSSARY.md`.

## Sequencing — 8 lots

```
Lot 1 — Foundations
  ARCHITECTURE.md, MODULES.md, GLOSSARY (compare only)

Lot 2 — Contracts and evidence
  APPROVALS.md, TASK_CONTRACTS.md, TASK_CONTRACT_REVISIONS.md, EVIDENCE_PACK.md

Lot 3 — Memory and knowledge
  MEMORY.md, MEMORY_EVENT_SCHEMA.md, KNOWLEDGE_TAXONOMY.md,
  EPISTEMIC_CONTROL.md, EPISTEMIC_CONTROL_PROPAGATION.md

Lot 4 — Workflows and signals
  ROLE_SIGNALS.md, ROLE_SIGNAL_PROFILES.md,
  WORKFLOW_SCHEMA.md, WORKFLOW_ADAPTATION.md,
  RUN_GRAPH.md, REQUEST_ORCHESTRATION.md, EXECUTION_DISCIPLINE.md

Lot 5 — Routing
  ROUTING_FOUNDATION.md, MODEL_ROUTING_POLICY.md

Lot 6 — Integrations
  HERMES_INTEGRATION.md, OPENWEBUI_INTEGRATION.md,
  OPENWEBUI_DOMAIN_MAPPING.md, OPENWEBUI_PLUGIN_POLICY.md

Lot 7 — External and audit
  EXTERNAL_TOOLS_POLICY.md, EXTERNAL_RUNTIME_OPTIONS.md,
  CODE_AUDIT_POST_PIVOT.md, SKILL_LIFECYCLE.md

Lot 8 — Assets
  docs/assets/README.md and migrated assets
```

A lot is not a single PR. A lot is a group of migrations whose ordering is suggested. Each file inside a lot is a separate PR.

## Coordination with Phase D (schemas)

Phase D has already started in parallel on `schemas/`.

- Claude operates on `docs/governance/*.md` for Phase C migration PRs.
- ChatGPT operates on `schemas/*` for Phase D PRs.
- No file overlap between Phase C and Phase D PRs.
- Claude does not touch `schemas/`, `tests/`, `operations/`, `platform/`, Docker, `.env*`, `pyproject.toml`, `CLAUDE.md`.
- ChatGPT does not touch `docs/governance/*.md` during Phase C migration PRs except for the post-merge reconciliation explicitly requested by Claude or the doctrine owner.

Schemas that include a `governance_refs` field must resolve to migrated Pantheon-Next docs or to explicit stubs. This is checked at each Phase D schema PR, not at each Phase C migration PR.

## Migration mapping

A dedicated file tracks the migration:

```text
ai_logs/migration-mapping.md
```

The mapping records, for each governance file:

- Pantheon-Next path;
- Pantheon-OS source path;
- Pantheon-OS SHA at migration time;
- Phase C lot;
- migration PR number;
- status: `pending`, `migrated`, `voluntarily not migrated`, `condensed`, `split into <files>`;
- short note on doctrinal transformations applied.

The mapping is initialized in the first Phase C migration PR and updated incrementally.

## Critère d'arrêt for Phase C

Phase C is complete when all of the following hold.

- No `docs/governance/*.md` file retains the `Status: stub` header.
- `STATUS.md` shows no entries under `Stub present — non implemented` other than entries explicitly marked `Voluntarily not migrated`.
- The governance index `docs/governance/README.md` shows no `Documents referenced but absent` section other than entries explicitly deferred.
- `ai_logs/migration-mapping.md` is complete and reflects every migrated, condensed, split or voluntarily not migrated entry.
- `CHANGELOG.md` records a Phase C closure section, normally tagged `0.2.0`.

After Phase C closure, Phase D (already running) and Phase E (operations tooling) may proceed without documentation debt.

## Anti-runtime reminder

Phase C migrates doctrine, not behavior. Phase C does not introduce a runtime, a scheduler, a queue, a message bus, a provider router, an installer, an endpoint, a Docker stack, a schema, a test or operations tooling. Any migration PR that introduces such content must be rejected and rewritten.

Pantheon Next governs.

Hermes Agent executes.

OpenWebUI exposes.
