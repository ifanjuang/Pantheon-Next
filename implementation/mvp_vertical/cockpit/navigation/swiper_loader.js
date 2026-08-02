const SWIPER_VERSION = "14.0.7";

function loadExternalScript(src) {
  return new Promise((resolve, reject) => {
    const script = document.createElement("script");
    script.src = src;
    script.async = true;
    script.crossOrigin = "anonymous";
    script.onload = () => resolve(true);
    script.onerror = () => reject(new Error(`Impossible de charger ${src}`));
    document.head.append(script);
  });
}

function markReady(ready) {
  document.documentElement.dataset.swiperReady = ready ? "true" : "false";
  if (ready) document.documentElement.dataset.swiperVersion = SWIPER_VERSION;
  else delete document.documentElement.dataset.swiperVersion;
}

export async function ensureSwiper() {
  if (typeof window.Swiper === "function") {
    markReady(true);
    return true;
  }

  const candidates = [
    `https://cdn.jsdelivr.net/npm/swiper@${SWIPER_VERSION}/swiper-bundle.min.js`,
    `https://unpkg.com/swiper@${SWIPER_VERSION}/swiper-bundle.min.js`,
  ];

  for (const src of candidates) {
    try {
      await loadExternalScript(src);
      if (typeof window.Swiper === "function") {
        markReady(true);
        return true;
      }
    } catch (error) {
      console.warn(`Swiper indisponible depuis ${src}`, error);
    }
  }

  markReady(false);
  return false;
}

export const swiperVersion = SWIPER_VERSION;
