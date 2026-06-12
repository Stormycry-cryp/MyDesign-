# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| reveal | viewport | animation | 300ms | 0ms | cubic-bezier(.23,1,.32,1) | 入场元素viewport：animation translateY(-20px) -> translate(0)，300ms cubic-bezier(.23,1,.32,1)，viewport 触发 |
| overlay | load | animation | 200ms | 0ms | ease-in | 浮层load：animation 0 -> 1，200ms ease-in，load 触发 |
| overlay | load | animation | 200ms | 0ms | ease-in | 浮层load：animation 1 -> 0，200ms ease-in，load 触发 |
| overlay | state-change | opacity | 100ms | 0ms | ease-in | 浮层state-change：opacity，100ms ease-in，state-change 触发 |
| component | load | animation | 200ms | 0ms | ease-in | 组件load：animation 0 -> 1，200ms ease-in，load 触发 |
| component | load | animation | 1000ms | 0ms | ease-in-out | 组件load：animation rotate(360deg) -> rotate(360deg)，1000ms ease-in-out，load 触发 |
| reveal | viewport | animation | 1500ms | 0ms | cubic-bezier(.4,0,.6,1) | 入场元素viewport：animation .5 -> .5，1500ms cubic-bezier(.4,0,.6,1)，viewport 触发 |
| reveal | viewport | animation | 1000ms | 0ms | linear | 入场元素viewport：animation rotate(360deg) -> rotate(360deg)，1000ms linear，viewport 触发 |
| component | state-change | color | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：color，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | background-color | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：background-color，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | border-color | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：border-color，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | outline-color | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：outline-color，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | text-decoration-color | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：text-decoration-color，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | fill | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：fill，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | stroke | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：stroke，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | --tw-gradient-from | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：--tw-gradient-from，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | --tw-gradient-via | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：--tw-gradient-via，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | --tw-gradient-to | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：--tw-gradient-to，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | opacity | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：opacity，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | box-shadow | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：box-shadow，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | transform | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：transform，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | translate | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：translate，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | scale | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：scale，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | rotate | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：rotate，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | filter | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：filter，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | -webkit-backdrop-filter | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：-webkit-backdrop-filter，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | backdrop-filter | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：backdrop-filter，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | display | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：display，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | visibility | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：visibility，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | content-visibility | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：content-visibility，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | overlay | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：overlay，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | pointer-events | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：pointer-events，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | height | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：height，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | width | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：width，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | all | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：all，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | color | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：color，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | background-color | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：background-color，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | border-color | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：border-color，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | outline-color | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：outline-color，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | text-decoration-color | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：text-decoration-color，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | fill | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：fill，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | stroke | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：stroke，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | --tw-gradient-from | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：--tw-gradient-from，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| component | state-change | --tw-gradient-via | 500ms | 0ms | cubic-bezier(0,0,.2,1) | 组件state-change：--tw-gradient-via，500ms cubic-bezier(0,0,.2,1)，state-change 触发 |
| navigation | focus | boxShadow | 0ms | 0ms | ease | 导航focus：boxShadow missing -> rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(255, 255, 255) 0px 0px 0px 2px, oklch(0.585 0.233 277.117) 0px 0px 0px 4px, rgba(0, 0, 0, 0) 0px 0px 0px 0px，0ms ease，focus 触发；样本 ds-navigation-2 |
| navigation | hover | color | 100ms | 0ms | ease-in | 导航hover：color missing -> oklch(0.21 0.006 285.885)，100ms ease-in，hover 触发；样本 Login |
| navigation | focus | color | 100ms | 0ms | ease-in | 导航focus：color missing -> oklch(0.21 0.006 285.885)，100ms ease-in，focus 触发；样本 Login |
| button | hover | backgroundColor | 150ms | 0ms | cubic-bezier(0.4, 0, 0.2, 1) | 按钮hover：backgroundColor missing -> oklab(0.94365 0.000794381 -0.0025425 / 0.775098)，150ms cubic-bezier(0.4, 0, 0.2, 1)，hover 触发；样本 Last 28 days |
| button | focus | backgroundColor | 150ms | 0ms | cubic-bezier(0.4, 0, 0.2, 1) | 按钮focus：backgroundColor missing -> oklab(0.94365 0.000794381 -0.0025425 / 0.794136)，150ms cubic-bezier(0.4, 0, 0.2, 1)，focus 触发；样本 Last 28 days |
| button | focus | boxShadow | 0ms | 0ms | ease | 按钮focus：boxShadow missing -> rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(255, 255, 255) 0px 0px 0px 2px, oklch(0.585 0.233 277.117) 0px 0px 0px 4px, rgba(0, 0, 0, 0) 0px 0px 0px 0px，0ms ease，focus 触发；样本 CHANNELS |
| button | focus | boxShadow | 0ms | 0ms | ease | 按钮focus：boxShadow missing -> rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(255, 255, 255) 0px 0px 0px 2px, oklch(0.585 0.233 277.117) 0px 0px 0px 4px, rgba(0, 0, 0, 0) 0px 0px 0px 0px，0ms ease，focus 触发；样本 SOURCES |
| button | focus | boxShadow | 0ms | 0ms | ease | 按钮focus：boxShadow missing -> rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(255, 255, 255) 0px 0px 0px 2px, oklch(0.585 0.233 277.117) 0px 0px 0px 4px, rgba(0, 0, 0, 0) 0px 0px 0px 0px，0ms ease，focus 触发；样本 CAMPAIGNS |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: assets/2026-06-12-plausible-analytics-live-dashboard-motion.json

