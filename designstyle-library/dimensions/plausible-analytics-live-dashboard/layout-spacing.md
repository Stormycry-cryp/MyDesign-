# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `Login Sign up plausible.io 73 current visitors Filter Last 28 days UNIQUE VISITORS 303k 4% TOTAL VISITS 511k 3% TOTAL PAGEVIEWS 1.8M 4% VIEWS PER VISIT 3.61 6% BOUNCE RATE 42% 0% VISIT DURATION 7m 18s 4% 0 2k 4k 6k 8k 10k 12k 14k 7 May 12 May 17 May 22 May 27 `.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 2, image count 13, document height 2879.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 2879}.
  - Media/card aspect stability: image natural sizes include 300x73; 300x73; 32x32; 150x150; 20x20; 48x48; 32x32; 32x32; 150x150; 32x32.
  - Observed border radii: 4px; 6px; 6px; 6px; 6px; 6px; 6px; 6px; 6px; 6px; 6px; 6px
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 2879}
  - Observed media ratios: 300:73; 300:73; 32:32; 150:150; 20:20; 48:48; 32:32; 32:32; 150:150; 32:32
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: animation, easing, intersection, keyframes, request_animation_frame, transform, transition
  - Performance/accessibility concerns: heavy media count 13 and scripts 3; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
