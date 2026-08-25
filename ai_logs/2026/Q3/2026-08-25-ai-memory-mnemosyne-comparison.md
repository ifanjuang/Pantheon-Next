# 2026-08-25 — ai-memory vs Mnemosyne comparison checkpoint

Purpose: refresh the external runtime-memory comparison on current Pantheon main without adopting a new provider or changing memory authority.

Pantheon baseline:

```text
0f834822cab34268696112971500c454d213a4fa
```

Rechecked upstream identities:

```text
ai-memory 1.32.0
c304ff6ecba54b05c488345e2c4b0bba81cb9574

Mnemosyne main
8e6c010bc823b7833061f0ee53c2a73a9dd6dd24

ai-memory Hermes plugin main
8e61b19b7481c86ece5ee24285e74514daf2398c

plugin compatibility PR #2
open, head af8885b35ebb00ff0199fb01f44b4d3f77c31bd3
validated upstream only against ai-memory 1.28.1 / Hermes 0.20.5
```

Observed interpretation:

```text
Mnemosyne
= stronger current fit for fluid Hermes conversational/runtime memory

ai-memory
= stronger conceptual fit for explicit cross-session/cross-agent workstream handoff

Hindsight
= separate workspace/document retrieval responsibility
```

Decision posture:

```text
KEEP Mnemosyne current observed runtime path
KEEP Hindsight separate
QUALIFY ai-memory only as possible Mnemosyne successor
DO NOT activate ai-memory
DO NOT run two steady-state fluid runtime memories
```

Main blocking uncertainty: current Hermes compatibility for ai-memory 1.32.0 is not demonstrated because the community plugin fix remains unmerged and its reported validation matrix is older.

Governance boundaries retained:

```text
memory recalled != truth
memory artifact != Evidence
handoff delivered != authorization
runtime write success != ingestion authority
folder/path != governed identity
```

No runtime, dependency, Docker, provider configuration, Hindsight path, Pantheon state or Evidence path was changed by this checkpoint.
