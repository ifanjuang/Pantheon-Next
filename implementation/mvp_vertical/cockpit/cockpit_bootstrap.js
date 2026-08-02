document.documentElement.classList.add("cockpit");

function reportFailure(error) {
  console.error(error);
  document.documentElement.dataset.cockpitLoad = "failed";

  const stage = document.getElementById("v2-stage");
  if (stage) {
    const message = document.createElement("p");
    message.className = "v2-empty";
    message.setAttribute("role", "status");
    message.textContent = String(error?.message || error).includes("Swiper")
      ? "Le moteur de navigation (Swiper) n’a pas pu être chargé depuis le CDN. Vérifiez la connexion ou un bloqueur de contenu, puis rechargez."
      : "Le Cockpit n’a pas pu être chargé. Rechargez la page.";
    stage.replaceChildren(message);
  }

  const network = document.getElementById("v2-network");
  if (network) network.textContent = "chargement impossible";
}

try {
  const params = new URLSearchParams(window.location.search);
  if (params.get("mode") === "demo") {
    document.documentElement.dataset.cockpitMode = "demo";
    await import("./demo/collection_app.js");
    await import("./shell_controls.js");
  } else {
    document.documentElement.dataset.cockpitMode = "live";
    await import("./live_bootstrap.js");
  }
} catch (error) {
  reportFailure(error);
}
