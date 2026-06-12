# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| reveal | viewport | animation | 1000ms | 0ms | linear | 入场元素viewport：animation rotate(1turn) -> rotate(1turn)，1000ms linear，viewport 触发 |
| component | state-change | color | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：color，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | background-color | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：background-color，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | border-color | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：border-color，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | text-decoration-color | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：text-decoration-color，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | fill | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：fill，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | stroke | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：stroke，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | opacity | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：opacity，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | color | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：color，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | background-color | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：background-color，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | border-color | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：border-color，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | text-decoration-color | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：text-decoration-color，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | fill | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：fill，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | stroke | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：stroke，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | opacity | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：opacity，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | box-shadow | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：box-shadow，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | transform | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：transform，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | filter | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：filter，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | backdrop-filter | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：backdrop-filter，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | -webkit-backdrop-filter | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：-webkit-backdrop-filter，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | all | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：all，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | border | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：border，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | color | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：color，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | load | animation | 400ms | 0ms | ease-out | 组件load：animation，400ms ease-out，load 触发 |
| component | load | animation | 400ms | 0ms | ease-out | 组件load：animation，400ms ease-out，load 触发 |
| component | hover | opacity | 400ms | 0ms | ease | 组件hover：opacity，400ms ease，hover 触发 |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: assets/2026-06-12-viviens-creative-talent-motion.json

## Missing Evidence
- motion-component-state-change-all-missing-missing lacks duration_ms
- motion-component-state-change-all-missing-missing lacks easing
- motion-component-state-change-all-300-missing lacks easing
- motion-component-state-change-all-500-missing lacks easing
- motion-component-state-change-all-700-missing lacks easing
- motion-component-state-change-all-1000-missing lacks easing
- motion-component-load-animation-300-missing lacks easing
- motion-component-load-animation-500-missing lacks easing
- motion-component-load-animation-700-missing lacks easing
- motion-component-load-animation-1000-missing lacks easing
- motion-component-load-animation-1000-missing lacks easing
- motion-component-load-cubic-bezier-4-missing-cubic-bezier-4-0-2-1 lacks duration_ms
- motion-component-load-cubic-bezier-4-missing-cubic-bezier-4-0-2-1 lacks duration_ms
- motion-component-state-change-color-400-missing lacks easing

## Snippet Appendix
### motion-reveal-viewport-animation-1000-linear

```css
.animate-spin { animation: spin 1s linear infinite; }
```

### motion-component-state-change-color-150-cubic-bezier-4-0-2-1

```css
.transition-colors { transition-property: color; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-background-color-150-cubic-bezier-4-0-2-1

```css
.transition-colors { transition-property: background-color; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-border-color-150-cubic-bezier-4-0-2-1

```css
.transition-colors { transition-property: border-color; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-text-decoration-color-150-cubic-bezier-4-0-2-1

```css
.transition-colors { transition-property: text-decoration-color; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-fill-150-cubic-bezier-4-0-2-1

```css
.transition-colors { transition-property: fill; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-stroke-150-cubic-bezier-4-0-2-1

```css
.transition-colors { transition-property: stroke; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-opacity-150-cubic-bezier-4-0-2-1

```css
.transition-opacity { transition-property: opacity; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-color-150-cubic-bezier-4-0-2-1

```css
.transition { transition-property: color; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-background-color-150-cubic-bezier-4-0-2-1

```css
.transition { transition-property: background-color; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-border-color-150-cubic-bezier-4-0-2-1

```css
.transition { transition-property: border-color; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-text-decoration-color-150-cubic-bezier-4-0-2-1

```css
.transition { transition-property: text-decoration-color; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-fill-150-cubic-bezier-4-0-2-1

```css
.transition { transition-property: fill; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-stroke-150-cubic-bezier-4-0-2-1

```css
.transition { transition-property: stroke; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-opacity-150-cubic-bezier-4-0-2-1

```css
.transition { transition-property: opacity; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-box-shadow-150-cubic-bezier-4-0-2-1

```css
.transition { transition-property: box-shadow; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-transform-150-cubic-bezier-4-0-2-1

```css
.transition { transition-property: transform; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-filter-150-cubic-bezier-4-0-2-1

```css
.transition { transition-property: filter; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-backdrop-filter-150-cubic-bezier-4-0-2-1

```css
.transition { transition-property: backdrop-filter; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-webkit-backdrop-filter-150-cubic-bezier-4-0-2-1

```css
.transition { transition-property: -webkit-backdrop-filter; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-all-150-cubic-bezier-4-0-2-1

```css
.transition-all { transition-property: all; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-border-150-cubic-bezier-4-0-2-1

```css
.transition-\[border\] { transition-property: border; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-color-150-cubic-bezier-4-0-2-1

```css
.transition-\[color\] { transition-property: color; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-load-animation-400-ease-out

```css
.accordion-content[data-state=open] { animation: slideDown .4s ease-out; }
```

### motion-component-load-animation-400-ease-out

```css
.accordion-content[data-state=closed] { animation: slideUp .4s ease-out; }
```

### motion-component-hover-opacity-400-ease

```css
.media-wrapper:hover .caption { transition: opacity .4s ease; }
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
