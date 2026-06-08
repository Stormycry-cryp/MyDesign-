# Motion And Code

## Observed
- Motion:
  - Page transitions: no direct transition evidence found
  - Micro-interactions: infer only when backed by transition/animation evidence or visible screenshot states.
  - Scroll/entrance behavior: ion Hl(a){["MutationObserver","ResizeObserver","PerformanceObserver","IntersectionObserver","ReportingObserver"].forEach(b=>{const c=a[b];if(c&&aa(c)){const d=de[b];Cb(a,b,c,{construct:(e,f)=>{if(f[0]){const g=X(f[0],voi, rver:K("ResizeObserver"),PerformanceObserver:K("PerformanceObserver"),IntersectionObserver:K("IntersectionObserver"),ReportingObserver:K("ReportingObserver")}, yg={setInterval:y("setInterval"),setTimeout:y("setTimeout"),, nction Gl(a){"setInterval setTimeout setImmediate requestIdleCallback requestAnimationFrame webkitRequestAnimationFrame queueMicrotask".split(" ").forEach(b=> {const c=a[b];if(c&&aa(c)){const d=yg[b];a[b]=O(c,{apply:(e,f,, tTimeout setImmediate requestIdleCallback requestAnimationFrame webkitRequestAnimationFrame queueMicrotask".split(" ").forEach(b=> {const c=a[b];if(c&&aa(c)){const d=yg[b];a[b]=O(c,{apply:(e,f,g)=>{"string"==typeof g[0]&&
  - Timing/easing: no direct timing evidence found
- Motion code:
  - Motion source: public styles/scripts sampled from captured DOM.
  - CSS animation/transition evidence: none observed
  - Public CSS/JS probe keywords: intersection, request_animation_frame
  - Public CSS/JS motion snippets: ion Hl(a){["MutationObserver","ResizeObserver","PerformanceObserver","IntersectionObserver","ReportingObserver"].forEach(b=>{const c=a[b];if(c&&aa(c)){const d=de[b];Cb(a,b,c,{const; rver:K("ResizeObserver"),PerformanceObserver:K("PerformanceObserver"),IntersectionObserver:K("IntersectionObserver"),ReportingObserver:K("ReportingObserver")}, yg={setInterval:y("s; ,PerformanceObserver:K("PerformanceObserver"),IntersectionObserver:K("IntersectionObserver"),ReportingObserver:K("ReportingObserver")}, yg={setInterval:y("setInterval"),setTimeout:; nction Gl(a){"setInterval setTimeout setImmediate requestIdleCallback requestAnimationFrame webkitRequestAnimationFrame queueMicrotask".split(" ").forEach(b=> {const c=a[b];if(c&&a; tTimeout setImmediate requestIdleCallback requestAnimationFrame webkitRequestAnimationFrame queueMicrotask".split(" ").forEach(b=> {const c=a[b];if(c&&aa(c)){const d=yg[b];a[b]=O(c; ediate:y("setImmediate"),requestIdleCallback:y("requestIdleCallback"),requestAnimationFrame:y("requestAnimationFrame"),webkitRequestAnimationFrame:y("webkitRequestAnimationFrame"),; requestIdleCallback:y("requestIdleCallback"),requestAnimationFrame:y("requestAnimationFrame"),webkitRequestAnimationFrame:y("webkitRequestAnimationFrame"),queueMicrotask:y("queueMi; IdleCallback"),requestAnimationFrame:y("requestAnimationFrame"),webkitRequestAnimationFrame:y("webkitRequestAnimationFrame"),queueMicrotask:y("queueMicrotask")},$a=K("Promise"),Tc=
  - Exact motion parameters: no direct code evidence; preserve only visible motion intent
  - JavaScript/runtime motion evidence: ion Hl(a){["MutationObserver","ResizeObserver","PerformanceObserver","IntersectionObserver","ReportingObserver"].forEach(b=>{const c=a[b];if(c&&aa(c)){const d=de[b];Cb(a,b,c,{const; rver:K("ResizeObserver"),PerformanceObserver:K("PerformanceObserver"),IntersectionObserver:K("IntersectionObserver"),ReportingObserver:K("ReportingObserver")}, yg={setInterval:y("s; ,PerformanceObserver:K("PerformanceObserver"),IntersectionObserver:K("IntersectionObserver"),ReportingObserver:K("ReportingObserver")}, yg={setInterval:y("setInterval"),setTimeout:; nction Gl(a){"setInterval setTimeout setImmediate requestIdleCallback requestAnimationFrame webkitRequestAnimationFrame queueMicrotask".split(" ").forEach(b=> {const c=a[b];if(c&&a; tTimeout setImmediate requestIdleCallback requestAnimationFrame webkitRequestAnimationFrame queueMicrotask".split(" ").forEach(b=> {const c=a[b];if(c&&aa(c)){const d=yg[b];a[b]=O(c; ediate:y("setImmediate"),requestIdleCallback:y("requestIdleCallback"),requestAnimationFrame:y("requestAnimationFrame"),webkitRequestAnimationFrame:y("webkitRequestAnimationFrame"),; requestIdleCallback:y("requestIdleCallback"),requestAnimationFrame:y("requestAnimationFrame"),webkitRequestAnimationFrame:y("webkitRequestAnimationFrame"),queueMicrotask:y("queueMi; IdleCallback"),requestAnimationFrame:y("requestAnimationFrame"),webkitRequestAnimationFrame:y("webkitRequestAnimationFrame"),queueMicrotask:y("queueMicrotask")},$a=K("Promise"),Tc=
  - Stylesheet evidence: https://www.bulgari.com/resources/9c96854fd9e79c739cb6267ecff5ff839180425c884ba; https://www.bulgari.com/akam/13/207732d2
  - Interpreted motion tags: hero media, hover states, menu transitions
  - Use this as implementation guidance only where evidence is direct. If CSS/JS is minified or only CDN names are visible, mark library/framework attribution as weak.
- Code surface:
  - Framework/runtime hints: intersection, request_animation_frame
  - Public stylesheet/script URLs: https://www.bulgari.com/resources/9c96854fd9e79c739cb6267ecff5ff839180425c884ba; https://www.bulgari.com/akam/13/207732d2
  - CSS variables/tokens observed: automated pass did not isolate variables; inspect fetched resources for token naming if needed.
  - Layout primitives observed: infer from screenshot and DOM; automated pass records page shape but not semantic layout primitives.
  - Component or class naming clues: raw DOM is not retained in the library; use L4 on-demand recapture from `https://www.bulgari.com/en-us/` when L0-L3 evidence is insufficient.
  - Component computed-style evidence: `assets/2026-06-05-bulgari-official-component-styles.json`
  - Asset CDN and media loading patterns: none observed
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: intersection, request_animation_frame
  - Performance/accessibility concerns: heavy media count 0 and scripts 36; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
