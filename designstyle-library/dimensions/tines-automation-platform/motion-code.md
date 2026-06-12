# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| component | load | animation | 2000ms | 0ms | linear | 组件load：animation rotate(1turn) -> rotate(1turn)，2000ms linear，load 触发 |
| component | load | animation | 1450ms | 0ms | ease-in-out | 组件load：animation，1450ms ease-in-out，load 触发 |
| component | state-change | transform | 250ms | 0ms | ease | 组件state-change：transform missing -> translateY(0)，250ms ease，state-change 触发 |
| component | state-change | opacity | 250ms | 0ms | ease | 组件state-change：opacity missing -> translateY(0)，250ms ease，state-change 触发 |
| component | state-change | transform | 250ms | 0ms | ease | 组件state-change：transform missing -> translateY(0)，250ms ease，state-change 触发 |
| component | state-change | opacity | 250ms | 0ms | ease | 组件state-change：opacity missing -> translateY(0)，250ms ease，state-change 触发 |
| component | state-change | transform | 600ms | 0ms | cubic-bezier(.075,.82,.165,1) | 组件state-change：transform，600ms cubic-bezier(.075,.82,.165,1)，state-change 触发 |
| component | state-change | transform | 167ms | 0ms | cubic-bezier(.33,0,0,1) | 组件state-change：transform，167ms cubic-bezier(.33,0,0,1)，state-change 触发 |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: assets/2026-06-12-tines-automation-platform-motion.json

## Missing Evidence
- motion-component-state-change-opacity-750-missing lacks easing
- motion-component-load-animation-100-missing lacks easing
- motion-component-state-change-opacity-100-missing lacks easing
- motion-component-hover-all-75-missing lacks easing
- motion-component-load-animation-300-missing lacks easing
- motion-component-load-animation-3000-missing lacks easing
- motion-component-state-change-var-s1c3jptw-8-missing-missing lacks duration_ms
- motion-component-state-change-var-s1c3jptw-8-missing-missing lacks easing
- motion-reveal-viewport-animation-500-missing lacks easing
- motion-component-state-change-all-100-missing lacks easing
- motion-button-state-change-all-100-missing lacks easing
- motion-component-state-change-all-100-missing lacks easing
- motion-component-state-change-all-100-missing lacks easing
- motion-component-state-change-all-100-missing lacks easing
- motion-component-state-change-opacity-100-missing lacks easing
- motion-component-state-change-opacity-100-missing lacks easing
- motion-component-state-change-opacity-100-missing lacks easing
- motion-component-state-change-top-250-missing lacks easing
- motion-component-state-change-all-50-missing lacks easing
- motion-component-state-change-all-100-missing lacks easing
- motion-component-state-change-all-50-missing lacks easing
- motion-component-state-change-all-100-missing lacks easing
- motion-component-state-change-all-0-missing lacks easing
- motion-component-state-change-opacity-100-missing lacks easing
- motion-component-state-change-background-color-100-missing lacks easing
- motion-component-state-change-all-100-missing lacks easing
- motion-component-state-change-all-100-missing lacks easing
- motion-component-state-change-all-100-missing lacks easing
- motion-component-state-change-all-50-missing lacks easing
- motion-navigation-state-change-transform-100-missing lacks easing
- motion-component-state-change-transform-100-missing lacks easing
- motion-component-state-change-opacity-200-missing lacks easing
- motion-component-state-change-transform-0-missing lacks easing
- motion-component-state-change-opacity-500-missing lacks easing
- motion-component-state-change-transform-0-missing lacks easing
- motion-component-state-change-all-100-missing lacks easing
- motion-component-state-change-all-100-missing lacks easing
- motion-component-state-change-top-250-missing lacks easing
- motion-component-state-change-max-height-250-missing lacks easing
- motion-component-state-change-transform-100-missing lacks easing
- motion-component-state-change-transform-100-missing lacks easing

## Snippet Appendix
### motion-component-load-animation-2000-linear

```css
.lvhzxbp { animation: LoadingIndicatorSpin-lvhzxbp 2s linear infinite; }
```

### motion-component-load-animation-1450-ease-in-out

```css
.lvhzxbp circle { animation: LoadingIndicatorRingStretch-lvhzxbp 1.45s ease-in-out infinite; }
```

### motion-component-state-change-transform-250-ease

```css
html[data-has-intercom-banner]:after { transition: transform .25s ease 0s; }
```

### motion-component-state-change-opacity-250-ease

```css
html[data-has-intercom-banner]:after { transition: opacity .25s ease 0s; }
```

### motion-component-state-change-transform-250-ease

```css
html[data-has-intercom-banner]:before { transition: transform .25s ease 0s; }
```

### motion-component-state-change-opacity-250-ease

```css
html[data-has-intercom-banner]:before { transition: opacity .25s ease 0s; }
```

### motion-component-state-change-transform-600-cubic-bezier-075-82-165-1

```css
.s1xyphoy { transition: transform .6s cubic-bezier(.075,.82,.165,1); }
```

### motion-component-state-change-transform-167-cubic-bezier-33-0-0-1

```css
.i18lchxu { transition: transform 167ms cubic-bezier(.33,0,0,1); }
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
