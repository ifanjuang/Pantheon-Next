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
    return createSnapshot({
      source: "live",
      revision,
      space,
      collection: { id: key, title: "", canCreate: false },
      // Preserve every projected item. The CockpitSnapshot reader owns
      // validation and must visibly refuse an item without stable identity;
      // the provider must never turn invalid input into a partial success.
      items: siblings.map(model => (
        model && typeof model === "object"
          ? { ...model, id: model.entity_id }
          : model
      )),
      index,
      path,
    });
  }

  return Object.freeze({ toSnapshot });
}
