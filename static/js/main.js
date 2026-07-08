document.addEventListener("DOMContentLoaded", () => {
  const navLinks = document.querySelectorAll(".nav-links a");
  const currentPath = window.location.pathname;

  navLinks.forEach((link) => {
    const linkPath = new URL(link.href).pathname;
    if (linkPath === currentPath || (linkPath !== "/" && currentPath.startsWith(linkPath))) {
      link.classList.add("active");
    }
  });

  const liveInput = document.getElementById("live-search-input");
  const cards = document.querySelectorAll(".phone-card");
  const emptyState = document.getElementById("empty-state");

  if (liveInput && cards.length) {
    liveInput.addEventListener("input", () => {
      const term = liveInput.value.trim().toLowerCase();
      let visibleCount = 0;

      cards.forEach((card) => {
        const haystack = `${card.dataset.name} ${card.dataset.brand}`.toLowerCase();
        const matches = haystack.includes(term);
        card.style.display = matches ? "" : "none";
        if (matches) visibleCount += 1;
      });

      if (emptyState) {
        emptyState.style.display = visibleCount === 0 ? "block" : "none";
      }
    });
  }

  const storageKey = "phonehub:favorites";
  const readFavorites = () => {
    try {
      return new Set(JSON.parse(localStorage.getItem(storageKey) || "[]").map(String));
    } catch {
      return new Set();
    }
  };
  const writeFavorites = (favorites) => {
    localStorage.setItem(storageKey, JSON.stringify([...favorites]));
  };

  const favorites = readFavorites();
  const syncButton = (btn) => {
    const id = String(btn.dataset.phoneId || "");
    const liked = favorites.has(id);
    btn.classList.toggle("liked", liked);
    btn.textContent = liked ? "♥" : "♡";
    btn.setAttribute("aria-pressed", liked ? "true" : "false");
  };

  document.querySelectorAll(".like-btn").forEach((btn) => {
    syncButton(btn);
    btn.addEventListener("click", () => {
      const id = String(btn.dataset.phoneId || "");
      if (!id) return;

      if (favorites.has(id)) {
        favorites.delete(id);
      } else {
        favorites.add(id);
      }

      writeFavorites(favorites);
      document.querySelectorAll(`.like-btn[data-phone-id="${id}"]`).forEach(syncButton);
      renderFavoritesPage();
    });
  });

  function renderFavoritesPage() {
    const favoriteGrid = document.getElementById("favorites-grid");
    if (!favoriteGrid) return;

    const items = favoriteGrid.querySelectorAll(".favorite-item");
    let visibleCount = 0;

    items.forEach((item) => {
      const isFavorite = favorites.has(String(item.dataset.phoneId));
      item.style.display = isFavorite ? "" : "none";
      if (isFavorite) visibleCount += 1;
    });

    const empty = document.getElementById("favorites-empty");
    if (empty) empty.style.display = visibleCount === 0 ? "block" : "none";
  }

  renderFavoritesPage();
});
