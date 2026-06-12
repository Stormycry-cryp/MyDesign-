# Assets

## Observed
- Assets:
  - Image style: polished hospitality interiors with warm reflective materials and dramatic lighting fixtures
  - Illustration/icon style: none central to the first viewport
  - Texture/pattern: brass, dark wood, lacquer, and high-end interior ceiling geometry
  - Likely sources or production method: professionally art-directed project photography
- Images/video observed:
  - Captured URL: https://www.avroko.com/
  - Page title: AvroKO — Interior Design
  - Screenshot: screenshots/avroko-desktop.png
  - Viewport: 1440x1000, with probe document height about 1000px in the captured state
  - Community signal: Selected in the 2026-06-08 curated daily candidate batch for DesignStyle and explicitly confirmed by the user for ingestion after passing the aesthetic gate with a stable first viewport.
  - Page scope: Official homepage for the interior design practice; homepage-led reference with project and studio storytelling.
  - Secondary pages inspected: attempted `/work/oiji-mi`, `Work`, and `/work/single-thread`, but all timed out in the deeper automated pass
  - H1 observed: `Celebrating excellence and innovation in hospitality design`
  - H2 samples: `Selected Work`; `Subscribe to keep up with AvroKO World news, openings, opportunities, and announcements.`
  - Navigation samples: About; Work; Services; Awards & Press; Culture; Contact
  - Images observed: chandelier-dominant hospitality hero plus multiple project thumbnails sourced from Webflow CDN
  - Video observed: missing
  - Overlays or fixed elements: no accepted-overlay contamination in the final screenshot
- Asset loading:
  - Framework/runtime hints: Webflow runtime plus `IntersectionObserver`, `requestAnimationFrame`, and Locomotive Scroll references appeared in the captured resources
  - CSS variables/tokens observed: explicit variable names were not extracted cleanly, but the stylesheets expose a tokenized Webflow/custom-CSS stack
  - Layout primitives observed: fixed-like top nav, split text field, full-width image section, slider/list structures deeper in the page
  - Component or class naming clues: `nav`, `n-brand`, `n-link`, `slider1-list`, `hp-list`, `newsletter-field`
  - Component computed-style evidence: `assets/2026-06-08-avroko-component-styles.json`
  - Asset CDN and media loading patterns: Webflow CDN image delivery with multiple `.webp` hero assets
  - Public stylesheet/script URLs: missing

## Inference
- Borrow:
  - Borrow the split of declarative headline and validation quote.
  - Borrow the combination of soft shell, luxury-material imagery, and restrained nav.
  - Borrow the practice of proving the narrative with a single strong project image immediately below the fold line.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy AvroKO’s hospitality positioning, exact testimonial, or project imagery.
- Do not blindly import all Webflow/scroll behaviors into a simpler product context.
- Do not over-expand the typography system; its power comes from restraint.
