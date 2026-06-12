# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| component | load | animation | 800ms | 0ms | linear | 组件load：animation rotate(0) -> rotate(360deg)，800ms linear，load 触发 |
| button | hover | transform | 100ms | 0ms | ease-in-out, ease-in-out, ease-in-out, ease-in-out | 按钮hover：transform missing -> matrix(1.05, 0, 0, 1.05, 0, 0)，100ms ease-in-out, ease-in-out, ease-in-out, ease-in-out，hover 触发；样本 Talk to an engineer |
| button | focus | transform | 100ms | 0ms | ease-in-out, ease-in-out, ease-in-out, ease-in-out | 按钮focus：transform missing -> matrix(1.05, 0, 0, 1.05, 0, 0)，100ms ease-in-out, ease-in-out, ease-in-out, ease-in-out，focus 触发；样本 Talk to an engineer |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: assets/2026-06-11-mezmo-observability-saas-motion.json

## Missing Evidence
- motion-component-state-change-unset-missing-missing lacks duration_ms
- motion-component-state-change-unset-missing-missing lacks easing
- motion-component-state-change-unset-missing-missing lacks duration_ms
- motion-component-state-change-unset-missing-missing lacks easing
- motion-component-state-change-background-color-100-missing lacks easing
- motion-component-state-change-color-100-missing lacks easing
- motion-component-state-change-all-300-missing lacks easing
- motion-button-state-change-transform-200-missing lacks easing
- motion-button-state-change-border-color-200-missing lacks easing
- motion-button-state-change-background-color-200-missing lacks easing
- motion-button-state-change-transform-200-missing lacks easing
- motion-button-state-change-border-color-200-missing lacks easing
- motion-button-state-change-background-color-200-missing lacks easing
- motion-button-state-change-transform-200-missing lacks easing
- motion-navigation-state-change-all-200-missing lacks easing
- motion-navigation-state-change-all-200-missing lacks easing
- motion-component-state-change-background-color-350-missing lacks easing
- motion-component-state-change-color-200-missing lacks easing
- motion-component-state-change-background-color-200-missing lacks easing
- motion-component-state-change-box-shadow-200-missing lacks easing
- motion-navigation-state-change-color-200-missing lacks easing
- motion-navigation-state-change-background-color-200-missing lacks easing
- motion-navigation-state-change-box-shadow-200-missing lacks easing
- motion-navigation-state-change-color-200-missing lacks easing
- motion-navigation-state-change-background-color-200-missing lacks easing
- motion-navigation-state-change-box-shadow-200-missing lacks easing
- motion-button-state-change-transform-200-missing lacks easing
- motion-button-state-change-border-color-250-missing lacks easing
- motion-button-state-change-background-color-250-missing lacks easing
- motion-button-state-change-opacity-250-missing lacks easing
- motion-button-state-change-border-color-250-missing lacks easing
- motion-button-state-change-background-color-250-missing lacks easing
- motion-button-state-change-all-250-missing lacks easing
- motion-button-state-change-all-250-missing lacks easing
- motion-button-state-change-opacity-250-missing lacks easing
- motion-button-state-change-border-color-250-missing lacks easing
- motion-button-state-change-background-color-250-missing lacks easing
- motion-button-state-change-opacity-250-missing lacks easing
- motion-button-state-change-border-color-250-missing lacks easing
- motion-button-state-change-background-color-250-missing lacks easing
- motion-button-state-change-all-250-missing lacks easing
- motion-button-state-change-all-250-missing lacks easing
- motion-component-state-change-all-200-missing lacks easing
- motion-component-state-change-box-shadow-200-missing lacks easing
- motion-component-state-change-transform-200-missing lacks easing
- motion-component-state-change-box-shadow-200-missing lacks easing
- motion-component-state-change-filter-200-missing lacks easing
- motion-component-state-change-all-200-missing lacks easing
- motion-component-state-change-box-shadow-500-missing lacks easing

## Snippet Appendix
### motion-component-load-animation-800-linear

```css
.w-lightbox-spinner { animation: .8s linear infinite spin; }
```

### motion-button-hover-transform-100-ease-in-out-ease-in-out-ease-in-out-ease-in-out

```css
{"boxShadow": "rgba(0, 0, 0, 0.2) 0px 2px 5px 0px", "transform": "matrix(1.05, 0, 0, 1.05, 0, 0)"}
```

### motion-button-focus-transform-100-ease-in-out-ease-in-out-ease-in-out-ease-in-out

```css
{"boxShadow": "rgba(0, 0, 0, 0.2) 0px 2px 5px 0px", "transform": "matrix(1.05, 0, 0, 1.05, 0, 0)"}
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
