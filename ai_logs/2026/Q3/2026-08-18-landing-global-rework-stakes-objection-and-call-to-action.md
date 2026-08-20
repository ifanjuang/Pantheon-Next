# Landing global rework — stakes, the work objection, honest state and a call to action

Date: 2026-08-18

Status: validation-only trace — editorial change, documented non-implemented.
Boundary profile: validation_only_trace.

Global rework of `docs/index.html` / `docs/index-en.html` after a full re-read of the page from three viewpoints: a practising architect who uses AI, one who refuses it, and an investor.

## Change

- Updated: reading order. The scene now runs hero → one case → **and it is not only you** → why it happens → Pantheon → what it makes possible → the work objection → how it is built → memories → method and its provenance → visible context → rites → design → tools → where the project stands. The distributed-uses section moved up because it is the argument that holds the reader who does not use AI at all: AI is already in the record through partners and software.
- Added: `#enjeux` / `#stakes` — the three horizons that state what the frame makes possible rather than what it is. Today: not re-reading everything, because the consequence is classified before the answer. Tomorrow: letting AI act without handing it the pen, since external action is refused by default. In five years: owning what the practice learns, because the register is attached to the project rather than to the engine. Closes on the question a client, insurer or peer will ask about how AI took part.
- Added: `#travail` / `#work` — the first objection, answered instead of avoided: the four gates only pay off if qualification happens where information arrives, once. Four honest columns — what can be surfaced without re-entry, what is proposed for confirmation, what stays a human gesture, and what the frame should not require — and an explicit statement that where the line falls is what pilot records are for.
- Added: `#commencer` / `#start` — the project's own status in four states (established, read-only, candidate, not yet), who it is too early for, who it is the right moment for, and the first call to action the page ever had. It replaces the former Transparency block, which stated the same posture without any next step.
- Updated: hero. The former pivot line ("c’est un problème de dossier") overclaimed and read as a reproach about filing. It becomes: a better model would not have known either, nor would a better question — the problem is what the AI received. Hero actions now point at the case, the stakes and the project status.
- Updated: `#grammaire` / `#grammar` — function before Greek name in the eight-viewpoint grid, with a progressively disclosed explanation rather than requiring the reader to learn the mythology first.
- Removed: the standalone `#intelligence` section, absorbed into the third horizon of `#enjeux` (continuity, transmission, independence from the tool).

## Why

Read as a practising architect, the page explained the risk well but never said what to do next, and never answered "who does the qualification work?" — the objection that decides whether the frame survives three weeks in an office. Read as a sceptic, the argument that holds is that AI already enters the record through partners and software, and it was buried mid-page. Read as an investor, the page had no call to action, no statement of what is testable today, and no articulation of what the frame makes possible rather than what it forbids.

Wording follows `EDITORIAL_LANGUAGE.md`; the status statements follow `WHAT_RUNS.md` and `STATUS.md`; the four gates and the audience come from `docs/intro-professionnelle.md`.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none — static HTML, no script added.
Authority impact: none. The landing projects the canonical doctrine but does not define it.
Schema/test/CI impact: none from the landing itself.
External action: none. The call to action links to the repository's public issue tracker; no address, form or third-party service is introduced.
Memory behavior: none.

## Local distinctions

```text
documented != implemented
available != installed != approved
pilot record != product
what it forbids != what it makes possible
```

## Follow-up — editorial junction with #680 (2026-08-19)

- Updated: public synthetic examples adopt the naming convention retained in #680 — pronounceable three-letter code with an attached number. `Projet Alpha` / `Projet Bêta` and `Project Alpha` / `Project Beta` become `LIA21` / `SOL14`; `Affaire Alpha` / `Alpha project` becomes `Dossier LIA21` / `Project LIA21`.
- Updated: the fictional person in the opening scene follows the same convention — civil title and one initial. The client becomes `Mme. C`, in both languages.
- Result: the landing retains one synthetic narrative hook while the explanatory sections are free to use broader examples.
- At that date, the direct link to `comprendre.html` / `understand.html` was deferred because #680 had not yet merged.

## Historical follow-up — former seven-role alignment (2026-08-19)

The branch temporarily normalised the public grid to seven Roles because the then-current `AGENTS.md`, Task Contract schema and Role Signal schema all exposed seven canonical values. Mnemosyne was therefore described only as a visual memory figure.

