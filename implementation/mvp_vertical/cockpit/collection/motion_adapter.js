// Cockpit — MotionAdapter.
//
// The only module that knows Swiper exists. It exposes a deliberately small
// surface and can swap between compact swipe motion and an expanded desktop
// collection without changing NavigationState or CollectionController.

const BASE_OPTIONS = Object.freeze({
  noSwipingSelector: "button,input,select,textarea,a,[contenteditable='true']",
});
const EXPANDED_MIN_WIDTH = 960;
const INTERACTIVE_SELECTOR = "button,input,select,textarea,a,[contenteditable='true']";

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
  wrapper.className = "swiper-wrapper v2-swiper-wrapper";
  shell.append(wrapper);
  mount.append(shell);
  return shell;
}

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
      addSlidesBefore: 1,
      addSlidesAfter: 1,
      slides: [],
      renderSlide(_item, index) {
        const slide = document.createElement("div");
        slide.className = "swiper-slide v2-swiper-slide v3-swiper-slide";
        const node = renderAt(index, { presentation: "compact" });
        if (node) slide.append(node);
        return slide;
      },
    },
    on: {
      touchStart() { onMoveState(true); },
      sliderMove() { onMoveState(true); },
      touchEnd(instance) { if (!instance.animating) onMoveState(false); },
      slideChange(instance) { onIndexChange(instance.activeIndex, { presentation: "compact" }); },
      slideChangeTransitionEnd() { onMoveState(false); },
    },
  });

  function mountCount(nextCount, index = 0) {
    count = Math.max(0, Number(nextCount) || 0);
    swiper.virtual.slides = new Array(count).fill(null).map((_, position) => position);
    swiper.virtual.update(true);
    goTo(index, { animate: false });
  }

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
    get presentation() { return "compact"; },
  });
}

function createExpandedMotion({
  mount,
  renderAt,
  onIndexChange = () => {},
  onActivate = () => {},
  label = "",
}) {
  if (!mount) throw new Error("MotionAdapter requires a mount element");
  if (typeof renderAt !== "function") throw new Error("MotionAdapter requires renderAt");

  const shell = document.createElement("div");
  shell.className = "v3-expanded-collection";
  shell.setAttribute("role", "region");
  if (label) shell.setAttribute("aria-label", label);
  const grid = document.createElement("div");
  grid.className = "v3-expanded-grid";
  shell.append(grid);
  mount.append(shell);

  let count = 0;
  let index = 0;
  let locked = false;

  const bounded = value => {
    if (!count) return 0;
    return Math.max(0, Math.min(count - 1, Number(value) || 0));
  };

  function activate(position, reselected) {
    if (locked) return;
    onActivate(position, { presentation: "expanded", reselected });
  }

  function select(position, { activateItem = false } = {}) {
    const target = bounded(position);
    const reselected = target === index;
    if (!reselected) {
      index = target;
      onIndexChange(index, { presentation: "expanded" });
      render();
    }
    if (activateItem) activate(target, reselected);
  }

  function render() {
    grid.replaceChildren();
    for (let position = 0; position < count; position += 1) {
      const cell = document.createElement("div");
      cell.className = "v3-expanded-cell";
      cell.dataset.active = position === index ? "true" : "false";
      cell.tabIndex = 0;
      cell.setAttribute("aria-current", position === index ? "true" : "false");
      const node = renderAt(position, { presentation: "expanded" });
      if (node) cell.append(node);

      cell.addEventListener("click", event => {
        const interactive = event.target instanceof Element && event.target.closest(INTERACTIVE_SELECTOR);
        if (position !== index) {
          event.preventDefault();
          event.stopPropagation();
          select(position, { activateItem: true });
          return;
        }
        if (!interactive) activate(position, true);
      }, true);

      cell.addEventListener("keydown", event => {
        if (event.key !== "Enter" && event.key !== " ") return;
        if (event.target !== cell) return;
        event.preventDefault();
        select(position, { activateItem: true });
      });
      grid.append(cell);
    }
  }

  function mountCount(nextCount, nextIndex = 0) {
    count = Math.max(0, Number(nextCount) || 0);
    index = bounded(nextIndex);
    render();
  }

  function extendTo(nextCount) {
    const target = Math.max(count, Number(nextCount) || 0);
    if (target === count) return;
    count = target;
    render();
  }

  function goTo(nextIndex) {
    index = bounded(nextIndex);
    render();
  }

  function move(delta) {
    if (locked || !count) return;
    const target = bounded(index + Math.sign(Number(delta) || 0));
    if (target === index) return;
    index = target;
    onIndexChange(index, { presentation: "expanded" });
    render();
  }

  return Object.freeze({
    element: shell,
    mount: mountCount,
    extendTo,
    goTo,
    move,
    refresh: render,
    activeElement() { return grid.querySelector('.v3-expanded-cell[data-active="true"]'); },
    lock() { locked = true; },
    unlock() { locked = false; },
    dispose() { shell.remove(); },
    get index() { return index; },
    get count() { return count; },
    get presentation() { return "expanded"; },
  });
}

