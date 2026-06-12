# AI log — Step 4: the vertical is proven end to end (Tilleuls)

Date: 2026-06-12.

## Intent

Execute step 4 of `TARGET_ARCHITECTURE.md` ("prove ONE vertical, kept
green by regression"), as instructed by the maintainer ("Go").

## What was built

- `mcp-server/examples/hermes_vertical_runner.py` — plays the Hermes side
  of the Phase 5 integration contract over the **real MCP stdio protocol**
  on the Résidence Les Tilleuls fixture (fictional VEFA surface claim):
  classify (K4/V4/C4, blocked), Task Contract candidate, explicitly
  SIMULATED execution outside Pantheon, Evidence Pack candidate **validated
  against `schemas/evidence_pack.schema.yaml`**, Register Candidate
  **validated against the E6 `register_candidate` schema**, refusal probes
  in French and English over the wire, `check_external_action` blocked by
  default, then the Hermes output envelope — and the run **stops at the
  User Decision Gate**. Exit 1 on any conformance deviation.
- `mcp-server/tests/test_vertical_e2e.py` — ASSERT-style regression that
  runs the runner as a subprocess and checks the markers plus the envelope
  structure (stopped_here, effects listed as forbidden, C4). Skips when
  the MCP SDK is absent (governance CI).
- `mcp-server/examples/README.md` — boundary: not Hermes, not a runtime;
  deterministic read-only demonstration; in a real deployment Hermes
  performs the execution step under the reviewed Task Contract.

## Verification

29 module tests green (including the e2e regression over real stdio);
runner exit 0; the four Lot 1 checks green with baseline origin/main.

## Boundary

Read-only demonstration; the execution step is simulated and fictional;
nothing sent, written, approved, promoted or scheduled; no protected path
touched. The proven vertical is a conformance fact, not a professional
validation of any content.
