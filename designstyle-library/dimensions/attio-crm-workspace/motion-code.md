# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| hero | load | animation | 30000ms | 0ms | linear | 首屏load：animation，30000ms linear，load 触发 |
| card | load | animation | 10000ms | 0ms | linear | 卡片load：animation，10000ms linear，load 触发 |
| card | load | --pricing-cards-grid-line-position-start | 1000ms | 0ms | ease-out | 卡片load：--pricing-cards-grid-line-position-start，1000ms ease-out，load 触发 |
| card | load | --pricing-cards-grid-line-position-end | 1000ms | 0ms | ease-out | 卡片load：--pricing-cards-grid-line-position-end，1000ms ease-out，load 触发 |
| card | load | animation | 1500ms | 0ms | ease-out | 卡片load：animation，1500ms ease-out，load 触发 |
| card | load | --pricing-cards-grid-line-position-start | 1000ms | 0ms | ease-out | 卡片load：--pricing-cards-grid-line-position-start，1000ms ease-out，load 触发 |
| card | load | --pricing-cards-grid-line-position-end | 1000ms | 0ms | ease-out | 卡片load：--pricing-cards-grid-line-position-end，1000ms ease-out，load 触发 |
| card | load | animation | 1500ms | 0ms | ease-out | 卡片load：animation，1500ms ease-out，load 触发 |
| card | load | animation | 0ms | 0ms | ease-in-out | 卡片load：animation，0ms ease-in-out，load 触发 |
| card | load | animation | 0ms | 0ms | ease-in-out | 卡片load：animation，0ms ease-in-out，load 触发 |
| card | load | animation | 0ms | 0ms | ease-in-out | 卡片load：animation，0ms ease-in-out，load 触发 |
| card | load | animation | 0ms | 0ms | linear | 卡片load：animation，0ms linear，load 触发 |
| component | state-change | background-size | 400ms | 0ms | cubic-bezier(.65, 0, .35, 1) | 组件state-change：background-size，400ms cubic-bezier(.65, 0, .35, 1)，state-change 触发 |
| hero | viewport | animation | 4000ms | 0ms | ease-out | 首屏viewport：animation，4000ms ease-out，viewport 触发 |
| hero | viewport | animation | 4000ms | 0ms | ease-out | 首屏viewport：animation，4000ms ease-out，viewport 触发 |
| hero | viewport | animation | 4000ms | 0ms | ease-out | 首屏viewport：animation，4000ms ease-out，viewport 触发 |
| overlay | viewport | animation | 200ms | 0ms | cubic-bezier(.45, .05, .55, .95) | 浮层viewport：animation，200ms cubic-bezier(.45, .05, .55, .95)，viewport 触发 |
| reveal | viewport | animation | 300ms | 0ms | cubic-bezier(.65, 0, .35, 1) | 入场元素viewport：animation，300ms cubic-bezier(.65, 0, .35, 1)，viewport 触发 |
| reveal | viewport | animation | 800ms | 0ms | linear | 入场元素viewport：animation，800ms linear，viewport 触发 |
| reveal | viewport | animation | 800ms | 0ms | linear | 入场元素viewport：animation，800ms linear，viewport 触发 |
| reveal | viewport | animation | 2000ms | 0ms | cubic-bezier(.4, 0, .6, 1) | 入场元素viewport：animation，2000ms cubic-bezier(.4, 0, .6, 1)，viewport 触发 |
| reveal | viewport | animation | 1000ms | 0ms | ease-in-out | 入场元素viewport：animation，1000ms ease-in-out，viewport 触发 |
| reveal | viewport | animation | 1000ms | 0ms | linear | 入场元素viewport：animation，1000ms linear，viewport 触发 |
| card | load | animation | 10000ms | 0ms | linear | 卡片load：animation 1 -> .99，10000ms linear，load 触发 |
| card | load | animation | 500ms | 0ms | cubic-bezier(.33,1,.68,1) | 卡片load：animation，500ms cubic-bezier(.33,1,.68,1)，load 触发 |
| card | load | animation | 1500ms | 100ms | cubic-bezier(.33,1,.68,1) | 卡片load：animation，1500ms cubic-bezier(.33,1,.68,1)，load 触发 |
| component | load | animation | 4000ms | 0ms | cubic-bezier(.33,1,.68,1) | 组件load：animation，4000ms cubic-bezier(.33,1,.68,1)，load 触发 |
| reveal | viewport | animation | 1600ms | 0ms | cubic-bezier(.38,.01,.12,1) | 入场元素viewport：animation，1600ms cubic-bezier(.38,.01,.12,1)，viewport 触发 |
| reveal | viewport | animation | 1600ms | 0ms | cubic-bezier(.38,.01,.12,1) | 入场元素viewport：animation，1600ms cubic-bezier(.38,.01,.12,1)，viewport 触发 |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: assets/2026-06-11-attio-crm-workspace-motion.json

