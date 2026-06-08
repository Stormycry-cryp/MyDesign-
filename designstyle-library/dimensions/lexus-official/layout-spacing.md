# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `Skip to Main Content VEHICLES SHOP MY LEXUS SIGN IN Prototype vehicle shown The all-new TZ. Arriving Fall 2026. LEARN MORE Meet the models SUV 7 SEDAN 2 HYBRID & ELECTRIC 7 PERFORMANCE 7 ALL 11 HYBRIDHYBRIDHYBRIDHYBRIDHYBRIDHYBRIDHYBRID ES Hybrid All-Electric `.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 0, image count 31, document height 6097.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 6097}.
  - Media/card aspect stability: image natural sizes include 208x150; 22x22; 1920x795; 750x471; 750x471; 750x471; 750x471; 750x471; 750x471; 750x471.
  - Observed border radii: 24px; 20px; 932px; 932px; 9999px; 9999px
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 6097}
  - Observed media ratios: 208:150; 22:22; 1920:795; 750:471; 750:471; 750:471; 750:471; 750:471; 750:471; 750:471
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: intersection, request_animation_frame
  - Performance/accessibility concerns: heavy media count 31 and scripts 36; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
