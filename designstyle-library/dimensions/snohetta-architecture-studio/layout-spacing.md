# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `Snøhetta Menu ⛰ Snøhetta is a global transdisciplinary practice, working on projects of all scales. Aura Viabizzuno Renaissance of the real USM Haller Installation for Milan Design Week 2026 Array by Snøhetta for mdf italia wins the ADI Compasso d’Oro Solstice`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 2, image count 20, document height 5139.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 5139}.
  - Media/card aspect stability: image natural sizes include 518x345; 346x230; 230x153; 230x153; 230x153; 230x153; 230x153; 230x153; 230x153; 230x153.
  - Observed border radii: 16px
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 5139}
  - Observed media ratios: 518:345; 346:230; 230:153; 230:153; 230:153; 230:153; 230:153; 230:153; 230:153; 230:153
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: easing, gsap, intersection, request_animation_frame, transform, transition
  - Performance/accessibility concerns: heavy media count 20 and scripts 3; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