## Missing Evidence
- motion-button-state-change-color-missing-missing lacks duration_ms
- motion-button-state-change-color-missing-missing lacks easing
- motion-button-state-change-border-color-missing-missing lacks duration_ms
- motion-button-state-change-border-color-missing-missing lacks easing
- motion-button-state-change-button-primary-bg-from-missing-missing lacks duration_ms
- motion-button-state-change-button-primary-bg-from-missing-missing lacks easing
- motion-button-state-change-button-primary-bg-to-missing-missing lacks duration_ms
- motion-button-state-change-button-primary-bg-to-missing-missing lacks easing
- motion-button-state-change-background-color-missing-missing lacks duration_ms
- motion-button-state-change-background-color-missing-missing lacks easing
- motion-card-load-animation-0-missing lacks easing
- motion-card-load-animation-0-missing lacks easing
- motion-card-load-animation-0-missing lacks easing
- motion-component-active-all-50-missing lacks easing
- motion-component-focus-all-300-missing lacks easing
- motion-card-load-animation-0-missing lacks easing
- motion-card-load-animation-0-missing lacks easing

## Snippet Appendix
### motion-hero-load-animation-30000-linear

```css
.ai-hero-box-gradient-progress { animation: 30s linear infinite ai-hero-box-gradient-spin; }
```

### motion-card-load-animation-10000-linear

```css
.reporting-hero-card-reports { animation: 10s linear infinite rotate-reporting; }
```

### motion-card-load-pricing-cards-grid-line-position-start-1000-ease-out

```css
.pricing-cards-grid-line { transition-property: --pricing-cards-grid-line-position-start; transition-duration: 1s; transition-timing-function: ease-out; }
```

### motion-card-load-pricing-cards-grid-line-position-end-1000-ease-out

```css
.pricing-cards-grid-line { transition-property: --pricing-cards-grid-line-position-end; transition-duration: 1s; transition-timing-function: ease-out; }
```

### motion-card-load-animation-1500-ease-out

```css
.pricing-cards-grid-line { animation: 1.5s ease-out both pricing-cards-grid-line-appear; }
```

### motion-card-load-pricing-cards-grid-line-position-start-1000-ease-out

```css
.pricing-cards-grid-line-vertical { transition-property: --pricing-cards-grid-line-position-start; transition-duration: 1s; transition-timing-function: ease-out; }
```

### motion-card-load-pricing-cards-grid-line-position-end-1000-ease-out

```css
.pricing-cards-grid-line-vertical { transition-property: --pricing-cards-grid-line-position-end; transition-duration: 1s; transition-timing-function: ease-out; }
```

### motion-card-load-animation-1500-ease-out

```css
.pricing-cards-grid-line-vertical { animation: 1.5s ease-out both pricing-cards-grid-line-appear; }
```

### motion-card-load-animation-0-ease-in-out

