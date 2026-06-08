# Motion And Code

## Observed
- Motion:
  - Page transitions: no direct code evidence
  - Micro-interactions: likely hover states in the commerce/navigation shell, but not proven
  - Scroll/entrance behavior: missing evidence
  - Timing/easing: missing evidence
- Motion code:
  - Motion source: screenshot and probe text only
  - CSS animation/transition evidence: no direct code evidence
  - Public CSS/JS probe keywords: missing evidence
  - Public CSS/JS motion snippets: missing evidence
  - Exact motion parameters: no direct code evidence
  - JavaScript/runtime motion evidence: Shopify runtime import string observed in probe body text, but not enough to infer motion behavior
  - Stylesheet evidence: missing evidence
  - Interpreted motion tags: minimal-motion, fade-reveal
  - Use this as implementation guidance only where evidence is direct. If CSS/JS is minified or only CDN names are visible, mark library/framework attribution as weak.
- Code surface:
  - Framework/runtime hints: Shopify storefront runtime was visible in the probe output
  - Public stylesheet/script URLs: no reliable stylesheet list captured in the successful probe; deeper formal extraction later timed out
  - CSS variables/tokens observed: missing evidence
  - Layout primitives observed: sticky or fixed commerce header over full-width hero inferred from screenshot
  - Component or class naming clues: missing evidence
  - Component computed-style evidence: `assets/2026-06-08-roman-and-williams-component-styles.json`
  - Asset CDN and media loading patterns: one Shopify-hosted video URL was observed during probe
- Implementation notes:
  - CSS/layout primitives: horizontal header rail, wide media hero, lower-left text anchoring, generous negative space
  - Token ideas: warm cream background, dark charcoal text, restrained serif/sans pairing, muted heritage-photo palette
  - Libraries or techniques: no direct code evidence
  - Performance/accessibility concerns: cookie and commerce overlays can easily pollute the first viewport; strong QA is required if reused

## Inference
- Borrow:
  - Borrow the restraint of the header and the confidence of letting imagery and serif copy do the persuasion.
  - Borrow the mix of design-practice storytelling with a commerce-capable shell.
  - Borrow the warm-neutral palette and low-contrast sophistication.

## Missing Evidence
- None recorded.

## Do Not Copy
- Do not copy the exact Roman and Williams voice, wordmark treatment, or luxury-craft phrasing.
- Do not copy the street-sign hero motif or the brand’s historical romance framing verbatim.
- Do not overstate motion or component detail that was not directly captured.
