# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| reveal | viewport | animation | 5000ms | 0ms | linear | 入场元素viewport：animation，5000ms linear，viewport 触发 |
| reveal | viewport | animation | 250ms | 75ms | ease-out | 入场元素viewport：animation，250ms ease-out，viewport 触发 |
| reveal | viewport | animation | 1250ms | 0ms | cubic-bezier(.4, .04, .04, 1) | 入场元素viewport：animation，1250ms cubic-bezier(.4, .04, .04, 1)，viewport 触发 |
| reveal | viewport | animation | 350ms | 0ms | cubic-bezier(.16, 1, .3, 1) | 入场元素viewport：animation，350ms cubic-bezier(.16, 1, .3, 1)，viewport 触发 |
| reveal | viewport | animation | 500ms | 0ms | cubic-bezier(.4, .04, .04, 1) | 入场元素viewport：animation，500ms cubic-bezier(.4, .04, .04, 1)，viewport 触发 |
| reveal | viewport | animation | 500ms | 0ms | cubic-bezier(.4, .04, .04, 1) | 入场元素viewport：animation，500ms cubic-bezier(.4, .04, .04, 1)，viewport 触发 |
| reveal | viewport | animation | 0ms | 0ms | cubic-bezier(0, 0, .2, 1) | 入场元素viewport：animation，0ms cubic-bezier(0, 0, .2, 1)，viewport 触发 |
| reveal | viewport | animation | 1000ms | 0ms | cubic-bezier(0, 0, .2, 1) | 入场元素viewport：animation，1000ms cubic-bezier(0, 0, .2, 1)，viewport 触发 |
| reveal | viewport | animation | 10000ms | 0ms | linear | 入场元素viewport：animation，10000ms linear，viewport 触发 |
| reveal | viewport | animation | 2000ms | 0ms | cubic-bezier(.4, 0, .6, 1) | 入场元素viewport：animation，2000ms cubic-bezier(.4, 0, .6, 1)，viewport 触发 |
| reveal | viewport | animation | 500ms | 0ms | ease-in-out | 入场元素viewport：animation，500ms ease-in-out，viewport 触发 |
| reveal | viewport | animation | 500ms | 0ms | ease-in-out | 入场元素viewport：animation，500ms ease-in-out，viewport 触发 |
| reveal | viewport | animation | 500ms | 0ms | ease-in-out | 入场元素viewport：animation，500ms ease-in-out，viewport 触发 |
| reveal | viewport | animation | 500ms | 0ms | ease-in-out | 入场元素viewport：animation，500ms ease-in-out，viewport 触发 |
| reveal | viewport | animation | 1250ms | 0ms | cubic-bezier(.4, .04, .04, 1) | 入场元素viewport：animation，1250ms cubic-bezier(.4, .04, .04, 1)，viewport 触发 |
| reveal | viewport | animation | 1000ms | 0ms | linear | 入场元素viewport：animation，1000ms linear，viewport 触发 |
| component | load | animation | 1200ms | 0ms | linear | 组件load：animation 1 -> .15，1200ms linear，load 触发 |
| component | state-change | opacity | 500ms | 0ms | cubic-bezier(.4, .01, .165, .99) | 组件state-change：opacity missing -> translateY(24px)，500ms cubic-bezier(.4, .01, .165, .99)，state-change 触发 |
| navigation | state-change | color | 90ms | 0ms | ease | 导航state-change：color，90ms ease，state-change 触发 |
| component | load | animation | 1500ms | 0ms | ease-in-out | 组件load：animation translate(-50%) -> translate(-50%)，1500ms ease-in-out，load 触发 |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: assets/2026-06-12-vercel-developer-platform-motion.json

## Missing Evidence
- motion-reveal-viewport-animation-1000-missing lacks easing
- motion-reveal-viewport-animation-1000-missing lacks easing
- motion-reveal-viewport-animation-missing-missing lacks duration_ms
- motion-reveal-viewport-animation-missing-missing lacks easing
- motion-reveal-viewport-animation-missing-missing lacks duration_ms
- motion-reveal-viewport-animation-missing-missing lacks easing
- motion-reveal-viewport-animation-missing-missing lacks duration_ms
- motion-reveal-viewport-animation-missing-missing lacks easing
- motion-reveal-viewport-animation-missing-missing lacks duration_ms
- motion-reveal-viewport-animation-missing-missing lacks easing
- motion-reveal-viewport-animation-missing-ease-in-out lacks duration_ms
- motion-component-state-change-all-important-missing-cubic-bezier-0-0-2-1 lacks duration_ms
- motion-component-state-change-color-missing-cubic-bezier-0-0-2-1 lacks duration_ms
- motion-component-state-change-background-color-missing-cubic-bezier-0-0-2-1 lacks duration_ms
- motion-component-state-change-border-color-missing-cubic-bezier-0-0-2-1 lacks duration_ms
- motion-component-state-change-outline-color-missing-cubic-bezier-0-0-2-1 lacks duration_ms
- motion-component-state-change-text-decoration-color-missing-cubic-bezier-0-0-2-1 lacks duration_ms
- motion-component-state-change-fill-missing-cubic-bezier-0-0-2-1 lacks duration_ms
- motion-component-state-change-stroke-missing-cubic-bezier-0-0-2-1 lacks duration_ms
- motion-component-state-change-tw-gradient-from-missing-cubic-bezier-0-0-2-1 lacks duration_ms
- motion-component-state-change-tw-gradient-via-missing-cubic-bezier-0-0-2-1 lacks duration_ms
- motion-component-state-change-tw-gradient-to-missing-cubic-bezier-0-0-2-1 lacks duration_ms
- motion-component-state-change-opacity-missing-cubic-bezier-0-0-2-1 lacks duration_ms
- motion-component-state-change-box-shadow-missing-cubic-bezier-0-0-2-1 lacks duration_ms
- motion-component-state-change-transform-missing-cubic-bezier-0-0-2-1 lacks duration_ms
- motion-component-state-change-translate-missing-cubic-bezier-0-0-2-1 lacks duration_ms
- motion-component-state-change-scale-missing-cubic-bezier-0-0-2-1 lacks duration_ms
- motion-component-state-change-rotate-missing-cubic-bezier-0-0-2-1 lacks duration_ms
- motion-component-state-change-filter-missing-cubic-bezier-0-0-2-1 lacks duration_ms
- motion-component-state-change-webkit-backdrop-filter-missing-cubic-bezier-0-0-2-1 lacks duration_ms
- motion-component-state-change-backdrop-filter-missing-cubic-bezier-0-0-2-1 lacks duration_ms
- motion-component-state-change-display-missing-cubic-bezier-0-0-2-1 lacks duration_ms
- motion-component-state-change-content-visibility-missing-cubic-bezier-0-0-2-1 lacks duration_ms
- motion-component-state-change-overlay-missing-cubic-bezier-0-0-2-1 lacks duration_ms
- motion-component-state-change-pointer-events-missing-cubic-bezier-0-0-2-1 lacks duration_ms
- motion-component-state-change-background-missing-cubic-bezier-0-0-2-1 lacks duration_ms
- motion-button-state-change-background-150-missing lacks easing
- motion-component-state-change-color-200-missing lacks easing

