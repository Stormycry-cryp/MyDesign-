# Components And States

## Observed
- Components:
  - Navigation: DEALERSHIPS; BEYOND; MUSEUM; STORE; NEWS; Design; Sustainability; History; Financial services; Warranty extension; Driving Programs; Lounge; Club; Podcast; COMPANY; SUSTAINABILITY
  - Buttons/links: MENU; MODELS; OWNERSHIP; COMPANY; MOTORSPORT; LANGUAGES; Allow animations; EXPLORE THE MODEL; DOWNLOAD BROCHURE; EXPLORE THE MODEL; DOWNLOAD BROCHURE; EXPLORE THE MODEL
  - Computed component styles: `assets/2026-06-05-lamborghini-official-component-styles.json`
  - Cards/sections: inspect screenshot and DOM; automated pass records visible text and media.
  - Forms/inputs: automated pass did not classify forms.
  - Feedback states: not captured; do not infer.
- Code surface:
  - Framework/runtime hints: request_animation_frame, swiper
  - CSS variables/tokens observed: automated pass did not isolate variables; inspect fetched resources for token naming if needed.
  - Layout primitives observed: infer from screenshot and DOM; automated pass records page shape but not semantic layout primitives.
  - Component or class naming clues: raw DOM is not retained in the library; use L4 on-demand recapture from `https://www.lamborghini.com/en-en` when L0-L3 evidence is insufficient.
  - Component computed-style evidence: `assets/2026-06-05-lamborghini-official-component-styles.json`
  - Asset CDN and media loading patterns: https://www.lamborghini.com/sites/it-en/files/DAM/lamborghini/logos/2024/03_26/logo_header_01.svg; https://www.lamborghini.com/sites/it-en/files/DAM/lamborghini/homepage/slider/2026/05_09/hero-optim.jpg; https://www.lamborghini.com/sites/it-en/files/DAM/lamborghini/0_facelift_2025/loghi/temerario/temerario_center_light.svg; https://www.lamborghini.com/sites/it-en/files/DAM/lamborghini/0_facelift_2025/homepage/models/temerario/familyChooser-Temerario_0.png; https://www.lamborghini.com/sites/it-en/files/DAM/lamborghini/0_facelift_2025/loghi/urus/urus_center_light.svg; https://www.lamborghini.com/sites/it-en/files/DAM/lamborghini/0_facelift_2025/homepage/models/urus/models_urus_se.png; data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7; data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7
  - Public stylesheet/script URLs: missing

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- Component grammar from Component Grammar

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
