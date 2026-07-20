# Native Hermes multi-model deliberation candidate

Date: 2026-07-19

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

- Added a disabled native Hermes MoA configuration fragment.
- Added bounded deliberation handoff and return candidate templates.
- Added a ready-to-fill two-pass prompt template for the named MoA preset.
- Updated the Hermes integration boundary with a one-pass plus optional
  challenge-pass protocol tied to Work Issues and Hermes runs.
- Clarified that model plurality does not create Pantheon Role authority.
- Recorded the candidate honestly in `WHAT_RUNS.md` and the Hermes template map.

## Why

Occasional comparison between OpenAI, Claude and other models can expose blind
spots in Pantheon doctrine, UX and implementation proposals. Hermes Agent
`0.18.2` already provides the appropriate external binding through native
Mixture of Agents presets, so Pantheon should govern that surface rather than
invent another orchestrator.

The upstream capability was reviewed at commit
`e361c5e20402375c74a65ca52810c6a380461226`. Native MoA runs reference models
without tools, then gives their advice to one acting aggregator model.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none in this repository; external Hermes configuration remains inactive.
Authority impact: active integration doctrine clarified; no new Pantheon Role.
Schema/test/CI impact: none.
External action: none.
Memory behavior: deliberation output remains candidate; automatic promotion forbidden.

## Local distinctions

```text
model plurality != role authority
aggregator synthesis != ZEUS arbitration
model agreement != evidence
enabled preset != authorized data exposure
deliberation returned != issue resolved
```