## Missing Evidence
- motion-component-state-change-fill-100-missing lacks easing
- motion-component-state-change-fill-100-missing lacks easing
- motion-component-state-change-all-300-missing lacks easing
- motion-component-state-change-all-300-missing lacks easing

## Snippet Appendix
### motion-reveal-viewport-animation-300-cubic-bezier-23-1-32-1

```css
.flatpickr-calendar.animate.open { animation: .3s cubic-bezier(.23,1,.32,1) fpFadeInDown; }
```

### motion-overlay-load-animation-200-ease-in

```css
.modal[aria-hidden=false] .modal__overlay { animation: .2s ease-in mm-fade-in; }
```

### motion-overlay-load-animation-200-ease-in

```css
.modal[aria-hidden=true] .modal__overlay { animation: .2s ease-in mm-fade-out; }
```

### motion-overlay-state-change-opacity-100-ease-in

```css
.modal-enter-active { transition: opacity .1s ease-in; }
```

### motion-component-load-animation-200-ease-in

```css
.loading { animation: .2s ease-in loader-fade-in; }
```

### motion-component-load-animation-1000-ease-in-out

```css
.loading div { animation: 1s ease-in-out infinite spin; }
```

### motion-reveal-viewport-animation-1500-cubic-bezier-4-0-6-1

```css
.animate-pulse { animation: pulse 1.5s cubic-bezier(.4,0,.6,1)infinite; }
```

### motion-reveal-viewport-animation-1000-linear

```css
.animate-spin { animation: spin 1s linear infinite; }
```

### motion-component-state-change-color-500-cubic-bezier-0-0-2-1

