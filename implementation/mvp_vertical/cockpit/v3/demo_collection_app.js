// Cockpit demo — fictional agency universe.
//
// Wiring only. The business projection lives in the DemoProvider, which emits
// CockpitSnapshots; the cockpit core consumes the same shape the live path
// produces. Every motion concern belongs to the MotionAdapter.

import { createLevelController } from "./collection/level_controller.js";
import { renderCard, renderPlaceholder, renderNewSlide } from "./collection/card_renderer.js";
import { createDemoProvider } from "./providers/demo_provider.js";

const SWIPER_VERSION = "14.0.7";
const stage = document.getElementById("v2-stage");
const breadcrumb = document.getElementById("v2-breadcrumb");
const status = document.getElementById("v2-status");
const network = document.getElementById("v2-network");
const spaceButtons = [...document.querySelectorAll("[data-space]")];

if (!stage) throw new Error("Cockpit stage unavailable");

async function ensureSwiper() {
  if (typeof window.Swiper === "function") return;
  const candidates = [
    `https://cdn.jsdelivr.net/npm/swiper@${SWIPER_VERSION}/swiper-bundle.min.js`,
    `https://unpkg.com/swiper@${SWIPER_VERSION}/swiper-bundle.min.js`,
  ];
  for (const src of candidates) {
    try {
      await new Promise((resolve, reject) => {
        const script = document.createElement("script");
        script.src = src;
        script.async = true;
        script.onload = resolve;
        script.onerror = () => reject(new Error(`Swiper unavailable: ${src}`));
        document.head.append(script);
      });
      if (typeof window.Swiper === "function") return;
    } catch (_) {
      // Try next CDN.
    }
  }
  throw new Error("Swiper runtime unavailable");
}

const fixture = await fetch("demo-data.json", { cache: "no-store" }).then(response => {
  if (!response.ok) throw new Error(`Fixture indisponible (${response.status})`);
  return response.json();
});

await ensureSwiper();

document.documentElement.dataset.swiperReady = "true";
document.documentElement.dataset.swiperVersion = SWIPER_VERSION;
document.documentElement.dataset.cockpitMode = "demo";
window.PANTHEON_COCKPIT_DEMO = true;
if (network) network.textContent = "démo · données fictives";

const provider = createDemoProvider(fixture);
const stack = [];

function currentFrame() {
  return stack[stack.length - 1];
}

function activeItem(frame) {
  if (!frame || frame.activeSynthetic) return null;
  return frame.items[frame.index] || null;
}

function childCollectionFor(frame) {
  const collection = provider.collectionFor(activeItem(frame));
  return collection?.items?.length ? collection : null;
}

function parentItemFor() {
  return stack.length < 2 ? null : activeItem(stack[stack.length - 2]);
}

function createFrame(collection, rootSpace) {
  return { ...collection, index: 0, activeSynthetic: false, rootSpace };
}

function setFlipState(card, flipped) {
  if (!card) return;
  const front = card.querySelector(".card-front");
  const back = card.querySelector(".card-back");
  card.dataset.flipped = flipped ? "true" : "false";
  card.setAttribute("aria-pressed", flipped ? "true" : "false");
  front?.setAttribute("aria-hidden", flipped ? "true" : "false");
  back?.setAttribute("aria-hidden", flipped ? "false" : "true");
}

function toggleFlip(card) {
  if (!card) return;
  setFlipState(card, card.dataset.flipped !== "true");
}

