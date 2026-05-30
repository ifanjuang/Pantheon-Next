# AI Log — Public README Channel and Conduct Framing

Date: 2026-05-30

## Scope

Improved the public-facing hook of both README files to reposition Pantheon Next
as the professional-conduct frame that sits between the practitioner, the usual
discussion channels, and interchangeable AI engines.

## Changes made

Updated:

- `README.md`;
- `README.fr.md`.

Added:

- `ai_logs/2026-05-30-public-readme-channel-framing.md`.

## Editorial intent

The previous hook described Pantheon as "a control method for professional
dossiers". This was accurate but abstract for a first-time reader.

Following `docs/governance/EDITORIAL_LANGUAGE.md`, the hook now starts from the
practitioner situation:

- Pantheon is positioned as the frame between the user, their usual tools and any
  AI engine, not as another AI;
- the engine (ChatGPT, Claude, Gemini, local model) is presented as
  interchangeable;
- a new distinction was made explicit: `answering ≠ acting`. The AI may draft an
  email; preparing is not sending; sending stays a visible human decision, or a
  bounded and traced action when the practitioner explicitly decides so;
- a short "in plain terms" list and contrast pairs were added for memorability;
- a new section, "From your usual channels" / "Depuis vos canaux habituels",
  names messaging apps (WhatsApp, Telegram), email and OpenWebUI as the surfaces
  the frame can sit behind.

The French and English versions were kept aligned.

## Honesty boundary

The named channels (WhatsApp, Telegram, email), assisted email sending, and
multi-engine routing are **not implemented**. They are described as method.

Both new sections close with an explicit pointer to `docs/governance/STATUS.md`
for what is actually available today. No "safe AI", "automatic sending" or
"compliant by design" promise was introduced, per the editorial guide.

## Explicit non-implementation

This intervention did not implement:

- channel connectors (WhatsApp, Telegram, email);
- email sending or assisted-send runtime;
- provider routing or multi-engine gateway;
- automatic approval;
- automatic memory promotion;
- any runtime behavior.

No files were modified under:

- `schemas/`;
- `tests/`;
- `operations/`;
- `hermes/`;
- Docker;
- `.env`;
- `pyproject.toml`;
- `CLAUDE.md`.

## Boundary phrase

```text
The README describes the conduct frame and the surfaces it can sit behind.
It does not connect, route, send or execute anything by itself.
```
