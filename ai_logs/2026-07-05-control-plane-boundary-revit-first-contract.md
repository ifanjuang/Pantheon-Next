# AI log — Control-plane hardening and Revit first sandbox contract

Date: 2026-07-05

Repository: `ifanjuang/Pantheon-Next`

## Summary

Performed the requested A + C follow-up:

```text
A — verify / harden the control-plane boundary relation.
C — define the first Revit sandbox action contract.
```

Changed files:

```text
docs/governance/PANTHEON_CONTROL_PLANE_BOUNDARY.md
docs/governance/PANTHEON_REVIT_FIRST_SANDBOX_ACTION_CONTRACT.md
docs/governance/authority/ARCHITECTURE_AUTHORITY_INDEX.md
```

Added this ai_log:

```text
ai_logs/2026-07-05-control-plane-boundary-revit-first-contract.md
```

## A — control-plane hardening

Updated `PANTHEON_CONTROL_PLANE_BOUNDARY.md` to clarify the relationship with the older slim dashboard boundary:

```text
PANTHEON_CONTROL_BOUNDARY.md
= dashboard / verification surface boundary.

PANTHEON_CONTROL_PLANE_BOUNDARY.md
= generic operational control-plane doctrine.
```

The update preserves the distinction:

```text
The dashboard may verify liveness, logs and install visibility.
The control-plane doctrine defines status vocabulary and handoff posture.
Neither grants Docker socket access, repository write access, credentials, runtime authority, approval authority or memory authority.
```

Any conflict must route through `AUTHORITY_INDEX.md`.

## C — first Revit sandbox action contract

Added:

```text
docs/governance/PANTHEON_REVIT_FIRST_SANDBOX_ACTION_CONTRACT.md
```

The first loop is:

```text
context pack
-> method candidate
-> light confirmation
-> write_light action
-> action log
-> action report candidate
```

Scope:

```text
Sandbox libre only
local disposable RVT file or explicit sandbox copy
architecture only
read_only / candidate_only / write_light / log / local export only
```

Explicitly blocked:

```text
write_model
external_effect
save
sync
purge
delete
linked-model write
family load into production
arbitrary generated code execution
MCP exposure
hidden scheduler
hidden queue
memory promotion
professional validation
```

Recommended first write action:

```text
create_text_note
```

Fallback first write action:

```text
create_detail_line
```

Optional helper action:

```text
create_sandbox_view
```

## Authority index

Updated the architecture sub-index:

```text
docs/governance/authority/ARCHITECTURE_AUTHORITY_INDEX.md
```

Added row:

```text
docs/governance/PANTHEON_REVIT_FIRST_SANDBOX_ACTION_CONTRACT.md
```

Classification:

```text
authority_class: candidate support doctrine
repo_state: documented non-implemented
```

## Checked context

Relevant current files checked before/during work:

```text
docs/governance/PANTHEON_CONTROL_BOUNDARY.md
docs/governance/PANTHEON_CONTROL_PLANE_BOUNDARY.md
docs/governance/PANTHEON_REVIT_LOCAL_SANDBOX_EXCEPTION.md
docs/governance/authority/ARCHITECTURE_AUTHORITY_INDEX.md
.github/scripts/check_index_coverage.py
```

The checker script confirms that registered sub-index table rows extend authority coverage and that prose mentions do not count as indexing.

## Decision classification

Accepted:

```text
Clarify boundary relation instead of merging files.
Keep dashboard boundary and generic control-plane doctrine separate.
Define one first Revit action contract instead of widening the whole tool surface.
Use `write_light` as the first Revit executable-effect ceiling.
Index the new Revit contract in the architecture sub-index.
```

Refused:

```text
No schema.
No test.
No plugin.
No Revit add-in.
No C# project.
No MCP server.
No local relay.
No runtime worker.
No Docker / operations / platform change.
No production profile.
No save / sync / purge / delete.
No write_model.
No automatic memory promotion.
No professional validation by runtime success.
```

To verify:

```text
Run `.github/scripts/check_index_coverage.py` in a real checkout or CI.
Decide whether the first contract should later produce non-executable templates under `templates/hermes/`.
Decide whether a future protected schema package is needed after observed Revit sandbox use.
```

## Protected paths

```text
schemas/: no
tests/: no
operations/: no
platform/: no
Docker: no
.env: no
runtime code: no
Hermes implementation: no
OpenWebUI implementation: no
Revit plugin implementation: no
```

## Repo state

```text
implemented: no
documented_non_implemented: yes
partial: first Revit contract documented and indexed only
to_verify: CI/checker result and later template/schema promotion
```
