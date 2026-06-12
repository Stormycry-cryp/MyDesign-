# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| card | state-change | transform | 250ms | 0ms | ease-out | 卡片state-change：transform，250ms ease-out，state-change 触发 |
| card | state-change | box-shadow | 250ms | 0ms | ease-out | 卡片state-change：box-shadow，250ms ease-out，state-change 触发 |
| card | state-change | transform | 250ms | 0ms | ease-out | 卡片state-change：transform，250ms ease-out，state-change 触发 |
| card | state-change | box-shadow | 250ms | 0ms | ease-out | 卡片state-change：box-shadow，250ms ease-out，state-change 触发 |
| card | state-change | transform | 250ms | 0ms | ease-out | 卡片state-change：transform，250ms ease-out，state-change 触发 |
| card | state-change | box-shadow | 250ms | 0ms | ease-out | 卡片state-change：box-shadow，250ms ease-out，state-change 触发 |
| card | state-change | transform | 250ms | 0ms | ease-out | 卡片state-change：transform，250ms ease-out，state-change 触发 |
| card | state-change | box-shadow | 250ms | 0ms | ease-out | 卡片state-change：box-shadow，250ms ease-out，state-change 触发 |
| card | state-change | transform | 250ms | 0ms | ease-out | 卡片state-change：transform，250ms ease-out，state-change 触发 |
| card | state-change | box-shadow | 250ms | 0ms | ease-out | 卡片state-change：box-shadow，250ms ease-out，state-change 触发 |
| button | state-change | opacity | 300ms | 0ms | ease | 按钮state-change：opacity，300ms ease，state-change 触发 |
| component | state-change | opacity | 300ms | 0ms | ease | 组件state-change：opacity，300ms ease，state-change 触发 |
| component | state-change | background | 100ms | 0ms | linear | 组件state-change：background，100ms linear，state-change 触发 |
| button | state-change | background | 200ms | 0ms | ease-in-out | 按钮state-change：background，200ms ease-in-out，state-change 触发 |
| component | state-change | opacity | 500ms | 0ms | ease-in-out | 组件state-change：opacity，500ms ease-in-out，state-change 触发 |
| component | load | animation | 1000ms | 0ms | linear | 组件load：animation rotate(360deg) -> rotate(360deg)，1000ms linear，load 触发 |
| component | load | animation | 2000ms | 0ms | linear | 组件load：animation rotate(0deg) -> rotate(359deg)，2000ms linear，load 触发 |
| navigation | hover | style | 125ms | 0ms | ease-in-out | 导航hover：style，125ms ease-in-out，hover 触发；样本 GUILD SHOP |
| navigation | focus | style | 125ms | 0ms | ease-in-out | 导航focus：style，125ms ease-in-out，focus 触发；样本 GUILD SHOP |
| navigation | hover | color | 125ms | 0ms | ease-in-out | 导航hover：color missing -> rgba(0, 0, 0, 1)，125ms ease-in-out，hover 触发；样本 BUILDINGS AND INTERIORS |
| navigation | focus | color | 125ms | 0ms | ease-in-out | 导航focus：color missing -> rgb(0, 0, 0)，125ms ease-in-out，focus 触发；样本 BUILDINGS AND INTERIORS |
| navigation | hover | color | 125ms | 0ms | ease-in-out | 导航hover：color missing -> rgb(0, 0, 0)，125ms ease-in-out，hover 触发；样本 RESTAURANTS |
| navigation | focus | color | 125ms | 0ms | ease-in-out | 导航focus：color missing -> rgb(0, 0, 0)，125ms ease-in-out，focus 触发；样本 RESTAURANTS |
| navigation | hover | color | 125ms | 0ms | ease-in-out | 导航hover：color missing -> rgba(0, 0, 0, 0.996)，125ms ease-in-out，hover 触发；样本 WORLD OF RW |
| navigation | focus | color | 125ms | 0ms | ease-in-out | 导航focus：color missing -> rgb(0, 0, 0)，125ms ease-in-out，focus 触发；样本 WORLD OF RW |
| button | hover | style | 125ms | 0ms | ease-in-out | 按钮hover：style，125ms ease-in-out，hover 触发；样本 ds-button-2 |
| button | focus | style | 125ms | 0ms | ease-in-out | 按钮focus：style，125ms ease-in-out，focus 触发；样本 ds-button-2 |
| button | hover | color | 125ms | 0ms | ease-in-out, ease-in-out | 按钮hover：color missing -> rgb(0, 0, 0)，125ms ease-in-out, ease-in-out，hover 触发；样本 LIGHTING |
| button | focus | color | 125ms | 0ms | ease-in-out, ease-in-out | 按钮focus：color missing -> rgb(0, 0, 0)，125ms ease-in-out, ease-in-out，focus 触发；样本 LIGHTING |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: assets/2026-06-11-roman-and-williams-motion.json

