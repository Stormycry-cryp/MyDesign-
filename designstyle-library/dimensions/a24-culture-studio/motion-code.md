# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| navigation | state-change | backgroundColor | 150ms | 0ms | linear | 导航state-change：backgroundColor rgba(0, 0, 0, 0) -> missing，150ms linear，state-change 触发；样本 ds-navigation-0 |
| navigation | state-change | color | 100ms | 0ms | linear | 导航state-change：color rgb(0, 0, 0) -> missing，100ms linear，state-change 触发；样本 ds-navigation-1 |
| button | state-change | opacity | 150ms | 0ms | linear | 按钮state-change：opacity 1 -> missing，150ms linear，state-change 触发；样本 ds-button-1 |
| button | state-change | opacity | 100ms | 0ms | ease-out | 按钮state-change：opacity 0 -> missing，100ms ease-out，state-change 触发；样本 ds-button-2 |
| button | state-change | transform | 200ms | 0ms | ease-in-out | 按钮state-change：transform none -> missing，200ms ease-in-out，state-change 触发；样本 ds-button-4 |
| card | state-change | opacity | 200ms | 0ms | ease-in-out | 卡片state-change：opacity 1 -> missing，200ms ease-in-out，state-change 触发；样本 Backrooms 2026 |
| card | state-change | opacity | 200ms | 0ms | ease-in-out | 卡片state-change：opacity 1 -> missing，200ms ease-in-out，state-change 触发；样本 The Death of Robin Hood 2026 |
| card | state-change | opacity | 200ms | 0ms | ease-in-out | 卡片state-change：opacity 1 -> missing，200ms ease-in-out，state-change 触发；样本 The Invite 2026 |
| card | state-change | opacity | 200ms | 0ms | ease-in-out | 卡片state-change：opacity 1 -> missing，200ms ease-in-out，state-change 触发；样本 Tony 2026 |
| card | state-change | opacity | 200ms | 0ms | ease-in-out | 卡片state-change：opacity 1 -> missing，200ms ease-in-out，state-change 触发；样本 Onslaught 2026 |
| card | state-change | opacity | 200ms | 0ms | ease-in-out | 卡片state-change：opacity 1 -> missing，200ms ease-in-out，state-change 触发；样本 Primetime 2026 |
| form | state-change | transform | 75ms | 0ms | ease-in | 表单state-change：transform matrix(0.7, 0, 0, 0.7, 0, -26.95) -> missing，75ms ease-in，state-change 触发；样本 EMAIL |
| form | state-change | transform | 75ms | 0ms | ease-in | 表单state-change：transform matrix(0.7, 0, 0, 0.7, 0, -23.8) -> missing，75ms ease-in，state-change 触发；样本 EMAIL |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: missing

## Missing Evidence
- None recorded.

## Snippet Appendix
### motion-navigation-state-change-backgroundcolor-150-linear

```css
{"transition": "background-color 0.15s linear, transform 0.2s ease-in-out, -webkit-transform 0.2s ease-in-out"}
```

### motion-navigation-state-change-color-100-linear

```css
{"transition": "color 0.1s linear"}
```

### motion-button-state-change-opacity-150-linear

```css
{"transition": "opacity 0.15s linear"}
```

### motion-button-state-change-opacity-100-ease-out

```css
{"transition": "opacity 0.1s ease-out 0.35s"}
```

### motion-button-state-change-transform-200-ease-in-out

```css
{"transition": "width 0.25s cubic-bezier(0, 1, 0.25, 1), transform 0.2s ease-in-out, -webkit-transform 0.2s ease-in-out"}
```

### motion-card-state-change-opacity-200-ease-in-out

```css
{"transition": "opacity 0.2s ease-in-out"}
```

### motion-card-state-change-opacity-200-ease-in-out

```css
{"transition": "opacity 0.2s ease-in-out"}
```

### motion-card-state-change-opacity-200-ease-in-out

```css
{"transition": "opacity 0.2s ease-in-out"}
```

### motion-card-state-change-opacity-200-ease-in-out

```css
{"transition": "opacity 0.2s ease-in-out"}
```

### motion-card-state-change-opacity-200-ease-in-out

```css
{"transition": "opacity 0.2s ease-in-out"}
```

### motion-card-state-change-opacity-200-ease-in-out

```css
{"transition": "opacity 0.2s ease-in-out"}
```

### motion-form-state-change-transform-75-ease-in

```css
{"transition": "transform 0.075s ease-in, -webkit-transform 0.075s ease-in"}
```

### motion-form-state-change-transform-75-ease-in

```css
{"transition": "transform 0.075s ease-in, -webkit-transform 0.075s ease-in"}
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
