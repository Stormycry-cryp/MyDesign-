# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| reveal | viewport | animation | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 入场元素viewport：animation scale(2) -> scale(2)，500ms cubic-bezier(0,0,.2,1)，viewport 触发 |
| reveal | viewport | animation | 1500ms | 0ms | linear | 入场元素viewport：animation 1 -> .3，1500ms linear，viewport 触发 |
| reveal | viewport | animation | 2000ms | 0ms | cubic-bezier(.4,0,.6,1) | 入场元素viewport：animation .5 -> .5，2000ms cubic-bezier(.4,0,.6,1)，viewport 触发 |
| reveal | viewport | animation | 200ms | 0ms | ease-out | 入场元素viewport：animation scale(.95) -> scale(1)，200ms ease-out，viewport 触发 |
| reveal | viewport | animation | 250ms | 0ms | ease-out | 入场元素viewport：animation translateY(-8px) -> translateY(0)，250ms ease-out，viewport 触发 |
| reveal | viewport | animation | 1000ms | 0ms | linear | 入场元素viewport：animation rotate(360deg) -> rotate(360deg)，1000ms linear，viewport 触发 |
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
| component | state-change | color | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：color，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | box-shadow | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：box-shadow，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | color | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：color，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | box-shadow | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：box-shadow，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | height | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：height，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | width | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：width，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | height | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：height，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | width | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：width，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | left | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：left，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | right | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：right，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | width | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：width，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | left | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：left，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | right | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：right，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | width | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：width，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | left | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：left，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | right | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：right，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | margin | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：margin，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | opa | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：opa，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | margin | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：margin，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | opa | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：opa，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | width | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：width，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | height | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：height，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | padding | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：padding，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | width | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：width，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | height | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：height，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | padding | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：padding，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | width | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：width，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | height | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：height，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | padding | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：padding，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | width | 150ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：width，150ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| button | load | animation | 2000ms | 0ms | linear | 按钮load：animation rotate(0) -> rotate(1turn)，2000ms linear，load 触发 |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: assets/2026-06-12-electricity-maps-app-motion.json

## Missing Evidence
- motion-reveal-viewport-animation-1000-missing lacks easing

## Snippet Appendix
### motion-reveal-viewport-animation-500-cubic-bezier-0-0-2-1

```css
.animate-\[ping_0\.5s_cubic-bezier\(0\,0\,0\.2\,1\)\] { animation: ping .5s cubic-bezier(0,0,.2,1); }
```

### motion-reveal-viewport-animation-1500-linear

```css
.animate-fade-in-out { animation: fade-in-out 1.5s linear 0s infinite; }
```

### motion-reveal-viewport-animation-2000-cubic-bezier-4-0-6-1

```css
.animate-pulse { animation: pulse 2s cubic-bezier(.4,0,.6,1) infinite; }
```

### motion-reveal-viewport-animation-200-ease-out

```css
.animate-reveal { animation: reveal .2s ease-out forwards; }
```

### motion-reveal-viewport-animation-250-ease-out

```css
.animate-slide-in-down { animation: fade-in-down .25s ease-out forwards; }
```

### motion-reveal-viewport-animation-1000-linear

```css
.animate-spin { animation: spin 1s linear infinite; }
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

### motion-component-state-change-color-150-cubic-bezier-4-0-2-1

```css
.transition-\[color\ { transition-property: color; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-box-shadow-150-cubic-bezier-4-0-2-1

```css
.transition-\[color\ { transition-property: box-shadow; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-color-150-cubic-bezier-4-0-2-1

```css
box-shadow\] { transition-property: color; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-box-shadow-150-cubic-bezier-4-0-2-1

```css
box-shadow\] { transition-property: box-shadow; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-height-150-cubic-bezier-4-0-2-1

```css
.transition-\[height\ { transition-property: height; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-width-150-cubic-bezier-4-0-2-1

```css
.transition-\[height\ { transition-property: width; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-height-150-cubic-bezier-4-0-2-1

```css
width\] { transition-property: height; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-width-150-cubic-bezier-4-0-2-1

```css
width\] { transition-property: width; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-left-150-cubic-bezier-4-0-2-1

```css
.transition-\[left\ { transition-property: left; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-right-150-cubic-bezier-4-0-2-1

```css
.transition-\[left\ { transition-property: right; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-width-150-cubic-bezier-4-0-2-1

```css
.transition-\[left\ { transition-property: width; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-left-150-cubic-bezier-4-0-2-1

```css
right\ { transition-property: left; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-right-150-cubic-bezier-4-0-2-1

```css
right\ { transition-property: right; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-width-150-cubic-bezier-4-0-2-1

```css
right\ { transition-property: width; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-left-150-cubic-bezier-4-0-2-1

```css
width\] { transition-property: left; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-right-150-cubic-bezier-4-0-2-1

```css
width\] { transition-property: right; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-margin-150-cubic-bezier-4-0-2-1

```css
.transition-\[margin\ { transition-property: margin; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-opa-150-cubic-bezier-4-0-2-1

```css
.transition-\[margin\ { transition-property: opa; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-margin-150-cubic-bezier-4-0-2-1

```css
opa\] { transition-property: margin; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-opa-150-cubic-bezier-4-0-2-1

```css
opa\] { transition-property: opa; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-width-150-cubic-bezier-4-0-2-1

```css
.transition-\[width\ { transition-property: width; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-height-150-cubic-bezier-4-0-2-1

```css
.transition-\[width\ { transition-property: height; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-padding-150-cubic-bezier-4-0-2-1

```css
.transition-\[width\ { transition-property: padding; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-width-150-cubic-bezier-4-0-2-1

```css
height\ { transition-property: width; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-height-150-cubic-bezier-4-0-2-1

```css
height\ { transition-property: height; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-padding-150-cubic-bezier-4-0-2-1

```css
height\ { transition-property: padding; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-width-150-cubic-bezier-4-0-2-1

```css
padding\] { transition-property: width; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-height-150-cubic-bezier-4-0-2-1

```css
padding\] { transition-property: height; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-padding-150-cubic-bezier-4-0-2-1

```css
padding\] { transition-property: padding; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-width-150-cubic-bezier-4-0-2-1

```css
.transition-\[width\] { transition-property: width; transition-duration: .15s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-button-load-animation-2000-linear

```css
.maplibregl-ctrl button.maplibregl-ctrl-geolocate.maplibregl-ctrl-geolocate-waiting .maplibregl-ctrl-icon { animation: maplibregl-spin 2s linear infinite; }
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
