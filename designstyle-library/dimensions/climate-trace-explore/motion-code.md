# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| component | load | animation | 300ms | 0ms | ease-in | 组件load：animation 0 -> 1，300ms ease-in，load 触发 |
| component | load | animation | 300ms | 0ms | ease-out | 组件load：animation translateY(100%) -> translateY(0)，300ms ease-out，load 触发 |
| card | load | transform | 400ms | 0ms | ease-in-out | 卡片load：transform missing -> translateX(calc(-1 * 6px))，400ms ease-in-out，load 触发 |
| card | state-change | color | 200ms | 0ms | ease-in-out | 卡片state-change：color，200ms ease-in-out，state-change 触发 |
| card | state-change | opacity | 200ms | 0ms | ease-in-out | 卡片state-change：opacity，200ms ease-in-out，state-change 触发 |
| card | state-change | color | 200ms | 0ms | ease-in-out | 卡片state-change：color，200ms ease-in-out，state-change 触发 |
| card | state-change | opacity | 200ms | 0ms | ease-in-out | 卡片state-change：opacity，200ms ease-in-out，state-change 触发 |
| component | state-change | transform | 300ms | 0ms | ease | 组件state-change：transform，300ms ease，state-change 触发 |
| button | state-change | background | 300ms | 0ms | ease | 按钮state-change：background，300ms ease，state-change 触发 |
| component | state-change | transform | 300ms | 0ms | ease | 组件state-change：transform，300ms ease，state-change 触发 |
| component | state-change | transform | 300ms | 0ms | ease | 组件state-change：transform，300ms ease，state-change 触发 |
| component | state-change | transform | 300ms | 0ms | ease | 组件state-change：transform，300ms ease，state-change 触发 |
| component | state-change | transform | 300ms | 0ms | ease | 组件state-change：transform，300ms ease，state-change 触发 |
| component | state-change | all | 300ms | 0ms | ease | 组件state-change：all，300ms ease，state-change 触发 |
| component | state-change | transform | 300ms | 0ms | ease | 组件state-change：transform missing -> translateY(-50%)，300ms ease，state-change 触发 |
| component | state-change | transform | 300ms | 0ms | ease | 组件state-change：transform missing -> scale(1)，300ms ease，state-change 触发 |
| component | state-change | transform | 300ms | 0ms | ease | 组件state-change：transform missing -> translateX(-2px)，300ms ease，state-change 触发 |
| component | state-change | transform | 300ms | 0ms | ease | 组件state-change：transform missing -> translateX(0)，300ms ease，state-change 触发 |
| component | state-change | opacity | 300ms | 0ms | ease-in-out | 组件state-change：opacity，300ms ease-in-out，state-change 触发 |
| component | state-change | transform | 300ms | 0ms | ease | 组件state-change：transform，300ms ease，state-change 触发 |
| navigation | state-change | width | 300ms | 0ms | ease-out | 导航state-change：width，300ms ease-out，state-change 触发 |
| card | state-change | width | 300ms | 0ms | ease-out | 卡片state-change：width，300ms ease-out，state-change 触发 |
| card | state-change | width | 300ms | 0ms | ease-out | 卡片state-change：width，300ms ease-out，state-change 触发 |
| navigation | state-change | margin | 300ms | 0ms | ease-out | 导航state-change：margin，300ms ease-out，state-change 触发 |
| component | load | animation | 400ms | 0ms | ease-out | 组件load：animation translate(-50%,-50%) scale(.6) -> translate(-50%,-50%) scale(1)，400ms ease-out，load 触发 |
| button | state-change | transform | 200ms | 0ms | ease-in-out | 按钮state-change：transform，200ms ease-in-out，state-change 触发 |
| component | state-change | transform | 200ms | 0ms | ease-in-out | 组件state-change：transform，200ms ease-in-out，state-change 触发 |
| component | load | animation | 3000ms | 0ms | cubic-bezier(0,.2,.8,1) | 组件load：animation scale(.5) -> scale(1.5)，3000ms cubic-bezier(0,.2,.8,1)，load 触发 |
| component | load | animation | 2000ms | 0ms | cubic-bezier(0,.2,.8,1) | 组件load：animation scale(.5) -> scale(1.5)，2000ms cubic-bezier(0,.2,.8,1)，load 触发 |
| component | state-change | bottom | 300ms | 0ms | ease-out | 组件state-change：bottom，300ms ease-out，state-change 触发 |
| card | load | animation | 500ms | 0ms | ease-in-out | 卡片load：animation 0 -> 1，500ms ease-in-out，load 触发 |
| button | state-change | opacity | 200ms | 0ms | linear | 按钮state-change：opacity，200ms linear，state-change 触发 |
| button | load | animation | 2000ms | 0ms | linear | 按钮load：animation rotate(0deg) -> rotate(1turn)，2000ms linear，load 触发 |
| component | state-change | opacity | 750ms | 0ms | ease-in-out | 组件state-change：opacity，750ms ease-in-out，state-change 触发 |
| component | state-change | opacity | 750ms | 0ms | ease-in-out | 组件state-change：opacity，750ms ease-in-out，state-change 触发 |
| component | state-change | opacity | 100ms | 0ms | ease-in-out | 组件state-change：opacity，100ms ease-in-out，state-change 触发 |
| component | state-change | opacity | 100ms | 0ms | ease-in-out | 组件state-change：opacity，100ms ease-in-out，state-change 触发 |
| button | state-change | margin | 300ms | 0ms | ease-out | 按钮state-change：margin，300ms ease-out，state-change 触发 |
| card | state-change | transform | 300ms | 0ms | ease-in-out | 卡片state-change：transform missing -> scaleX(0)，300ms ease-in-out，state-change 触发 |
| button | hover | backgroundColor | 200ms | 0ms | ease | 按钮hover：backgroundColor missing -> rgb(153, 153, 153)，200ms ease，hover 触发；样本 ds-button-7 |
| button | focus | backgroundColor | 200ms | 0ms | ease | 按钮focus：backgroundColor missing -> rgb(153, 153, 153)，200ms ease，focus 触发；样本 ds-button-7 |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: assets/2026-06-12-climate-trace-explore-motion.json

