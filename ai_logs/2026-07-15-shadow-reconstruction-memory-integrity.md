# Shadow reconstruction memory-integrity review

Status: validation-only intervention trace.

Date: 2026-07-15

## Human decision recorded

The maintainer approved proceeding with a bounded memory-integrity direction:
deconstruct admitted project material into atomic claims, reconstruct a separate
candidate projection and compare it with the current register projection to
surface consequential inconsistencies.

The approved boundary is non-destructive:

```text
sources remain
current register remains
shadow reconstruction stays candidate
differences route to review
the human arbitrates consequential status changes
```

The maintainer then requested a visible timing profile and action catalogue for
Pantheon Control, with every optional operational action disabled by default.
The recorded activation rule is:

```text
passive doctrine / declared-status display may remain visible
scheduled, compute, ingestion, vector, memory and notification actions start disabled
first activation is explicit and scoped
mandatory protections have no off switch during an admitted run
suspend is preferred to uninstall
```

## Placement decision

No new governance-document family or Pantheon runtime was created.

- `MEMORY.md` carries the durable integrity invariant.
- `EVIDENCE_MEMORY_DEV_PLAN.md` carries the candidate development sequence,
  discrepancy classes, cadence profiles, result shape and the default-off
  mapping to the existing external Hermes night-operations template.
- `GOVERNED_RESOURCE_DASHBOARD_MODEL.md` carries the dashboard action contract,
  separated runtime states, mandatory protections and external schedule card.
- `MODULES.md` and `WHAT_RUNS.md` expose the boundary and honest implementation
  status.
- The already-merged Pantheon Modules plugin and
  `night-operations.template.yaml` remain the single dashboard/runtime
  referent. No parallel schedule or competing dashboard page is created.
- Its Night ops cards now expose separately confirmed pause/resume, paused
  timing edit and immediate-run controls only for one observed finite Hermes
  job. Job creation/deletion and scope/command changes remain native-Cron work.
- The incremental integrity review maps to its existing
  `contradiction_drift_review` operation; full milestone reconstruction stays
  explicit and on demand.
- `docs/examples/architecture_memory_integrity_review/` provides the explicit
  fictional architecture referent.
- The existing authority-index row is clarified; no authority class changes.

## Runtime boundary

```text
exposed_by: OpenWebUI or another governed review surface
executed_by: Hermes or another external execution runtime
governed_by: Pantheon register, evidence, scope and approval rules
approved_by: human reviewer for consequential status change
forbidden: destructive rebuild, automatic promotion, automatic semantic merge,
  automatic supersession or revocation, cross-project reconstruction, scheduler
  inside Pantheon
```

## Repository status

Documented non-implemented.

No schema, test, MCP server, reconstruction worker, diff engine, vector store,
memory backend, scheduler, register mutation or automatic discrepancy
resolution was added. Existing external night-operation entries remain absent
or inactive until an operator configures a finite, scoped Hermes trial.

## Validation

Executed from a clean clone of `main` after the documentation patch:

```text
root pytest: 20 passed
mcp-server unittest: 145 passed
Governance Doctor: pass; 6/6 checks; 552/552 items evaluated
status-header guard: pass against origin/main
internal-link guard: pass against origin/main
authority-index coverage guard: pass against origin/main
axis-vocabulary guard: pass against origin/main
obsolete-authority consistency guard: pass against origin/main
long-document truncation guard: pass
packaging contract guard: pass
git diff --check: pass
```

A separate full-tree obsolete-authority scan reported the pre-existing
`docs/governance/rites/_TEMPLATE_RITE.md` status-template finding. The CI-aligned
diff-scoped check against `origin/main` passes and this patch does not touch that
file or introduce a new retired-document inconsistency.
