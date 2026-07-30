// Cockpit — CockpitSnapshot contract.
//
// The single projection shape the cockpit consumes, whatever produces it (demo
// fixture, live renderer, or a future server endpoint). Pure data: no DOM, no
// Swiper, no rendering.
//
//   {
//     snapshot_version, generated_at, revision, source,
//     space: { id, title },
//     collection: { id, title, can_create },
//     items: [ { id, title, ... } ],
//     navigation: { active_index, active_entity_id, path },
//     warnings: []
//   }
//
// The cockpit refuses a snapshot it does not understand instead of guessing:
// an incompatible payload stays visible as a refusal, never a silent success.
//
// `actions` and `schemas` are reserved for server-owned contracts. They are
// carried through untouched and deliberately NOT interpreted here: the cockpit
// displays what a server exposes, it does not decide what is authorized.
//
//   visible != authorized

export const SNAPSHOT_VERSION = "cockpit.snapshot.v1";

const REFUSALS = Object.freeze({
  NOT_AN_OBJECT: "snapshot_not_an_object",
  INCOMPATIBLE_VERSION: "snapshot_incompatible_version",
  INVALID_ITEMS: "snapshot_invalid_items",
  ITEM_WITHOUT_IDENTITY: "snapshot_item_without_identity",
});

export const SNAPSHOT_REFUSALS = REFUSALS;

// Build a snapshot from a producer that already holds trusted projections.
export function createSnapshot({
  space = null,
  collection = null,
  items = [],
  index = 0,
  path = [],
  warnings = [],
  revision = null,
  source = "unknown",
  generatedAt = null,
  actions = null,
  schemas = null,
} = {}) {
  const list = Array.isArray(items) ? items : [];
  const activeIndex = list.length ? clamp(index, 0, list.length - 1) : -1;

  const snapshot = {
    snapshot_version: SNAPSHOT_VERSION,
    generated_at: generatedAt || new Date().toISOString(),
    revision,
    source,
    space: space ? { id: space.id ?? null, title: space.title ?? "" } : null,
    collection: {
      id: collection?.id ?? null,
      title: collection?.title ?? "",
      can_create: Boolean(collection?.canCreate ?? collection?.can_create),
    },
    items: list,
    navigation: {
      active_index: activeIndex,
      active_entity_id: activeIndex >= 0 ? list[activeIndex]?.id ?? null : null,
      path: Array.isArray(path) ? path.slice() : [],
    },
    warnings: Array.isArray(warnings) ? warnings.slice() : [],
  };

  // Reserved, server-owned; carried through without interpretation.
  if (actions) snapshot.actions = actions;
  if (schemas) snapshot.schemas = schemas;
  return snapshot;
}

// Validate an incoming payload. Returns { ok: true, snapshot } or
// { ok: false, reason, detail } — never a partially-coerced snapshot.
export function readSnapshot(payload) {
  if (!payload || typeof payload !== "object" || Array.isArray(payload)) {
    return refusal(REFUSALS.NOT_AN_OBJECT, "A snapshot must be an object.");
  }
  if (payload.snapshot_version !== SNAPSHOT_VERSION) {
    return refusal(
      REFUSALS.INCOMPATIBLE_VERSION,
      `Expected ${SNAPSHOT_VERSION}, received ${String(payload.snapshot_version)}.`,
    );
  }
  if (!Array.isArray(payload.items)) {
    return refusal(REFUSALS.INVALID_ITEMS, "`items` must be an array.");
  }
  const orphan = payload.items.findIndex(item => !item || item.id == null || item.id === "");
  if (orphan >= 0) {
    return refusal(
      REFUSALS.ITEM_WITHOUT_IDENTITY,
      `Item at index ${orphan} has no stable identity.`,
    );
  }
  return { ok: true, snapshot: payload };
}

// Convenience for consumers that hold a validated snapshot.
export function collectionOf(snapshot) {
  return {
    id: snapshot.collection?.id ?? null,
    title: snapshot.collection?.title ?? "",
    canCreate: Boolean(snapshot.collection?.can_create),
    spaceId: snapshot.space?.id ?? null,
  };
}

export function activeIndexOf(snapshot) {
  const index = snapshot.navigation?.active_index;
  return Number.isInteger(index) && index >= 0 ? index : 0;
}

function refusal(reason, detail) {
  return { ok: false, reason, detail };
}

function clamp(value, min, max) {
  const numeric = Number.isFinite(value) ? value : min;
  return Math.max(min, Math.min(max, numeric));
}
