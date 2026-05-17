# AI Log — README worked-example samples

Date: 2026-05-17

## Scope

Pushed the two professional worked examples in both README files from "described" to "shown" by adding collapsible sample artifacts.

## Files changed

- `README.md`
- `README.fr.md`
- `ai_logs/2026-05-17-readme-worked-example-samples.md`

## Main changes

For each of the two scenarios (law firm preparing a case management hearing, general practitioner writing a referral letter), added two collapsible `<details>` blocks:

- **Sample mission sheet (Task Contract)** — fixed-format text block showing mission, scope, allowed sources, forbidden sources, expected output, approval ceiling and memory rules. Uses fictional masked tokens like `[DOCKET-MASKED]`, `[PSEUDO-A7]`, `[DATE-MASKED]`.
- **Sample candidate deliverable** — for the lawyer, a three-argument extract of a strategy note with source/exhibit references and a flagged unverified case-law citation. For the doctor, a one-page pseudonymized referral letter with clinical findings, lab values and an explicit clinical question.

All samples are illustrative narratives. The masked tokens are deliberate placeholders, not field formats — they exist to make the readability of the artifact obvious without inventing identifying data.

Both samples are wrapped in `<details>` so they do not lengthen the main reading flow; engaged readers can expand them, casual readers stay on the synthesis bullets above.

## Boundary check

This intervention is README copy only. The samples are illustrative — they do not declare any Task Contract or Evidence Pack schema, do not implement any generator, and do not commit Pantheon Next to a specific artifact format.

## Status

Both READMEs now show, not just tell. Two scenarios (lawyer, doctor), four sample blocks per file (mission sheet + deliverable per scenario). Total length: 540 lines per file (up from 448).
