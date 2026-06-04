# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `For Customer Service For Sales For Chefs Company BOOK A DEMO Office robots built for wholesale distributors Automate orders, grow sales, and serve customers with our suite of AI robots GET A DEMO OrderAI InboxAI MenuAI Marketplace Turn hours of manual data ent`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 6, image count 18, document height 3981.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 3981}.
  - Media/card aspect stability: image natural sizes include 210x118; 90x97; 210x118; 90x97; 210x118; 90x97; 1300x448; 1192x672; 1192x672; 1192x672.
  - Observed border radii: 6px; 2px; 59px; 38px 38px 0px 0px; 30px 30px 0px 0px; 14px 14px 0px 0px; 59px; 24px; 24px; 24px; 8px; 8px
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 3981}
  - Observed media ratios: 210:118; 90:97; 210:118; 90:97; 210:118; 90:97; 1300:448; 1192:672; 1192:672; 1192:672
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: easing, request_animation_frame, transition
  - Performance/accessibility concerns: heavy media count 18 and scripts 11; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
