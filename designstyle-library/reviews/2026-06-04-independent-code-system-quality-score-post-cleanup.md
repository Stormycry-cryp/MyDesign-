# Independent Code/System Quality Score After Blocked-Page Cleanup

Date: 2026-06-04

Scope: current active DesignStyle reference library in this repo. Active references are only `designstyle-library/references/*.md`. Files under `references-excluded/`, `assets-excluded/`, and `screenshots-excluded/` are treated as excluded evidence.

## Overall Score

**88/100**

The library is now practically useful as a code/design-system reference layer. The strongest improvement is that all 76 active references have non-empty computed component JSON and validator-backed progressive cards/design-system paths. The main remaining weakness is not color/aesthetic quality; it is evidence cleanliness and exact implementation reliability: 16 active reference Markdown files, plus matching dimension summaries, still contain raw scientific-notation radius noise such as `3.35544e+07px`. The newer component JSON and generated design-system files appear clean for that specific noise, but the active L3/L2 text layer is not fully clean yet.

## Rubric

| Area | Weight | Score | Notes |
|---|---:|---:|---|
| Component/code evidence usefulness | 30 | 26 | 76/76 active component JSON files are non-empty; median 89 samples. Low-sample tail remains. |
| Design-system pack practicality | 25 | 22 | 76/76 `tokens.json` and `component-styles.md` files exist and pass progressive validation. Summaries are useful but not always exact spec-grade. |
| Retrieval/reference practicality | 20 | 18 | Cards and dimensions validate; broad SaaS/dashboard/developer/product coverage. Some entries are more inspiration than component system. |
| Contamination/noise hygiene | 15 | 12 | Blocked Arc evidence is excluded. Challenge-page signatures are absent from active refs/component JSON/design-systems, but sci-px noise remains in references/dimensions. |
| Skill/docs/process readiness | 10 | 10 | Skill docs explicitly define active/excluded handling, component capture, validators, and failure rules. |

## Verified Stats

| Metric | Value |
|---|---:|
| Active reference count | 76 |
| Active design-system directories | 76 |
| Active `tokens.json` count | 76 |
| Active `component-styles.md` count | 76 |
| Active 2026-06-04 component JSON count | 76 |
| Non-empty component JSON files | 76 |
| Total raw component samples | 6,226 |
| Median samples per active reference | 89 |
| Min samples | 6 |
| Max samples | 147 |
| Component JSON files with fewer than 20 samples | 5 |
| Component JSON files with fewer than 50 samples | 14 |
| `validate_references.py` status | pass: 76 valid / 0 invalid |
| `validate_progressive_library.py --json` status | pass: valid true, 76 cards / 0 invalid |
| Excluded blocked reference count | 1 (`arc-browser-product-site`) |
| Active blocked/challenge contamination count | 0 in active references, component JSON, design-systems, and dimensions |
| Active raw DOM challenge-like hits | 4 DOM files / 14 matches, manually checked as product/prose text, not blocked pages |
| Active scientific-notation px noise | 16 active references / 81 matches; 16 dimensions / 81 matches |
| Scientific-notation px in active component JSON | 0 |
| Scientific-notation px in active design-systems | 0 |
| `9999px` retention | retained: 8 references / 47 matches; 11 component JSON / 80 matches; 20 design-system files / 132 matches |

Notes on contamination: broad searches for `captcha`/`recaptcha` find ordinary raw DOM/script/product-copy occurrences such as Vercel's "BotID Invisible CAPTCHA" and Clay's reCAPTCHA script. I did not count those as blocked-page contamination because the actual challenge-page signatures (`Attention Required`, `Cloudflare Ray ID`, `Performance & security by Cloudflare`, `verify you are human`, etc.) are absent from active references, component JSON, design-systems, and dimensions. The previous Arc blocked evidence is preserved only under excluded folders.

## Per-Reference Scores

