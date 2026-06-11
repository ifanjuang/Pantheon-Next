# AI log — mcp-server Phases 5-6: review and fixes

Date: 2026-06-12.

## Intent

Review the ChatGPT-track Phase 5-6 work on `chatgpt/mcp-p5-p6` (built on
the #102 first slice), fix what the review found, and prepare the branch
for merge, per the maintainer's instruction.

## Review findings and fixes

- The branch added `contracts.py` (candidate skeleton tools), the Hermes
  integration contract, 9 development fixtures and the collective-housing
  vertical (Résidence Les Tilleuls), but **no tests** for any of it.
  Added `mcp-server/tests/test_phase5_6.py`: fixture-driven coverage
  (skeleton invariants, forbidden-language scan, sequence conformance,
  housing vertical K4/V4/C4, refusal cases, all base fixtures).
- The refusal posture only matched **English** action words; the housing
  fixture's refusal cases are in French ("envoyer un courrier",
  "promouvoir en mémoire") and were not refused. Added French/English
  word-boundary patterns mapped to the same refused effects.
- The C4 escalation only applied to explicit flags; a K4 reached through
  the professional-position lexicon stayed C3, contradicting the fixture
  and the branch's own commit intent. K4-by-lexicon now escalates to C4.
- A documentary-authority contradiction and a register-candidate proposal
  classified as K2; both are evidence-class. Added the missing K3
  triggers and a structural rule: a request carrying
  `register_candidates` is K3 minimum.
- Merged current `main` into the branch (Lot 1 CI checks present).

## Verification

24 tests green; 8 tools / 20 resources over the SDK; the four Lot 1
checks and both legacy lints green with baseline `origin/main`.

## Boundary

Read-only module work; no protected path touched; everything remains
candidate until reviewed.
