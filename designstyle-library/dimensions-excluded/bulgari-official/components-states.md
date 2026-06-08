# Components And States

## Observed
- Components:
  - Navigation: none observed
  - Buttons/links: EXPLORE GOLD & STEEL; SHOP JEWELRY; SHOP WATCHES; DISCOVER MORE; Cookies settings; United States
  - Computed component styles: `assets/2026-06-05-bulgari-official-component-styles.json`
  - Cards/sections: inspect screenshot and DOM; automated pass records visible text and media.
  - Forms/inputs: automated pass did not classify forms.
  - Feedback states: not captured; do not infer.
- Code surface:
  - Framework/runtime hints: intersection, request_animation_frame
  - Public stylesheet/script URLs: https://www.bulgari.com/resources/9c96854fd9e79c739cb6267ecff5ff839180425c884ba; https://www.bulgari.com/akam/13/207732d2
  - CSS variables/tokens observed: automated pass did not isolate variables; inspect fetched resources for token naming if needed.
  - Layout primitives observed: infer from screenshot and DOM; automated pass records page shape but not semantic layout primitives.
  - Component or class naming clues: raw DOM is not retained in the library; use L4 on-demand recapture from `https://www.bulgari.com/en-us/` when L0-L3 evidence is insufficient.
  - Component computed-style evidence: `assets/2026-06-05-bulgari-official-component-styles.json`
  - Asset CDN and media loading patterns: none observed

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- Component grammar from Component Grammar

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
