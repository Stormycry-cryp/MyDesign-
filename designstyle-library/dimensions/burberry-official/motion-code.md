# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| navigation | hover | transform | 280ms | 0ms | ease-in-out | 导航hover：transform matrix(1, 0, 0, 1, 0, -6.89156) -> matrix(1, 0, 0, 1, 0, 0)，280ms ease-in-out，hover 触发；样本 Skip to Main Content Skip to Footer Women Men Children Gifts Trench Scarves Bags |
| navigation | focus | transform | 280ms | 0ms | ease-in-out | 导航focus：transform matrix(1, 0, 0, 1, 0, -6.89156) -> matrix(1, 0, 0, 1, 0, 0)，280ms ease-in-out，focus 触发；样本 Skip to Main Content Skip to Footer Women Men Children Gifts Trench Scarves Bags |
| navigation | hover | color | 280ms | 0ms | cubic-bezier(0.4, 0, 0.6, 1) | 导航hover：color rgb(0, 0, 0) -> rgb(0, 0, 16)，280ms cubic-bezier(0.4, 0, 0.6, 1)，hover 触发；样本 ds-navigation-3 |
| navigation | focus | color | 280ms | 0ms | cubic-bezier(0.4, 0, 0.6, 1) | 导航focus：color rgb(0, 0, 0) -> rgb(0, 0, 16)，280ms cubic-bezier(0.4, 0, 0.6, 1)，focus 触发；样本 ds-navigation-3 |
| form | state-change | transform | 200ms | 0ms | ease-out | 表单state-change：transform matrix(1, 0, 0, 1, 0, 32) -> missing，200ms ease-out，state-change 触发；样本 Email |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: missing

## Missing Evidence
- None recorded.

## Snippet Appendix
### motion-navigation-hover-transform-280-ease-in-out

```css
{"transform": "matrix(1, 0, 0, 1, 0, 0)", "transition": "transform 0.28s ease-in-out, color 0.28s ease-in-out"}
```

### motion-navigation-focus-transform-280-ease-in-out

```css
{"transform": "matrix(1, 0, 0, 1, 0, 0)", "transition": "transform 0.28s ease-in-out, color 0.28s ease-in-out"}
```

### motion-navigation-hover-color-280-cubic-bezier-0-4-0-0-6-1

```css
{"color": "rgb(0, 0, 16)", "transition": "color 0.28s cubic-bezier(0.4, 0, 0.6, 1)"}
```

### motion-navigation-focus-color-280-cubic-bezier-0-4-0-0-6-1

```css
{"color": "rgb(0, 0, 16)", "transition": "color 0.28s cubic-bezier(0.4, 0, 0.6, 1)"}
```

### motion-form-state-change-transform-200-ease-out

```css
{"transition": "transform 0.2s ease-out"}
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