## Missing Evidence
- motion-card-load-animation-missing-missing lacks duration_ms
- motion-card-load-animation-missing-missing lacks easing
- motion-component-state-change-var-transition-fast-missing-missing lacks duration_ms
- motion-component-state-change-var-transition-fast-missing-missing lacks easing
- motion-component-state-change-all-200-missing lacks easing
- motion-component-state-change-opacity-200-missing lacks easing
- motion-component-load-animation-2000-missing lacks easing

## Snippet Appendix
### motion-component-load-animation-300-ease-in

```css
.style_overlay__0gXDM { animation: style_fadeIn__sMfUi .3s ease-in; }
```

### motion-component-load-animation-300-ease-out

```css
.style_banner__xD97B { animation: style_slideUp__B_QTj .3s ease-out; }
```

### motion-card-load-transform-400-ease-in-out

```css
.style_blurb__3Gtxr .style_blurbItem___GO34 { transition: transform .4s ease-in-out; }
```

### motion-card-state-change-color-200-ease-in-out

```css
.style_blurb__3Gtxr .style_blurbItem___GO34 .style_arrow__21Tkb { transition: color .2s ease-in-out; }
```

### motion-card-state-change-opacity-200-ease-in-out

```css
.style_blurb__3Gtxr .style_blurbItem___GO34 .style_arrow__21Tkb { transition: opacity .2s ease-in-out; }
```

### motion-card-state-change-color-200-ease-in-out

```css
.style_blurb__3Gtxr .style_blurbItem___GO34 strong { transition: color .2s ease-in-out; }
```

### motion-card-state-change-opacity-200-ease-in-out

```css
.style_blurb__3Gtxr .style_blurbItem___GO34 strong { transition: opacity .2s ease-in-out; }
```

### motion-component-state-change-transform-300-ease

```css
.style_actions__xNzh0 .ant-btn .anticon { transition: transform .3s ease!important; }
```

### motion-button-state-change-background-300-ease

```css
.styles_stat__pEIoO .styles_buttonLink__8aU_e { transition: background .3s ease; }
```

### motion-component-state-change-transform-300-ease

```css
.styles_viewMoreLink__m_MY2 .anticon { transition: transform .3s ease!important; }
```

### motion-component-state-change-transform-300-ease

```css
.style_imageContainer__xi0f1 .style_image__67uNP { transition: transform .3s ease; }
```

### motion-component-state-change-transform-300-ease

```css
.style_image___ssCz { transition: transform .3s ease; }
```

### motion-component-state-change-transform-300-ease

