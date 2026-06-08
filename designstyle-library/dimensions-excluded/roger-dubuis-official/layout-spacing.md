# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `GO TO THE CONTENT TO ACCESS INFORMATION RELEVANT TO YOUR GEOGRAPHIC LOCATION, WE RECOMMEND USING THE VERSION: HONG KONG SAR, CHINA 中國香港特別行政區 MENU HOMEPAGE MOVEMENTS OF THE SKY WATCHES AND WONDERS 2026 DISCOVER NOVELTIES THE LATEST BIRETROGRADE PERPETUAL CALEND`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 6, image count 24, document height 8462.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 8462}.
  - Media/card aspect stability: image natural sizes include 250x334; 294x399; 294x399; 0x0; 0x0; 0x0; 294x399; 294x399; 294x399; 2400x608.
  - Observed border radii: 2px; 50%; 50%; 1px; 1px; 50%; 50%; 50%; 50%; 50%; 50%; 50%
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 8462}
  - Observed media ratios: 250:334; 294:399; 294:399; 294:399; 294:399; 294:399; 2400:608; 422:629; 422:629; 422:629
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: animation, easing, intersection, keyframes, request_animation_frame, swiper, transform, transition
  - Performance/accessibility concerns: heavy media count 24 and scripts 11; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
