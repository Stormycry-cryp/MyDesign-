# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| button | state-change | transform | 900ms | 0ms | cubic-bezier(.19,1,.22,1) | 按钮state-change：transform missing -> translate3d(-70%,-60%,0)，900ms cubic-bezier(.19,1,.22,1)，state-change 触发 |
| button | state-change | all | 700ms | 0ms | cubic-bezier(.19,1,.22,1) | 按钮state-change：all，700ms cubic-bezier(.19,1,.22,1)，state-change 触发 |
| button | state-change | fill | 700ms | 0ms | cubic-bezier(.19,1,.22,1) | 按钮state-change：fill，700ms cubic-bezier(.19,1,.22,1)，state-change 触发 |
| button | state-change | fill | 700ms | 0ms | cubic-bezier(.19,1,.22,1) | 按钮state-change：fill，700ms cubic-bezier(.19,1,.22,1)，state-change 触发 |
| button | state-change | fill | 700ms | 0ms | cubic-bezier(.19,1,.22,1) | 按钮state-change：fill，700ms cubic-bezier(.19,1,.22,1)，state-change 触发 |
| button | state-change | all | 700ms | 0ms | cubic-bezier(.19,1,.22,1) | 按钮state-change：all，700ms cubic-bezier(.19,1,.22,1)，state-change 触发 |
| button | state-change | background-color | 700ms | 0ms | cubic-bezier(.19,1,.22,1) | 按钮state-change：background-color，700ms cubic-bezier(.19,1,.22,1)，state-change 触发 |
| button | state-change | fill | 700ms | 0ms | cubic-bezier(.19,1,.22,1) | 按钮state-change：fill，700ms cubic-bezier(.19,1,.22,1)，state-change 触发 |
| button | state-change | fill | 700ms | 0ms | cubic-bezier(.19,1,.22,1) | 按钮state-change：fill，700ms cubic-bezier(.19,1,.22,1)，state-change 触发 |
| button | state-change | fill | 700ms | 0ms | cubic-bezier(.19,1,.22,1) | 按钮state-change：fill，700ms cubic-bezier(.19,1,.22,1)，state-change 触发 |
| button | load | background-color | 300ms | 0ms | ease | 按钮load：background-color，300ms ease，load 触发 |
| button | load | animation | 1200ms | 0ms | ease-in-out | 按钮load：animation scaleY(.75) -> scaleY(1)，1200ms ease-in-out，load 触发 |
| overlay | state-change | opacity | 500ms | 0ms | cubic-bezier(.32,.72,0,1) | 浮层state-change：opacity，500ms cubic-bezier(.32,.72,0,1)，state-change 触发 |
| component | load | animation | 400ms | 0ms | linear | 组件load：animation rotate(0deg) -> rotate(1turn)，400ms linear，load 触发 |
| component | state-change | grid-template-rows | 600ms | 0ms | cubic-bezier(.4,.05,.32,1) | 组件state-change：grid-template-rows，600ms cubic-bezier(.4,.05,.32,1)，state-change 触发 |
| component | state-change | opacity | 800ms | 0ms | cubic-bezier(.4,.05,.32,1) | 组件state-change：opacity，800ms cubic-bezier(.4,.05,.32,1)，state-change 触发 |
| reveal | viewport | all | 300ms | 0ms | ease-in | 入场元素viewport：all missing -> translateY(350%)，300ms ease-in，viewport 触发 |
| component | state-change | all | 180ms | 0ms | ease-in-out | 组件state-change：all missing -> translateZ(0)，180ms ease-in-out，state-change 触发 |
| component | state-change | all | 180ms | 0ms | ease-in-out | 组件state-change：all missing -> translateZ(0)，180ms ease-in-out，state-change 触发 |
| component | state-change | width | 300ms | 0ms | ease-out | 组件state-change：width，300ms ease-out，state-change 触发 |
| component | load | animation | 1000ms | 0ms | linear | 组件load：animation，1000ms linear，load 触发 |
| component | load | animation | 1000ms | 0ms | linear | 组件load：animation rotate(0deg) -> rotate(1turn)，1000ms linear，load 触发 |
| card | state-change | stroke-dashoffset | 500ms | 0ms | ease-out | 卡片state-change：stroke-dashoffset，500ms ease-out，state-change 触发 |
| component | state-change | transform | 250ms | 0ms | ease-in-out | 组件state-change：transform missing -> translate3d(0,-105%,0)，250ms ease-in-out，state-change 触发 |
| component | state-change | opacity | 250ms | 0ms | ease-in-out | 组件state-change：opacity missing -> translate3d(0,-105%,0)，250ms ease-in-out，state-change 触发 |
| component | state-change | transform | 250ms | 0ms | ease-in-out | 组件state-change：transform missing -> translateZ(0)，250ms ease-in-out，state-change 触发 |
| component | state-change | opacity | 250ms | 0ms | ease-in-out | 组件state-change：opacity missing -> translateZ(0)，250ms ease-in-out，state-change 触发 |
| button | state-change | color | 500ms | 0ms | cubic-bezier(.19,1,.22,1) | 按钮state-change：color，500ms cubic-bezier(.19,1,.22,1)，state-change 触发 |
| navigation | hover | transform | 700ms | 0ms | cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.4, 0.05, 0.32, 1) | 导航hover：transform missing -> none，700ms cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.4, 0.05, 0.32, 1)，hover 触发；样本 MENU |
| navigation | focus | transform | 700ms | 0ms | cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.4, 0.05, 0.32, 1) | 导航focus：transform missing -> none，700ms cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.4, 0.05, 0.32, 1)，focus 触发；样本 MENU |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: assets/2026-06-12-patek-philippe-official-motion.json