| Slug | Score | Short note |
|---|---:|---|
| `a24-culture-studio` | 95 | 81 samples; 12 state probes |
| `amie-productivity-calendar` | 93 | 69 samples; 7 state probes; high practical UI fit |
| `apple-vision-pro-product-story` | 96 | 124 computed samples; 12 state probes |
| `bauhaus-clock-interactive-product` | 81 | thin samples (32) |
| `benvenusa-food-wine` | 88 | 51 samples; 1 state probe |
| `buffet-digital-agency` | 91 | 57 samples; 9 state probes |
| `capital-finance-product` | 87 | thin samples (26); 10 state probes |
| `cleo-ai-fintech-storytelling` | 96 | 110 computed samples; 11 state probes |
| `cosmos-creative-network` | 86 | 69 samples; 4 state probes; sci-px noise in reference (12) |
| `counter-forms-typography-resource` | 81 | thin samples (39); 1 state probe; more inspirational than system-grade |
| `developments-media-production` | 93 | 85 samples; 9 state probes |
| `eclipse-builders-software` | 94 | 82 samples; 9 state probes |
| `figma-design-platform` | 96 | 106 computed samples; 12 state probes; high practical UI fit |
| `footer-design-gallery-resource` | 94 | 102 computed samples; 12 state probes; more inspirational than system-grade |
| `glyphs-app-design-tool` | 95 | 112 computed samples; 12 state probes |
| `jacky-winter-gallery` | 92 | 97 samples; 9 state probes; more inspirational than system-grade |
| `linear-product-saas` | 96 | 119 computed samples; 11 state probes; high practical UI fit |
| `livesurface-product-software` | 93 | 77 samples; 12 state probes |
| `lunchbox-restaurant-commerce-saas` | 96 | 146 computed samples; 12 state probes; high practical UI fit |
| `making-software-editorial-tooling` | 89 | 63 samples; 5 state probes; more inspirational than system-grade |
| `mezmo-observability-saas` | 96 | 93 samples; 11 state probes; high practical UI fit |
| `middle-name-agency-studio` | 81 | thin samples (18); 6 state probes |
| `notion-workspace-product` | 96 | 147 computed samples; 8 state probes; high practical UI fit |
| `ossa-wine-ecommerce` | 95 | 85 samples; 12 state probes |
| `overpass-software-platform` | 96 | 126 computed samples; 12 state probes; high practical UI fit |
| `patrick-mason-studio-portfolio` | 75 | thin samples (6); 1 state probe; more inspirational than system-grade |
| `rekki-food-service-app` | 88 | thin samples (42); 11 state probes |
| `snohetta-architecture-studio` | 92 | 59 samples; 9 state probes |
| `stripe-product-platform` | 96 | 114 computed samples; 9 state probes; high practical UI fit |
| `teenage-engineering-hardware-brand` | 92 | 62 samples; 12 state probes |
| `typeform-product-forms-saas` | 96 | 97 samples; 7 state probes; high practical UI fit |
| `uncut-typography-resource` | 79 | thin samples (16); 5 state probes; more inspirational than system-grade |
| `usps-delivers-generational-report` | 86 | thin samples (22); 11 state probes |
| `vercel-developer-platform` | 96 | 131 computed samples; 2 state probes; high practical UI fit |
| `viens-la-travel-hospitality` | 94 | 87 samples; 9 state probes |
| `visual-journal-editorial` | 78 | thin samples (7); 4 state probes; more inspirational than system-grade |
| `viviens-creative-talent` | 80 | thin samples (21) |
| `wam-architecture-studio` | 91 | 69 samples; 10 state probes |
| `webinspoo-accessgrid-pricing-page` | 92 | 99 samples; 12 state probes; sci-px noise in reference (5) |
| `webinspoo-airmee-landing-page` | 92 | 97 samples; 12 state probes; sci-px noise in reference (5) |
| `webinspoo-bevel-landing-page` | 92 | 99 samples; 12 state probes; sci-px noise in reference (5) |
| `webinspoo-braintrust-pricing-page` | 94 | 103 computed samples; 12 state probes; sci-px noise in reference (5) |
| `webinspoo-browserbase-pricing-page` | 94 | 103 computed samples; 12 state probes; sci-px noise in reference (5) |
| `webinspoo-cloudflare-pricing-pattern` | 94 | 103 computed samples; 12 state probes; sci-px noise in reference (5) |
| `webinspoo-exa-ai-pricing-page` | 94 | 103 computed samples; 12 state probes; sci-px noise in reference (5) |
| `webinspoo-expenseai-landing-page` | 94 | 103 computed samples; 12 state probes; sci-px noise in reference (5) |
| `webinspoo-mistral-ai-landing-page` | 94 | 103 computed samples; 12 state probes; sci-px noise in reference (5) |
| `webinspoo-poolside-ai-landing-page` | 94 | 102 computed samples; 12 state probes; sci-px noise in reference (5) |
| `webinspoo-rerun-developer-landing-page` | 95 | 99 samples; 12 state probes; sci-px noise in reference (5); high practical UI fit |
| `webinspoo-unkey-pricing-page` | 92 | 98 samples; 12 state probes; sci-px noise in reference (5) |
| `webinspoo-weav-saas-landing-page` | 96 | 103 computed samples; 12 state probes; sci-px noise in reference (5); high practical UI fit |
| `wiz-cybersecurity-saas` | 94 | 125 computed samples; 1 state probe; sci-px noise in reference (3); high practical UI fit |
| `attio-crm-workspace` | 96 | 94 samples; 4 state probes; high practical UI fit |
| `better-stack-observability` | 96 | 132 computed samples; 7 state probes; high practical UI fit |
| `clay-data-workspace` | 96 | 127 computed samples; 9 state probes; high practical UI fit |
| `climate-trace-explore` | 93 | 97 samples; 9 state probes |
| `cron-calendar-interface` | 83 | thin samples (18); 8 state probes; high practical UI fit |
| `electricity-maps-app` | 90 | 71 samples; 4 state probes |
| `equals-spreadsheet-analytics` | 95 | 74 samples; 12 state probes; high practical UI fit |
| `hex-data-workspace` | 96 | 137 computed samples; 1 state probe; high practical UI fit |
| `mercury-financial-dashboard` | 96 | 104 computed samples; 1 state probe; high practical UI fit |
| `observable-data-platform` | 93 | 70 samples; 6 state probes; high practical UI fit |
| `pitch-interactive-data-studio` | 85 | thin samples (44); 7 state probes |
| `pitch-presentation-workspace` | 96 | 81 samples; 12 state probes; high practical UI fit |
| `plausible-analytics-live-dashboard` | 93 | 73 samples; 7 state probes; high practical UI fit |
| `railway-developer-platform` | 88 | thin samples (38); 4 state probes; high practical UI fit |
| `raycast-productivity` | 84 | thin samples (24); 4 state probes |
| `reflect-notes-interface` | 94 | 91 samples; 12 state probes |
| `render-cloud-platform` | 95 | 73 samples; 12 state probes; high practical UI fit |
| `retool-internal-tools` | 96 | 117 computed samples; 4 state probes; high practical UI fit |
| `rows-spreadsheet-dashboard` | 95 | 60 samples; 12 state probes; high practical UI fit |
| `supabase-developer-platform` | 92 | 63 samples; 2 state probes; high practical UI fit |
| `the-pudding-data-stories` | 93 | 70 samples; 11 state probes |
| `tines-automation-platform` | 96 | 126 computed samples; 9 state probes; high practical UI fit |
| `tinybird-analytics-infrastructure` | 93 | 98 samples; 6 state probes; sci-px noise in reference (1); high practical UI fit |
| `visual-cinnamon-data-art` | 92 | 55 samples; 12 state probes |

