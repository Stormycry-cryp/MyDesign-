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
  - Component or class naming clues: raw DOM is not retained in the library; use L4 on-demand recapture from `https://www.longines.com/en-us` when L0-L3 evidence is insufficient.
  - Component computed-style evidence: `assets/2026-06-05-longines-official-component-styles.json`
  - Asset CDN and media loading patterns: https://cms.longines.com/media/3421/download/fathers-day_header-d.jpg?v=1&w=1440; https://cms.longines.com/media/3530/download/HydroConquest_video-fallback_d.jpg?v=1&w=1440; https://api.ecom.longines.com/media/catalog/product/w/a/watch-collection-conquest-heritage-l1-649-4-92-6-fd8f30-hero.png?w=320; https://api.ecom.longines.com/media/catalog/product/w/a/watch-collection-longines-spirit-pilot-l3-809-4-53-9-7e4498-hero.png?w=320; https://api.ecom.longines.com/media/catalog/product/w/a/watch-collection-conquest-l3-720-4-52-6-29b991-hero.png?w=320; https://api.ecom.longines.com/media/catalog/product/w/a/watch-collection-flagship-heritage-moonphase-l4-815-4-78-2-b16857-hero.png?w=320; https://api.ecom.longines.com/media/catalog/product/w/a/watch-collection-longines-dolcevita-l5-767-4-71-0-65a2de-hero.png?w=320; https://api.ecom.longines.com/media/catalog/product/w/a/watch-collection-longines-spirit-zulu-time-l3-802-4-63-6-1f3e25-hero.png?w=320
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: none proven
  - Performance/accessibility concerns: heavy media count 34 and scripts 36; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
