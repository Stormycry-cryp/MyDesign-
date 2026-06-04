# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `Rows joined Superhuman. For any inquiries, email support@rows.com. The Superhuman Privacy Policy and Terms will apply as of June 16. Product Rows AI Your number crunching sidekick Integrations Seamless connections to your tools Support Docs Learn how to make t`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 24, image count 29, document height 6775.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 6775}.
  - Media/card aspect stability: image natural sizes include 5984x3072; 6001x3072; 1436x1288; 1255x456; 684x588; 684x588; 2853x2382; 0x0; 150x150; 0x0.
  - Observed border radii: 8px; 8px; 2px; 2px; 50%; 12px; 12px; 12px; 12px; 8px; 8px; 8px
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 6775}
  - Observed media ratios: 5984:3072; 6001:3072; 1436:1288; 1255:456; 684:588; 684:588; 2853:2382; 150:150; 80:80; 80:80
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: animation, easing, keyframes, transform, transition
  - Performance/accessibility concerns: heavy media count 29 and scripts 36; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
