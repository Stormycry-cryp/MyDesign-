# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| button | hover | backgroundColor | 200ms | 0ms | ease | 按钮hover：backgroundColor rgba(0, 0, 0, 0) -> rgba(0, 0, 0, 0.875)，200ms ease，hover 触发；样本 ds-button-1 |
| button | focus | backgroundColor | 200ms | 0ms | ease | 按钮focus：backgroundColor rgba(0, 0, 0, 0) -> rgba(0, 0, 0, 0.92)，200ms ease，focus 触发；样本 ds-button-1 |
| button | hover | transform | 200ms | 0ms | ease | 按钮hover：transform matrix(-1, 0, 0, 1, 0, 0) -> matrix(-1.08024, 0, 0, 1.08024, 0, 0)，200ms ease，hover 触发；样本 ds-button-8 |
| button | focus | transform | 200ms | 0ms | ease | 按钮focus：transform matrix(-1, 0, 0, 1, 0, 0) -> matrix(-1.08715, 0, 0, 1.08715, 0, 0)，200ms ease，focus 触发；样本 ds-button-8 |
| button | hover | transform | 200ms | 0ms | ease | 按钮hover：transform none -> matrix(1.02206, 0, 0, 1.02206, 0, 0)，200ms ease，hover 触发；样本 ds-button-9 |
| button | focus | transform | 200ms | 0ms | ease | 按钮focus：transform none -> matrix(1.02206, 0, 0, 1.02206, 0, 0)，200ms ease，focus 触发；样本 ds-button-9 |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: missing

## Missing Evidence
- None recorded.

## Snippet Appendix
### motion-button-hover-backgroundcolor-200-ease

```css
{"backgroundColor": "rgba(0, 0, 0, 0.875)", "transition": "background-color 0.2s"}
```

### motion-button-focus-backgroundcolor-200-ease

```css
{"backgroundColor": "rgba(0, 0, 0, 0.92)", "transition": "background-color 0.2s"}
```

### motion-button-hover-transform-200-ease

```css
{"transform": "matrix(-1.08024, 0, 0, 1.08024, 0, 0)", "transition": "transform 0.2s"}
```

### motion-button-focus-transform-200-ease

```css
{"transform": "matrix(-1.08715, 0, 0, 1.08715, 0, 0)", "transition": "transform 0.2s"}
```

### motion-button-hover-transform-200-ease

```css
{"transform": "matrix(1.02206, 0, 0, 1.02206, 0, 0)", "transition": "transform 0.2s"}
```

### motion-button-focus-transform-200-ease

```css
{"transform": "matrix(1.02206, 0, 0, 1.02206, 0, 0)", "transition": "transform 0.2s"}
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