That correction was valid against the repository state at the time but is **superseded** by the semantic governance decision merged later through PR #682. It must not be read as current doctrine.

## Follow-up — convergence after #680 and #682 (2026-08-20)

Base after convergence:

```text
main@3ac042ac630b14952da9159d91af6a388da1b27c
```

The landing branch was reanchored on that exact `main` while preserving the landing rework. The current default branch already contains:

- the FR/EN learning Atlas from #680;
- the canonical eight-Role registry from #682;
- `MNEMOSYNE` in the shared schema vocabulary and general Role enums.

### Canonical Role correction

The landing now presents eight canonical governance Roles, function first:

```text
ATHENA      -> understand / frame the task
ARGOS       -> check sources and evidentiary support
THEMIS      -> surface limits, risk and approval needs
APOLLO      -> check clarity, completeness and delivery readiness
HEPHAISTOS  -> qualify fabrication or modification work
IRIS        -> prepare transmission and recipient adaptation
ZEUS        -> arbitrate status and next procedure
MNEMOSYNE   -> recover useful history, review dates/indices/versions/supersession, propose retention placement
```

The public explanation explicitly states that these are eight responsibilities of judgement, not eight agents that must participate in every request. Roles may remain on standby until their viewpoint is material.

The ARGOS / MNEMOSYNE boundary is kept visible:

```text
ARGOS      -> what does the source support and how authoritative is it?
MNEMOSYNE  -> where should prior context be sought, which version/state is being reused, what was superseded, where may retention be proposed?
```

The newest remembered state is not presented as automatically the strongest evidence.

### Generalisation of examples

The opening `LIA21` / `Mme. C` scene remains as the single narrative hook of the landing.

The explanatory material is now mostly generic so Pantheon does not read as an architecture-specific anecdote:

- memory contrasts a drafting preference with a dated, sourced and scoped decision;
- visible context uses generic reference documents, review notes, decisions and internal guides;
- the Rite example compares two documents carrying incompatible states rather than a ventilation-specific case;
- Mnemosyne demonstrates version/supersession review while Argos evaluates source support and Themis evaluates consequence/risk.

### Progressive disclosure

The landing now reduces Roles / Rites / Places to three first-read questions:

```text
Roles  -> who looks at what?
Rites  -> how do we check when things become difficult?
Places / scopes -> in which context may the information be reused?
```

Greek names are introduced only after their functions.

### Atlas junction

Because #680 is now on `main`, the landing links directly to:

- `comprendre.html` — *Comprendre l’IA moderne*;
- `understand.html` — *Understanding modern AI*.

The Atlas carries the deeper explanation of models, context, RAG, memory, execution, Roles, Rites, governed places and Pantheon governance. The landing remains problem-first and does not duplicate the full tutorial.

### Editorial precision

Several absolute claims were softened to remain verifiable:

- “three things you cannot do today” becomes “three capabilities difficult to sustain without a shared frame”;
- “what the frame picks up alone” becomes “what the frame can surface without re-entry when metadata already exist”;
- “never asked” becomes “what the frame should not require”;
- public doctrine is described as “public, versioned, verifiable” rather than “opposable”.

A temporary CSS filler introduced for the former seven-item Role grid was removed after the return to eight Roles; the CSS now matches `main` exactly.

## Verification plan — final #676 head

Before merge:

1. confirm the PR remains limited to the FR landing, EN landing and this trace;
2. confirm no residual “seven Roles”, “seven and only seven”, `Project Alpha/Beta` or non-canonical Mnemosyne wording remains;
3. confirm `comprendre.html` / `understand.html` links resolve on the current base;
4. confirm static-only boundaries and local references;
5. run exact-head Governance CI and Obsolete Authority Consistency;
6. merge only the exact verified head;
7. recheck `main` after merge.

## Done criteria

The landing subject is complete when:

- #676 is rebased/converged on the current `main`;
- FR and EN carry the same eight-Role doctrine and generic explanatory examples;
- the learning Atlas is reachable from both languages;
- the obsolete seven-Role narrative is absent from active public HTML;
- no CSS workaround for a seven-item grid remains;
- exact-head CI is green;
- #676 is merged and `main` is rechecked.
