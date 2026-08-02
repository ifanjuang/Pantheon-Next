// Cockpit — LevelController.
//
// TRANSITIONAL: this is the demo's two-axis presentation, not the general
// target. The durable pieces are NavigationState, CollectionController and
// MotionAdapter; this file only arranges them as a parent/current/child deck.
// A desktop master/detail projection would replace it without touching state.
//
// Three level hosts exist and are recycled in place; the current host owns the
// single horizontal CollectionController and is never re-rendered from scratch.

import { createCollectionController } from "./collection_controller.js";
import { createDeckMotion } from "./motion_adapter.js";
import { renderPreview } from "./card_renderer.js";

const PARENT = 0;
const CURRENT = 1;
const CHILD = 2;

export function createLevelController({
  stage,
  renderItem,
  renderNew,
  renderPlaceholder,
  onActiveChange = () => {},
  onCommit = () => {},
  onMoveState = () => {},
}) {
  const host = document.createElement("div");
  host.className = "v3-level-host";
  stage.replaceChildren(host);

  let committing = false;
  let bounds = { previous: false, next: false };

  const deck = createDeckMotion({
    mount: host,
    hosts: 3,
    initial: CURRENT,
    direction: "vertical",
    label: "Navigation verticale entre les niveaux",
    onMoveState,
    onSettled(index) {
      if (committing || index === CURRENT) return;
      committing = true;
      if (index === CHILD && bounds.next) onCommit(1);
      else if (index === PARENT && bounds.previous) onCommit(-1);
      else {
        deck.goTo(CURRENT, { animate: true });
        committing = false;
      }
    },
  });

  // The single horizontal controller lives inside the current level host.
  const collectionHost = document.createElement("div");
  collectionHost.className = "v3-collection-host";
  deck.hostAt(CURRENT).append(collectionHost);

  const collection = createCollectionController({
    mount: collectionHost,
    renderItem,
    renderNew,
    renderPlaceholder,
    onActiveChange,
    onMoveState,
    label: "Cartes de la collection courante",
  });

  // Re-point the deck at the current stack position. Hosts are recycled: only
  // the two neighbour previews are replaced, the current host is left alone.
  function render({ snapshot, parentItem = null, childItem = null, canAscend = false, canDescend = false }) {
    committing = false;
    bounds = { previous: Boolean(canAscend), next: Boolean(canDescend) };

    deck.hostAt(PARENT).replaceChildren(renderPreview(parentItem));
    deck.hostAt(CHILD).replaceChildren(renderPreview(childItem));
    deck.setBounds(bounds);
    deck.goTo(CURRENT, { animate: false });

    return collection.load(snapshot);
  }

  function updateDescendability(canDescend) {
    bounds = { ...bounds, next: Boolean(canDescend) };
    deck.setBounds(bounds);
  }

  return Object.freeze({
    render,
    updateDescendability,
    collection,
    descend() { deck.move(1); },
    ascend() { deck.move(-1); },
    slidePrevCard() { collection.move(-1); },
    slideNextCard() { collection.move(1); },
    activeElement() { return collection.activeElement(); },
    dispose() {
      collection.dispose();
      deck.dispose();
    },
  });
}
