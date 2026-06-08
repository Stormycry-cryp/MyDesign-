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
  - Interpreted motion tags: hero media, hover states, menu transitions
  - Use this as implementation guidance only where evidence is direct. If CSS/JS is minified or only CDN names are visible, mark library/framework attribution as weak.
- Code surface:
  - Framework/runtime hints: no direct runtime hint found
  - Public stylesheet/script URLs: none observed
  - CSS variables/tokens observed: automated pass did not isolate variables; inspect fetched resources for token naming if needed.
  - Layout primitives observed: infer from screenshot and DOM; automated pass records page shape but not semantic layout primitives.
  - Component or class naming clues: raw DOM is not retained in the library; use L4 on-demand recapture from `https://www.iwc.com/us-en` when L0-L3 evidence is insufficient.
  - Component computed-style evidence: `assets/2026-06-05-iwc-schaffhausen-official-component-styles.json`
  - Asset CDN and media loading patterns: https://img.iwc.com/cluster-family-background-2xl-1/c03c739fb3f13df2d2934c239d9cd3be0a10d31b.jpg; https://img.iwc.com/family-2xl-1/ab2ee22bbbcad4d6835c4909adf6271be92ce5cc.jpg; data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width=%221023%22%20height=%22993%22%20viewBox%3D%220%200%201023%20993%22%3E%3C%2Fsvg%3E; data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width=%221023%22%20height=%22993%22%20viewBox%3D%220%200%201023%20993%22%3E%3C%2Fsvg%3E; data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width=%221023%22%20height=%22993%22%20viewBox%3D%220%200%201023%20993%22%3E%3C%2Fsvg%3E; data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width=%22957%22%20height=%221080%22%20viewBox%3D%220%200%20957%201080%22%3E%3C%2Fsvg%3E; data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width=%22957%22%20height=%221080%22%20viewBox%3D%220%200%20957%201080%22%3E%3C%2Fsvg%3E; data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width=%22957%22%20height=%221080%22%20viewBox%3D%220%200%20957%201080%22%3E%3C%2Fsvg%3E
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: none proven
  - Performance/accessibility concerns: heavy media count 23 and scripts 36; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
