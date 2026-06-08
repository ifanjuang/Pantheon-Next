# AI log — E3: promote EVIDENCE_MEMORY_CANONICALIZATION as the central Registre Probatoire document

Date: 2026-06-08.

## Intent

Third downstream step (E3) of the Registre Probatoire direction. Promote
`EVIDENCE_MEMORY_CANONICALIZATION.md` as the central document for the Registre
Probatoire, retire the "Canonical Memory" wording, and map certainty onto the
`E0–E4` scale.

## Change

In `docs/governance/EVIDENCE_MEMORY_CANONICALIZATION.md` only:

- retitled to "Registre Probatoire — evidence canonicalization" and reframed the
  opening to position it as the central register document (links `GLOSSARY.md`
  and `REGISTRE_PROBATOIRE_DIRECTION.md`; certainty uses `E0–E4`);
- renamed the governed-path endpoint and all occurrences: `Memory Candidate`
  -> `Register Candidate`, `Canonical Memory` -> `Registre Probatoire entry`
  (11 + 9 occurrences), with grammar fixed where the rename needed an article;
- reframed the core distinction so "memory" is Hermès's ungoverned recall and the
  `Registre Probatoire entry` is the approved, dated, cited record;
- added `E0–E4` to the entry definition.

The filename is unchanged (retitle in place, per the checklist), so inbound links
from other documents stay valid. A file rename is optional later work.

## Boundary

Documentation only. No schema, test, runtime or protected-path change. The doc
remains a candidate support note (documented non-implemented). Reindexing the
authority map and the file rename are later steps (E5; the schema rename is the
protected E6). Verified clean against the governance forbidden-phrase lint.