## Missing Evidence
- motion-component-state-change-text-decoration-color-missing-missing lacks duration_ms
- motion-component-state-change-text-decoration-color-missing-missing lacks easing
- motion-component-state-change-color-missing-missing lacks duration_ms
- motion-component-state-change-color-missing-missing lacks easing
- motion-component-load-animation-150-missing lacks easing
- motion-card-state-change-opacity-missing-missing lacks duration_ms
- motion-card-state-change-opacity-missing-missing lacks easing
- motion-card-state-change-transform-missing-missing lacks duration_ms
- motion-card-state-change-transform-missing-missing lacks easing
- motion-overlay-state-change-backdrop-filter-missing-missing lacks duration_ms
- motion-overlay-state-change-backdrop-filter-missing-missing lacks easing
- motion-overlay-load-animation-missing-missing lacks duration_ms
- motion-overlay-load-animation-missing-missing lacks easing
- motion-overlay-load-opacity-missing-missing lacks duration_ms
- motion-overlay-load-opacity-missing-missing lacks easing
- motion-overlay-load-animation-missing-missing lacks duration_ms
- motion-overlay-load-animation-missing-missing lacks easing
- motion-overlay-load-animation-missing-missing lacks duration_ms
- motion-overlay-load-animation-missing-missing lacks easing
- motion-overlay-load-animation-missing-missing lacks duration_ms
- motion-overlay-load-animation-missing-missing lacks easing
- motion-overlay-load-animation-missing-missing lacks duration_ms
- motion-overlay-load-animation-missing-missing lacks easing
- motion-button-state-change-color-missing-missing lacks duration_ms
- motion-button-state-change-color-missing-missing lacks easing
- motion-button-state-change-box-shadow-missing-missing lacks duration_ms
- motion-button-state-change-box-shadow-missing-missing lacks easing
- motion-button-state-change-background-color-missing-missing lacks duration_ms
- motion-button-state-change-background-color-missing-missing lacks easing
- motion-button-state-change-color-missing-missing lacks duration_ms
- motion-button-state-change-color-missing-missing lacks easing
- motion-button-state-change-box-shadow-missing-missing lacks duration_ms
- motion-button-state-change-box-shadow-missing-missing lacks easing
- motion-button-state-change-background-color-missing-missing lacks duration_ms
- motion-button-state-change-background-color-missing-missing lacks easing
- motion-button-state-change-color-missing-missing lacks duration_ms
- motion-button-state-change-color-missing-missing lacks easing
- motion-button-state-change-box-shadow-missing-missing lacks duration_ms
- motion-button-state-change-box-shadow-missing-missing lacks easing
- motion-button-state-change-background-color-missing-missing lacks duration_ms
- motion-button-state-change-background-color-missing-missing lacks easing
- motion-button-state-change-color-missing-missing lacks duration_ms
- motion-button-state-change-color-missing-missing lacks easing
- motion-button-state-change-box-shadow-missing-missing lacks duration_ms
- motion-button-state-change-box-shadow-missing-missing lacks easing
- motion-button-state-change-background-color-missing-missing lacks duration_ms
- motion-button-state-change-background-color-missing-missing lacks easing
- motion-component-state-change-transform-missing-missing lacks duration_ms
- motion-component-state-change-transform-missing-missing lacks easing
- motion-component-state-change-transform-missing-missing lacks duration_ms
- motion-component-state-change-transform-missing-missing lacks easing
- motion-component-state-change-transform-missing-missing lacks duration_ms
- motion-component-state-change-transform-missing-missing lacks easing
- motion-button-state-change-transform-missing-missing lacks duration_ms
- motion-button-state-change-transform-missing-missing lacks easing
- motion-overlay-state-change-opacity-missing-missing lacks duration_ms
- motion-overlay-state-change-opacity-missing-missing lacks easing
- motion-button-load-animation-missing-missing lacks duration_ms
- motion-button-load-animation-missing-missing lacks easing
- motion-overlay-load-animation-missing-missing lacks duration_ms
- motion-overlay-load-animation-missing-missing lacks easing
- motion-overlay-load-animation-missing-missing lacks duration_ms
- motion-overlay-load-animation-missing-missing lacks easing
- motion-overlay-state-change-transform-missing-missing lacks duration_ms
- motion-overlay-state-change-transform-missing-missing lacks easing
- motion-component-state-change-opacity-missing-missing lacks duration_ms
- motion-component-state-change-opacity-missing-missing lacks easing
- motion-overlay-state-change-transform-missing-missing lacks duration_ms
- motion-overlay-state-change-transform-missing-missing lacks easing
- motion-component-state-change-box-shadow-missing-ease lacks duration_ms
- motion-overlay-viewport-animation-1000-missing lacks easing

