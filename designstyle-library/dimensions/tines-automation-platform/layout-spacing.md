# Layout And Spacing

## Observed
- Visual layout:
  - Layout: infer from screenshot and viewport; primary page text sample starts `Log in Sign up Book a demo Platform Solutions Resources Company Pricing Explore Workflow capability matrix The intelligent workflow platform Securely scale AI and automation. Integrate agents, teams, and tools with speed and control. Book a demo Sign up free T`.
  - Typography: observed font stacks and role rhythm are recorded below.
  - Color: observed computed foreground/background pairs are recorded below.
  - Density: navigation count 6, image count 40, document height 9154.
  - Shape: border radii samples recorded below.
  - Shadow/depth: inspect screenshot; automated pass records no shadow taxonomy.
- Layout geometry:
  - First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement.
  - Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 9154}.
  - Media/card aspect stability: image natural sizes include 61x63; 40x67; 88x61; 78x75; 1200x630; 160x178; 157x175; 78x68; 336x522; 196x116.
  - Observed border radii: 6.5px; 6.5px; 6.5px; 39px; 13px; 13px; 10px; 13px; 28px; 50%; 50%; 12px
- Dimension ratios:
  - Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 9154}
  - Observed media ratios: 61:63; 40:67; 88:61; 78:75; 1200:630; 160:178; 157:175; 78:68; 336:522; 196:116
  - Observed spacing samples: automated pass did not measure spacing; use screenshot for exact spacing before implementation.
  - Preserve ratios as implementation constraints: preserve hero/media/card proportions visible in screenshot; avoid free-floating cards unless the captured page uses them.
  - Do not translate these references into free-floating cards; record the page grid and media proportions before styling details.
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: animation, easing, intersection, keyframes, reduced_motion, request_animation_frame, transform, transition
  - Performance/accessibility concerns: heavy media count 40 and scripts 7; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