function bindFlip(card) {
  let pointerId = null;
  let startX = 0;
  let startY = 0;
  let dragged = false;

  setFlipState(card, false);

  card.addEventListener("pointerdown", event => {
    pointerId = event.pointerId;
    startX = event.clientX;
    startY = event.clientY;
    dragged = false;
  }, { passive: true });

  card.addEventListener("pointermove", event => {
    if (event.pointerId !== pointerId) return;
    if (Math.hypot(event.clientX - startX, event.clientY - startY) > 8) dragged = true;
  }, { passive: true });

  card.addEventListener("pointercancel", () => {
    pointerId = null;
    dragged = true;
  }, { passive: true });

  card.addEventListener("click", event => {
    pointerId = null;
    if (dragged || stage.dataset.swiperMoving === "true" || event.target.closest("button,a,input,textarea,select")) {
      dragged = false;
      return;
    }
    toggleFlip(card);
  });

  card.addEventListener("keydown", event => {
    if (event.key !== "Enter" && event.key !== " ") return;
    if (event.target.closest("button,a,input,textarea,select")) return;
    event.preventDefault();
    toggleFlip(card);
  });
}

const level = createLevelController({
  stage,
  renderItem(item) {
    const card = renderCard(item, { hydrated: true, interactive: true });
    bindFlip(card);
    return card;
  },
  renderNew(collection) {
    return renderNewSlide(collection, col => stage.dispatchEvent(new CustomEvent("pantheon:create-requested", { bubbles: true, detail: { collection_id: col.id } })));
  },
  renderPlaceholder,
  onActiveChange(item, index, meta) {
    const frame = currentFrame();
    if (!frame) return;
    frame.activeSynthetic = meta?.synthetic === "create";
    if (!frame.activeSynthetic && index >= 0) frame.index = index;
    level.updateDescendability(Boolean(childCollectionFor(frame)));
    updateLocation();
  },
  onCommit(direction) {
    if (direction > 0) {
      const child = childCollectionFor(currentFrame());
      if (child) stack.push(createFrame(child, currentFrame().rootSpace));
    } else if (stack.length > 1) {
      stack.pop();
    }
    renderDeck();
  },
  onMoveState(moving) {
    if (moving) stage.dataset.swiperMoving = "true";
    else delete stage.dataset.swiperMoving;
  },
});

function updateLocation() {
  if (breadcrumb) breadcrumb.textContent = stack.map(frame => frame.title).join(" / ");
  const frame = currentFrame();
  const active = activeItem(frame);
  if (status) {
    status.textContent = frame.activeSynthetic
      ? `Créer dans ${frame.title}`
      : active ? `${frame.items.length} carte(s) · ${active.title}` : "Collection vide";
  }
  spaceButtons.forEach(button => button.classList.toggle("is-active", frame.rootSpace === button.dataset.space));
}

function renderDeck() {
  const frame = currentFrame();
  const child = childCollectionFor(frame);
  const snapshot = provider.toSnapshot(frame, {
    index: frame.index,
    space: { id: frame.rootSpace, title: frame.title },
    path: stack.map(item => ({ collection_id: item.id, entity_id: activeItem(item)?.id ?? null })),
  });

  const result = level.render({
    snapshot,
    parentItem: parentItemFor(),
    childItem: child?.items?.[0] || null,
    canAscend: stack.length > 1,
    canDescend: Boolean(child),
  });

  if (result && result.ok === false && status) {
    status.textContent = `Projection refusée : ${result.reason}`;
    return;
  }
  updateLocation();
}

spaceButtons.forEach(button => button.addEventListener("click", () => {
  const index = provider.rootItems.findIndex(item => item.id === `space:${button.dataset.space}`);
  if (index < 0) return;
  stack.splice(1);
  stack[0].index = index;
  stack[0].activeSynthetic = false;
  renderDeck();
}));

document.getElementById("v2-descend")?.addEventListener("click", () => level.descend());
document.getElementById("v2-ascend")?.addEventListener("click", () => level.ascend());
document.getElementById("v2-previous")?.addEventListener("click", () => level.slidePrevCard());
document.getElementById("v2-next")?.addEventListener("click", () => level.slideNextCard());
document.getElementById("v2-flip")?.addEventListener("click", () => {
  toggleFlip(level.activeElement()?.querySelector(".card"));
});

window.addEventListener("pagehide", () => level.dispose(), { once: true });

stack.push(createFrame(provider.rootCollection(), "pantheon"));
renderDeck();