## Weaknesses

- Active reference and dimension Markdown still retain scientific-notation px radius noise. This is the main post-cleanup quality gap because users may read L3/L2 evidence directly.
- Some references remain thin as component-system sources despite being valid references: `patrick-mason-studio-portfolio` (6 samples), `visual-journal-editorial` (7), `uncut-typography-resource` (16), `middle-name-agency-studio` (18), and `cron-calendar-interface` (18).
- Several entries are useful visual/copy references but weaker for reusable product UI systems, especially typography resources, gallery/editorial entries, and portfolio/studio sites.
- Raw DOM assets naturally contain scripts, product copy, route data, and large framework payloads. They are useful as evidence, but not clean consumption surfaces. For implementation, prefer component JSON plus design-system summaries.
- Component summaries are practical guides, not exact component specifications for every state. Form, icon, feedback, disabled, loading, and responsive component states are still unevenly captured.

## Improvement Opportunities

- Regenerate or patch only the active reference/dimension text fields that contain `3.35544e+07px`, preserving valid `9999px` pill radii.
- Add a strict validator gate that fails active references and dimensions on scientific-notation `px` values, while allowing `9999px`.
- Add a focused low-sample recrawl or manual enrichment pass for the five under-20-sample references.
- Mark inspiration-heavy references in cards as weaker for implementation-grade component reuse, so search does not over-rank them for dashboard/app-system tasks.
- Add compact per-reference component coverage summaries: categories present, state probes present, missing states, and exact JSON path.