```css
.workflows-hero-card .workflows-hero-card-connection { animation: missing var(--duration) ease-in-out 0ms; }
```

### motion-card-load-animation-0-ease-in-out

```css
.workflows-hero-card .workflows-hero-card-running { animation: missing var(--duration) ease-in-out 0ms; }
```

### motion-card-load-animation-0-ease-in-out

```css
.workflows-hero-card .workflows-hero-card-completed { animation: missing var(--duration) ease-in-out 0ms; }
```

### motion-card-load-animation-0-linear

```css
.workflows-hero-card { animation: rotate var(--duration) linear 0ms; }
```

### motion-component-state-change-background-size-400-cubic-bezier-65-0-35-1

```css
.attio-group-hover-underline { transition-property: background-size; transition-duration: .4s; transition-timing-function: cubic-bezier(.65, 0, .35, 1); }
```

### motion-hero-viewport-animation-4000-ease-out

```css
.animate-\[video-hero-pulse_4s_ease-out_infinite\] { animation: 4s ease-out infinite video-hero-pulse; }
```

### motion-hero-viewport-animation-4000-ease-out

```css
.animate-\[video-hero-ripple-inner_4s_ease-out_infinite\] { animation: 4s ease-out infinite video-hero-ripple-inner; }
```

### motion-hero-viewport-animation-4000-ease-out

```css
.animate-\[video-hero-ripple-outer_4s_ease-out_infinite\] { animation: 4s ease-out infinite video-hero-ripple-outer; }
```

### motion-overlay-viewport-animation-200-cubic-bezier-45-05-55-95

```css
.animate-dialog-scale-in { animation: dialog-scale-in .2s cubic-bezier(.45, .05, .55, .95); }
```

### motion-reveal-viewport-animation-300-cubic-bezier-65-0-35-1

```css
.animate-in { animation: enter .3s cubic-bezier(.65, 0, .35, 1); }
```

### motion-reveal-viewport-animation-800-linear

```css
.animate-productivity-intro-height { animation: productivity-intro-height .8s linear; }
```

### motion-reveal-viewport-animation-800-linear

```css
.animate-productivity-intro-width { animation: productivity-intro-width .8s linear; }
```

### motion-reveal-viewport-animation-2000-cubic-bezier-4-0-6-1

```css
.animate-pulse { animation: pulse 2s cubic-bezier(.4, 0, .6, 1) infinite; }
```

### motion-reveal-viewport-animation-1000-ease-in-out

```css
.animate-search-shine { animation: search-shine 1s ease-in-out infinite; }
```

### motion-reveal-viewport-animation-1000-linear

```css
.animate-spin { animation: spin 1s linear infinite; }
```

### motion-card-load-animation-10000-linear

```css
.data-model-cards-mobile-connection-container { animation: 10s linear infinite data-model-cards-mobile-connection-container; }
```

### motion-card-load-animation-500-cubic-bezier-33-1-68-1

```css
.data-model-cards-mobile-connector { animation: missing .5s cubic-bezier(.33,1,.68,1) 0ms; }
```

### motion-card-load-animation-1500-cubic-bezier-33-1-68-1

```css
.data-model-cards-mobile-connection { animation: missing 1.5s cubic-bezier(.33,1,.68,1) .1s; }
```

### motion-component-load-animation-4000-cubic-bezier-33-1-68-1

```css
.data-model-progress-active { animation: 4s cubic-bezier(.33,1,.68,1) both data-model-progress-process; }
```

### motion-reveal-viewport-animation-1600-cubic-bezier-38-01-12-1

```css
.mask-reveal-to-right { animation: 1.6s cubic-bezier(.38,.01,.12,1) both reveal-to-right; }
```

### motion-reveal-viewport-animation-1600-cubic-bezier-38-01-12-1

```css
.mask-reveal-to-bottom { animation: 1.6s cubic-bezier(.38,.01,.12,1) both reveal-to-bottom; }
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
