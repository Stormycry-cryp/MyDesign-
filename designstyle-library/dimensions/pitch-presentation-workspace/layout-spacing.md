# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `Introducing Pitch Agent: Generate on-brand presentations in seconds with AI. See what’s new Product Use Cases Templates Resources Pricing Log in Sign up Create slides that win. Prompts Generate From prompt to presentation, 4M+ teams create and deliver winning `.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 7, image count 40, document height 15001.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 15001}.
  - Media/card aspect stability: image natural sizes include 1700x884; 1897x1920; 1920x1080; 1200x675; 1920x1080; 1920x1080; 1200x675; 1200x675; 1920x1080; 1200x675.
  - Observed border radii: 30px; 4px; 24px; 60px; 16px; 100px; 8px; 4px; 12px; 12px; 12px; 12px
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 15001}
  - Observed media ratios: 1700:884; 1897:1920; 1920:1080; 1200:675; 1920:1080; 1920:1080; 1200:675; 1200:675; 1920:1080; 1200:675
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: easing, request_animation_frame
  - Performance/accessibility concerns: heavy media count 40 and scripts 18; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
