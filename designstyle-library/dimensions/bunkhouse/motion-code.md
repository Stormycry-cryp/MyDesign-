# Motion And Code

## Observed
- Motion:
  - Page transitions: no direct transition evidence found
  - Micro-interactions: infer only when backed by transition/animation evidence or visible screenshot states.
  - Scroll/entrance behavior: not proven in automated pass
  - Timing/easing: no direct timing evidence found
- Motion code:
  - Motion source: public styles/scripts sampled from captured DOM.
  - CSS animation/transition evidence: none observed
  - Public CSS/JS probe keywords: none
  - Public CSS/JS motion snippets: none observed
  - Exact motion parameters: no direct code evidence; preserve only visible motion intent
  - JavaScript/runtime motion evidence: none observed
  - Stylesheet evidence: none observed
  - Interpreted motion tags: subtle-scroll, reveal-light
  - Use this as implementation guidance only where evidence is direct. If CSS/JS is minified or only CDN names are visible, mark library/framework attribution as weak.
- Code surface:
  - Framework/runtime hints: no direct runtime hint found
  - Public stylesheet/script URLs: none observed
  - CSS variables/tokens observed: automated pass did not isolate variables; inspect fetched resources for token naming if needed.
  - Layout primitives observed: infer from screenshot and DOM; automated pass records page shape but not semantic layout primitives.
  - Component or class naming clues: raw DOM is not retained in the library; use L4 on-demand recapture from `https://www.bunkhousehotels.com/` when L0-L3 evidence is insufficient.
  - Component computed-style evidence: `assets/2026-06-05-bunkhouse-component-styles.json`
  - Asset CDN and media loading patterns: https://login.bunkhousehotels.com/wp-content/uploads/2024/08/BH-Logo_BH-Hotels-Logo-Stacked.png; https://login.bunkhousehotels.com/wp-content/uploads/2022/11/3d6c05c39beebf4615e5e385d710630d-1.png; https://www.bunkhousehotels.com/_next/static/media/dropdown-icon.5d170162.png; https://www.bunkhousehotels.com/_next/static/media/calendar-icon.cec4882e.png; https://www.bunkhousehotels.com/_next/static/media/calendar-icon.cec4882e.png; https://www.bunkhousehotels.com/_next/static/media/dropdown-icon.5d170162.png; https://login.bunkhousehotels.com/wp-content/uploads/2025/05/20231127_HotelSanCritobal_NickSimonite_MiscProperty_006_SMALL.jpeg; https://login.bunkhousehotels.com/wp-content/uploads/2023/12/Screenshot-2023-12-12-at-12.52.33-PM.png
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: none proven
  - Performance/accessibility concerns: heavy media count 36 and scripts 19; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
