(function () {
  const THEME_STORAGE_KEY = "al-folio-theme";
  const root = document.documentElement;
  const THEME_CLASSES = ["theme-light", "theme-dark"];
  const prefersDarkQuery = window.matchMedia
    ? window.matchMedia("(prefers-color-scheme: dark)")
    : null;
  let storedTheme;

  const readStoredTheme = () => {
    if (storedTheme !== undefined) {
      return storedTheme;
    }
    try {
      storedTheme = localStorage.getItem(THEME_STORAGE_KEY);
    } catch (error) {
      storedTheme = null;
    }
    return storedTheme;
  };

  const writeStoredTheme = (value) => {
    storedTheme = value;
    try {
      localStorage.setItem(THEME_STORAGE_KEY, value);
    } catch (error) {
      // ignore storage errors (e.g., Safari private mode)
    }
  };

  const removeStoredTheme = () => {
    storedTheme = null;
    try {
      localStorage.removeItem(THEME_STORAGE_KEY);
    } catch (error) {
      // ignore storage errors
    }
  };

  const toggleState = {
    button: null,
    label: null,
  };

  let currentTheme = null;
  let hasStoredPreference = false;

  const updateToggleState = () => {
    if (!toggleState.button) {
      return;
    }
    const isDark = currentTheme === "theme-dark";
    toggleState.button.dataset.theme = isDark ? "dark" : "light";
    toggleState.button.setAttribute("aria-pressed", isDark ? "true" : "false");
    toggleState.button.setAttribute(
      "aria-label",
      isDark ? "Switch to light theme" : "Switch to dark theme"
    );
    if (toggleState.label) {
      toggleState.label.textContent = isDark ? "Light mode" : "Dark mode";
    }
  };

  const applyTheme = (theme) => {
    const nextTheme = THEME_CLASSES.includes(theme) ? theme : "theme-light";
    THEME_CLASSES.forEach((themeClass) => {
      if (themeClass !== nextTheme) {
        root.classList.remove(themeClass);
      }
    });
    if (!root.classList.contains(nextTheme)) {
      root.classList.add(nextTheme);
    }
    currentTheme = nextTheme;
    root.setAttribute("data-theme", nextTheme);
    updateToggleState();
  };

  const resolveInitialTheme = () => {
    const stored = readStoredTheme();
    if (THEME_CLASSES.includes(stored)) {
      hasStoredPreference = true;
      return stored;
    }
    hasStoredPreference = false;
    if (prefersDarkQuery && typeof prefersDarkQuery.matches === "boolean") {
      return prefersDarkQuery.matches ? "theme-dark" : "theme-light";
    }
    return "theme-light";
  };

  const initTheme = () => {
    applyTheme(resolveInitialTheme());
  };

  const handlePreferenceChange = (event) => {
    if (hasStoredPreference) {
      return;
    }
    applyTheme(event.matches ? "theme-dark" : "theme-light");
  };

  const toggleTheme = () => {
    const nextTheme = currentTheme === "theme-dark" ? "theme-light" : "theme-dark";
    hasStoredPreference = true;
    applyTheme(nextTheme);
    writeStoredTheme(nextTheme);
  };

  const resetToSystemPreference = () => {
    removeStoredTheme();
    hasStoredPreference = false;
    applyTheme(resolveInitialTheme());
  };

  const createToggle = () => {
    if (!document.body) {
      return;
    }

    const button = document.createElement("button");
    button.type = "button";
    button.className = "theme-toggle";
    button.dataset.themeToggle = "true";
    button.title = "Toggle color theme";

    const sunIcon = document.createElement("span");
    sunIcon.className = "theme-toggle__icon";
    sunIcon.dataset.themeIcon = "sun";
    sunIcon.setAttribute("aria-hidden", "true");
    sunIcon.textContent = "☀️";

    const moonIcon = document.createElement("span");
    moonIcon.className = "theme-toggle__icon";
    moonIcon.dataset.themeIcon = "moon";
    moonIcon.setAttribute("aria-hidden", "true");
    moonIcon.textContent = "🌙";

    const label = document.createElement("span");
    label.className = "theme-toggle__label";

    button.appendChild(sunIcon);
    button.appendChild(moonIcon);
    button.appendChild(label);

    button.addEventListener("click", (event) => {
      if (event.metaKey || event.ctrlKey) {
        resetToSystemPreference();
        return;
      }
      toggleTheme();
    });

    button.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        toggleTheme();
      } else if ((event.key === "Backspace" || event.key === "Delete") && hasStoredPreference) {
        event.preventDefault();
        resetToSystemPreference();
      }
    });

    toggleState.button = button;
    toggleState.label = label;
    updateToggleState();

    document.body.appendChild(button);
  };

  const init = () => {
    initTheme();
    createToggle();
    if (prefersDarkQuery && typeof prefersDarkQuery.addEventListener === "function") {
      prefersDarkQuery.addEventListener("change", handlePreferenceChange);
    } else if (prefersDarkQuery && typeof prefersDarkQuery.addListener === "function") {
      prefersDarkQuery.addListener(handlePreferenceChange);
    }
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
