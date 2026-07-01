# AI log — de-version base_metier PDFs, keep out of git (B-2, decision c)

Date: 2026-07-01.

Actor: Claude Code.

## Intent

Arbitration B-2, maintainer decision **(c)**: keep the `base_metier/architecte/`
source PDFs out of git (private / local storage), with a `.gitignore` and a
reconstructible manifest. The licence determination stays with the maintainer.

## Change

- `git rm` the 12 source PDFs (~55 MB, incl. 3 exact duplicates at the folder root).
  The working tree no longer versions them.
- `.gitignore`: `base_metier/**/*.pdf` so they are not re-added.
- `base_metier/architecte/knowledge/sources/SOURCES.manifest.yaml` (new): a
  reconstructible manifest — per source: filename, declared origin, licence status
  (to verify), size, sha256 — so a restored corpus can be verified. Records
  provenance/integrity only; promotes nothing.
- `docs/governance/AUTHORITY_INDEX.md`: `base_metier/architecte/` indexed as
  `external professional corpus / to verify` — candidate corpus, not authority,
  not proof; frozen pending the licence decision.

## Not done here (deliberate)

- The ~55 MB stays in git **history**; purging history needs a maintainer-run
  `git filter-repo` / BFG pass (a rewrite), out of scope for a normal PR.
- Moving the 2 executable skills Hermes-side and the licence determination remain
  follow-ups / maintainer calls. `Code-de-La-Construction…txt` (official code, text)
  is kept.

## Boundary

Repository hygiene + indexing. Removes binaries and records provenance; it decides
no licence, promotes nothing, and adds no runtime. The corpus stays frozen and
candidate until qualified.
