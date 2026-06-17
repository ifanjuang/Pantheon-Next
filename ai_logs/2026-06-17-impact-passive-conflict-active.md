# 2026-06-17 passive impact and active conflict distinction

Status: documented non-implemented.

Updated `docs/assets/pantheon-control/impact_conflict_lifecycle.md` to distinguish impact and conflict lifecycle:

- Applied impacts leave the active graph and become passive audit traces.
- Active conflicts remain active until resolution or validated reanalysis.
- Impact state and coherence / conflict state are separate axes.
- Preflight warnings now separate impacts to apply from conflicts to create.
- Transactions now mark impact links as applied/passive and conflict links as active.

No runtime, registry write, memory promotion, approval or external action was added.