## Snippet Appendix
### motion-card-state-change-transform-250-ease-out

```css
.product-card { transition: transform .25s ease-out; }
```

### motion-card-state-change-box-shadow-250-ease-out

```css
.product-card { transition: box-shadow .25s ease-out; }
```

### motion-card-state-change-transform-250-ease-out

```css
.collection-card { transition: transform .25s ease-out; }
```

### motion-card-state-change-box-shadow-250-ease-out

```css
.collection-card { transition: box-shadow .25s ease-out; }
```

### motion-card-state-change-transform-250-ease-out

```css
.resource-card { transition: transform .25s ease-out; }
```

### motion-card-state-change-box-shadow-250-ease-out

```css
.resource-card { transition: box-shadow .25s ease-out; }
```

### motion-card-state-change-transform-250-ease-out

```css
.predictive-search-results__card--product { transition: transform .25s ease-out; }
```

### motion-card-state-change-box-shadow-250-ease-out

```css
.predictive-search-results__card--product { transition: box-shadow .25s ease-out; }
```

### motion-card-state-change-transform-250-ease-out

```css
.predictive-search-results__card { transition: transform .25s ease-out; }
```

### motion-card-state-change-box-shadow-250-ease-out

```css
.predictive-search-results__card { transition: box-shadow .25s ease-out; }
```

### motion-button-state-change-opacity-300-ease

```css
.deferred-media__poster-button.deferred-media__playing { transition: opacity .3s ease; }
```

### motion-component-state-change-opacity-300-ease

```css
deferred-media img { transition: opacity .3s ease; }
```

### motion-component-state-change-background-100-linear

```css
slideshow-progress[type=full] { transition: background .1s linear; }
```

### motion-button-state-change-background-200-ease-in-out

```css
.shopify-payment-button__button { transition: background .2s ease-in-out; }
```

### motion-component-state-change-opacity-500-ease-in-out

```css
.announcement-bar__slide { transition: opacity .5s ease-in-out; }
```

### motion-component-load-animation-1000-linear

```css
.klaviyo-form.klaviyo-form.klaviyo-form .klaviyo-spinner:after { animation: klaviyo-spinner 1s linear infinite; }
```

### motion-component-load-animation-2000-linear

```css
.fa-spin { animation: fa-spin 2s infinite linear; }
```

### motion-navigation-hover-style-125-ease-in-out

```css
{"columnGap": "2.5px", "gap": "2.5px", "rowGap": "2.5px"}
```

### motion-navigation-focus-style-125-ease-in-out

```css
{"columnGap": "2.5px", "gap": "2.5px", "rowGap": "2.5px"}
```

### motion-navigation-hover-color-125-ease-in-out

