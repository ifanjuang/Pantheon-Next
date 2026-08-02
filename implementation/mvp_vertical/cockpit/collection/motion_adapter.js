// Cockpit — MotionAdapter.
//
// The only module that knows Swiper exists. It exposes a deliberately small
// surface:
//
//   mount() · goTo(index) · lock() · unlock() · dispose()
//
// The cockpit never calls appendSlide(), removeAllSlides() or updateSlides():
// those stay internal here, so Swiper can later be swapped for CSS scroll-snap,
// a grid, a list or a desktop master/detail view without touching the cockpit.

// Swiper's own defaults are used for everything, including `speed`: during a
// drag the card follows the finger (followFinger), so `speed` only governs the
// settle after release, and 300ms is what Swiper tunes its easing around.
//
// One override remains, and it is not cosmetic: without `noSwipingSelector`,
// a drag starting inside a form control swipes the deck instead of interacting
// with the control. Measured in Chromium — dragging inside a text field moved
// the deck from card 0 to card 1, making selection impossible. The live cockpit
// renders its editors inside cards, so this must stay.
const BASE_OPTIONS = Object.freeze({
  noSwipingSelector: "button,input,select,textarea,a,[contenteditable='true']",
});

function requireSwiper() {
  if (typeof window.Swiper !== "function") throw new Error("Swiper runtime unavailable");
}

function createShell(mount, className, label) {
  const shell = document.createElement("div");
  shell.className = className;
  if (label) {
    shell.setAttribute("role", "region");
    shell.setAttribute("aria-roledescription", "carrousel");
    shell.setAttribute("aria-label", label);
  }
  const wrapper = document.createElement("div");
  // `v2-swiper-wrapper` is what the V3 geometry stylesheet sizes.
  wrapper.className = "swiper-wrapper v2-swiper-wrapper";
  shell.append(wrapper);
  mount.append(shell);
  return shell;
}

// Windowed motion: only the active projection and its two neighbours are ever
// mounted in the DOM (Swiper's Virtual slides). The collection itself stays in
// NavigationState as data.
export function createWindowedMotion({
  mount,
  renderAt,
  onIndexChange = () => {},
  onMoveState = () => {},
  direction = "horizontal",
  label = "",
}) {
  requireSwiper();
  if (!mount) throw new Error("MotionAdapter requires a mount element");
  if (typeof renderAt !== "function") throw new Error("MotionAdapter requires renderAt");

  const shell = createShell(mount, "swiper v3-swiper v3-collection-swiper", label);
  let count = 0;

  const swiper = new window.Swiper(shell, {
    ...BASE_OPTIONS,
    direction,
    nested: direction === "horizontal",
    virtual: {
      enabled: true,
      cache: false,
      // Exactly one projection on each side of the active one.
      addSlidesBefore: 1,
      addSlidesAfter: 1,
      slides: [],
      renderSlide(_item, index) {
        const slide = document.createElement("div");
        slide.className = "swiper-slide v2-swiper-slide v3-swiper-slide";
        const node = renderAt(index);
        if (node) slide.append(node);
        return slide;
      },
    },
    on: {
      touchStart() { onMoveState(true); },
      sliderMove() { onMoveState(true); },
      touchEnd(instance) { if (!instance.animating) onMoveState(false); },
      slideChange(instance) { onIndexChange(instance.activeIndex); },
      slideChangeTransitionEnd() { onMoveState(false); },
    },
  });

  // (Re)bind to `nextCount` virtual projections and position on `index`.
  function mountCount(nextCount, index = 0) {
    count = Math.max(0, Number(nextCount) || 0);
    swiper.virtual.slides = new Array(count).fill(null).map((_, position) => position);
    swiper.virtual.update(true);
    goTo(index, { animate: false });
  }

  // Grow the window when a progressive source yields more projections.
  function extendTo(nextCount) {
    if (nextCount <= count) return;
    for (let position = count; position < nextCount; position += 1) {
      swiper.virtual.appendSlide(position);
    }
    count = nextCount;
  }

  function goTo(index, { animate = true } = {}) {
    if (!count) return;
    const target = Math.max(0, Math.min(count - 1, Number(index) || 0));
    swiper.slideTo(target, animate ? undefined : 0, false);
  }

  function move(delta) {
    if (delta < 0) swiper.slidePrev();
    else swiper.slideNext();
  }

  // Force the currently mounted projections to be produced again (used when the
  // active one must switch from an inert preview to an interactive card).
  function refresh() {
    swiper.virtual.update(true);
  }

  function activeElement() {
    return swiper.slides?.[swiper.activeIndex] || null;
  }

  return Object.freeze({
    element: shell,
    mount: mountCount,
    extendTo,
    goTo,
    move,
    refresh,
    activeElement,
    lock() { swiper.allowTouchMove = false; },
    unlock() { swiper.allowTouchMove = true; },
    dispose() { swiper.destroy(true, true); shell.remove(); },
    get index() { return swiper.activeIndex; },
    get count() { return count; },
  });
}

// Deck motion: a fixed, small set of hosts you fill yourself (used for the
// parent/current/child level deck, whose current host owns a live sub-view and
// must therefore never be re-rendered from scratch).
export function createDeckMotion({
  mount,
  hosts = 3,
  initial = 1,
  direction = "vertical",
  onSettled = () => {},
  onMoveState = () => {},
  label = "",
}) {
  requireSwiper();
  if (!mount) throw new Error("MotionAdapter requires a mount element");

  const shell = createShell(mount, "swiper v3-level-swiper", label);
  const wrapper = shell.querySelector(".swiper-wrapper");
  wrapper.classList.add("v3-level-wrapper");

  const slots = [];
  for (let position = 0; position < hosts; position += 1) {
    const slide = document.createElement("div");
    slide.className = "swiper-slide v3-level-slide";
    slide.dataset.levelIndex = String(position);
    wrapper.append(slide);
    slots.push(slide);
  }

  const swiper = new window.Swiper(shell, {
    ...BASE_OPTIONS,
    direction,
    initialSlide: initial,
    on: {
      touchStart() { onMoveState(true); },
      sliderMove() { onMoveState(true); },
      touchEnd(instance) { if (!instance.animating) onMoveState(false); },
      slideChangeTransitionEnd(instance) {
        onMoveState(false);
        onSettled(instance.activeIndex);
      },
    },
  });

  return Object.freeze({
    element: shell,
    hostAt(index) { return slots[index] || null; },
    goTo(index, { animate = true } = {}) { swiper.slideTo(index, animate ? undefined : 0, false); },
    move(delta) { if (delta < 0) swiper.slidePrev(); else swiper.slideNext(); },
    setBounds({ previous, next }) {
      swiper.allowSlidePrev = Boolean(previous);
      swiper.allowSlideNext = Boolean(next);
    },
    lock() { swiper.allowTouchMove = false; },
    unlock() { swiper.allowTouchMove = true; },
    dispose() { swiper.destroy(true, true); shell.remove(); },
    get index() { return swiper.activeIndex; },
  });
}
