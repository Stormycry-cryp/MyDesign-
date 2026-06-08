# Components And States

## Observed
- Components:
  - Navigation: FIND A RETAILER; Racing
  - Buttons/links: USA; McLAREN.COM / AUTOMOTIVE; MODELS; MSO; OWNERSHIP; EXPERIENCES; ABOUT; PRE-OWNED; 01; 02; 03; 04
  - Computed component styles: `assets/2026-06-05-mclaren-official-component-styles.json`
  - Cards/sections: inspect screenshot and DOM; automated pass records visible text and media.
  - Forms/inputs: automated pass did not classify forms.
  - Feedback states: not captured; do not infer.
- Code surface:
  - Framework/runtime hints: intersection, swiper
  - Public stylesheet/script URLs: https://cdn.plyr.io/3.7.8/plyr.css; https://fonts.googleapis.com/css2?family=Noto+Sans:ital,wght@0,100..900;1,100..900&display=swap; https://cars.mclaren.com/assets/index-BOmZ3I7K.css; https://cars.mclaren.com/assets/plyr-JIUNXpB2.css; https://cdn-ukwest.onetrust.com/scripttemplates/otSDKStub.js?did=55d255c2-aeea-44af-8cd0-c6cf18323f83; https://www.googletagmanager.com/gtm.js?id=GTM-NMKLLLLQ; https://cars.mclaren.com/assets/index-Cf4dXNTm.js
  - CSS variables/tokens observed: automated pass did not isolate variables; inspect fetched resources for token naming if needed.
  - Layout primitives observed: infer from screenshot and DOM; automated pass records page shape but not semantic layout primitives.
  - Component or class naming clues: raw DOM is not retained in the library; use L4 on-demand recapture from `https://cars.mclaren.com/us_en` when L0-L3 evidence is insufficient.
  - Component computed-style evidence: `assets/2026-06-05-mclaren-official-component-styles.json`
  - Asset CDN and media loading patterns: https://cars-assets-production.mclaren.com/3805/united-states.webp; https://cars-assets-production.mclaren.com/5505/Hero-Artura-1000GP.jpg; https://cars-assets-production.mclaren.com/5518/1000GP-Home-Slider-Mobile.jpg; https://cars-assets-production.mclaren.com/5515/Hero-Mobile-Artura-1000GP.jpg; https://cars-assets-production.mclaren.com/5418/McLaren_PE_Track_Thumbnail.png; https://cars-assets-production.mclaren.com/5373/mclaren-artura-mcl39-carousel-thumbnail.jpg; https://cars-assets-production.mclaren.com/5375/mclaren-mso-nat-bowen-carousel-thumbnail.jpg; https://cars-assets-production.mclaren.com/5376/mclaren-750s-jc96-carousel-thumbnail.jpg

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- Component grammar from Component Grammar

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
