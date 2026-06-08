# Motion And Code

## Observed
- Motion:
  - Page transitions: subtle nav/top transition evidence plus slider/lightbox transitions in public CSS
  - Micro-interactions: hover and filter transitions on images and buttons; likely reveal behaviors as content enters view
  - Scroll/entrance behavior: JavaScript evidence points to intersection-triggered lazy/reveal logic and requestAnimationFrame-backed scroll orchestration
  - Timing/easing: direct snippets include `top 0.4s cubic-bezier(0.65, 0, 0.35, 1)`, `.2s ease-out`, `.25s ease-out`, `.3s`, and `.8s linear infinite spin`
- Motion code:
  - Motion source: public CSS/JS resources sampled from the live page
  - CSS animation/transition evidence: transitions for nav position, button color, grayscale image hover, slider controls, and Webflow lightbox spinner
  - Public CSS/JS probe keywords: animation, easing, intersection, keyframes, reduced_motion, request_animation_frame, transform, transition
  - Public CSS/JS motion snippets: `top 0.4s cubic-bezier(0.65, 0, 0.35, 1)` on nav-like elements; image grayscale hover transitions; Webflow spinner keyframes; button color transition
  - Exact motion parameters: `0.4s cubic-bezier(0.65, 0, 0.35, 1)`, `.25s ease-out`, `.3s ease-out`, `.2s ease-in-out`, `.8s linear infinite spin`
  - JavaScript/runtime motion evidence: `IntersectionObserver` and `requestAnimationFrame` usage plus Locomotive Scroll dependency
  - Stylesheet evidence: Webflow CSS bundle plus custom scripts listed above
  - Interpreted motion tags: minimal-motion, fade-reveal
  - Use this as implementation guidance only where evidence is direct. If CSS/JS is minified or only CDN names are visible, mark library/framework attribution as weak.
- Code surface:
  - Framework/runtime hints: Webflow runtime plus `IntersectionObserver`, `requestAnimationFrame`, and Locomotive Scroll references appeared in the captured resources
  - Public stylesheet/script URLs: `avroko.webflow.shared.de3876f8c.min.css`; Locomotive Scroll; Finsweet CMS Slider; js-cookie; jQuery 3.5.1; Webflow chunk scripts
  - CSS variables/tokens observed: explicit variable names were not extracted cleanly, but the stylesheets expose a tokenized Webflow/custom-CSS stack
  - Layout primitives observed: fixed-like top nav, split text field, full-width image section, slider/list structures deeper in the page
  - Component or class naming clues: `nav`, `n-brand`, `n-link`, `slider1-list`, `hp-list`, `newsletter-field`
  - Component computed-style evidence: `assets/2026-06-08-avroko-component-styles.json`
  - Asset CDN and media loading patterns: Webflow CDN image delivery with multiple `.webp` hero assets
- Implementation notes:
  - CSS/layout primitives: leverage broad padding, top-anchored nav, two-column intro copy, and panoramic media bands
  - Token ideas: ivory background, charcoal text, muted gold accent, literary serif plus disciplined sans
  - Libraries or techniques: Webflow stack, Locomotive Scroll, Finsweet CMS Slider, requestAnimationFrame-driven behavior
  - Performance/accessibility concerns: heavy media payload and scroll libraries mean reduced-motion and image-loading policies need active review

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