export function createResponsiveMotion({
  mount,
  renderAt,
  onIndexChange = () => {},
  onActivate = () => {},
  onMoveState = () => {},
  onPresentationChange = () => {},
  label = "",
}) {
  if (!mount) throw new Error("MotionAdapter requires a mount element");

  let count = 0;
  let index = 0;
  let locked = false;
  let delegate = null;
  let presentation = null;
  let resizeObserver = null;

  function measuredWidth() {
    return Number(mount.getBoundingClientRect?.().width || mount.clientWidth || window.innerWidth || 0);
  }

  function wantedPresentation() {
    return measuredWidth() >= EXPANDED_MIN_WIDTH ? "expanded" : "compact";
  }

  function build(nextPresentation) {
    if (presentation === nextPresentation && delegate) return false;
    delegate?.dispose();
    presentation = nextPresentation;
    const common = { mount, renderAt, onIndexChange, onMoveState, label };
    delegate = presentation === "expanded"
      ? createExpandedMotion({ ...common, onActivate })
      : createWindowedMotion(common);
    delegate.mount(count, index);
    if (locked) delegate.lock();
    onPresentationChange(presentation);
    return true;
  }

  function ensurePresentation() {
    return build(wantedPresentation());
  }

  function mountCount(nextCount, nextIndex = 0) {
    count = Math.max(0, Number(nextCount) || 0);
    index = count ? Math.max(0, Math.min(count - 1, Number(nextIndex) || 0)) : 0;
    const rebuilt = ensurePresentation();
    if (!rebuilt) delegate.mount(count, index);
  }

  function extendTo(nextCount) {
    count = Math.max(count, Number(nextCount) || 0);
    const rebuilt = ensurePresentation();
    if (!rebuilt) delegate.extendTo(count);
  }

  function goTo(nextIndex, options = {}) {
    index = count ? Math.max(0, Math.min(count - 1, Number(nextIndex) || 0)) : 0;
    const rebuilt = ensurePresentation();
    if (!rebuilt) delegate.goTo(index, options);
  }

  function move(delta) {
    ensurePresentation();
    delegate.move(delta);
    index = delegate.index;
  }

  function onResize() {
    const next = wantedPresentation();
    if (next !== presentation) build(next);
  }

  if (typeof ResizeObserver === "function") {
    resizeObserver = new ResizeObserver(onResize);
    resizeObserver.observe(mount);
  } else {
    window.addEventListener("resize", onResize);
  }

  return Object.freeze({
    mount: mountCount,
    extendTo,
    goTo,
    move,
    refresh() { ensurePresentation(); delegate.refresh(); },
    activeElement() { return delegate?.activeElement?.() || null; },
    lock() { locked = true; delegate?.lock(); },
    unlock() { locked = false; delegate?.unlock(); },
    dispose() {
      resizeObserver?.disconnect();
      if (!resizeObserver) window.removeEventListener("resize", onResize);
      delegate?.dispose();
    },
    get index() { return delegate?.index ?? index; },
    get count() { return count; },
    get presentation() { return presentation || wantedPresentation(); },
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
