# AI log — E5: reindex the authority map to the Registre Probatoire vocabulary

Date: 2026-06-08.

## Intent

Fifth downstream step (E5) of the Registre Probatoire direction. Retire the
retired object terms ("Canonical Memory", "Memory Candidate") from the index /
map files so the whole corpus vocabulary is consistent after E1–E3.

## Change

- `docs/governance/AUTHORITY_INDEX.md`: in the external runtime memory adapter
  rule, `Memory Candidates` -> `Register Candidates` and `Canonical Memory`
  -> `Registre Probatoire entries`.
- `docs/governance/MODULES.md`: the "Memory module" reframed as the "Memory and
  Registre Probatoire module" (memory belongs to Hermès, ungoverned; Pantheon
  governs the Registre Probatoire); `Memory Candidate` -> `Register Candidate`
  and `Canonical Memory` -> `Registre Probatoire entry` throughout the module,
  the integration modules and the request-flow.

## Scope decision

Only the object terms were renamed. The boundary phrases "automatic memory
promotion" / "promote memory" are kept verbatim in `AUTHORITY_INDEX.md`,
`MODULES.md`, `STATUS.md` and `README.md`: they name a rejected pattern, they
remain true (Pantheon now governs no memory at all), and the CI lint relies on
"automatic memory promotion" as a forbidden phrase. `STATUS.md` and `README.md`
contained only such boundary phrases, so they are unchanged.

## Boundary

Documentation only. No schema, test, runtime or protected-path change. With
E1–E3 and E5 landed, the Registre Probatoire vocabulary is consistent across the
governance corpus and the index files; remaining downstream work is E4 (the
bridge rule in the Answer Verification Gate, owned by the parallel track on #71)
and the protected E6 schema rename. Verified clean against the governance lint.
