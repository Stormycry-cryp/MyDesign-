# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| component | state-change | opacity | 0ms | 0ms | ease | 组件state-change：opacity，0ms ease，state-change 触发 |
| component | state-change | opacity | 0ms | 0ms | ease | 组件state-change：opacity，0ms ease，state-change 触发 |
| component | state-change | filter | 150ms | 0ms | ease | 组件state-change：filter，150ms ease，state-change 触发 |
| component | state-change | opacity | 100ms | 0ms | ease | 组件state-change：opacity，100ms ease，state-change 触发 |
| component | state-change | transform | 450ms | 0ms | cubic-bezier(.77,0,.175,1) | 组件state-change：transform，450ms cubic-bezier(.77,0,.175,1)，state-change 触发 |
| component | state-change | opacity | 80ms | 0ms | ease | 组件state-change：opacity，80ms ease，state-change 触发 |
| component | state-change | opacity | 80ms | 0ms | ease | 组件state-change：opacity，80ms ease，state-change 触发 |
| component | state-change | opacity | 80ms | 0ms | ease | 组件state-change：opacity，80ms ease，state-change 触发 |
| navigation | state-change | transform | 450ms | 0ms | cubic-bezier(.77,0,.175,1) | 导航state-change：transform，450ms cubic-bezier(.77,0,.175,1)，state-change 触发 |
| navigation | state-change | transform | 450ms | 0ms | cubic-bezier(.77,0,.175,1) | 导航state-change：transform missing -> rotate(-90deg) translate3d(-100%,0,0)，450ms cubic-bezier(.77,0,.175,1)，state-change 触发 |
| navigation | state-change | transform | 450ms | 0ms | cubic-bezier(.77,0,.175,1) | 导航state-change：transform missing -> translate3d(-100%,0,0)，450ms cubic-bezier(.77,0,.175,1)，state-change 触发 |
| navigation | state-change | opacity | 150ms | 0ms | ease | 导航state-change：opacity，150ms ease，state-change 触发 |
| component | state-change | opacity | 150ms | 0ms | ease | 组件state-change：opacity，150ms ease，state-change 触发 |
| overlay | state-change | transform | 450ms | 0ms | cubic-bezier(.77,0,.175,1) | 浮层state-change：transform missing -> translate3d(100%,0,0)，450ms cubic-bezier(.77,0,.175,1)，state-change 触发 |
| component | state-change | transform | 450ms | 0ms | cubic-bezier(.77,0,.175,1) | 组件state-change：transform，450ms cubic-bezier(.77,0,.175,1)，state-change 触发 |
| button | hover | backgroundColor | 450ms | 0ms | cubic-bezier(0.77, 0, 0.175, 1) | 按钮hover：backgroundColor missing -> rgb(0, 0, 0)，450ms cubic-bezier(0.77, 0, 0.175, 1)，hover 触发；样本 ds-button-1 |
| button | focus | backgroundColor | 450ms | 0ms | cubic-bezier(0.77, 0, 0.175, 1) | 按钮focus：backgroundColor missing -> rgb(0, 0, 0)，450ms cubic-bezier(0.77, 0, 0.175, 1)，focus 触发；样本 ds-button-1 |
| button | hover | backgroundColor | 0ms | 0ms | ease | 按钮hover：backgroundColor missing -> rgb(0, 0, 0)，0ms ease，hover 触发；样本 REFERENCES |
| button | focus | backgroundColor | 0ms | 0ms | ease | 按钮focus：backgroundColor missing -> rgb(0, 0, 0)，0ms ease，focus 触发；样本 REFERENCES |
| button | hover | backgroundColor | 0ms | 0ms | ease | 按钮hover：backgroundColor missing -> rgb(0, 0, 0)，0ms ease，hover 触发；样本 DEVELOPMENT |
| button | focus | backgroundColor | 0ms | 0ms | ease | 按钮focus：backgroundColor missing -> rgb(0, 0, 0)，0ms ease，focus 触发；样本 DEVELOPMENT |
| button | hover | backgroundColor | 0ms | 0ms | ease | 按钮hover：backgroundColor missing -> rgb(0, 0, 0)，0ms ease，hover 触发；样本 STRATEGY |
| button | focus | backgroundColor | 0ms | 0ms | ease | 按钮focus：backgroundColor missing -> rgb(0, 0, 0)，0ms ease，focus 触发；样本 STRATEGY |
| button | hover | backgroundColor | 0ms | 0ms | ease | 按钮hover：backgroundColor missing -> rgb(0, 0, 0)，0ms ease，hover 触发；样本 ADVICE |
| button | focus | backgroundColor | 0ms | 0ms | ease | 按钮focus：backgroundColor missing -> rgb(0, 0, 0)，0ms ease，focus 触发；样本 ADVICE |
| button | hover | backgroundColor | 0ms | 0ms | ease | 按钮hover：backgroundColor missing -> rgb(0, 0, 0)，0ms ease，hover 触发；样本 MANAGEMENT |
| button | focus | backgroundColor | 0ms | 0ms | ease | 按钮focus：backgroundColor missing -> rgb(0, 0, 0)，0ms ease，focus 触发；样本 MANAGEMENT |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: assets/2026-06-12-developments-media-production-motion.json

