# Pantheon RPG City Memory Export Provenance Update

Date: 2026-05-15

## Scope

Updated repository documentation for the Pantheon RPG visual system, specifically planche 2 / governed memory city.

## User request

The user asked to drop the accepted memory mechanism image into the repository for the Pantheon memory mechanism planche.

## Action performed

The generated PNG candidate was identified locally and recorded in provenance and status documentation.

Recorded candidate:

```text
Local generated file: /mnt/data/isometric_map_of_a_medieval_city_complex.png
Planned repository path: docs/assets/pantheon-rpg/exports/pantheon-rpg-city-memory-v01.png
Format: PNG
Dimensions: 1448 x 1086 px
Size: 3,448,189 bytes
SHA256: 7200154131d9e071700975c8d71769cabefc997ea4ecbbbe927d274c32bed80e
```

Updated files:

```text
docs/assets/pantheon-rpg/exports/pantheon-rpg-city-memory-v01.provenance.md
docs/assets/pantheon-rpg/STATUS.md
```

## Limitation

The available GitHub connector write path in this session supports UTF-8 text file operations and did not provide a direct binary PNG upload path.

Therefore, the binary image itself was not committed to the repository in this intervention.

The provenance note and status file now document the exact expected repository path and file metadata for the future binary drop.

## Doctrine boundary

This intervention adds visual asset documentation only.

It does not implement or modify:

- execution runtime;
- agent runtime;
- tool runtime;
- provider routing;
- scheduler;
- workflow engine;
- memory auto-promotion;
- OpenWebUI canonical memory;
- Hermes governance authority.

## Follow-up

When a binary-capable repository upload path is available, add the PNG at:

```text
docs/assets/pantheon-rpg/exports/pantheon-rpg-city-memory-v01.png
```

Then update the provenance note to:

```text
Review status: accepted export committed
```
