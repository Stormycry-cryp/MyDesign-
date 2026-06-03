# Beauty Cold Start Batch Review

Created: 2026-06-03

## What Changed

The previous designstyle library was useful but too broad: technology platforms, developer tools, and culture sites were being retrieved for beauty/skincare work because they shared generic terms like product, motion, ecommerce, and storytelling.

This batch adds 10 scene-fit references for skincare, body care, fragrance, spa, clinical-natural, and botanical luxury.

## Included References

- Diptyque: sensorial seasonal fragrance/water-garden campaign.
- Typology: clinical-minimal formula transparency.
- Augustinus Bader: science-backed premium skincare.
- True Botanicals: editorial clean wellness with conversion mechanics.
- Nécessaire: object-led minimal body care.
- La Mer: split luxury product/story hero.
- Osea Malibu: seaweed wellness commerce.
- Flamingo Estate: surreal garden editorial commerce.
- Monastery: dark botanical salon/spa mood.
- Amala Beauty: soft spa-natural split ritual.

## Excluded Or Weak Samples

- Aesop: Cloudflare verification page; not usable visual evidence.
- Susanne Kaufmann: captured blank page; not enough visible evidence.
- Dr. Barbara Sturm: initial evidence had usable screenshot in manual view but extracted DOM was empty in one capture; needs clean recapture before reference.
- Le Labo and Byredo: useful visual cues, but first capture was heavily contaminated by region/cookie overlays. Recapture after dismissing overlays before adding.
- Tata Harper: newsletter/cookie overlays dominated the capture. Recapture cleanly before adding.
- Costa Brazil, Vintner's Daughter, Noble Panacea: blocked, captcha, or timed out during replacement capture.

## Skill Lesson

`add-designstyle` needs a stricter evidence matrix. A useful reference must preserve not just mood, but first-viewport geometry, typography stack roles, color source, asset production plan, media contamination, interaction states, and implementation primitives. Otherwise `use-designstyle` will retrieve vague taste words and the build will drift.

## Verification

- Evidence JSON: `designstyle-capture/reviews/beauty-cold-start-evidence.json` and `designstyle-capture/reviews/beauty-replacement-evidence.json`.
- Screenshots: `designstyle-capture/screenshots/`.
- Draft references: `designstyle-capture/references/`.
