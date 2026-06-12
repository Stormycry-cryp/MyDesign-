# Blind E2E: dashboard

## Selected Reference
- Query: `dashboard analytics table metrics hover`
- Need: `motion:L2,scene:dashboard`
- Reference: Plausible Analytics Live Dashboard (`plausible-analytics-live-dashboard`)

## Apply Pack
- variables_css: /Users/chenyunzhe/Documents/Codex/2026-06-04/files-mentioned-by-the-user-designstyle/work/DesignStyle/designstyle-library/reviews/2026-06-12-final-blind-e2e/dashboard/apply-pack/variables.css
- motion_presets: /Users/chenyunzhe/Documents/Codex/2026-06-04/files-mentioned-by-the-user-designstyle/work/DesignStyle/designstyle-library/reviews/2026-06-12-final-blind-e2e/dashboard/apply-pack/motion-presets.css
- tailwind_theme: /Users/chenyunzhe/Documents/Codex/2026-06-04/files-mentioned-by-the-user-designstyle/work/DesignStyle/designstyle-library/reviews/2026-06-12-final-blind-e2e/dashboard/apply-pack/tailwind.theme.json
- tokens: /Users/chenyunzhe/Documents/Codex/2026-06-04/files-mentioned-by-the-user-designstyle/work/DesignStyle/designstyle-library/reviews/2026-06-12-final-blind-e2e/dashboard/apply-pack/tokens.json
- motion: /Users/chenyunzhe/Documents/Codex/2026-06-04/files-mentioned-by-the-user-designstyle/work/DesignStyle/designstyle-library/reviews/2026-06-12-final-blind-e2e/dashboard/apply-pack/motion.json

## Screenshot QA Evidence
- immediate-load screenshot: /Users/chenyunzhe/Documents/Codex/2026-06-04/files-mentioned-by-the-user-designstyle/work/DesignStyle/designstyle-library/reviews/2026-06-12-final-blind-e2e/dashboard/screenshots/immediate-load.png
- post-animation screenshot: /Users/chenyunzhe/Documents/Codex/2026-06-04/files-mentioned-by-the-user-designstyle/work/DesignStyle/designstyle-library/reviews/2026-06-12-final-blind-e2e/dashboard/screenshots/post-animation.png
- hover/focus screenshot: /Users/chenyunzhe/Documents/Codex/2026-06-04/files-mentioned-by-the-user-designstyle/work/DesignStyle/designstyle-library/reviews/2026-06-12-final-blind-e2e/dashboard/screenshots/hover-focus.png
- mobile screenshot: /Users/chenyunzhe/Documents/Codex/2026-06-04/files-mentioned-by-the-user-designstyle/work/DesignStyle/designstyle-library/reviews/2026-06-12-final-blind-e2e/dashboard/screenshots/mobile.png
- reduced-motion screenshot: /Users/chenyunzhe/Documents/Codex/2026-06-04/files-mentioned-by-the-user-designstyle/work/DesignStyle/designstyle-library/reviews/2026-06-12-final-blind-e2e/dashboard/screenshots/reduced-motion.png

## Motion Traceability
- motion-presets.css: /Users/chenyunzhe/Documents/Codex/2026-06-04/files-mentioned-by-the-user-designstyle/work/DesignStyle/designstyle-library/reviews/2026-06-12-final-blind-e2e/dashboard/apply-pack/motion-presets.css
- motion.json: /Users/chenyunzhe/Documents/Codex/2026-06-04/files-mentioned-by-the-user-designstyle/work/DesignStyle/designstyle-library/reviews/2026-06-12-final-blind-e2e/dashboard/apply-pack/motion.json
- Rule: local fixture may tune timing but keeps preset source files traceable.

## Reference Comparison
- Comparison report: /Users/chenyunzhe/Documents/Codex/2026-06-04/files-mentioned-by-the-user-designstyle/work/DesignStyle/designstyle-library/reviews/2026-06-12-final-blind-e2e/dashboard/comparison.md

## Aesthetic Probe
- score: 84
- decision: proceed
- screenshot: designstyle-library/reviews/2026-06-12-final-blind-e2e/dashboard/probe/dashboard-aesthetic.png

## DNA Checklist
- pass_rate: 1.0
| Decision | Source | Status |
|---|---|---|
| First viewport structure: captured in screenshot at 1440x1000; record exact split/sidebar/hero geometry during manual refinement. | Layout Geometry And Spacing | pass |
| Macro geometry: document size {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 2879}. | Layout Geometry And Spacing | pass |
| Media/card aspect stability: image natural sizes include 300x73; 300x73; 32x32; 150x150; 20x20; 48x48; 32x32; 32x32; 150x150; 32x32. | Layout Geometry And Spacing | pass |
| Observed border radii: 4px; 6px; 6px; 6px; 6px; 6px; 6px; 6px; 6px; 6px; 6px; 6px | Layout Geometry And Spacing | pass |
| Viewport and document: {'w': 1440, 'h': 1000, 'docW': 1440, 'docH': 2879} | Dimension And Ratio System | pass |
| Observed media ratios: 300:73; 300:73; 32:32; 150:150; 20:20; 48:48; 32:32; 32:32; 150:150; 32:32 | Dimension And Ratio System | pass |
| reveal viewport motion uses 300ms cubic-bezier(.23,1,.32,1) | motion.json | pass |
| overlay load motion uses 200ms ease-in | motion.json | pass |
| overlay state-change motion uses 100ms ease-in | motion.json | pass |
| component load motion uses 200ms ease-in | motion.json | pass |
| component load motion uses 1000ms ease-in-out | motion.json | pass |
| reveal viewport motion uses 1500ms cubic-bezier(.4,0,.6,1) | motion.json | pass |

## Iteration Log
| Trigger | Change | Verification |
|---|---|---|
| initial blind E2E | generated fixture from selected Apply Pack | screenshots and comparison report written |
