# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `SKIP TO NAVIGATION GO TO MAIN CONTENT NAVIGATION.ARIA.GOTOSEARCH ACCESSIBILITY OPTIONS Jump to main content New In NAVIGATE TO PAGE: NEW IN Jump to main content New Arrivals Grenoble S/S 2026 Men Grenoble S/S 2026 Women New In for Men New In for Women Father's`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 24, image count 19, document height 6338.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 6338}.
  - Media/card aspect stability: image natural sizes include 1900x2850; 1900x2850; 1900x2850; 1900x2850; 0x0; 3600x2025; 3600x2025; 0x0; 0x0; 0x0.
  - Observed border radii: 50%; 50%; 50%; 50%
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 6338}
  - Observed media ratios: 1900:2850; 1900:2850; 1900:2850; 1900:2850; 3600:2025; 3600:2025; 320:168; 320:168
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: request_animation_frame
  - Performance/accessibility concerns: heavy media count 19 and scripts 9; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
