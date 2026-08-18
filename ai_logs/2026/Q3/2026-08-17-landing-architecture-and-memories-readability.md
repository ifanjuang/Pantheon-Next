# Landing readability — architecture, two memories, anonymised project names

Date: 2026-08-17

Status: validation-only trace — editorial landing change, documented non-implemented.
Boundary profile: validation_only_trace.

## Change

- Added: `#architecture` section on `docs/index.html` / `docs/index-en.html` — four named resources an AI draws on (models, skills, knowledge/web, connections) plus one overview diagram (`Schéma 02` / `Diagram 02`) placing resources, active context, the checkpoint, the human decision and the two memories in a single view.
- Added: `#memoires` / `#memories` section contrasting fluid memory (Hermès side, self-filling, no authority) with register memory (`Registre Probatoire`, Pantheon side, candidate until human review, citable), with the review gate stated explicitly and a concrete example.
- Added: `.memory-duo`, `.memory-card`, `.memory-gate` styles in `docs/assets/landing-docs-components.css` and their responsive rules.
- Updated: page title, meta/OpenGraph description and hero on both landing pages (`Toutes les IA de l’agence. / Un seul cadre de travail.`, `Every AI in the practice. / One shared frame of work.`), hero call-to-actions and the three hero thesis chips.
- Updated: illustrative project names anonymised — `Affaire FLOQUET` → `Affaire Alpha`, `FLOQUET project` → `Alpha project`, `Projet A/B` → `Projet Alpha/Bêta`, `Project A/B` → `Project Alpha/Beta`.
- Updated: diagram numbering shifted (grammar 02→04, active context 03→05, Rite 04→06) to make room for the new overview diagram.
- Updated: landing navigation reduced to five entries and the `≤1120px` blanket rule replaced by scoped `≤1180px` / `≤960px` rules; this also removes a pre-existing overlap where the absolutely centred wordmark ran under the navigation at every width above ~1228px, and stops the manifesto pages from hiding their whole navigation.

## Why

Readers reported the landing page as abstract: the doctrine was legible but the architecture was not, and the distinction between what an assistant merely remembers and what the practice may cite — the most operative distinction in `docs/governance/MEMORY.md` — appeared only as a passing sentence. The hero title also stated a question rather than what Pantheon is. Illustrative project names read as a real client dossier.

Wording follows `docs/governance/EDITORIAL_LANGUAGE.md`: start from the practitioner situation, use *cadrer* in public copy, and never promise automatic proof.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no. `docs/assets/pantheon-control/` is untouched; no `dashboard/` module is introduced.
Runtime impact: none — static HTML/CSS only, no script added.
Authority impact: none — the page describes the existing register/candidate distinction and does not create, promote or approve anything.
Schema/test/CI impact: none. `check_asset_references.py` and `check_no_local_cockpit.py` re-run clean.
External action: none.
Memory behavior: none — the two memories are described, not implemented.

## Local distinctions

```text
documented != implemented
remembered != citable
landing copy != doctrine
diagram != runtime topology
```
