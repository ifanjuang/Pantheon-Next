# AI Log — Modular domain reorientation reconciliation

Date: 2026-05-31

## Scope

Reconciled `MODULAR_DOMAIN_REORIENTATION.md` per Issue #25 and indexed the orphan
governance documents that had been added to `main` without being placed in the read
path. Consolidated onto the open PR branch (`claude/review-recent-changes-flSzY`,
PR #26) so that a single change touches the governance index files, avoiding
divergent edits to `STATUS.md`, `README.md`, `MODULES.md` and `CORE_CONCEPTS_MAP.md`.

This follows the agreed role split during review: Claude reconciles and indexes;
content creation and the AgentOS distillation (Issue #27) remain elsewhere.

## Files changed

Changed:

- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md` (abstraction of product names,
  manifest status reconciliation with `MODULE_ACTIVATION.md`, hierarchy note,
  domain-pack-not-module clarification, bindings/adapters exception);
- `docs/governance/ADAPTERS_AND_BINDINGS.md` (bindings/adapters exception note);
- `docs/governance/STATUS.md`, `docs/governance/README.md`,
  `docs/governance/MODULES.md`, `docs/governance/CORE_CONCEPTS_MAP.md` (indexing);
- `CHANGELOG.md` (0.1.23 entry).

Added:

- `ai_logs/2026-05-31-modular-domain-reorientation-reconciliation.md`.

This branch also carries the previously committed `ADAPTERS_AND_BINDINGS.md`
(0.1.22) and a merge of the current `main`.

## Why the change was made

Issue #25 recorded that `MODULAR_DOMAIN_REORIENTATION.md` was active but invisible
in the read path, still named products outside the bindings registry, compressed the
manifest status against `MODULE_ACTIVATION.md`, and risked making a domain pack look
like a runtime module. Separately, `main` had received several governance documents
(architecture agency domain pack, knowledge ingestion and memory, workflow lifecycle,
data platform) that were not indexed.

The reconciliation answers Issue #25's four questions:

1. Keep the stricter bindings rule, with an explicit exception for integration and
   adapter documents.
2. Make `status` documentary only; `activation` (state and scope) and
   `task_authorization` become separate axes, with the vocabulary owned by
   `MODULE_ACTIVATION.md`.
3. Index the reorientation in the read path and read it in orientation before
   capability, domain or module placement work.
4. Frame the domain pack as a governed methodology configuration, not a runtime
   module.

## Governance boundary

Documentation and indexing only.

It does not implement a runtime, a bridge, a plugin manager, a skill installer, a
module registry runtime, an executable schema, automatic approval or automatic
memory promotion.

The `DATA_PLATFORM_*` documents are indexed with a `to verify` status. Indexing does
not endorse them as canonical. A data platform must not become a Pantheon runtime,
so they remain pending a boundary review against `CLAUDE.md`.

AgentOS distillation (Issue #27) is intentionally out of scope.

## Explicit non-implementation

No files were touched under:

```text
schemas/
tests/
operations/
platform/
Docker
.env
pyproject.toml
CLAUDE.md
```

## Boundary phrase

```text
Pantheon defines the contract.
The tools carry the work.
The validated remains.
```
