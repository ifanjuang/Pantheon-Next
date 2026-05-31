# AI Log — Align README and landing page with the modular reorientation

Date: 2026-05-31

## Scope

After review, the public README and the GitHub Pages landing page were checked
against `docs/governance/MODULAR_DOMAIN_REORIENTATION.md` (#24). Two coherence
gaps were found and fixed.

## Problem found

1. **README presented Pantheon as a funnel.** The hook diagram and prose showed
   everything flowing through Pantheon (`you -> [Pantheon: what enters] -> AI ->
   [Pantheon: what leaves]`, "Pantheon sends the AI only the minimum context",
   and a Mermaid diagram drawing `OW -> TC -> CP -> Hermes -> engine`). The
   reorientation states the opposite: Pantheon is not a funnel; it attaches only
   at consequential decisions, and the tools (OpenWebUI, Hermes) carry the work,
   including pre-transmission minimization executed by Hermes under Pantheon's
   rule.

2. **Landing page missed two pillars.** It was governance/agent-framed only:
   no tool-agnostic / interchangeable-bindings notion, and no professional
   methodology / domain-pack dimension — both central to the reorientation and
   to the README's professional framing.

## Changes made

Updated:

- `README.md`;
- `README.fr.md`;
- `docs/index.html`.

Added:

- `ai_logs/2026-05-31-align-readme-page-with-reorientation.md`.

### README (FR + EN)

- hook ascii reframed: tools carry the work (`you -> prepare -> AI -> return ->
  you decide`); Pantheon governs the line (what enters / leaves / remains);
- "Pantheon sends the AI only the minimum" -> "only the minimum reaches the AI
  ... that is Pantheon's rule, your tools carry it out";
- the module diagram replaced (and revalidated, `valid: true`) with a
  tools-carry / Pantheon-attaches-only-at-consequential-decisions model: a WORK
  subgraph `OpenWebUI <-> Hermes <-> interchangeable engines`, and a PANTHEON
  subgraph attaching the rule (dotted), the decision gate and scoped memory;
- closing line now states "most of the work never needs Pantheon" and links
  `CORE_CONCEPTS_MAP.md` and `MODULAR_DOMAIN_REORIENTATION.md`.

### Landing page (`docs/index.html`)

- hero lead bridged to the professional audience (architect, lawyer, doctor,
  accountant who answers for what they sign);
- new section "Une méthode, deux projections": domain pack (single source, 11
  sections), bindings registry (interchangeable tools), "pas un entonnoir"
  (consequential decisions only);
- two link cards added: `MODULAR_DOMAIN_REORIENTATION.md`, `DOMAIN_PACK_SPEC.md`.

## Input used

A user-provided deep-research document on AI for architecture practice
management informed this alignment. It corroborated the reorientation: "branch
AI onto the firm's document system, not the firm onto a chatbot", a cible
pipeline whose only consequential point is human review/signature, and a legal
basis for answering-not-acting (code de déontologie, loi sur l'architecture,
MAF). Product names from that document were intentionally NOT carried into the
governance body (they belong in the bindings registry); citation tokens from the
source tool were not copied.

## Honesty boundary

No runtime added. The README still describes method, not implemented behavior;
`STATUS.md` remains the authority. The diagram is a relationship model. The new
landing-page section describes the projection model as doctrine, not as a
shipped feature.

## Explicit non-implementation

No files touched under `schemas/`, `tests/`, `hermes/`, `operations/`,
`pyproject.toml`, or `CLAUDE.md`.
