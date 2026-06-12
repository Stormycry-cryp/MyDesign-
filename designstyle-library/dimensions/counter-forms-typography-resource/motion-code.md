# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| component | state-change | opacity | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：opacity，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | all | 100ms | 0ms | ease | 组件state-change：all，100ms ease，state-change 触发 |
| button | hover | color | 0ms | 0ms | ease | 按钮hover：color missing -> rgb(255, 101, 0)，0ms ease，hover 触发；样本 BULLETIN |
| button | focus | color | 0ms | 0ms | ease | 按钮focus：color missing -> rgb(255, 101, 0)，0ms ease，focus 触发；样本 BULLETIN |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: assets/2026-06-12-counter-forms-typography-resource-motion.json

## Missing Evidence
- None recorded.

## Snippet Appendix
### motion-component-state-change-opacity-150-cubic-bezier-4-0-2-1

```css
.transition-opacity { transition-property: opacity; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-all-100-ease

```css
.hand { transition: all .1s ease; }
```

### motion-button-hover-color-0-ease

```css
{"color": "rgb(255, 101, 0)"}
```

### motion-button-focus-color-0-ease

```css
{"color": "rgb(255, 101, 0)"}
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
