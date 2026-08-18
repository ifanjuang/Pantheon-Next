# Landing global rework — stakes, the work objection, honest state and a call to action

Date: 2026-08-18

Status: validation-only trace — editorial change, documented non-implemented.
Boundary profile: validation_only_trace.

Global rework of `docs/index.html` / `docs/index-en.html` after a full re-read of the page from three viewpoints: a practising architect who uses AI, one who refuses it, and an investor.

## Change

- Updated: reading order. The scene now runs hero → one case → **and it is not only you** → why it happens → Pantheon → what it makes possible → the work objection → how it is built → memories → method and its provenance → visible context → rites → design → tools → where the project stands. The distributed-uses section moved up because it is the argument that holds the reader who does not use AI at all: AI is already in the record through partners and software.
- Added: `#enjeux` / `#stakes` — the three horizons that state what the frame makes possible rather than what it is. Today: not re-reading everything, because the consequence is classified before the answer. Tomorrow: letting AI act without handing it the pen, since external action is refused by default. In five years: owning what the practice learns, because the register is attached to the project rather than to the engine. Closes on the question a client, insurer or peer will ask about how AI took part.
- Added: `#travail` / `#work` — the first objection, answered instead of avoided: the four gates only pay off if qualification happens where information arrives, once. Four honest columns — what the frame picks up alone, what it proposes for confirmation, what stays a human gesture, and what will never be asked (no re-filing, no migration, no taxonomy, no change of tool) — and an explicit statement that where the line falls is what pilot records are for.
- Added: `#commencer` / `#start` — the project's own status in four states (established, read-only, candidate, not yet), who it is too early for, who it is the right moment for, and the first call to action the page ever had. It replaces the former Transparency block, which stated the same posture without any next step.
- Updated: hero. The former pivot line ("c’est un problème de dossier") overclaimed and read as a reproach about filing. It becomes: a better model would not have known either, nor would a better question — the problem is what the AI received. Hero actions now point at the case, the stakes and the project status.
- Updated: `#grammaire` / `#grammar` — function before Greek name in the eight-viewpoint grid, and the "why Greek names" note now concedes the sceptic's first reaction instead of ignoring it.
- Removed: the standalone `#intelligence` section, absorbed into the third horizon of `#enjeux` (continuity, transmission, independence from the tool).

## Why

Read as a practising architect, the page explained the risk well but never said what to do next, and never answered "who does the qualification work?" — the objection that decides whether the frame survives three weeks in an office. Read as a sceptic, the argument that holds is that AI already enters the record through partners and software, and it was buried mid-page. Read as an investor, the page had no call to action, no statement of what is testable today, and no articulation of what the frame makes possible rather than what it forbids.

Wording follows `EDITORIAL_LANGUAGE.md`; the status statements follow `WHAT_RUNS.md` and `STATUS.md`; the four gates and the audience come from `docs/intro-professionnelle.md`.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none — static HTML, no script added.
Authority impact: none. The public status statement was made more precise, not looser: established doctrine, read-only policy server, candidate application server and cockpit in a separate repository, and turnkey installation explicitly named as not yet built.
Schema/test/CI impact: none; the read-only checks re-run clean.
External action: none. The call to action links to the repository's public issue tracker; no address, form or third-party service is introduced.
Memory behavior: none.

## Local distinctions

```text
documented != implemented
available != installed != approved
pilot record != product
what it forbids != what it makes possible
```
