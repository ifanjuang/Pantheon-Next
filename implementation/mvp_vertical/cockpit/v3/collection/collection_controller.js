// Cockpit — CollectionController.
//
// Binds the independent pieces together and owns none of their concerns:
//
//   CockpitSnapshot (input) · NavigationState (data) · MotionAdapter (motion)
//
// It accepts exactly one input shape — a CockpitSnapshot — so the demo and the
// live path drive the same cockpit. The rest of the cockpit talks to this
// controller, never to Swiper. Only the active projection and its two
// neighbours are ever mounted; the collection stays in state as data.

import { createNavigationState } from "./navigation_state.js";
import { createWindowedMotion } from "./motion_adapter.js";
import { loadCollection } from "./collection_provider.js";
import { readSnapshot, collectionOf, activeIndexOf } from "./cockpit_snapshot.js";

export function createCollectionController({
  mount,
  renderItem,
  renderNew = () => null,
  renderPlaceholder,
  renderEmpty = null,
  renderRefusal = null,
  onActiveChange = () => {},
  onMoveState = () => {},
  onRefusal = () => {},
  state = null,
  label = "",
}) {
  if (typeof renderItem !== "function") throw new Error("CollectionController requires renderItem");
  if (typeof renderPlaceholder !== "function") throw new Error("CollectionController requires renderPlaceholder");

  const navigation = state || createNavigationState();
  let collection = { id: null, title: "", canCreate: false };
  let refused = null;
  let cancelLoad = null;
  let syncing = false;
  let refreshFrame = 0;

  const offset = () => (collection.canCreate && !refused ? 1 : 0);

  function renderAt(virtualIndex) {
    if (refused) return renderRefusalNode(refused);
    if (offset() && virtualIndex === 0) return renderNew(collection);

    const itemIndex = virtualIndex - offset();
    const item = navigation.itemAt(itemIndex);
    if (!item) {
      const snapshot = navigation.snapshot();
      if (snapshot.loading || !renderEmpty) return renderPlaceholder();
      return renderEmpty(collection);
    }
    return renderItem(item, {
      active: itemIndex === navigation.snapshot().activeIndex,
      index: itemIndex,
    });
  }

  // A refused snapshot stays visible as a refusal. It is never downgraded to an
  // empty collection or a silent success.
  function renderRefusalNode(result) {
    if (renderRefusal) return renderRefusal(result);
    const node = document.createElement("p");
    node.className = "v2-empty";
    node.setAttribute("role", "status");
    node.textContent = `Projection refusée (${result.reason}). ${result.detail || ""}`.trim();
    return node;
  }

  const motion = createWindowedMotion({
    mount,
    renderAt,
    label,
    onMoveState,
    onIndexChange(virtualIndex) {
      if (refused) return;
      if (offset() && virtualIndex === 0) {
        onActiveChange(null, -1, { synthetic: "create", collection });
        return;
      }
      syncing = true;
      navigation.setIndex(virtualIndex - offset());
      syncing = false;
      scheduleRefresh();
      const snapshot = navigation.snapshot();
      onActiveChange(snapshot.activeItem, snapshot.activeIndex, { synthetic: null, collection });
    },
  });

  // Re-produce the mounted window so the newly active projection becomes the
  // interactive one and its neighbours fall back to inert previews.
  function scheduleRefresh() {
    window.cancelAnimationFrame(refreshFrame);
    refreshFrame = window.requestAnimationFrame(() => {
      refreshFrame = 0;
      motion.refresh();
    });
  }

  function projectionCount() {
    if (refused) return 1;
    return offset() + (navigation.snapshot().itemCount || 1);
  }

  function syncMotion() {
    const snapshot = navigation.snapshot();
    motion.mount(projectionCount(), Math.max(0, snapshot.activeIndex) + offset());
  }

  navigation.subscribe(() => {
    if (syncing || refused) return;
    // Items arrived (or the collection changed) while we were not driving.
    motion.extendTo(projectionCount());
    scheduleRefresh();
  });

  // Load a CockpitSnapshot. Returns the validation result so a caller can react
  // to a refusal; the refusal is rendered either way.
  function load(payload) {
    cancelLoad?.();
    const result = readSnapshot(payload);

    if (!result.ok) {
      refused = result;
      collection = { id: null, title: "", canCreate: false };
      navigation.setCollection({ collectionId: null, items: [], index: 0, loading: false });
      syncMotion();
      motion.refresh();
      onRefusal(result);
      return result;
    }

    refused = null;
    const snapshot = result.snapshot;
    collection = collectionOf(snapshot);
    cancelLoad = loadCollection(navigation, collection, snapshot.items, activeIndexOf(snapshot));
    syncMotion();

    const current = navigation.snapshot();
    onActiveChange(current.activeItem, current.activeIndex, { synthetic: null, collection });
    return result;
  }

  return Object.freeze({
    state: navigation,
    load,
    move(delta) { motion.move(delta); },
    goTo(index) { motion.goTo(index + offset(), { animate: false }); },
    refresh() { motion.refresh(); },
    activeElement() { return motion.activeElement(); },
    lock() { motion.lock(); },
    unlock() { motion.unlock(); },
    dispose() {
      cancelLoad?.();
      window.cancelAnimationFrame(refreshFrame);
      motion.dispose();
    },
    get collection() { return collection; },
    get refusal() { return refused; },
  });
}
