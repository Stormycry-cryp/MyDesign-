# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| navigation | state-change | transform | 1000ms | 0ms | linear | 导航state-change：transform none -> missing，1000ms linear，state-change 触发；样本 MENU MODELS OWNERSHIP DEALERSHIPS BEYOND COMPANY MOTORSPORT MUSEUM STORE NEWS De |
| navigation | state-change | height | 300ms | 0ms | ease-out | 导航state-change：height missing -> missing，300ms ease-out，state-change 触发；样本 MENU |
| button | state-change | opacity | 300ms | 0ms | ease-out | 按钮state-change：opacity 1 -> missing，300ms ease-out，state-change 触发；样本 Allow animations |
| card | state-change | height | 300ms | 0ms | ease-out | 卡片state-change：height missing -> missing，300ms ease-out，state-change 触发；样本 MENU |
| card | state-change | opacity | 300ms | 0ms | ease-in-out | 卡片state-change：opacity 1 -> missing，300ms ease-in-out，state-change 触发；样本 YOU CAN'T HIDE WHO YOU ARE |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: missing

## Missing Evidence
- None recorded.

## Snippet Appendix
### motion-navigation-state-change-transform-1000-linear

```css
{"transition": "transform 1s linear"}
```

### motion-navigation-state-change-height-300-ease-out

```css
{"transition": "height 0.3s ease-out, padding 0.3s ease-out"}
```

### motion-button-state-change-opacity-300-ease-out

```css
{"transition": "opacity 0.3s ease-out"}
```

### motion-card-state-change-height-300-ease-out

```css
{"transition": "height 0.3s ease-out, padding 0.3s ease-out"}
```

### motion-card-state-change-opacity-300-ease-in-out

```css
{"transition": "opacity 0.3s ease-in-out"}
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
