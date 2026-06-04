# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `Visual Journal About and support Hello! I’m Alessandro Scarpellini, art director and design manager from Italy with a reductive and modernist visual language, specialized in strategy, branding, and visual communication. Visual Journal is my blog, where I showc`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 1, image count 12, document height 5900.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 5900}.
  - Media/card aspect stability: image natural sizes include 1700x1152; 1700x1151; 1700x1153; 1700x1152; 1700x1153; 1700x1152; 1700x1152; 1700x1152; 1700x1152; 1700x1151.
  - Observed border radii: none observed
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 5900}
  - Observed media ratios: 1700:1152; 1700:1151; 1700:1153; 1700:1152; 1700:1153; 1700:1152; 1700:1152; 1700:1152; 1700:1152; 1700:1151
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: easing, intersection, transform, transition
  - Performance/accessibility concerns: heavy media count 12 and scripts 3; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
