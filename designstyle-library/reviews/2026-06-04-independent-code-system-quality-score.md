# Independent Code/System Quality Score

Date: 2026-06-04
Evaluator stance: clean-context file inspection only. Emphasis is code/design-system usefulness and practical reuse, not color taste.

## Overall Score

**84/100**

This is a strong B/B+ reference library for design-to-code guidance. The current update materially improves usefulness: every reference now has a retained design-system pack and non-empty computed component JSON. It is not yet a fully implementation-grade component/state library because raw JSON still contains browser-computed radius noise in 17 references, hover/focus deltas are absent, and some entries have very thin component samples.

## Rubric

| Area | Weight | Score | Evidence |
|---|---:|---:|---|
| Component/code evidence usefulness | 40 | 33 | 77/77 component JSON files are non-empty; 6,230 total computed samples with rect + styles. Weakness: 0 refs with hover/focus deltas and some refs have very small sample counts. |
| Design-system retention | 25 | 22 | 77/77 `tokens.json` and `component-styles.md`; 77/77 design systems reference computed component evidence; validator accepts all component style systems. |
| Reference practicality/retrieval | 20 | 17 | 77 L1 cards, 539 L2 dimensions planned, search returns design-system paths and excerpts. Practicality is strongest for SaaS, dashboard, developer, workspace, pricing, and analytics references; weaker for portfolio/editorial/resource references. |
| Evidence hygiene and limits | 15 | 12 | Validators pass and summaries state missing evidence. Deducted because raw `assets/*component-styles.json` still contains `3.35544e+07px` radius noise in 17 refs, despite design-system summaries being clean. |

## Verified Stats

- References: **77** Markdown files in `designstyle-library/references`.
- L1 cards: **77** JSON files in `designstyle-library/indexes/cards`.
- Design-system packs: **77** directories in `designstyle-library/design-systems`.
- Component JSON files: **77** files matching `designstyle-library/assets/2026-06-04-*-component-styles.json`.
- JSON samples: **77/77 non-empty**.
- Component sample counts: **6,230 total**, **87 median**, **4 min**, **147 max**.
- Style/rect completeness: **6,230/6,230 samples** include computed style evidence and rect evidence.
- Category coverage per JSON: **5 median**, **2 min**, **6 max** categories.
- Design systems with computed component evidence references: **77/77**.
- Validators run:
  - `validate_references.py --json`: **77 total, 77 valid, 0 invalid**.
  - `validate_progressive_library.py --json`: **valid=true, 77 cards, 0 invalid, 0 errors**.
  - `build_progressive_reference.py --all --dry-run`: **planned_cards=77, planned_dimensions=539**.
- Search-side practicality check: `search_references.py "dashboard analytics color system table components" --matrix --design-system` returned ranked cards with design-system paths, palette excerpts, and component-style excerpts.
- Recrawl reports: batch reports 01-08 record all references as `ok` with component sample counts.
- Scientific-notation radius noise:
  - `designstyle-library/design-systems/*/{tokens.json,component-styles.md}`: **0 files** with `e+06/e+07/e+08px` radius noise.
  - Raw `designstyle-library/assets/2026-06-04-*-component-styles.json`: **17 refs / 431 matches** still contain `3.35544e+07px`.

## Per-Reference Scores

