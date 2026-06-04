# Motion And Code

## Observed
- Motion:
  - Page transitions: no direct transition evidence found
  - Micro-interactions: infer only when backed by transition/animation evidence or visible screenshot states.
  - Scroll/entrance behavior: not proven in automated pass
  - Timing/easing: x-wrap: wrap; width: 440px; max-width: 90%; padding: 6px; background: linear-gradient(180deg, rgba(255, 238, 204, 0.08) 0%, rgba(255, 255, 255, 0.11) 100%); border: 1px solid rgba(255, 238, 204, 0.05); bord, gin: 40px auto 100px auto; } .request-access-form:hover { background: linear-gradient(180deg, rgba(255, 255, 255, 0.11) 0%, rgba(255, 255, 255, 0.14) 100%); } #email-input, .email-input { flex: 1 1 auto; he, ex: 0 0 auto; min-height: 50px; padding: 0 30px 1px 30px; background: linear-gradient(180deg, #ff661a 0%, #ff4705 100%); border: none; border-radius: 3px; font-size: 15px; font-weight: 500; color: #fff; lin
- Motion code:
  - Motion source: public styles/scripts sampled from captured DOM.
  - CSS animation/transition evidence: none observed
  - Public CSS/JS probe keywords: easing, transform
  - Public CSS/JS motion snippets: x-wrap: wrap; width: 440px; max-width: 90%; padding: 6px; background: linear-gradient(180deg, rgba(255, 238, 204, 0.08) 0%, rgba(255, 255, 255, 0.11) 100%); border: 1px solid rgba(; gin: 40px auto 100px auto; } .request-access-form:hover { background: linear-gradient(180deg, rgba(255, 255, 255, 0.11) 0%, rgba(255, 255, 255, 0.14) 100%); } #email-input, .email-; ex: 0 0 auto; min-height: 50px; padding: 0 30px 1px 30px; background: linear-gradient(180deg, #ff661a 0%, #ff4705 100%); border: none; border-radius: 3px; font-size: 15px; font-wei; : 0.9; } h2 { margin: 20px 0; font-size: 12px; font-weight: 200; text-transform: uppercase; letter-spacing: 2px; color: #fa0; } .request-access-form { display: flex; flex-wrap: wra
  - Exact motion parameters: x-wrap: wrap; width: 440px; max-width: 90%; padding: 6px; background: linear-gradient(180deg, rgba(255, 238, 204, 0.08) 0%, rgba(255, 255, 255, 0.11) 100%); border: 1px solid rgba(; gin: 40px auto 100px auto; } .request-access-form:hover { background: linear-gradient(180deg, rgba(255, 255, 255, 0.11) 0%, rgba(255, 255, 255, 0.14) 100%); } #email-input, .email-; ex: 0 0 auto; min-height: 50px; padding: 0 30px 1px 30px; background: linear-gradient(180deg, #ff661a 0%, #ff4705 100%); border: none; border-radius: 3px; font-size: 15px; font-wei; : 0.9; } h2 { margin: 20px 0; font-size: 12px; font-weight: 200; text-transform: uppercase; letter-spacing: 2px; color: #fa0; } .request-access-form { display: flex; flex-wrap: wra
  - JavaScript/runtime motion evidence: none observed
  - Stylesheet evidence: https://www.cron.com/style.css
  - Interpreted motion tags: restrained, glow-motion
  - Use this as implementation guidance only where evidence is direct. If CSS/JS is minified or only CDN names are visible, mark library/framework attribution as weak.
- Code surface:
  - Framework/runtime hints: no direct runtime hint found
  - Public stylesheet/script URLs: https://www.cron.com/style.css
  - CSS variables/tokens observed: automated pass did not isolate variables; inspect fetched resources for token naming if needed.
  - Layout primitives observed: infer from screenshot and DOM; automated pass records page shape but not semantic layout primitives.
  - Component or class naming clues: DOM saved at `assets/2026-06-04-cron-calendar-interface-dom.html` for manual inspection.
  - Component computed-style evidence: `assets/2026-06-04-cron-calendar-interface-component-styles.json`
  - Asset CDN and media loading patterns: https://www.cron.com/images/brand/cron-logotype-s.png; https://www.cron.com/images/product/cron-2023-02-28@2x.png
- Implementation notes:
  - CSS/layout primitives: use screenshot geometry and DOM resource evidence; refine manually before implementation-grade use.
  - Token ideas: extract from computed colors, font roles, and CSS resources.
  - Libraries or techniques: easing, transform
  - Performance/accessibility concerns: heavy media count 2 and scripts 0; check reduced-motion and image loading before copying motion patterns.

## Inference
- Borrow:
  - Borrow the page-scope-specific composition, hierarchy, media ratios, component density, and proven motion parameters.
  - Borrow category-relevant trust and conversion mechanics visible in the screenshot and text sample.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
