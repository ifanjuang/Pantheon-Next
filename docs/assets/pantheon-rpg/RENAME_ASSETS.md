# Pantheon RPG Asset Rename Plan

Status: executable local rename plan — documentation only.

This file defines the safe binary rename pass for Pantheon RPG README assets.

The current README already uses the correct boards, but it points to the temporary raw files such as `IMG_1452.jpeg`.

The goal of this pass is to replace raw filenames with stable semantic names.

## Why this exists

Binary image renaming should be done with `git mv` or an equivalent Git tree operation.

Do not rewrite binary JPG/JPEG files through a text-only API.

Do not copy base64 manually unless the binary integrity is verified.

## Rename commands

Run from repository root:

```bash
git mv docs/assets/pantheon-rpg/references/IMG_1452.jpeg docs/assets/pantheon-rpg/references/before_after_01_fr.jpg
git mv docs/assets/pantheon-rpg/references/IMG_1448.jpeg docs/assets/pantheon-rpg/references/ui_hermes_pantheon_01_fr.jpg
git mv docs/assets/pantheon-rpg/references/IMG_1446.jpeg docs/assets/pantheon-rpg/references/player_journey_01_fr.jpg
git mv docs/assets/pantheon-rpg/references/IMG_1451.jpeg docs/assets/pantheon-rpg/references/port_01_fr.jpg
git mv docs/assets/pantheon-rpg/references/IMG_1450.jpeg docs/assets/pantheon-rpg/references/evidence_01_fr.jpg
git mv docs/assets/pantheon-rpg/references/IMG_1457.jpeg docs/assets/pantheon-rpg/references/citadel_01_fr.jpg
git mv docs/assets/pantheon-rpg/references/IMG_1449.jpeg docs/assets/pantheon-rpg/references/memory_compartment_01_fr.jpg
git mv docs/assets/pantheon-rpg/references/IMG_1455.jpeg docs/assets/pantheon-rpg/references/pantheon_system_summary_01_fr.jpg
git mv docs/assets/pantheon-rpg/references/IMG_1454.jpeg docs/assets/pantheon-rpg/references/worldmap_ai_internet_01_fr.jpg
```

## README path replacements

After the rename, replace paths in `README.md`:

```text
docs/assets/pantheon-rpg/references/IMG_1452.jpeg
→ docs/assets/pantheon-rpg/references/before_after_01_fr.jpg

docs/assets/pantheon-rpg/references/IMG_1448.jpeg
→ docs/assets/pantheon-rpg/references/ui_hermes_pantheon_01_fr.jpg

docs/assets/pantheon-rpg/references/IMG_1446.jpeg
→ docs/assets/pantheon-rpg/references/player_journey_01_fr.jpg

docs/assets/pantheon-rpg/references/IMG_1451.jpeg
→ docs/assets/pantheon-rpg/references/port_01_fr.jpg

docs/assets/pantheon-rpg/references/IMG_1450.jpeg
→ docs/assets/pantheon-rpg/references/evidence_01_fr.jpg

docs/assets/pantheon-rpg/references/IMG_1457.jpeg
→ docs/assets/pantheon-rpg/references/citadel_01_fr.jpg

docs/assets/pantheon-rpg/references/IMG_1449.jpeg
→ docs/assets/pantheon-rpg/references/memory_compartment_01_fr.jpg

docs/assets/pantheon-rpg/references/IMG_1455.jpeg
→ docs/assets/pantheon-rpg/references/pantheon_system_summary_01_fr.jpg

docs/assets/pantheon-rpg/references/IMG_1454.jpeg
→ docs/assets/pantheon-rpg/references/worldmap_ai_internet_01_fr.jpg
```

## One-shot shell replacement

From repository root:

```bash
python - <<'PY'
from pathlib import Path

replacements = {
    'docs/assets/pantheon-rpg/references/IMG_1452.jpeg': 'docs/assets/pantheon-rpg/references/before_after_01_fr.jpg',
    'docs/assets/pantheon-rpg/references/IMG_1448.jpeg': 'docs/assets/pantheon-rpg/references/ui_hermes_pantheon_01_fr.jpg',
    'docs/assets/pantheon-rpg/references/IMG_1446.jpeg': 'docs/assets/pantheon-rpg/references/player_journey_01_fr.jpg',
    'docs/assets/pantheon-rpg/references/IMG_1451.jpeg': 'docs/assets/pantheon-rpg/references/port_01_fr.jpg',
    'docs/assets/pantheon-rpg/references/IMG_1450.jpeg': 'docs/assets/pantheon-rpg/references/evidence_01_fr.jpg',
    'docs/assets/pantheon-rpg/references/IMG_1457.jpeg': 'docs/assets/pantheon-rpg/references/citadel_01_fr.jpg',
    'docs/assets/pantheon-rpg/references/IMG_1449.jpeg': 'docs/assets/pantheon-rpg/references/memory_compartment_01_fr.jpg',
    'docs/assets/pantheon-rpg/references/IMG_1455.jpeg': 'docs/assets/pantheon-rpg/references/pantheon_system_summary_01_fr.jpg',
    'docs/assets/pantheon-rpg/references/IMG_1454.jpeg': 'docs/assets/pantheon-rpg/references/worldmap_ai_internet_01_fr.jpg',
}

for path in [Path('README.md'), Path('docs/assets/pantheon-rpg/ASSET_REGISTER.md')]:
    text = path.read_text(encoding='utf-8')
    for old, new in replacements.items():
        text = text.replace(old, new)
    path.write_text(text, encoding='utf-8')
PY
```

## Verification commands

```bash
git status --short

python - <<'PY'
from pathlib import Path

paths = [
    'docs/assets/pantheon-rpg/references/before_after_01_fr.jpg',
    'docs/assets/pantheon-rpg/references/ui_hermes_pantheon_01_fr.jpg',
    'docs/assets/pantheon-rpg/references/player_journey_01_fr.jpg',
    'docs/assets/pantheon-rpg/references/port_01_fr.jpg',
    'docs/assets/pantheon-rpg/references/evidence_01_fr.jpg',
    'docs/assets/pantheon-rpg/references/citadel_01_fr.jpg',
    'docs/assets/pantheon-rpg/references/memory_compartment_01_fr.jpg',
    'docs/assets/pantheon-rpg/references/pantheon_system_summary_01_fr.jpg',
    'docs/assets/pantheon-rpg/references/worldmap_ai_internet_01_fr.jpg',
]

missing = [p for p in paths if not Path(p).exists()]
if missing:
    raise SystemExit('Missing files:\n' + '\n'.join(missing))

for path in paths:
    if Path(path).stat().st_size < 1024:
        raise SystemExit(f'Suspiciously small image: {path}')

print('Asset rename verification passed.')
PY
```

## Commit message

```bash
git add README.md docs/assets/pantheon-rpg/ASSET_REGISTER.md docs/assets/pantheon-rpg/references
git commit -m "assets: rename Pantheon RPG boards to stable names"
```

## Boundary check

This pass must not modify:

- governance doctrine;
- runtime code;
- schemas;
- operations;
- tests;
- OpenWebUI integration;
- Hermes integration.

It is an asset hygiene pass only.
