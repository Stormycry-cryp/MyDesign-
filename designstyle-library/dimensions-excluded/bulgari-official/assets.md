# Assets

## Observed
- Assets:
  - Image style: none observed
  - Illustration/icon style: inspect screenshot; automated pass records image sources only.
  - Texture/pattern: inspect screenshot before use.
  - Likely sources or production method: asset URLs/domains in image samples.
- Images/video observed:
  - Captured URL: https://www.bulgari.com/en-us/
  - Page title: Fine Italian Jewelry, Watches and Luxury Goods | BVLGARI Official Store United States
  - Screenshot: screenshots/bulgari-official-desktop.png
  - Viewport: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 3155}
  - Community signal: User requested luxury brand official websites only; selected from aesthetic-gate passed official brand sites and excluded marketplaces/ordinary independent-site-looking pages.
  - Page scope: official brand homepage
  - Secondary pages inspected: link -> None | title:  | h1: none observed | h2: none observed
  - H1 observed: none observed
  - H2 samples: Gold & Steel; Bvlgari Creations; Join the Bvlgari Universe
  - Navigation samples: none observed
  - Images observed: none observed
  - Video observed: none observed
  - Overlays or fixed elements: clicked common overlay buttons none observed; inspect screenshot before final use.
- Asset loading:
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
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
