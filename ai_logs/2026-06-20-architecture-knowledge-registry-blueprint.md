# 2026-06-20 architecture knowledge registry blueprint

Status: documented non-implemented (candidate doctrine).

Created the architecture knowledge registry blueprint, resolving arbitration
item C ("Knowledge registry location") of
`docs/governance/ARCHITECTURE_OS_RECONCILIATION.md`, whose recommendation was
"blueprint in Pantheon, runnable mapping outside Pantheon". This also turns the
previously dangling reference at OS_RECONCILIATION:457 into a live document.

Added:

- `docs/governance/ARCHITECTURE_KNOWLEDGE_REGISTRY_BLUEPRINT.md`: documentation-
  only blueprint for how an architecture practice registers reusable knowledge
  (regulations, agency standards, construction details, lessons learned, supplier
  data, precedents) as governed entries, reusing `source_authority_level`,
  `proof_status` / `approval_state` and the shared scope vocabulary; the runnable
  mapping stays outside Pantheon (templates / external adapters);
- `docs/governance/AUTHORITY_INDEX.md`: index row for the new blueprint.

Boundary: no registry runtime, ingestion pipeline, OCR, vector/graph backend,
embedding store, retrieval service or external connector. Entries remain
candidates until reviewed; promotion is a governed human decision.

Scope note: I investigated the other pre-existing axis-vocabulary findings
(`confidence` fields in `evidence_pack` and `role_signal`, `approval_impact: C3`)
and deliberately left them unchanged — the `evidence_pack` `confidence` is
intentional per the schemas/README D3 note, and the `approval_impact: C3`
findings are linter false positives (correct use of the C approval axis). Only
the genuine, additive fix (this blueprint) was made.
