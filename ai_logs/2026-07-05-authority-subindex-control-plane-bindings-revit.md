# AI log — Authority sub-index rows for control plane, Hermes bindings and Revit sandbox

Date: 2026-07-05

Repository: `ifanjuang/Pantheon-Next`

## Summary

Follow-up to:

```text
ai_logs/2026-07-05-control-plane-bindings-revit-sandbox.md
```

Added authority visibility rows for the three new governance files using the decomposed Authority Index structure.

Updated:

```text
docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md
docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md
docs/governance/authority/ARCHITECTURE_AUTHORITY_INDEX.md
```

No row was added to the master `docs/governance/AUTHORITY_INDEX.md`, because the master already delegates detailed rows to the registered sub-indexes.

## Rows added

### Governance kernel sub-index

```text
docs/governance/PANTHEON_CONTROL_PLANE_BOUNDARY.md
```

Classification:

```text
authority_class: candidate support doctrine
repo_state: documented non-implemented
```

Reason:

```text
The file defines a bounded control-plane exception and status vocabulary. It is governance-kernel material because it clarifies the relation between governed operational state and execution runtime without becoming runtime.
```

### Runtime adapters sub-index

```text
docs/governance/HERMES_CAPABILITY_BINDINGS.md
```

Classification:

```text
authority_class: candidate support doctrine
repo_state: documented non-implemented
```

Reason:

```text
The file lists tool/product bindings for Hermes capability slots. It belongs in runtime adapters because product names are intentionally kept out of generic doctrine and placed in bindings/adapters/integration notes.
```

### Architecture sub-index

```text
docs/governance/PANTHEON_REVIT_LOCAL_SANDBOX_EXCEPTION.md
```

Classification:

```text
authority_class: candidate support doctrine
repo_state: documented non-implemented
```

Reason:

```text
The file is a Revit / architecture-domain local sandbox exception. It refines the existing Pantheon Revit Gate posture without implementing a plugin or changing production governance.
```

## Decision classification

Accepted:

```text
Use the decomposed sub-indexes for detailed rows.
Keep the master index as authority interpreter only.
Index the three new files without promoting them.
Keep all rows documented non-implemented.
```

Refused:

```text
No master-index bloat.
No authority-class promotion.
No runtime implementation.
No schema/test/operations/platform/Docker/.env change.
No Revit plugin implementation.
No Hermes implementation.
```

To verify:

```text
Whether the coverage checker passes after sub-index updates.
Whether a future `HERMES_CAPABILITY_INSTALLER_BOUNDARY.md` should also live in runtime adapters.
Whether Notion card should be updated to mark indexation complete.
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
partial: authority visibility only
to_verify: checker result and future installer-boundary decision
```