## Missing Evidence
- motion-button-load-animation-1200-missing lacks easing
- motion-button-load-animation-1200-missing lacks easing
- motion-button-load-animation-1200-missing lacks easing
- motion-button-load-animation-1200-missing lacks easing
- motion-button-load-animation-1200-missing lacks easing
- motion-button-load-animation-1200-missing lacks easing
- motion-button-load-animation-1200-missing lacks easing
- motion-overlay-load-animation-300-missing lacks easing
- motion-overlay-load-animation-300-missing lacks easing
- motion-overlay-state-change-all-200-missing lacks easing
- motion-overlay-load-animation-300-missing lacks easing
- motion-overlay-load-animation-300-missing lacks easing
- motion-component-state-change-background-color-300-missing lacks easing
- motion-component-state-change-color-300-missing lacks easing
- motion-component-state-change-height-200-missing lacks easing
- motion-component-state-change-background-color-missing-missing lacks duration_ms
- motion-component-state-change-background-color-missing-missing lacks easing
- motion-card-state-change-all-missing-ease lacks duration_ms
- motion-card-state-change-all-200-missing lacks easing
- motion-card-state-change-all-200-missing lacks easing
- motion-card-state-change-all-200-missing lacks easing
- motion-card-state-change-all-200-missing lacks easing

## Snippet Appendix
### motion-button-state-change-transform-900-cubic-bezier-19-1-22-1

```css
.cta_cta__g1ZkP.cta_--is-contained__qMN1S:after { transition: transform .9s cubic-bezier(.19,1,.22,1); }
```

### motion-button-state-change-all-700-cubic-bezier-19-1-22-1

```css
.cta_cta__g1ZkP.cta_--is-outlined__z_8B9 { transition: all .7s cubic-bezier(.19,1,.22,1); }
```

### motion-button-state-change-fill-700-cubic-bezier-19-1-22-1

```css
.cta_cta__g1ZkP.cta_--is-outlined__z_8B9.cta_--is-brown__sjk4Z svg { transition: fill .7s cubic-bezier(.19,1,.22,1); }
```

### motion-button-state-change-fill-700-cubic-bezier-19-1-22-1

```css
.cta_cta__g1ZkP.cta_--is-outlined__z_8B9.cta_--is-orange__f6_tK svg { transition: fill .7s cubic-bezier(.19,1,.22,1); }
```

### motion-button-state-change-fill-700-cubic-bezier-19-1-22-1

```css
.cta_cta__g1ZkP.cta_--is-outlined__z_8B9.cta_--is-white__0hlgs svg { transition: fill .7s cubic-bezier(.19,1,.22,1); }
```

### motion-button-state-change-all-700-cubic-bezier-19-1-22-1

```css
.cta_cta__g1ZkP.cta_--is-text__oeq0q { transition: all .7s cubic-bezier(.19,1,.22,1); }
```

### motion-button-state-change-background-color-700-cubic-bezier-19-1-22-1

```css
.cta_cta__g1ZkP.cta_--is-text__oeq0q .cta_label__svrSv:after { transition: background-color .7s cubic-bezier(.19,1,.22,1); }
```

