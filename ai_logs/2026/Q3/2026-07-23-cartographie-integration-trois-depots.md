# 2026-07-23 — Cartographie d'intégration des trois zones (Next / MCP / MVP)

Status: validation-only intervention trace.
Boundary profile: validation_only_trace.

## Change

New read-only audit added at `docs/audits/2026-07-23-cartographie-integration-trois-depots.md`. It maps, capability by capability, what is implemented, partial, documented-non-implemented, candidate or voluntarily absent across the governance core, the `mcp-server/` policy surface and the external `pantheon-mvp` candidate. It lists the cross-project connection points and the missing pieces for a fully functional platform.

## Findings recorded (constat, no doctrine change)

- The "three repositories" resolve to two GitHub repos plus one internal module: `pantheon-mcp` is `mcp-server/` inside Pantheon Next. `list_repos` confirms only `Pantheon-Next` and `pantheon-mvp` exist.
- The single wired inter-repo link is the pinned schema vendoring Next → MVP with report-only drift detection.
- Documentation drift noted: `pantheon-mvp/GOVERNANCE_STATUS.md` cites vendored commit `782afb4…` while `vendor/pantheon/UPSTREAM_COMMIT` holds `f8bc3bd…`. Recorded as a constat; correction belongs to a reviewed re-vendoring in the MVP repo, not to this audit.

## Effects

- Pantheon governs status; this audit only states it.
- No schema, test, protected path, `mcp-server/` code or CI script was modified.
- Hermes performs no execution; OpenWebUI exposes nothing new; no capability is installed, adopted or activated.

## Boundary

```text
audit != doctrine
constat != correction
documented drift != schema drift
mapping != adoption
```

No runtime, professional data, approval, Evidence admission, Register entry or external action is introduced.
