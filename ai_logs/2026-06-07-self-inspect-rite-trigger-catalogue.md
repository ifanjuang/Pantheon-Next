# AI log — self-inspect-mcp review and the Rite Trigger Catalogue

Date: 2026-06-07.

## Intent

The maintainer asked whether `https://github.com/ejentum/self-inspect-mcp` is
useful to improve Pantheon, then asked to capture the review and sketch the rite
catalogue it suggests.

## Assessment

self-inspect-mcp is the most directly relevant of the recent references. Its
founding premise — an agent cannot reliably self-correct using its own reasoning
— is Pantheon's own thesis, and its "attention failures" map almost one-to-one
onto existing rites (PREMISSES_CACHEES, AUTOCRITIQUE_CONTRADICTOIRE,
CONCORDANCE_DES_SOURCES, MÈTIS / the cap, RITE_SELECTION_MATRIX).

The useful distillation is its mechanism: a deterministic, no-LLM,
drift-verified `signal -> question` (metathought) catalogue that returns a
question, never a verdict. This shows how to move the rites from prose to a
compact, auditable, owned spec served read-only by an external surface — which
fits Pantheon's Phase 4 (read-only checks) and the MCP_POLICY_SERVER_CANDIDATE
validation-only resource idea.

## What was produced

- `docs/governance/reference_reviews/SELF_INSPECT_MCP.md` — the reference review
  (distill the metathought pattern; forbidden self-correction-loop / runtime
  import; question is never approval or proof).
- `docs/governance/rites/RITE_TRIGGER_CATALOGUE.md` — a candidate direction that
  proposes the `signal -> metathought question` catalogue shape, a starter table
  mapped to existing rites, and an execution target for the executor
  (deterministic, owned spec, drift-verified, question-only, no auto-trigger).
- Index rows in `reference_reviews/README.md` and `rites/README.md`.

## Boundary

Reference review and candidate direction only. No dependency, no installation,
no runtime, MCP server, classifier, trigger engine, schema, test, served surface
or protected-path change. The catalogue auto-triggers nothing; a signal suggests
a question, ZEUS decides whether a rite follows, the rite budget and
anti-chaining rules still apply, and nothing here promotes memory or approves.
