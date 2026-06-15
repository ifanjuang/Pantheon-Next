# AI Log — flow2a mobile text overlap fix

**Date:** 2026-06-15
**Issue:** #131
**Branch:** claude/awesome-babbage-iwq2ym
**Scope:** `docs/index.html` mobile section of `responsive("#flow2a", ...)`

## Problème

La fonction `card()` mobile utilisait des offsets génériques (`y+25` pour le kicker, `y+(kicker?55:42)` pour le titre, `y+h-20` pour le sous-texte) qui ne tenaient pas compte des petites hauteurs de cartes. Résultat : sur plusieurs cartes, le sous-texte apparaissait au-dessus du titre, et pour les cartes avec kicker de hauteur ≤52px le titre débordait hors de la carte.

Cartes affectées : Corpus, Contexte, Workflow IA, Résultat candidat qualifié, Décision, Action externe, Mémoire.

## Correction appliquée

Remplacement de la fonction `card()` mobile par deux helpers explicites :

- **`cardKicker(x,y,w,h,...,kicker,title,sub,o)`** — pour les cartes avec kicker (MATIÈRE, ATELIER, HUMAIN · ARBITRAGE). Positionne les trois lignes en proportions de h (`h*0.28`, `h*0.56` ou `h*0.60`, `h*0.84`), garantissant l'absence de chevauchement quelle que soit la hauteur.
- **`cardPlain(x,y,w,h,...,title,sub,o)`** — pour les cartes sans kicker. Si sous-texte présent : titre à `h*0.40`, sous-texte à `h*0.76`. Sinon : titre centré à `h/2+4`.

Les appels `card(...)` ont été convertis vers `cardKicker` ou `cardPlain` selon la présence d'un kicker.

## Périmètre

- Uniquement le bloc mobile de `responsive("#flow2a", ...)`.
- Aucun autre diagramme touché (`#flow2b`, `#flow3`, `dossierFlow`).
- Rendu desktop inchangé.
- Aucun chemin protégé touché.
- Vocabulaire validé conservé intégralement.

## Fichiers modifiés

- `docs/index.html` — section mobile flow2a uniquement
- `ai_logs/2026-06-15-flow2a-mobile-text-overlap-fix.md` — ce fichier