## Commands Run

```bash
find designstyle-library/references -maxdepth 1 -type f -name '*.md' | sort | wc -l
find designstyle-library/references -maxdepth 1 -type f -name '*.md' | sort
find designstyle-library/assets -maxdepth 1 -type f -name '2026-06-04-*-component-styles.json' | wc -l
find designstyle-library/design-systems -mindepth 1 -maxdepth 1 -type d | wc -l
find designstyle-library/design-systems -name tokens.json | wc -l
find designstyle-library/design-systems -name component-styles.md | wc -l
python3 skills/add-designstyle/scripts/validate_references.py --library designstyle-library
python3 skills/add-designstyle/scripts/validate_progressive_library.py --library designstyle-library --json
rg -n -i "cloudflare|captcha|security challenge|checking your browser|verify you are human|turnstile|access denied|blocked|cf-chl|challenge-platform|attention required" designstyle-library/references designstyle-library/assets designstyle-library/design-systems designstyle-library/indexes designstyle-library/dimensions
rg -n "[0-9]+\.[0-9]+e[+-]?[0-9]+px|[0-9]+e[+-]?[0-9]+px" designstyle-library/references designstyle-library/assets designstyle-library/design-systems designstyle-library/indexes designstyle-library/dimensions
rg -n "9999px" designstyle-library/references designstyle-library/assets designstyle-library/design-systems designstyle-library/indexes designstyle-library/dimensions
python3 - <<'PY'  # parsed active slugs, component JSON sample counts, contamination/noise counts
PY
git status --short
```

## Files Inspected

- `designstyle-library/references/*.md`
- `designstyle-library/assets/2026-06-04-*-component-styles.json`
- `designstyle-library/assets/*-dom.html` for contamination checks
- `designstyle-library/design-systems/*/tokens.json`
- `designstyle-library/design-systems/*/component-styles.md`
- `designstyle-library/dimensions/*/*.md`
- `designstyle-library/indexes/cards/*.json`
- `designstyle-library/indexes/manifest.json`
- `designstyle-library/reviews/2026-06-04-recrawl-component-evidence-batch-01.md` through `batch-08.md`
- `designstyle-library/reviews/2026-06-04-recrawl-dry-run.md`
- `designstyle-library/reviews/2026-06-04-blocked-reference-exclusions.md`
- `designstyle-library/reviews/2026-06-04-design-system-template-quality-review.md`
- `skills/designstyle/SKILL.md`
- `skills/add-designstyle/SKILL.md`
- `skills/use-designstyle/SKILL.md`
- `skills/add-designstyle/scripts/validate_references.py`
- `skills/add-designstyle/scripts/validate_progressive_library.py`