| Slug | Score | Note |
|---|---:|---|
| `a24-culture-studio` | 84 | 81 computed samples; 6 categories; more visual/reference-led |
| `amie-productivity-calendar` | 86 | 69 samples; 4 categories; practical scene fit |
| `apple-vision-pro-product-story` | 85 | 124 computed samples; 5 categories; more visual/reference-led |
| `arc-browser-product-site` | 73 | 4 samples; 2 categories; thin component evidence |
| `attio-crm-workspace` | 90 | 94 computed samples; 5 categories; strong practical workspace reference |
| `bauhaus-clock-interactive-product` | 77 | 32 samples; 3 categories; visual/interactive object more than reusable system |
| `benvenusa-food-wine` | 79 | 51 samples; 4 categories; content/brand-led |
| `better-stack-observability` | 90 | 132 computed samples; 6 categories; strong observability/system fit |
| `buffet-digital-agency` | 79 | 57 samples; 4 categories; studio-led practicality |
| `capital-finance-product` | 79 | 26 samples; 5 categories; practical scene but thin sample depth |
| `clay-data-workspace` | 90 | 127 computed samples; 5 categories; strong data-workspace fit |
| `cleo-ai-fintech-storytelling` | 90 | 110 computed samples; 5 categories; strong product/story component capture |
| `climate-trace-explore` | 86 | 97 computed samples; 4 categories; useful map/data display reference |
| `cosmos-creative-network` | 80 | 69 samples; 6 categories; raw radius noise 26x |
| `counter-forms-typography-resource` | 76 | 39 samples; 4 categories; resource page, limited system transfer |
| `cron-calendar-interface` | 78 | 18 samples; 3 categories; practical category but thin evidence |
| `developments-media-production` | 81 | 85 computed samples; 4 categories; media/studio-led |
| `eclipse-builders-software` | 87 | 82 computed samples; 5 categories; useful software product reference |
| `electricity-maps-app` | 85 | 71 samples; 4 categories; useful app/map UI evidence |
| `equals-spreadsheet-analytics` | 87 | 74 samples; 5 categories; practical spreadsheet analytics fit |
| `figma-design-platform` | 89 | 106 computed samples; 5 categories; strong product/platform system reference |
| `footer-design-gallery-resource` | 85 | 102 computed samples; 5 categories; useful pattern resource but not app-first |
| `glyphs-app-design-tool` | 85 | 112 computed samples; 4 categories; good tool reference, narrower component grammar |
| `hex-data-workspace` | 90 | 137 computed samples; 5 categories; strong analytics workspace fit |
| `jacky-winter-gallery` | 85 | 97 computed samples; 5 categories; good gallery evidence, less product-system practical |
| `linear-product-saas` | 90 | 119 computed samples; 6 categories; strong SaaS/product system fit |
| `livesurface-product-software` | 83 | 77 samples; 4 categories; solid but less state-rich |
| `lunchbox-restaurant-commerce-saas` | 90 | 146 computed samples; 6 categories; strong commerce SaaS fit |
| `making-software-editorial-tooling` | 82 | 63 samples; 5 categories; editorial/tooling hybrid, moderate practicality |
| `mercury-financial-dashboard` | 84 | 104 computed samples; 6 categories; raw radius noise 2x |
| `mezmo-observability-saas` | 89 | 93 computed samples; 4 categories; strong technical SaaS fit |
| `middle-name-agency-studio` | 73 | 18 samples; 5 categories; thin code evidence, studio-led |
| `notion-workspace-product` | 90 | 147 computed samples; 6 categories; strong workspace product reference |
| `observable-data-platform` | 86 | 70 samples; 4 categories; practical data-platform fit |
| `ossa-wine-ecommerce` | 85 | 85 computed samples; 6 categories; useful commerce reference |
| `overpass-software-platform` | 90 | 126 computed samples; 6 categories; strong software platform evidence |
| `patrick-mason-studio-portfolio` | 73 | 6 samples; 3 categories; very thin component evidence |
| `pitch-interactive-data-studio` | 76 | 44 samples; 4 categories; useful for data studio mood, less component-complete |
| `pitch-presentation-workspace` | 90 | 81 computed samples; 6 categories; practical productivity/workspace fit |
| `plausible-analytics-live-dashboard` | 86 | 73 samples; 4 categories; strong dashboard scene fit |
| `railway-developer-platform` | 84 | 38 samples; 4 categories; high scene fit but sample depth is lower |
| `raycast-productivity` | 78 | 24 samples; 3 categories; practical category but thin component capture |
| `reflect-notes-interface` | 90 | 91 computed samples; 5 categories; strong productivity UI fit |
| `rekki-food-service-app` | 79 | 42 samples; 6 categories; practical domain but moderate evidence |
| `render-cloud-platform` | 88 | 73 samples; 5 categories; strong cloud platform fit |
| `retool-internal-tools` | 90 | 117 computed samples; 5 categories; strong internal-tools fit |
| `rows-spreadsheet-dashboard` | 87 | 60 samples; 5 categories; practical spreadsheet dashboard fit |
| `snohetta-architecture-studio` | 80 | 59 samples; 5 categories; studio/portfolio-led |
| `stripe-product-platform` | 90 | 114 computed samples; 5 categories; strong platform reference |
| `supabase-developer-platform` | 88 | 63 samples; 5 categories; strong developer platform fit |
| `teenage-engineering-hardware-brand` | 80 | 62 samples; 5 categories; brand/product-led |
| `the-pudding-data-stories` | 82 | 70 samples; 6 categories; useful information-display reference |
| `tines-automation-platform` | 90 | 126 computed samples; 6 categories; strong automation SaaS fit |
| `tinybird-analytics-infrastructure` | 84 | 98 computed samples; 4 categories; raw radius noise 1x |
| `typeform-product-forms-saas` | 89 | 97 computed samples; 5 categories; strong forms/product fit |
| `uncut-typography-resource` | 73 | 16 samples; 5 categories; thin system evidence |
| `usps-delivers-generational-report` | 73 | 22 samples; 4 categories; report/editorial, limited component practicality |
| `vercel-developer-platform` | 90 | 131 computed samples; 6 categories; strong developer platform fit |
| `viens-la-travel-hospitality` | 84 | 87 computed samples; 5 categories; good content/service reference |
| `visual-cinnamon-data-art` | 80 | 55 samples; 5 categories; data-art reference, moderate system transfer |
| `visual-journal-editorial` | 73 | 7 samples; 4 categories; very thin component evidence |
| `viviens-creative-talent` | 73 | 21 samples; 2 categories; thin and portfolio-led |
| `wam-architecture-studio` | 80 | 69 samples; 4 categories; portfolio/studio-led |
| `webinspoo-accessgrid-pricing-page` | 84 | 99 computed samples; 6 categories; raw radius noise 27x |
| `webinspoo-airmee-landing-page` | 84 | 97 computed samples; 6 categories; raw radius noise 25x |
| `webinspoo-bevel-landing-page` | 84 | 99 computed samples; 6 categories; raw radius noise 27x |
| `webinspoo-braintrust-pricing-page` | 84 | 103 computed samples; 6 categories; raw radius noise 32x |
| `webinspoo-browserbase-pricing-page` | 84 | 103 computed samples; 6 categories; raw radius noise 32x |
| `webinspoo-cloudflare-pricing-pattern` | 84 | 103 computed samples; 6 categories; raw radius noise 31x |
| `webinspoo-exa-ai-pricing-page` | 84 | 103 computed samples; 6 categories; raw radius noise 31x |
| `webinspoo-expenseai-landing-page` | 84 | 103 computed samples; 6 categories; raw radius noise 32x |
| `webinspoo-mistral-ai-landing-page` | 84 | 103 computed samples; 6 categories; raw radius noise 31x |
| `webinspoo-poolside-ai-landing-page` | 84 | 102 computed samples; 6 categories; raw radius noise 30x |
| `webinspoo-rerun-developer-landing-page` | 84 | 99 computed samples; 6 categories; raw radius noise 27x |
| `webinspoo-unkey-pricing-page` | 84 | 98 computed samples; 6 categories; raw radius noise 26x |
| `webinspoo-weav-saas-landing-page` | 84 | 103 computed samples; 6 categories; raw radius noise 32x |
| `wiz-cybersecurity-saas` | 84 | 125 computed samples; 6 categories; raw radius noise 19x |

