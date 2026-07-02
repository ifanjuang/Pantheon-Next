# AI log — governed vertical slice architecture_devis_reprise (B-3 phase 1)

Date: 2026-07-02.

Actor: Claude Code.

## Intent

Arbitration B-3 (accepted strongly): prove the vertical, without turning Pantheon
into a runtime. Phase 1 (this change) delivers the part Pantheon can own and
machine-check: a schema-valid, end-to-end **governed dossier** exercising the whole
spine, a read-only doctor check, and a runbook specifying the external wiring. The
actual OpenWebUI/Hermes execution is phase 2 and lives outside the repo. Data is
fictional; base_metier is not used (its licence is unresolved).

## Change

- `docs/examples/vertical_devis_reprise/` — six spine instances (task contract,
  forged workflow manifest with two gates and signed capability_steps, gate-1 policy
  decision, evidence pack, answer status V2/E2/K3, project-scoped register candidate),
  each validated against its real schema; a `README.md` and a `RUNBOOK.md` (the latter
  under `docs/`, not the protected `operations/`).
- `mcp-server/pantheon_mcp/doctor.py` — `check_vertical_slice` (read-only): validates
  each instance and the coherence invariants (register scoped to a project; required
  evidence gate carries V and E; answer status references the dossier evidence pack and
  register candidate). Added to `run_all`.
- `.github/scripts/check_vertical_slice.py` + a `Vertical slice validation` CI step
  (imports the doctor — single source of truth).
- `mcp-server/tests/test_vertical_slice_doctor.py`.

## Validation

`check_vertical_slice` → 6 instances valid, coherent. mcp-server tests green.
Schema validation of every instance passes. The doctor flags and cites; it executes,
routes, approves and promotes nothing.

## Boundary

Governance loop proven end to end and machine-checked; the runtime (Hermes,
OpenWebUI) remains external. No forge engine, dispatch, scheduling or memory
promotion. A forged manifest is a candidate; `forged != authorized`.
