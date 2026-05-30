# AI Log — Public README Clarity Pass (Architecture Examples)

Date: 2026-05-30

## Scope

Second readability pass on the public hook of both README files, to make the
opening more impactful and concrete for a first-time professional reader.

## Changes made

Updated:

- `README.md`;
- `README.fr.md`.

Added:

- `ai_logs/2026-05-30-public-readme-clarity-architecture.md`.

## Editorial intent

Following `docs/governance/EDITORIAL_LANGUAGE.md` (start from the situation, not
the architecture):

- **Open with the felt risk**: the first line is now a question —
  "You already use AI. But who answers for what it writes? You do."
- **Professional analogy**: an architect does not hand a whole dossier to an
  outside engineering office; they give a brief and just what is needed. This
  explains "minimum necessary context" without jargon and de-mystifies the tool.
- **Text mini-diagram**: `you → [Pantheon: what enters] → AI → [Pantheon: what
  leaves] → you decide`, so the "thing in the middle" is graspable at a glance.
- **New "Four questions, four answers" section**, phrased positively (no
  fear/negative framing per the request), answering: what the AI sees, what if
  it errs, who keeps control, and what is remembered next time.

## Examples scope

Per explicit request, all worked examples in this pass are **architecture only**:

- surface note to a client (floor area + brief, not client identity);
- setback line from an old zoning plan marked "to verify";
- quote-approval email drafted but not sent;
- plot-bound allowed height not reused elsewhere.

The existing recovery-quote email example was kept (already architecture).

## Honesty boundary

No "safe AI", "automatic sending" or "compliant by design" promise was
introduced. The mini-diagram and analogy stay at method level. The "coherent but
partial" status note and the `STATUS.md` pointers remain in place.

## Explicit non-implementation

This intervention did not implement any runtime behavior. No files were modified
under `schemas/`, `tests/`, `operations/`, `hermes/`, `pyproject.toml`, or
`CLAUDE.md`. The earlier `.github/workflows/governance-ci.yml` negation-regex
widening is unrelated to this pass.

## Boundary phrase

```text
The README explains the conduct frame with concrete architecture cases.
It does not connect, route, send or execute anything by itself.
```