## Main Weaknesses

1. Raw component JSON still has obvious radius noise. The design-system summaries appear clean, but the scoped raw evidence files still contain `3.35544e+07px` in 17 references. Since the user explicitly asked to inspect raw `assets/2026-06-04-*-component-styles.json`, this counts as unresolved hygiene debt.
2. No observed hover/focus deltas. Component files contain transition values and Missing Evidence sections, but the stats show **0 refs** with actual hover/focus delta captures.
3. Some references are thin for code/system reuse. `arc-browser-product-site`, `patrick-mason-studio-portfolio`, `visual-journal-editorial`, `uncut-typography-resource`, `viviens-creative-talent`, and `middle-name-agency-studio` have low sample counts or weaker component breadth.
4. Component taxonomy is broad but shallow. Common sections are Navigation, Button, Card, Icon, Form, Feedback state, but forms and feedback states are often explicitly missing rather than captured.
5. WebInspoo-derived entries are numerous and structurally similar. They are useful for pricing/landing inspiration, but raw radius noise and repeated sample patterns reduce their independent reference value.

## Top Improvement Opportunities

1. Normalize raw JSON before retention. Replace abnormal computed radii like `3.35544e+07px` with a bounded semantic value, or keep the original under an `rawComputed` field and expose a cleaned `normalizedStyles` field.
2. Add real interaction-state capture. Re-run a focused browser pass that stores hover/focus deltas for buttons, links, nav menus, pricing cards, form controls, and toggles.
3. Backfill weak references with targeted captures or mark them lower-confidence. For sample counts under 25, either re-crawl meaningful secondary pages/states or explicitly demote retrieval confidence.
4. Add component role specificity. Separate real cards, layout containers, feature tiles, pricing tiers, nav shells, media frames, and dashboard widgets instead of relying heavily on generic `Card`.
5. Add task-oriented retrieval QA. Run representative queries for dashboard, pricing, internal tool, editorial, ecommerce, portfolio, and app screen tasks and snapshot whether the top 5 results are scene-fit rather than merely style-fit.