```css
.style_image__fiO_k { transition: transform .3s ease; }
```

### motion-component-state-change-all-300-ease

```css
.styles_feedbackMessage__uWc_5 { transition: all .3s ease; }
```

### motion-component-state-change-transform-300-ease

```css
.styles_root__g55kq .styles_placeholder__IrhC7 { transition: transform .3s ease; }
```

### motion-component-state-change-transform-300-ease

```css
.styles_root__g55kq .styles_placeholderText__ENe2y { transition: transform .3s ease; }
```

### motion-component-state-change-transform-300-ease

```css
.styles_icon__XqipF { transition: transform .3s ease; }
```

### motion-component-state-change-transform-300-ease

```css
.styles_arrowLink__2qtcZ .styles_arrow__EbczU { transition: transform .3s ease; }
```

### motion-component-state-change-opacity-300-ease-in-out

```css
.fade-effect { transition: opacity .3s ease-in-out; }
```

### motion-component-state-change-transform-300-ease

```css
.news-thumb img { transition: transform .3s ease; }
```

### motion-navigation-state-change-width-300-ease-out

```css
.trace-main-menu .has-children:after { transition: width .3s ease-out; }
```

### motion-card-state-change-width-300-ease-out

```css
.trace-main-menu .parent-item:after { transition: width .3s ease-out; }
```

### motion-card-state-change-width-300-ease-out

```css
.trace-main-menu .child-item:after { transition: width .3s ease-out; }
```

### motion-navigation-state-change-margin-300-ease-out

```css
.trace-menu-stroke { transition: margin .3s ease-out; }
```

### motion-component-load-animation-400-ease-out

```css
.styles_copiedIcon__KaUbz:after { animation: styles_pulse__RNCqG .4s ease-out 1 forwards; }
```

### motion-button-state-change-transform-200-ease-in-out

```css
.styles_closeButton__Uf1Ht { transition: transform .2s ease-in-out; }
```

### motion-component-state-change-transform-200-ease-in-out

```css
.trace-popup-close { transition: transform .2s ease-in-out; }
```

### motion-component-load-animation-3000-cubic-bezier-0-2-8-1

```css
.active-marker-ring-large { animation: ripple 3s cubic-bezier(0,.2,.8,1) infinite; }
```

### motion-component-load-animation-2000-cubic-bezier-0-2-8-1

```css
.active-marker-ring-small { animation: ripple 2s cubic-bezier(0,.2,.8,1) infinite; }
```

### motion-component-state-change-bottom-300-ease-out

```css
.overlay { transition: bottom .3s ease-out; }
```

### motion-card-load-animation-500-ease-in-out

```css
.asset-item-meta { animation: fadeIn .5s ease-in-out; }
```

### motion-button-state-change-opacity-200-linear

```css
.style_layerButton__Bxw_0 .style_image__d24ro:before { transition: opacity .2s linear; }
```

### motion-button-load-animation-2000-linear

```css
.mapboxgl-ctrl button.mapboxgl-ctrl-geolocate.mapboxgl-ctrl-geolocate-waiting .mapboxgl-ctrl-icon { animation: mapboxgl-spin 2s linear infinite; }
```

### motion-component-state-change-opacity-750-ease-in-out

```css
.mapboxgl-scroll-zoom-blocker { transition: opacity .75s ease-in-out; }
```

### motion-component-state-change-opacity-750-ease-in-out

```css
.mapboxgl-touch-pan-blocker { transition: opacity .75s ease-in-out; }
```

### motion-component-state-change-opacity-100-ease-in-out

```css
.mapboxgl-scroll-zoom-blocker-show { transition: opacity .1s ease-in-out; }
```

### motion-component-state-change-opacity-100-ease-in-out

```css
.mapboxgl-touch-pan-blocker-show { transition: opacity .1s ease-in-out; }
```

### motion-button-state-change-margin-300-ease-out

```css
.styles_menuButton__BpaTo .styles_menuStroke__F4hO0 { transition: margin .3s ease-out; }
```

### motion-card-state-change-transform-300-ease-in-out

```css
.styles_menuItem__tz491:before { transition: transform .3s ease-in-out; }
```

### motion-button-hover-backgroundcolor-200-ease

```css
{"backgroundColor": "rgb(153, 153, 153)"}
```

### motion-button-focus-backgroundcolor-200-ease

```css
{"backgroundColor": "rgb(153, 153, 153)"}
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
