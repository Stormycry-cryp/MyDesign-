# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `Skip to main content Public Beta: Retool MCP Server Learn more ↗ BACK Solution Audience Resources Use cases Pricing Search ⌘K Sign in Book a demo Start for free AppGen Generate apps that are built for business—on your data, in your cloud, and secure by default`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 24, image count 40, document height 10451.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1410, 'docH': 10451}.
  - Media/card aspect stability: image natural sizes include 256x144; 1360x990; 239x352; 311x253; 123x297; 229x274; 343x230; 132x148; 98x250; 222x218.
  - Observed border radii: 9999px; 9999px; 9999px; 9999px; 40px; 20px; 20px; 20px; 24px; 9999px; 9999px; 9999px
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1410, 'docH': 10451}
  - Observed media ratios: 256:144; 1360:990; 239:352; 311:253; 123:297; 229:274; 343:230; 132:148; 98:250; 222:218
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: animation, easing, keyframes, reduced_motion, transform, transition
  - Performance/accessibility concerns: heavy media count 40 and scripts 36; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