## Files Inspected

- `README.md`
- `MANIFEST.md`
- `skills/designstyle/SKILL.md`
- `skills/add-designstyle/SKILL.md`
- `skills/use-designstyle/SKILL.md`
- `skills/add-designstyle/scripts/validate_references.py`
- `skills/add-designstyle/scripts/validate_progressive_library.py`
- `skills/add-designstyle/scripts/build_progressive_reference.py`
- `skills/use-designstyle/scripts/search_references.py`
- `designstyle-library/references/*.md`
- `designstyle-library/indexes/cards/*.json`
- `designstyle-library/dimensions/*/*.md`
- `designstyle-library/design-systems/*/tokens.json`
- `designstyle-library/design-systems/*/component-styles.md`
- `designstyle-library/assets/2026-06-04-*-component-styles.json`
- `designstyle-library/reviews/2026-06-04-recrawl-component-evidence-batch-01.md` through `batch-08.md`
- `designstyle-library/reviews/2026-06-04-recrawl-dry-run.md`
- `designstyle-library/reviews/2026-06-04-design-system-template-quality-review.md`

## Commands Run

```bash
find designstyle-library/references -maxdepth 1 -type f -name '*.md' | wc -l
find designstyle-library/indexes/cards -maxdepth 1 -type f -name '*.json' | wc -l
find designstyle-library/design-systems -mindepth 1 -maxdepth 1 -type d | wc -l
find designstyle-library/assets -maxdepth 1 -type f -name '2026-06-04-*-component-styles.json' | wc -l
python3 skills/add-designstyle/scripts/validate_references.py --library designstyle-library --json
python3 skills/add-designstyle/scripts/validate_progressive_library.py --library designstyle-library --json
python3 skills/add-designstyle/scripts/build_progressive_reference.py --library designstyle-library --all --dry-run
python3 skills/use-designstyle/scripts/search_references.py "dashboard analytics color system table components" --library designstyle-library --matrix --design-system
rg -n "3\\.35544e\\+07|e\\+07|e\\+08|e\\+06" designstyle-library/design-systems designstyle-library/assets/2026-06-04-*-component-styles.json
```

