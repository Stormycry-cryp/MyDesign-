# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `Home Map Developer Hub Coverage Help & Support Sign in Toggle Sidebar Jun 4, 2026 1:15 PM GMT+8 15 min 5 min 15 min hourly daily monthly yearly 6:00 PM Jun 4 6:00 AM Fixing climate change... Jun 4, 2026 1:15 PM Carbon intensity gCO₂eq/kWh 0 300 600 900 1200 15`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 0, image count 3, document height 1000.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 1000}.
  - Media/card aspect stability: image natural sizes include 36x36; 10x10; 78x13.
  - Observed border radii: 6px; 6px; 50px; 50px; 0px 0px 6px 6px; 6px; 6px; 6px; 6px; 6px; 9999px; 6px
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 1000}
  - Observed media ratios: 36:36; 10:10; 78:13
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: animation, easing, intersection, keyframes, reduced_motion, request_animation_frame, transform, transition
  - Performance/accessibility concerns: heavy media count 3 and scripts 6; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
