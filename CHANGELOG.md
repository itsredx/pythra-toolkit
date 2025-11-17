# PyThra Framework - Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.13] - 2025-11-17

This release fixes missing template assets in the installed package so that `pythra create-project` can correctly scaffold new projects.

### 🛠️ Fixed

* **Project template assets not included in distribution:**
  * **Problem:** The HTML, CSS, JavaScript, fonts, and icon assets under `project_template/render` and `project_template/assets` were not being bundled into the published wheel. As a result, `pythra create-project` produced projects with missing frontend files, causing the generated apps to fail or render with broken UI.
  * **Solution:** Updated packaging configuration (`MANIFEST.in` and `pyproject.toml`) to include all required template assets (e.g. `*.html`, `*.css`, `*.js`, `*.yaml`, `*.yml`, `*.ttf`, `*.ico`, `*.json`, `*.in`, plus nested asset folders). These files are now shipped inside the wheel, ensuring that freshly created PyThra projects have all required frontend resources available out of the box.

---

## [0.1.6] - 2025-11-17

This release focuses on improving stability and user experience on Windows systems, specifically addressing critical rendering bugs that occurred when resuming a machine from sleep or hibernation.

### 🛠️ Fixed

* **WebView Content Shrinking After System Resume:**
  * **Problem:** On resuming from sleep, the `QWebEngineView` content would often fail to reflow, appearing "shrunken" or incorrectly sized within the application window. This required a manual window resize to fix.
  * **Solution:** A robust viewport synchronization routine (`_sync_webview_viewport`) has been implemented. It is automatically triggered when the application becomes active after a system resume. This function forces the underlying Chromium engine's viewport to match the Qt widget's dimensions and then dispatches a JavaScript `resize` event, ensuring all web content (CSS and JavaScript layouts) correctly recalculates and fills the window as intended.

* **DPI Scaling Reset to 96 on Resume:**
  * **Problem:** On systems with high-DPI displays (e.g., 125% or 150% scaling), resuming from sleep could cause the application to lose its awareness of the correct scaling factor, defaulting to a base of 96 DPI. This made all content appear too small.
  * **Solution:** The resume handler now intelligently re-probes the browser's actual `window.devicePixelRatio` after waking up. It compares this value to the baseline established at startup and dynamically applies the correct `zoomFactor` to the `QWebEnginePage`. This restores the proper content scale, overriding any incorrect DPI information reported by the operating system post-resume.

### ✨ Changed

* **Enhanced System Power Event Handling on Windows:**
  * The WMI-based power event watcher (`watch_for_power_events`) has been improved to detect both "suspend" (entering sleep) and "resume" (waking up) events. This allows for more sophisticated state management, such as the automatic minimizing and restoring of windows during sleep cycles.
