# AI log — inventory of base_metier/architecte/ (B-2, read-only)

Date: 2026-07-01.

Actor: Claude Code.

## Intent

Arbitration B-2 (accepted, controlled transition). Before the maintainer's licence
decision on `base_metier/architecte/`, produce the facts: what is there, what
executes, which PDFs carry redistribution risk, and what is declared about
provenance. Read-only: nothing under `base_metier/` is moved, deleted or changed.

## What was found

- 58 MB, 42 files; not indexed in `AUTHORITY_INDEX.md` / `MODULES.md`.
- 2 executable Python skills (`pdf_to_md`, `ingest_local_folder`) — out of the
  "governs, does not execute" doctrine; PyMuPDF dependency undeclared.
- 9 unique PDFs (3 also duplicated at the folder root): five MAF "Outils" (~47 MB,
  high copyright risk), one Ordre des Architectes publication, CCAG / Code texts
  (official, lower risk), one unidentified GLOSSAIRE.
- No provenance / licence manifest anywhere.
- Binaries versioned in git (not `.gitignore`d).

## What was produced

- `docs/audits/2026-07-01-base-metier-architecte-inventory.md` (validation-only): the
  full inventory with a PDF table (size · sha256 · apparent origin · non-legal risk
  read), the duplicate list, and mechanical recommendations (freeze; index as
  external professional corpus / to verify; de-version binaries + reconstructible
  manifest; move skills Hermes-side; do not ground the B-3 slice on unqualified
  sources). The licence determination is left explicitly to the maintainer.

## Boundary

Inventory only; decides nothing, moves nothing. No protected-path change.
