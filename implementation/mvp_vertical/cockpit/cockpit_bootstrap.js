document.documentElement.dataset.cockpitVersion = "3";
document.documentElement.classList.add("cockpit-v3");

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
    await import("./v3/demo_collection_app.js");
    await import("./shell_controls.js");
  } else {
    await import("./live_bootstrap.js");
  }
} catch (error) {
  reportFailure(error);
}