## Missing Evidence
- None recorded.

## Snippet Appendix
### motion-component-state-change-opacity-0-ease

```css
.lazy { transition: opacity 0ms ease; }
```

### motion-component-state-change-opacity-0-ease

```css
.lazy.no-fade { transition: opacity 0ms ease; }
```

### motion-component-state-change-filter-150-ease

```css
.lazy-blur { transition: filter .15s ease; }
```

### motion-component-state-change-opacity-100-ease

```css
.responsive-image.with-placeholder .placeholder { transition: opacity .1s ease; }
```

### motion-component-state-change-transform-450-cubic-bezier-77-0-175-1

```css
#container { transition: transform .45s cubic-bezier(.77,0,.175,1); }
```

### motion-component-state-change-opacity-80-ease

```css
#excerpts--list { transition: opacity 80ms ease; }
```

### motion-component-state-change-opacity-80-ease

```css
#interview--content { transition: opacity 80ms ease; }
```

### motion-component-state-change-opacity-80-ease

```css
#interviews { transition: opacity 80ms ease; }
```

### motion-navigation-state-change-transform-450-cubic-bezier-77-0-175-1

```css
#menu-toggle { transition: transform .45s cubic-bezier(.77,0,.175,1); }
```

### motion-navigation-state-change-transform-450-cubic-bezier-77-0-175-1

```css
#menu-toggle-tooltip { transition: transform .45s cubic-bezier(.77,0,.175,1); }
```

### motion-navigation-state-change-transform-450-cubic-bezier-77-0-175-1

```css
#menu { transition: transform .45s cubic-bezier(.77,0,.175,1); }
```

### motion-navigation-state-change-opacity-150-ease

```css
#menu-overlay { transition: opacity .15s ease; }
```

### motion-component-state-change-opacity-150-ease

```css
[g-component=Interview] [g-ref=overlay] { transition: opacity .15s ease; }
```

### motion-overlay-state-change-transform-450-cubic-bezier-77-0-175-1

```css
[g-component=Interview] [g-ref=drawer] { transition: transform .45s cubic-bezier(.77,0,.175,1); }
```

### motion-component-state-change-transform-450-cubic-bezier-77-0-175-1

```css
.block--question__topics { transition: transform .45s cubic-bezier(.77,0,.175,1); }
```

### motion-button-hover-backgroundcolor-450-cubic-bezier-0-77-0-0-175-1

```css
{"backgroundColor": "rgb(0, 0, 0)", "color": "rgb(255, 255, 255)"}
```

### motion-button-focus-backgroundcolor-450-cubic-bezier-0-77-0-0-175-1

```css
{"backgroundColor": "rgb(0, 0, 0)", "color": "rgb(255, 255, 255)"}
```

### motion-button-hover-backgroundcolor-0-ease

```css
{"backgroundColor": "rgb(0, 0, 0)", "color": "rgb(255, 255, 255)"}
```

### motion-button-focus-backgroundcolor-0-ease

```css
{"backgroundColor": "rgb(0, 0, 0)", "color": "rgb(255, 255, 255)"}
```

### motion-button-hover-backgroundcolor-0-ease

```css
{"backgroundColor": "rgb(0, 0, 0)", "color": "rgb(255, 255, 255)"}
```

### motion-button-focus-backgroundcolor-0-ease

```css
{"backgroundColor": "rgb(0, 0, 0)", "color": "rgb(255, 255, 255)"}
```

### motion-button-hover-backgroundcolor-0-ease

```css
{"backgroundColor": "rgb(0, 0, 0)", "color": "rgb(255, 255, 255)"}
```

### motion-button-focus-backgroundcolor-0-ease

```css
{"backgroundColor": "rgb(0, 0, 0)", "color": "rgb(255, 255, 255)"}
```

### motion-button-hover-backgroundcolor-0-ease

```css
{"backgroundColor": "rgb(0, 0, 0)", "color": "rgb(255, 255, 255)"}
```

### motion-button-focus-backgroundcolor-0-ease

```css
{"backgroundColor": "rgb(0, 0, 0)", "color": "rgb(255, 255, 255)"}
```

### motion-button-hover-backgroundcolor-0-ease

```css
{"backgroundColor": "rgb(0, 0, 0)", "color": "rgb(255, 255, 255)"}
```

### motion-button-focus-backgroundcolor-0-ease

```css
{"backgroundColor": "rgb(0, 0, 0)", "color": "rgb(255, 255, 255)"}
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
