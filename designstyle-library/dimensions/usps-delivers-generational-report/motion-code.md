# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| component | state-change | opacity | 150ms | 0ms | linear | 组件state-change：opacity，150ms linear，state-change 触发 |
| component | load | animation | 1000ms | 0ms | ease-in-out | 组件load：animation scale(1) -> scale(var(--fa-beat-scale,1.25))，1000ms ease-in-out，load 触发 |
| navigation | state-change | all | 250ms | 100ms | ease | 导航state-change：all，250ms ease，state-change 触发 |
| button | hover | opacity | 150ms | 0ms | linear | 按钮hover：opacity missing -> 0.800296，150ms linear，hover 触发；样本 Menu |
| button | focus | opacity | 150ms | 0ms | linear | 按钮focus：opacity missing -> 0.765496，150ms linear，focus 触发；样本 Menu |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: assets/2026-06-11-usps-delivers-generational-report-motion.json

## Missing Evidence
- motion-component-state-change-all-50-missing lacks easing
- motion-component-state-change-all-50-missing lacks easing
- motion-component-state-change-all-missing-missing lacks duration_ms
- motion-component-state-change-all-missing-missing lacks easing
- motion-component-state-change-all-missing-missing lacks duration_ms
- motion-component-state-change-all-missing-missing lacks easing
- motion-reveal-viewport-all-missing-missing lacks duration_ms
- motion-reveal-viewport-all-missing-missing lacks easing
- motion-reveal-viewport-all-missing-missing lacks duration_ms
- motion-reveal-viewport-all-missing-missing lacks easing
- motion-component-state-change-all-100-missing lacks easing
- motion-component-state-change-all-100-missing lacks easing
- motion-component-state-change-all-missing-missing lacks duration_ms
- motion-component-state-change-all-missing-missing lacks easing
- motion-component-state-change-all-missing-missing lacks duration_ms
- motion-component-state-change-all-missing-missing lacks easing
- motion-reveal-viewport-all-missing-missing lacks duration_ms
- motion-reveal-viewport-all-missing-missing lacks easing
- motion-reveal-viewport-all-missing-missing lacks duration_ms
- motion-reveal-viewport-all-missing-missing lacks easing
- motion-component-state-change-all-150-missing lacks easing
- motion-component-state-change-all-150-missing lacks easing
- motion-component-state-change-all-missing-missing lacks duration_ms
- motion-component-state-change-all-missing-missing lacks easing
- motion-component-state-change-all-missing-missing lacks duration_ms
- motion-component-state-change-all-missing-missing lacks easing
- motion-reveal-viewport-all-missing-missing lacks duration_ms
- motion-reveal-viewport-all-missing-missing lacks easing
- motion-reveal-viewport-all-missing-missing lacks duration_ms
- motion-reveal-viewport-all-missing-missing lacks easing
- motion-component-state-change-all-200-missing lacks easing
- motion-component-state-change-all-200-missing lacks easing
- motion-component-state-change-all-missing-missing lacks duration_ms
- motion-component-state-change-all-missing-missing lacks easing
- motion-component-state-change-all-missing-missing lacks duration_ms
- motion-component-state-change-all-missing-missing lacks easing
- motion-reveal-viewport-all-missing-missing lacks duration_ms
- motion-reveal-viewport-all-missing-missing lacks easing
- motion-reveal-viewport-all-missing-missing lacks duration_ms
- motion-reveal-viewport-all-missing-missing lacks easing
- motion-component-state-change-all-250-missing lacks easing
- motion-component-state-change-all-250-missing lacks easing
- motion-component-state-change-all-missing-missing lacks duration_ms
- motion-component-state-change-all-missing-missing lacks easing
- motion-component-state-change-all-missing-missing lacks duration_ms
- motion-component-state-change-all-missing-missing lacks easing
- motion-reveal-viewport-all-missing-missing lacks duration_ms
- motion-reveal-viewport-all-missing-missing lacks easing
- motion-reveal-viewport-all-missing-missing lacks duration_ms
- motion-reveal-viewport-all-missing-missing lacks easing
- motion-component-state-change-all-300-missing lacks easing
- motion-component-state-change-all-300-missing lacks easing
- motion-component-state-change-all-missing-missing lacks duration_ms
- motion-component-state-change-all-missing-missing lacks easing
- motion-component-state-change-all-missing-missing lacks duration_ms
- motion-component-state-change-all-missing-missing lacks easing
- motion-reveal-viewport-all-missing-missing lacks duration_ms
- motion-reveal-viewport-all-missing-missing lacks easing
- motion-reveal-viewport-all-missing-missing lacks duration_ms
- motion-reveal-viewport-all-missing-missing lacks easing
- motion-component-state-change-all-350-missing lacks easing
- motion-component-state-change-all-350-missing lacks easing
- motion-component-state-change-all-missing-missing lacks duration_ms
- motion-component-state-change-all-missing-missing lacks easing
- motion-component-state-change-all-missing-missing lacks duration_ms
- motion-component-state-change-all-missing-missing lacks easing
- motion-reveal-viewport-all-missing-missing lacks duration_ms
- motion-reveal-viewport-all-missing-missing lacks easing
- motion-reveal-viewport-all-missing-missing lacks duration_ms
- motion-reveal-viewport-all-missing-missing lacks easing
- motion-component-state-change-all-400-missing lacks easing
- motion-component-state-change-all-400-missing lacks easing
- motion-component-state-change-all-missing-missing lacks duration_ms
- motion-component-state-change-all-missing-missing lacks easing
- motion-component-state-change-all-missing-missing lacks duration_ms
- motion-component-state-change-all-missing-missing lacks easing
- motion-reveal-viewport-all-missing-missing lacks duration_ms
- motion-reveal-viewport-all-missing-missing lacks easing
- motion-reveal-viewport-all-missing-missing lacks duration_ms
- motion-reveal-viewport-all-missing-missing lacks easing

## Snippet Appendix
### motion-component-state-change-opacity-150-linear

```css
link https://github.com/jonsuh/hamburgers
 */.hamburger { transition-property: opacity; transition-duration: .15s; transition-timing-function: linear; }
```

### motion-component-load-animation-1000-ease-in-out

```css
.fa-beat { animation: fa-beat 1s ease-in-out 0s; }
```

### motion-navigation-state-change-all-250-ease

```css
#menuModal { transition-property: all; transition-duration: .25s; transition-timing-function: ease; }
```

### motion-button-hover-opacity-150-linear

```css
{"backgroundColor": "rgb(255, 255, 255)", "border": "0px none rgb(0, 0, 0)", "borderBottom": "0px none rgb(0, 0, 0)", "borderLeft": "0px none rgb(0, 0, 0)", "borderRight": "0px none rgb(0, 0, 0)", "borderTop": "0px none rgb(0, 0, 0)", "color": "rgb(0, 0, 0)", "opacity": "0.800296"}
```

### motion-button-focus-opacity-150-linear

```css
{"backgroundColor": "rgb(255, 255, 255)", "border": "2px solid rgb(0, 0, 255)", "borderBottom": "2px solid rgb(0, 0, 255)", "borderLeft": "2px solid rgb(0, 0, 255)", "borderRight": "2px solid rgb(0, 0, 255)", "borderTop": "2px solid rgb(0, 0, 255)", "color": "rgb(0, 0, 0)", "opacity": "0.765496"}
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