### motion-button-state-change-fill-700-cubic-bezier-19-1-22-1

```css
.cta_cta__g1ZkP.cta_--is-text__oeq0q.cta_--is-brown__sjk4Z svg { transition: fill .7s cubic-bezier(.19,1,.22,1); }
```

### motion-button-state-change-fill-700-cubic-bezier-19-1-22-1

```css
.cta_cta__g1ZkP.cta_--is-text__oeq0q.cta_--is-orange__f6_tK svg { transition: fill .7s cubic-bezier(.19,1,.22,1); }
```

### motion-button-state-change-fill-700-cubic-bezier-19-1-22-1

```css
.cta_cta__g1ZkP.cta_--is-text__oeq0q.cta_--is-white__0hlgs svg { transition: fill .7s cubic-bezier(.19,1,.22,1); }
```

### motion-button-load-background-color-300-ease

```css
.cta_line__xcZdo:before { transition: background-color .3s ease; }
```

### motion-button-load-animation-1200-ease-in-out

```css
.cta_line__xcZdo:before { animation: cta_pulse__QN_R6 calc(1.2s) ease-in-out infinite; }
```

### motion-overlay-state-change-opacity-500-cubic-bezier-32-72-0-1

```css
.dialog_overlay__4E4N1 { transition: opacity .5s cubic-bezier(.32,.72,0,1); }
```

### motion-component-load-animation-400-linear

```css
#nprogress .spinner-icon { animation: nprogress-spinner .4s linear infinite; }
```

### motion-component-state-change-grid-template-rows-600-cubic-bezier-4-05-32-1

```css
.watch-finder-styles_disclaimer-wrapper__7gcd2 { transition: grid-template-rows .6s cubic-bezier(.4,.05,.32,1); }
```

### motion-component-state-change-opacity-800-cubic-bezier-4-05-32-1

```css
.watch-finder-styles_disclamer__d4VOa { transition: opacity .8s cubic-bezier(.4,.05,.32,1); }
```

### motion-reveal-viewport-all-300-ease-in

```css
.uppy-Informer-animated { transition: all .3s ease-in; }
```

### motion-component-state-change-all-180-ease-in-out

```css
.uppy-Root [aria-label][role~=tooltip]:after { transition: all .18s ease-in-out 0s; }
```

### motion-component-state-change-all-180-ease-in-out

```css
.uppy-Root [aria-label][role~=tooltip]:before { transition: all .18s ease-in-out 0s; }
```

### motion-component-state-change-width-300-ease-out

```css
.uppy-StatusBar-progress { transition: width .3s ease-out; }
```

### motion-component-load-animation-1000-linear

```css
.uppy-StatusBar-progress.is-indeterminate { animation: uppy-StatusBar-ProgressStripes 1s linear infinite; }
```

### motion-component-load-animation-1000-linear

```css
.uppy-StatusBar-spinner { animation: uppy-StatusBar-spinnerAnimation 1s linear 0ms; }
```

### motion-card-state-change-stroke-dashoffset-500-ease-out

```css
.uppy-Dashboard-Item-progressIcon--progress { transition: stroke-dashoffset .5s ease-out; }
```

### motion-component-state-change-transform-250-ease-in-out

```css
.uppy-transition-slideDownUp-enter { transition: transform .25s ease-in-out; }
```

### motion-component-state-change-opacity-250-ease-in-out

```css
.uppy-transition-slideDownUp-enter { transition: opacity .25s ease-in-out; }
```

### motion-component-state-change-transform-250-ease-in-out

```css
.uppy-transition-slideDownUp-leave { transition: transform .25s ease-in-out; }
```

### motion-component-state-change-opacity-250-ease-in-out

```css
.uppy-transition-slideDownUp-leave { transition: opacity .25s ease-in-out; }
```

### motion-button-state-change-color-500-cubic-bezier-19-1-22-1

```css
.back-button_back-button__YK_xu { transition: color .5s cubic-bezier(.19,1,.22,1); }
```

### motion-navigation-hover-transform-700-cubic-bezier-0-19-1-0-22-1-cubic-bezier-0-4-0-05-0-32-1

```css
{"bottom": "900.938px", "transform": "none"}
```

### motion-navigation-focus-transform-700-cubic-bezier-0-19-1-0-22-1-cubic-bezier-0-4-0-05-0-32-1

```css
{"bottom": "900.938px", "transform": "none"}
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
