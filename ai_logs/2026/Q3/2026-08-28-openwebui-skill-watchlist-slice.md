# OpenWebUI skill-watchlist convergence — 2026-08-28

## Objective

Continue #785 from merged main `704b4e85ea7d5c70947bfb58671914b04815facf` with a bounded skill-watchlist slice. Remove current OpenWebUI ownership from the external skill watchlist while preserving product-specific observation, provenance and rejection material. Reduce the machine-tracked allowlist from 8 paths to 7.

## Scope

- `docs/governance/SKILL_WATCHLIST.md`
- `tests/test_openwebui_integration_owner_retirement.py`

No parallel pull request was open when the slice started.

## Observed need

`SKILL_WATCHLIST.md` still carried the old global `OpenWebUI exposes / Hermes executes / Pantheon governs` block. Full-file review through EOF showed that the remaining product references belong to the watchlist's distinct responsibility: they describe external sources, candidate patterns or explicit anti-patterns and are not current OpenWebUI ownership claims.

## Owner review

`SKILL_WATCHLIST.md` remains the owner for watching external skill ecosystems without automatic adoption or installation. `HERMES_INTEGRATION.md` remains the stable runtime/client/PDP/PEP boundary owner. No source entry is promoted, removed or reclassified by this slice.

## Overlap analysis

The slice does not change skill lifecycle, external tool admission, marketplace trust, Hermes capability binding, installation policy, approval policy or memory promotion. It only removes the duplicated global architecture statement and consumes the existing integration boundary. Product-specific references such as Agensi, Understand-Anything and vercel-labs/skills remain because they are the subjects being observed or bounded.

## Affected consumers

- maintainers reviewing external skill ecosystems;
- reviewers distinguishing watch signals from adopted capabilities;
- future Hermes Skill Candidate reviews;
- #785 regression tests.

No executable consumer changes.

## Convergence

The watchlist now inherits the client/runtime/Cockpit/authority split from `HERMES_INTEGRATION.md`. Its local consequence is explicit: visibility of a watched skill, catalogue or marketplace in a client does not confer approval, adoption or governance authority.

## Migration and rollback

Documentation-only change. No skill, marketplace, client, runtime, plugin or connector is installed, removed or configured. No data or persistent state migration exists. Rollback is a normal Git revert.

## Role / Rite / Space

- Role: MNEMOSYNE for watchlist/provenance continuity, with THEMIS authority-boundary review.
- Rite: Concordance des sources across exact main, #785, the regression and `HERMES_INTEGRATION.md`.
- Space: Pantheon Next governance repository.

These labels describe review context only and create no runtime state.

## Authority impact

None. Watched sources remain external signals. A watched, popular, compatible or visible skill is not approved or adopted. Pantheon retains governance authority; clients remain non-authoritative interaction surfaces.

## Runtime impact

None. No runtime, skill execution, installation, provider, plugin, external effect, approval execution or deployment behavior changes.

## Preserved invariants

```text
watched != adopted
popular != approved
visible in client != governance authority
skill output != Evidence
skill output != governed memory
client selected != governance authority
```

## Boundary

Documentation and regression-only convergence. No API, schema, persistence, provider, approval or memory behavior changes.

`SKILL_WATCHLIST.md` was read through EOF before editing. The published document commit was inspected directly: only the global ownership block changed, plus EOF newline normalization; no watchlist entries or long-document content were truncated. `.github/scripts/truncation_ack.txt` is unchanged.

## Verification rule

Any subsequent modification invalidates prior checks. Merge only after Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency are green on the final exact head and reviews/threads/comments have been read.
