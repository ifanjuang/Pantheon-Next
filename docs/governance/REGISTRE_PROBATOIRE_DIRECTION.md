# Registre Probatoire — Direction note

Status: validation-only — direction record. It captures a decision and orients
the executor; it does not itself rewrite the affected doctrine or touch any
protected path.

Decision date: 2026-06-07.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Decision captured

Two naming decisions reframe the memory model.

```text
1. "Memory" is reserved to Hermes (the execution runtime).
   Hermes owns its own runtime memory (mem0 or another system).
   It is free, self-evolving and ungoverned by Pantheon.
   Pantheon no longer uses the word "memory" for anything it governs.

2. Pantheon governs the Registre Probatoire.
   It is the rigorous, citeable record of evidence with certainty levels,
   exhibits (pièces), dates and citations.
   It replaces the former term "Canonical Memory".
```

## The model

The split is by nature, not by storage mechanism.

| | Hermès memory (mem0) | Registre Probatoire (Pantheon) |
|---|---|---|
| Nature | operational, subjective recall | probative, objective record |
| Evolution | free, self-evolving, fast | governed, dated, cited |
| Analogy | the architect's own recollection | the project's file of exhibits |
| Authority | none | the only basis one may rely on |
| Owner | Hermes / the execution runtime | Pantheon |

## The bridge rule

Free memory stays compatible with the doctrine only because of one hinge rule.
Without it, "free memory" would drift into silent authority, which the red
lines forbid (no self-learning loop, no auto-promoted memory).

```text
Hermès memory may SPEAK — propose, recall, accelerate.
Only the Registre Probatoire may be CITED and relied upon
for a consequential decision.
```

When a statement is consequential (structure, budget, urbanism, a client
commitment, professional liability), the runtime must resolve it to a Registre
Probatoire entry — with its certainty level, dates and source. This is exactly
the Answer Verification Gate posture:

```text
Memory first. Evidence when consequential. Status when deciding.
Approval when acting.
```

Pantheon never performs automatic memory promotion: nothing the runtime
remembers becomes probative on its own.

## Three orthogonal certainty axes

Renaming resolves the scale collision found across the corpus. Three different
questions get three distinct, GLOSSARY-owned scales — they are not merged.

```text
E0–E4   probative certainty   "how trustworthy is this piece?"   Registre
V0–V4   answer verification   "is this answer verified?"          Gate (#71)
C0–C5   approval ceiling      "what clearance to act?"            Approval / MCP
```

`GLOSSARY.md` becomes the single owner of all three enums.

## Registre Probatoire entry — required fields

The four maintainer requirements (certainty level, exhibits, dates, citation)
are already specified in `EVIDENCE_MEMORY_CANONICALIZATION.md`; they only need
to be promoted as the primary object:

```text
certainty_level     E0–E4 — an explainable score, absorbing the existing
                    source / date / language / context / coherence components.
exhibits (pièces)   linked_files, source_excerpt — the opposable attachment.
dates               source_date, received_date, effective_date.
citation            author_detected, page_or_location, origin_channel.
```

## Vocabulary migration (for the executor)

```text
Canonical Memory            -> Registre Probatoire entry (retained piece)
Memory Candidate (Pantheon) -> Evidence Candidate / Register Candidate
"Pantheon memory"           -> Registre Probatoire
Hermes runtime memory       -> unchanged: mem0, free, ungoverned
```

## What changes in the corpus

```text
MEMORY.md                          reframed: "memory" = Hermès runtime, free,
                                   ungoverned; Pantheon's only constraint is
                                   that it carries no authority.
EVIDENCE_MEMORY_CANONICALIZATION   becomes the central Registre Probatoire doc;
                                   the "-> Canonical Memory" endpoint renamed.
ANSWER_VERIFICATION_GATE (#71)     becomes the memory↔registre bridge rule.
EXTERNAL_RUNTIME_MEMORY_ADAPTERS   already aligned: mem0 proposes, never canonizes.
GLOSSARY.md                        owner of E0–E4 / V0–V4 / C0–C5.
AUTHORITY_INDEX / MODULES / STATUS  reindex; retire "Canonical Memory" wording.
```

## Boundary

Direction record only. No doctrine file is rewritten here, no schema, test or
runtime is added, and no protected path is touched. The schema rename
(`schemas/memory_candidate.schema.yaml` and related) is downstream protected-path
work and stays deferred until explicitly approved. Hermès memory remaining free
does not make it authoritative; only the Registre Probatoire is probative, and
only a human gate makes a consequential entry binding.

```text
Hermès remembers freely.
Pantheon keeps the proof.
The human decides what is established.
```
