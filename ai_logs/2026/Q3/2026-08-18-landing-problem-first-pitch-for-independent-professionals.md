# Landing pitch — problem first, Pantheon revealed after, addressed to independent professionals

Date: 2026-08-18

Status: validation-only trace — editorial change, documented non-implemented.
Boundary profile: validation_only_trace.

Third pass on `docs/index.html` / `docs/index-en.html`, after the two 2026-08-17 passes.

## Change

- Updated: the hero no longer names Pantheon at all. It states the reader's situation and the stake — *Vous utilisez déjà l’IA. Qui répond de ce qu’elle écrit ?* / *You already use AI. Who answers for what it writes?* — reusing the opening of `docs/intro-professionnelle.md`. The three hero chips are the doctrine's own distinctions: a fluent answer is not a safe answer, drafting is not sending, finding a source is not proving it.
- Added: `#cas` / `#case` — one concrete scene (Tuesday 6.40 pm, an email answering the client on a ventilation close-out) with the four things that happened and appear nowhere in the message: the exhibit declared rather than attested, an exhibit was missing, the message commits, nothing flagged it. It closes on "you did nothing wrong": the defect is in what the assistant received.
- Updated: `#bribes` / `#fragments` now explains that same scene mechanically, and closes on the professional stake — in a trade where you answer for your signature, a brilliant but wrong answer commits liability and becomes the version everyone quotes.
- Updated: the former `#difference` becomes `#ampleur` / `#scale` and is written for an independent professional rather than a large practice: you, your colleague, your software's built-in AI, and partners who send AI-assisted material without saying so — all landing in one record, under one responsibility.
- Updated: `#pantheon` is the reveal, placed fourth, and is built on the repository's own analogy — you do not hand a whole record to a consulting engineer; you give a commission, a scope and the exhibits that carry authority (`docs/intro-professionnelle.md`). Its four cards are the four gates of that document: entry, context, output, memory. The scene is then replayed under the frame, and the section closes on the "who it is for" list and the doctrine's non-equivalences (answering ≠ acting, drafted ≠ sent, sent ≠ true).
- Updated: `#usages` / `#uses` gains an honest "under the hood" paragraph on the policy surface: it answers as data — consequence class, required verification, approval ceiling, gates — refuses an external action by default with the path to legitimise it, and is exposed through a read-only MCP server that consults, validates and verifies without executing, sending or approving (`mcp-server/README.md`, `HTTP_API_CONTRACT.md`).
- Updated: the Transparency block now states the real posture from `WHAT_RUNS.md`: doctrine, schemas, read-only repository checks and an MCP policy server exist here; the application server, cockpit and Hermès connections live in a separate repository as candidates — available means neither installed nor approved.
- Updated: the illustrative thread is now single — the ventilation close-out runs from the hero scene through the fragments diagram, the active-context diagram and the Concordance des Sources rite, whose missing exhibit is the same test report.
- Removed: the four-card grid in `#contexte` / `#context`, made redundant by its own diagram.

## Why

Feedback: Pantheon appeared before the reader had understood the problem, the page addressed a practice rather than the independent professional who uses AI occasionally, and the pitch did not build desire. The narrative now runs hook → one concrete case → why it happens → and it is not only you → here is Pantheon → how it is built → the method and where it comes from → honest status.

Wording follows `EDITORIAL_LANGUAGE.md` (start from the professional risk, *cadrer*, no promise of automatic proof) and reuses the vocabulary of `docs/intro-professionnelle.md`, which already addresses this audience.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none — static HTML/CSS/SVG.
Authority impact: none. The public status statement was tightened towards `WHAT_RUNS.md` rather than loosened.
Schema/test/CI impact: none; the read-only checks re-run clean.
External action: none.
Memory behavior: none.

## Local distinctions

```text
documented != implemented
available != installed != approved
scene != product demonstration
pitch != authority claim
```
