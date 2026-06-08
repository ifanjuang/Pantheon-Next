# Rite Trigger Catalogue

Status: candidate / to verify — direction for operationalizing the rites as a
deterministic question catalogue.

Distilled from the external deterministic-metacognition pattern reviewed in
`../reference_reviews/SELF_INSPECT_MCP.md`, importing none of it.

This note proposes a shape; it does not add a runtime, MCP server, classifier,
scheduler, trigger engine, approval engine or automatic memory promotion engine.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Intent

The rites are excellent doctrine but they live as prose. This catalogue proposes
to express the *front edge* of the rites — the moment a methodological symptom
appears — as a compact, deterministic `signal -> metathought question` table
that Pantheon owns as spec and an external surface merely serves.

A metathought is a question, never a verdict. It surfaces an assumption, a drift
or an over-confidence for governed attention. It does not answer, approve, block
or trigger.

```text
The catalogue asks.
ZEUS decides whether a rite follows.
The human decides what to do with the answer.
```

## Relationship to existing rite doctrine

This catalogue does not replace `RITE_SELECTION_MATRIX.md`; it sits one step
earlier and finer-grained.

```text
Signal      a detectable surface cue in the work
-> Question a metathought that redirects attention (mode_light)
-> Symptom  if confirmed, RITE_SELECTION_MATRIX maps it to a candidate rite
-> ZEUS     decides whether the rite is allowed (RITE_INVOCATION_POLICY)
```

All existing guardrails still hold: a signal suggests, it does not trigger; the
anti-chaining rule, the rite budget and the closure statuses are unchanged. A
surfaced question is `mode_light` by default and may resolve the tension without
any full rite at all.

## Catalogue shape (owned spec)

The catalogue is a flat, reviewable spec. Each row:

```text
signal_id
signal_cues          observable surface cues (deterministic, no LLM judgement)
metathought          the question to surface
attention_failure    the named failure it guards against
related_rite         the rite it may lead to, if confirmed
default_mode         mode_light unless escalated
escalation_note      when to consider a full rite or a User Decision Gate
```

A universal default question applies when no signal matches.

## Starter catalogue

| signal | metathought (the question) | attention failure | related rite |
|---|---|---|---|
| First framing reused unchanged across several steps | "Is this still the same problem, or did the first framing harden into an assumption?" | commitment to first interpretation | `PREMISSES_CACHEES.md` |
| A preference or constraint appears that the user never stated | "Which of these is stated, and which did I infer?" | invented user preference | `PREMISSES_CACHEES.md` |
| Scope grew without an explicit decision | "Did the cap change, or did scope drift under it?" | scope / goal drift | MÈTIS — `REQUEST_LIFECYCLE.md` |
| A draft reads as smooth and convincing | "If a third party wrote this, which claim would I challenge first?" | premature satisfaction | `AUTOCRITIQUE_CONTRADICTOIRE.md` |
| Confidence is high but sources were not compared | "Do the sources actually agree, and are they fresh?" | unwarranted confidence | `CONCORDANCE_DES_SOURCES.md` |
| Retrieved text is being treated as proof | "Is this retrieved, or is it evidence I can cite?" | retrieval mistaken for evidence | `CONCORDANCE_DES_SOURCES.md` |
| Many local corrections, worsening coherence | "Are these fixes improving the whole, or only the part?" | Hydre-like proliferation | `REFONDATION_DE_SESSION.md` |
| About to deliver something with external effect | "What is the one thing that, if wrong here, would matter most?" | premature delivery | `AUTOCRITIQUE_CONTRADICTOIRE.md` |
| (no signal matched) | "What am I assuming that I have not named?" | universal default | — |

The cues column should be expressed as deterministic, observable patterns, not
as a model judgement, so selection stays explainable and driftable.

## Execution target (for the executor)

If this candidate is promoted, the executor (Hermès / ChatGPT) may build it as a
read-only, deterministic surface. This stays inside Pantheon's Phase 4 allowance
(read-only checks, governance reference validation) and outside the runtime.

```text
1. The catalogue is the single owned spec (one table / CSV under Pantheon).
2. Selection is deterministic: cue match -> question. No LLM, no embeddings.
3. Drift verification: any served form must match the owned spec exactly.
4. A served surface (Hermès, or a read-only MCP resource per
   MCP_POLICY_SERVER_CANDIDATE) only returns the question. It never approves,
   blocks, triggers a rite or writes memory.
5. The surfaced question and any resulting rite status may be shown in OpenWebUI.
```

Acceptance for promotion:

```text
the catalogue surfaces a QUESTION only, never a verdict;
selection is deterministic and explainable;
no signal auto-triggers a rite or chains rites;
the rite budget, anti-chaining and ZEUS closure statuses still apply;
nothing here promotes memory or grants approval.
```

## Forbidden drift

```text
no automatic self-correction loop (self-learning is rejected)
no auto-triggered rite or rite chain from a signal
no LLM-judge selection presented as deterministic
no question turned into an approval, a block or proof
no catalogue treated as a Registre Probatoire entry
no scheduler, queue or trigger engine inside Pantheon
```

## Open questions

```text
Which signals are reliably detectable without a model judgement?
Should the catalogue live as one table here, or as a small CSV spec?
Should the default question always apply, or only on consequential work?
How is the served surface drift-checked against the owned spec?
Which rite modes does each signal default to?
```

## Current repo state

Documented non-implemented. Candidate / to verify. No catalogue file, schema,
test, runtime, MCP server or served surface is added.