```css
.transition { transition-property: color; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-background-color-500-cubic-bezier-0-0-2-1

```css
.transition { transition-property: background-color; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-border-color-500-cubic-bezier-0-0-2-1

```css
.transition { transition-property: border-color; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-outline-color-500-cubic-bezier-0-0-2-1

```css
.transition { transition-property: outline-color; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-text-decoration-color-500-cubic-bezier-0-0-2-1

```css
.transition { transition-property: text-decoration-color; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-fill-500-cubic-bezier-0-0-2-1

```css
.transition { transition-property: fill; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-stroke-500-cubic-bezier-0-0-2-1

```css
.transition { transition-property: stroke; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-tw-gradient-from-500-cubic-bezier-0-0-2-1

```css
.transition { transition-property: --tw-gradient-from; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-tw-gradient-via-500-cubic-bezier-0-0-2-1

```css
.transition { transition-property: --tw-gradient-via; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-tw-gradient-to-500-cubic-bezier-0-0-2-1

```css
.transition { transition-property: --tw-gradient-to; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-opacity-500-cubic-bezier-0-0-2-1

```css
.transition { transition-property: opacity; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-box-shadow-500-cubic-bezier-0-0-2-1

```css
.transition { transition-property: box-shadow; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-transform-500-cubic-bezier-0-0-2-1

```css
.transition { transition-property: transform; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-translate-500-cubic-bezier-0-0-2-1

```css
.transition { transition-property: translate; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-scale-500-cubic-bezier-0-0-2-1

```css
.transition { transition-property: scale; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-rotate-500-cubic-bezier-0-0-2-1

```css
.transition { transition-property: rotate; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-filter-500-cubic-bezier-0-0-2-1

```css
.transition { transition-property: filter; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-webkit-backdrop-filter-500-cubic-bezier-0-0-2-1

```css
.transition { transition-property: -webkit-backdrop-filter; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-backdrop-filter-500-cubic-bezier-0-0-2-1

```css
.transition { transition-property: backdrop-filter; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-display-500-cubic-bezier-0-0-2-1

```css
.transition { transition-property: display; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-visibility-500-cubic-bezier-0-0-2-1

```css
.transition { transition-property: visibility; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-content-visibility-500-cubic-bezier-0-0-2-1

```css
.transition { transition-property: content-visibility; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-overlay-500-cubic-bezier-0-0-2-1

```css
.transition { transition-property: overlay; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-pointer-events-500-cubic-bezier-0-0-2-1

```css
.transition { transition-property: pointer-events; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-height-500-cubic-bezier-0-0-2-1

```css
.transition-\[height\] { transition-property: height; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-width-500-cubic-bezier-0-0-2-1

```css
.transition-\[width\] { transition-property: width; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-all-500-cubic-bezier-0-0-2-1

```css
.transition-all { transition-property: all; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-color-500-cubic-bezier-0-0-2-1

```css
.transition-colors { transition-property: color; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-background-color-500-cubic-bezier-0-0-2-1

```css
.transition-colors { transition-property: background-color; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-border-color-500-cubic-bezier-0-0-2-1

```css
.transition-colors { transition-property: border-color; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-outline-color-500-cubic-bezier-0-0-2-1

```css
.transition-colors { transition-property: outline-color; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-text-decoration-color-500-cubic-bezier-0-0-2-1

```css
.transition-colors { transition-property: text-decoration-color; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-fill-500-cubic-bezier-0-0-2-1

```css
.transition-colors { transition-property: fill; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-stroke-500-cubic-bezier-0-0-2-1

```css
.transition-colors { transition-property: stroke; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-tw-gradient-from-500-cubic-bezier-0-0-2-1

```css
.transition-colors { transition-property: --tw-gradient-from; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-component-state-change-tw-gradient-via-500-cubic-bezier-0-0-2-1

```css
.transition-colors { transition-property: --tw-gradient-via; transition-duration: .5s); transition-timing-function: cubic-bezier(0,0,.2,1)); }
```

### motion-navigation-focus-boxshadow-0-ease

```css
{"boxShadow": "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(255, 255, 255) 0px 0px 0px 2px, oklch(0.585 0.233 277.117) 0px 0px 0px 4px, rgba(0, 0, 0, 0) 0px 0px 0px 0px"}
```

### motion-navigation-hover-color-100-ease-in

```css
{"color": "oklch(0.21 0.006 285.885)"}
```

### motion-navigation-focus-color-100-ease-in

```css
{"boxShadow": "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0 0 0 / 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px", "color": "oklch(0.21 0.006 285.885)"}
```

### motion-button-hover-backgroundcolor-150-cubic-bezier-0-4-0-0-2-1

```css
{"backgroundColor": "oklab(0.94365 0.000794381 -0.0025425 / 0.775098)"}
```

### motion-button-focus-backgroundcolor-150-cubic-bezier-0-4-0-0-2-1

```css
{"backgroundColor": "oklab(0.94365 0.000794381 -0.0025425 / 0.794136)"}
```

### motion-button-focus-boxshadow-0-ease

```css
{"boxShadow": "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(255, 255, 255) 0px 0px 0px 2px, oklch(0.585 0.233 277.117) 0px 0px 0px 4px, rgba(0, 0, 0, 0) 0px 0px 0px 0px"}
```

### motion-button-focus-boxshadow-0-ease

```css
{"boxShadow": "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(255, 255, 255) 0px 0px 0px 2px, oklch(0.585 0.233 277.117) 0px 0px 0px 4px, rgba(0, 0, 0, 0) 0px 0px 0px 0px"}
```

### motion-button-focus-boxshadow-0-ease

```css
{"boxShadow": "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(255, 255, 255) 0px 0px 0px 2px, oklch(0.585 0.233 277.117) 0px 0px 0px 4px, rgba(0, 0, 0, 0) 0px 0px 0px 0px"}
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