```css
{"border": "0px none rgba(0, 0, 0, 1)", "borderBottom": "0px none rgba(0, 0, 0, 1)", "borderLeft": "0px none rgba(0, 0, 0, 1)", "borderRight": "0px none rgba(0, 0, 0, 1)", "borderTop": "0px none rgba(0, 0, 0, 1)", "color": "rgba(0, 0, 0, 1)", "columnGap": "2.5px", "gap": "2.5px", "rowGap": "2.5px"}
```

### motion-navigation-focus-color-125-ease-in-out

```css
{"border": "0px none rgb(0, 0, 0)", "borderBottom": "0px none rgb(0, 0, 0)", "borderLeft": "0px none rgb(0, 0, 0)", "borderRight": "0px none rgb(0, 0, 0)", "borderTop": "0px none rgb(0, 0, 0)", "color": "rgb(0, 0, 0)", "columnGap": "2.5px", "gap": "2.5px", "rowGap": "2.5px"}
```

### motion-navigation-hover-color-125-ease-in-out

```css
{"border": "0px none rgb(0, 0, 0)", "borderBottom": "0px none rgb(0, 0, 0)", "borderLeft": "0px none rgb(0, 0, 0)", "borderRight": "0px none rgb(0, 0, 0)", "borderTop": "0px none rgb(0, 0, 0)", "color": "rgb(0, 0, 0)", "columnGap": "2.5px", "gap": "2.5px", "rowGap": "2.5px"}
```

### motion-navigation-focus-color-125-ease-in-out

```css
{"border": "0px none rgb(0, 0, 0)", "borderBottom": "0px none rgb(0, 0, 0)", "borderLeft": "0px none rgb(0, 0, 0)", "borderRight": "0px none rgb(0, 0, 0)", "borderTop": "0px none rgb(0, 0, 0)", "color": "rgb(0, 0, 0)", "columnGap": "2.5px", "gap": "2.5px", "rowGap": "2.5px"}
```

### motion-navigation-hover-color-125-ease-in-out

```css
{"border": "0px none rgba(0, 0, 0, 0.996)", "borderBottom": "0px none rgba(0, 0, 0, 0.996)", "borderLeft": "0px none rgba(0, 0, 0, 0.996)", "borderRight": "0px none rgba(0, 0, 0, 0.996)", "borderTop": "0px none rgba(0, 0, 0, 0.996)", "color": "rgba(0, 0, 0, 0.996)", "columnGap": "2.5px", "gap": "2.5px", "rowGap": "2.5px"}
```

### motion-navigation-focus-color-125-ease-in-out

```css
{"border": "0px none rgb(0, 0, 0)", "borderBottom": "0px none rgb(0, 0, 0)", "borderLeft": "0px none rgb(0, 0, 0)", "borderRight": "0px none rgb(0, 0, 0)", "borderTop": "0px none rgb(0, 0, 0)", "color": "rgb(0, 0, 0)", "columnGap": "2.5px", "gap": "2.5px", "rowGap": "2.5px"}
```

### motion-button-hover-style-125-ease-in-out

```css
{"transition": "color 0.125s ease-in-out"}
```

### motion-button-focus-style-125-ease-in-out

```css
{"transition": "color 0.125s ease-in-out"}
```

### motion-button-hover-color-125-ease-in-out-ease-in-out

```css
{"borderLeft": "0px none rgb(0, 0, 0)", "borderRight": "0px none rgb(0, 0, 0)", "borderTop": "0px none rgb(0, 0, 0)", "color": "rgb(0, 0, 0)"}
```

### motion-button-focus-color-125-ease-in-out-ease-in-out

```css
{"borderLeft": "0px none rgb(0, 0, 0)", "borderRight": "0px none rgb(0, 0, 0)", "borderTop": "0px none rgb(0, 0, 0)", "color": "rgb(0, 0, 0)"}
```

## Do Not Copy
- Do not copy the exact Roman and Williams voice, wordmark treatment, or luxury-craft phrasing.
- Do not copy the street-sign hero motif or the brand’s historical romance framing verbatim.
- Do not overstate motion or component detail that was not directly captured.
