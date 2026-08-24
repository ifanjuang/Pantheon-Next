# Hindsight / Obsidian architecture audit — sequencing note

Date: 2026-08-24
Status: audit-start note only — no Hindsight/Obsidian change

During operator-path convergence, a fresh repository review confirmed that Hindsight/Obsidian optimization is the next functional architecture tranche, ahead of the separate Revit convergence.

Observed current authorities/work items:

- `docs/governance/OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md` is the current workspace topology doctrine;
- issue #659 is open and blocks broader IFJA durable-bank use pending Hindsight hardening, private/authenticated exposure, one ingestion authority, removal of Hermes durable writes unless re-qualified, restore drill and outage/recovery proof;
- issue #660 is open and currently frames Obsidian synchronization around Self-hosted LiveSync/CouchDB plus optional Obsidian Web;
- PR #685 separately records Hermes runtime-memory provider qualification; runtime conversation memory must remain distinct from Hindsight workspace retrieval;
- current user direction is reconsidering the synchronization transport, including Remotely Save, therefore #660 is a candidate requirement to re-evaluate, not an implementation instruction to execute unchanged.

Planned convergence order after the operator-path PR reaches CI:

```text
1. verify latest Hindsight + hindsight-obsidian + Obsidian synchronization candidates
2. close or revise #659 around one durable ingestion authority and bounded MCP read exposure
3. compare LiveSync/CouchDB vs Remotely Save against the actual NAS/PC/mobile topology
4. revise #660 to the selected synchronization responsibility
5. qualify synthetic sync + conflict/offline/recovery
6. connect exactly one Obsidian-derived producer to each durable Hindsight bank
7. keep Hermes Hindsight access bounded/read-oriented unless an explicit write authority is later approved
```

Target simplification:

```text
Obsidian Markdown = intentional human workspace/source notes
sync layer         = file/vault synchronization only
Hindsight          = derived associative retrieval/index
Hermes             = retrieval + reasoning + candidate generation
Mnemosyne/provider = runtime conversational memory, separate responsibility
Pantheon           = governed professional state / Evidence boundaries
```

No new memory registry, provider router, scheduler or second ingestion path is proposed.

Invariants:

```text
sync != memory
memory != source
retrieved != truth
memory != Evidence
bank != project identity
folder != governed identity
MCP tool available != write authorized
technical write success != ingestion authority
```
