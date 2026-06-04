# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `Use cases Revenue and Retention ARR Daily Pulse ARR Dashboard ARR Spreadsheet Average Contract Value Customer Dashboard Customer Retention Cohorts Net Revenue Retention Operating Model Dashboard Retention Dashboard Sales Pipeline and Funnel Deal Size and Veloc`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 24, image count 40, document height 9090.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 9090}.
  - Media/card aspect stability: image natural sizes include 4800x1100; 111x70; 132x70; 110x70; 87x70; 132x70; 83x70; 131x70; 103x70; 110x70.
  - Observed border radii: 12px; 6px; 6px; 6px; 6px; 6px; 6px; 6px; 6px; 6px; 6px; 6px
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 9090}
  - Observed media ratios: 4800:1100; 111:70; 132:70; 110:70; 87:70; 132:70; 83:70; 131:70; 103:70; 110:70
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: animation, easing, intersection, keyframes, reduced_motion, transform, transition
  - Performance/accessibility concerns: heavy media count 40 and scripts 9; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
