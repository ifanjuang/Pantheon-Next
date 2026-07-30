// Cockpit — LiveProvider.
//
// The live half of
//
//   DemoProvider ─┐
//                 ├→ CockpitSnapshot → same cockpit
//   LiveProvider ─┘
//
// Wraps what the live schema renderer already holds (the resolved sibling
// collection and the current position) into the same versioned envelope the
// demo produces. It projects; it does not fetch, decide or authorize.

import { createSnapshot } from "../collection/cockpit_snapshot.js";

export function createLiveProvider() {
  // `siblings` are the card models the live renderer resolved for the current
  // collection; `key` is its stable identity (the chosen parents).
  function toSnapshot({ key, siblings = [], index = 0, path = [], space = null, revision = null }) {
    const warnings = [];
    const identified = siblings.filter(item => item && item.entity_id);
    if (identified.length !== siblings.length) {
      warnings.push("Des cartes sans identité stable ont été écartées de la projection.");
    }

    return createSnapshot({
      source: "live",
      revision,
      space,
      collection: { id: key, title: "", canCreate: false },
      // The cockpit contract keys identity on `id`.
      items: identified.map(model => ({ ...model, id: model.entity_id })),
      index,
      path,
      warnings,
    });
  }

  return Object.freeze({ toSnapshot });
}
