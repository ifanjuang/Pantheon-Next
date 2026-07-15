# AI log — honest packaging and release contract

Date: 2026-07-15

## Decision

Option A is adopted: the repository root is a governance/documentation
workspace and is deliberately non-distributable. `mcp-server/` is the only
claimed Python distribution. Root validation dependencies are installed
explicitly without installing Pantheon Next as a library.

## Changes

- removed accidental root project/build metadata and retained tool
  configuration only;
- added an explicit rejection shim so fallback packaging tools report the
  intentional non-distributable contract instead of accidental auto-discovery;
- declared `VERSION` authoritative, with the changelog head and MCP metadata as
  CI-checked mirrors;
- made runtime `__version__` read installed `pantheon-mcp-server` metadata;
- modernized the MCP licence field to the SPDX string `MIT`;
- documented root rejection, development/test commands and release/tag rules;
- corrected earlier false or pending tag claims: the existing changelog entries
  are repository checkpoints, not published releases;
- added CI that rejects root packaging, runs root tests, builds and inspects the
  MCP wheel, installs it cleanly and compares runtime/metadata versions.

## Boundary

Packaging the read-only MCP surface does not make Pantheon a runtime. No
executor, installer, scheduler, queue, provider router, MCP host, plugin manager,
approval engine or memory engine is added.
