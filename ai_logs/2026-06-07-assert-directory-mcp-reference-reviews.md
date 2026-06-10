# AI log — Reference reviews: ASSERT and directory-mcp

Date: 2026-06-07.

## Intent

The maintainer asked whether two external projects are useful and good to draw
inspiration from:

- `https://github.com/responsibleai/ASSERT` — spec-driven evaluation and
  regression-testing framework with LLM-judge scoring grounded in traces;
- `https://github.com/ePaint/directory-mcp` — local MCP server holding a
  graph directory of entities, anchors, relations and sourced observations.

## Assessment

Both are useful as patterns, neither as a Pantheon component.

- **ASSERT**: distill the spec-to-executable-check and trace-grounded regression
  patterns; they realize the accepted keeper "regression review for governance
  behavior" and could keep a proven vertical non-regressive. Boundary: an
  LLM-judge verdict is a review signal, never truth, certainty (E0–E4), evidence
  or approval (C0–C5). Place it on the Hermès side under Task Contract.
- **directory-mcp**: distill the graph schema (Entities / Anchors / Edges /
  Observations / Interactions) as the actor layer of the Registre Probatoire —
  Observations as sourced facts map onto the evidence-with-citation posture, and
  Anchors separate identity from channel. The tool itself is a write-capable
  runtime memory, so it stays a Hermès-side identity directory under an MCP
  capability passport; its Observations enter the register as Evidence
  Candidates, never as canon or approval. It also illustrates the memory
  decision: a directory is operational recall, hence Hermès-owned.

## What was produced

- `docs/governance/reference_reviews/ASSERT.md`;
- `docs/governance/reference_reviews/DIRECTORY_MCP.md`;
- two rows in `docs/governance/reference_reviews/README.md`.

## Boundary

Reference reviews only. No dependency added, no installation approved, no
runtime, MCP server, evaluation backend, memory engine, schema, test or
protected-path change. Both projects are young; distill the pattern, do not
depend on the tool.
