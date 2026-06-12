# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| component | load | animation | 250ms | 0ms | ease-in-out | 组件load：animation scale(1) -> scale(1)，250ms ease-in-out，load 触发 |
| component | state-change | transform | 200ms | 0ms | ease-out | 组件state-change：transform，200ms ease-out，state-change 触发 |
| component | state-change | transform | 200ms | 0ms | ease-in | 组件state-change：transform，200ms ease-in，state-change 触发 |
| component | load | animation | 1000ms | 0ms | linear | 组件load：animation rotate(0) -> rotate(360deg)，1000ms linear，load 触发 |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: assets/2026-06-12-teenage-engineering-hardware-brand-motion.json

## Missing Evidence
- motion-component-state-change-box-shadow-200-missing lacks easing
- motion-component-state-change-transform-250-missing lacks easing
- motion-component-state-change-opacity-150-missing lacks easing

## Snippet Appendix
### motion-component-load-animation-250-ease-in-out

```css
.bag-animation { animation: .25s ease-in-out alternate bulge; }
```

### motion-component-state-change-transform-200-ease-out

```css
._message_1yt6t_1 { transition: transform .2s ease-out; }
```

### motion-component-state-change-transform-200-ease-in

```css
._message_1yt6t_1[data-state=entering] { transition: transform .2s ease-in; }
```

### motion-component-load-animation-1000-linear

```css
._spinner_hiku9_11:after { animation: 1s linear infinite _load_hiku9_1; }
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