## Snippet Appendix
### motion-reveal-viewport-animation-5000-linear

```css
.animate-\[border-trail_5s_linear_infinite\] { animation: 5s linear infinite border-trail; }
```

### motion-reveal-viewport-animation-250-ease-out

```css
.animate-\[fade-in_0\.25s_ease-out_0\.075s_forwards\] { animation: .25s ease-out 75ms forwards fade-in; }
```

### motion-reveal-viewport-animation-1250-cubic-bezier-4-04-04-1

```css
.animate-fade-in { animation: fade-in 1.25s cubic-bezier(.4, .04, .04, 1) forwards; }
```

### motion-reveal-viewport-animation-350-cubic-bezier-16-1-3-1

```css
.animate-fade-slide-in { animation: fade-slide-in .35s cubic-bezier(.16, 1, .3, 1) forwards; }
```

### motion-reveal-viewport-animation-500-cubic-bezier-4-04-04-1

```css
.animate-flip-back { animation: flip-back .5s cubic-bezier(.4, .04, .04, 1) forwards; }
```

### motion-reveal-viewport-animation-500-cubic-bezier-4-04-04-1

```css
.animate-flip-front { animation: flip-front .5s cubic-bezier(.4, .04, .04, 1) forwards; }
```

### motion-reveal-viewport-animation-0-cubic-bezier-0-0-2-1

```css
.animate-in { animation: enter initial) cubic-bezier(0, 0, .2, 1) 0s 1 normal none; }
```

### motion-reveal-viewport-animation-1000-cubic-bezier-0-0-2-1

```css
.animate-ping { animation: ping 1s cubic-bezier(0, 0, .2, 1) infinite; }
```

### motion-reveal-viewport-animation-10000-linear

```css
.animate-progress-bar { animation: progress-bar 10s linear infinite; }
```

### motion-reveal-viewport-animation-2000-cubic-bezier-4-0-6-1

```css
.animate-pulse { animation: pulse 2s cubic-bezier(.4, 0, .6, 1) infinite; }
```

### motion-reveal-viewport-animation-500-ease-in-out

```css
.animate-sandbox-left { animation: sandbox-left .5s ease-in-out forwards; }
```

### motion-reveal-viewport-animation-500-ease-in-out

```css
.animate-sandbox-left-reverse { animation: sandbox-left-reverse .5s ease-in-out forwards; }
```

### motion-reveal-viewport-animation-500-ease-in-out

```css
.animate-sandbox-right { animation: sandbox-right .5s ease-in-out forwards; }
```

### motion-reveal-viewport-animation-500-ease-in-out

```css
.animate-sandbox-right-reverse { animation: sandbox-right-reverse .5s ease-in-out forwards; }
```

### motion-reveal-viewport-animation-1250-cubic-bezier-4-04-04-1

```css
.animate-slide-in { animation: slide-in 1.25s cubic-bezier(.4, .04, .04, 1) forwards; }
```

### motion-reveal-viewport-animation-1000-linear

```css
.animate-spin { animation: spin 1s linear infinite; }
```

### motion-component-load-animation-1200-linear

```css
.spinner-module__gyz83a__line { animation: spinner-module__gyz83a__spin 1.2s linear infinite; }
```

### motion-component-state-change-opacity-500-cubic-bezier-4-01-165-99

```css
.fade-up-module__Jo1j7q__fadeUp { transition: opacity .5s cubic-bezier(.4, .01, .165, .99) 0s; }
```

### motion-navigation-state-change-color-90-ease

```css
.navigation-menu-module__AENi4G__trigger { transition-property: color; transition-duration: 90ms; transition-timing-function: ease; }
```

### motion-component-load-animation-1500-ease-in-out

```css
.playground-model-avatar-module__FAaERa__glimmer:after { animation: 1.5s ease-in-out infinite reverse playground-model-avatar-module__FAaERa__glimmer; }
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
