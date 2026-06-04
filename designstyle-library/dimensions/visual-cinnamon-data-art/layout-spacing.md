# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `DATA·VIZ DATA·ART CHART ABOUT CONTACT BLOG ARE YOU LOOKING FOR Unique & Beautiful Data Visualizations and Data Art to make an impact, tell a story, evoke emotions, and more? GET IN TOUCH! ⌄ more to see down here ⌄ client Google Trends client Scientific America`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 6, image count 33, document height 5442.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 5442}.
  - Media/card aspect stability: image natural sizes include 207x150; 512x512; 1200x800; 1200x800; 1200x800; 1200x800; 1200x800; 1200x800; 1080x720; 1200x800.
  - Observed border radii: none observed
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 5442}
  - Observed media ratios: 207:150; 512:512; 1200:800; 1200:800; 1200:800; 1200:800; 1200:800; 1200:800; 1080:720; 1200:800
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: easing, request_animation_frame, transform, transition
  - Performance/accessibility concerns: heavy media count 33 and scripts 3; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
