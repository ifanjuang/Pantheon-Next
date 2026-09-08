# 2026-09-08 — Boundary profile migration: docs/examples/

## Change

Migrated the 13 documents in `docs/examples/` that still restated the
exposure/execution/governance triad in prose onto declared `Boundary
profile` lines, per #996's suggested slicing order (next slice after
`docs/governance/` root+subdirectories and `docs/domain-packs/architecture/`).

Profiles chosen by reading each document's own `Status:` line and full
content, not by pattern-matching the shared "fictional example —
educational support only" phrasing 11 of the 13 share on their `Status:`
line:

```text
10  documentation_only        11 fictional/illustrative worked examples
                               that apply or illustrate already-existing
                               doctrine to a fictional scenario, but
                               propose nothing new (ABF handoff, decision-
                               memory-vs-registre, evidence topology,
                               pre-execution simulation, ERP effectif
                               impact, logement collectif fixture, notice
                               securite incendie, both governed-composition
                               examples, understand-anything) - one of
                               these is PRACTITIONER_HOOKS.md itself
                               (a topic list, also purely explanatory)
 1  candidate_support_note    architecture_proof_register/README.md - the
                               one file in this batch that is not a worked
                               illustration of settled doctrine: its own
                               text says it "exists to test the
                               architecture proof-register idea before
                               changing schemas/" and explicitly treats
                               PROOF_REGISTER.md's "direction as candidate,
                               not implementation" - it explores a
                               direction, it does not just apply one
 1  validation_only_trace     vertical_devis_reprise/README.md - its own
                               Status line already says "validation-only
                               / governed vertical slice ... checked
                               read-only by the mcp-server doctor,
                               check_vertical_slice, and in CI" - a
                               machine-checked trace proving coherence,
                               not a candidate proposal or a worked
                               illustration
```

Three files (`architecture_decision_memory_vs_registre/README.md`,
`architecture_erp_effectif_impact_workflow/README.md`,
`architecture_notice_securite_incendie_workflow/README.md`) carried two
extra distinct lines beyond the generic triad ("The Registre Probatoire
proves." / "The human decides.") - kept verbatim, only the generic three
lines removed, following the exception precedent from #1017/#1022.

None of the 13 were on `KNOWN_CANDIDATE_OPENWEBUI_RESIDUES` (#995's
ratchet, verified by grep); that list is unchanged at 9 entries.

## Why

Next slice in #996's suggested order. The batch's shared Status phrasing
("fictional example — educational support only") made a single-classification
temptation strong - exactly the shape of my last two mistakes on #1020 and
#1022 (grouping a document with siblings, or classifying by subject rather
than by what the document itself is and does). Read every file's full
content in this slice specifically to check for that failure mode before
assigning a profile, which is why 2 of the 13 depart from the shared
`documentation_only` classification the shared Status wording would have
suggested at a glance.

## Boundary

Documentation-only change. No Status line changed, no authority gained or
lost, no schema, test logic or CI workflow touched.

## Verification

- All 6 governance checks pass.
- `python3 -m pytest tests/ -q` — 678 passed.
- Fresh count on `main` before this change: 33 documents restate the triad
  with no profile. After: 20 documents — `docs/examples/` no longer
  appears in the remaining-work breakdown at all.
- Confirmed none of the 13 paths appear in
  `KNOWN_CANDIDATE_OPENWEBUI_RESIDUES` before or after (grep, not assumed).

## Local distinctions

```text
worked illustration of existing doctrine != candidate direction of its own
machine-checked coherence trace != documentation or candidate proposal
shared Status wording != shared boundary profile
```

Relates to #996 (does not close it — 20 of the original 112 documents
remain across `docs/assets/`, `templates/`, `hermes/profiles/`,
`mcp-server/docs/` and `docs/roadmaps/`; `docs/audits/` correctly stays
out of scope as dated historical traces).
