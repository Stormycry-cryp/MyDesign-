# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| component | load | animation | 1000ms | 0ms | linear | 组件load：animation rotate(0) -> rotate(360deg)，1000ms linear，load 触发 |
| component | load | animation | 1000ms | 0ms | linear | 组件load：animation rotate(0) -> rotate(360deg)，1000ms linear，load 触发 |
| component | load | animation | 1000ms | 0ms | steps(12) | 组件load：animation rotate(1turn) -> rotate(1turn)，1000ms steps(12)，load 触发 |
| component | state-change | transform | 600ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：transform，600ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | opacity | 700ms | 500ms | cubic-bezier(.4,0,.2,1) | 组件state-change：opacity，700ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | opacity | 1000ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：opacity，1000ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | opacity | 300ms | 0ms | cubic-bezier(.19,1,.22,1) | 组件state-change：opacity，300ms cubic-bezier(.19,1,.22,1)，state-change 触发 |
| component | state-change | all | 1000ms | 300ms | cubic-bezier(.215,.61,.355,1) | 组件state-change：all，1000ms cubic-bezier(.215,.61,.355,1)，state-change 触发 |
| component | state-change | opacity | 600ms | 0ms | cubic-bezier(.19,1,.22,1) | 组件state-change：opacity，600ms cubic-bezier(.19,1,.22,1)，state-change 触发 |
| component | state-change | padding-bottom | 1000ms | 0ms | cubic-bezier(.19,1,.22,1) | 组件state-change：padding-bottom，1000ms cubic-bezier(.19,1,.22,1)，state-change 触发 |
| component | state-change | box-shadow | 300ms | 0ms | ease | 组件state-change：box-shadow，300ms ease，state-change 触发 |
| component | load | transform | 400ms | 0ms | ease-in-out | 组件load：transform，400ms ease-in-out，load 触发 |
| component | load | animation | 300ms | 0ms | ease | 组件load：animation 0 -> 1，300ms ease，load 触发 |
| component | state-change | all | 100ms | 0ms | ease-in-out | 组件state-change：all，100ms ease-in-out，state-change 触发 |
| navigation | state-change | transform | 300ms | 0ms | ease | 导航state-change：transform，300ms ease，state-change 触发 |
| navigation | load | animation | 200ms | 0ms | ease | 导航load：animation translateY(10px) -> translateY(0)，200ms ease，load 触发 |
| navigation | state-change | height | 350ms | 0ms | cubic-bezier(.4,0,.2,1) | 导航state-change：height，350ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| navigation | state-change | width | 350ms | 0ms | cubic-bezier(.4,0,.2,1) | 导航state-change：width，350ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| card | state-change | all | 300ms | 0ms | ease | 卡片state-change：all，300ms ease，state-change 触发 |
| card | state-change | transform | 300ms | 0ms | ease | 卡片state-change：transform missing -> translateY(-50%) scale(0)，300ms ease，state-change 触发 |
| card | state-change | opacity | 300ms | 0ms | ease | 卡片state-change：opacity missing -> translateY(-50%) scale(0)，300ms ease，state-change 触发 |
| component | state-change | box-shadow | 300ms | 0ms | ease | 组件state-change：box-shadow，300ms ease，state-change 触发 |
| component | state-change | box-shadow | 300ms | 0ms | ease | 组件state-change：box-shadow，300ms ease，state-change 触发 |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: assets/2026-06-11-wam-architecture-studio-motion.json

## Missing Evidence
- motion-component-state-change-transform-missing-missing lacks duration_ms
- motion-component-state-change-transform-missing-missing lacks easing
- motion-component-state-change-transform-missing-missing lacks duration_ms
- motion-component-state-change-transform-missing-missing lacks easing
- motion-component-state-change-transform-missing-missing lacks duration_ms
- motion-component-state-change-transform-missing-missing lacks easing
- motion-component-state-change-height-missing-missing lacks duration_ms
- motion-component-state-change-height-missing-missing lacks easing
- motion-component-state-change-filter-1000-missing lacks easing
- motion-component-state-change-opacity-1000-missing lacks easing
- motion-component-state-change-transform-1000-missing lacks easing
- motion-component-state-change-opacity-1000-missing lacks easing
- motion-component-state-change-filter-1000-missing lacks easing
- motion-component-state-change-opacity-1000-missing lacks easing
- motion-component-state-change-transform-1000-missing lacks easing
- motion-component-state-change-opacity-1000-missing lacks easing
- motion-navigation-state-change-all-200-missing lacks easing
- motion-component-state-change-height-600-missing lacks easing
- motion-component-state-change-opacity-600-missing lacks easing
- motion-card-state-change-filter-1000-missing lacks easing
- motion-card-state-change-opacity-1000-missing lacks easing
- motion-component-state-change-opacity-200-missing lacks easing
- motion-component-state-change-visibility-1-missing lacks easing
- motion-component-state-change-height-200-missing lacks easing
- motion-component-state-change-height-700-missing lacks easing
- motion-component-state-change-opacity-1000-missing lacks easing
- motion-component-state-change-height-700-missing lacks easing
- motion-component-state-change-opacity-400-missing lacks easing
- motion-component-state-change-opacity-400-missing lacks easing

## Snippet Appendix
### motion-component-load-animation-1000-linear

```css
.swiper:not(.swiper-watch-progress) .swiper-lazy-preloader { animation: swiper-preloader-spin 1s infinite linear; }
```

### motion-component-load-animation-1000-linear

```css
.swiper-watch-progress .swiper-slide-visible .swiper-lazy-preloader { animation: swiper-preloader-spin 1s infinite linear; }
```

### motion-component-load-animation-1000-steps-12

```css
.loader { animation: l23 1s infinite steps(12); }
```

### motion-component-state-change-transform-600-cubic-bezier-4-0-2-1

```css
.burger>div { transition-property: transform; transition-duration: .6s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-opacity-700-cubic-bezier-4-0-2-1

```css
.curtain { transition-property: opacity; transition-duration: .7s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-opacity-1000-cubic-bezier-4-0-2-1

```css
.slider--fader .keen-slider__slide { transition-property: opacity; transition-duration: 1s; transition-timing-function: cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-opacity-300-cubic-bezier-19-1-22-1

```css
.block-image-text.text-carousel .paragraph:not(.is-active) { transition-property: opacity; transition-duration: .3s; transition-timing-function: cubic-bezier(.19,1,.22,1); }
```

### motion-component-state-change-all-1000-cubic-bezier-215-61-355-1

```css
.block-image-text.text-carousel .paragraph.is-active { transition-property: all; transition-duration: 1s; transition-timing-function: cubic-bezier(.215,.61,.355,1); }
```

### motion-component-state-change-opacity-600-cubic-bezier-19-1-22-1

```css
[data-swiper-news] .swiper-slide { transition-property: opacity; transition-duration: .6s; transition-timing-function: cubic-bezier(.19,1,.22,1); }
```

### motion-component-state-change-padding-bottom-1000-cubic-bezier-19-1-22-1

```css
[data-swiper-news] .swiper-slide .news-image { transition-property: padding-bottom; transition-duration: 1s; transition-timing-function: cubic-bezier(.19,1,.22,1); }
```

### motion-component-state-change-box-shadow-300-ease

```css
.plyr { transition: box-shadow .3s ease; }
```

### motion-component-load-transform-400-ease-in-out

```css
.plyr__captions { transition: transform .4s ease-in-out; }
```

### motion-component-load-animation-300-ease

```css
.plyr__captions { animation: plyr-fade-in .3s ease; }
```

### motion-component-state-change-all-100-ease-in-out

```css
.plyr__control { transition: all .1s ease-in-out; }
```

### motion-navigation-state-change-transform-300-ease

```css
.plyr__menu .plyr__control svg { transition: transform .3s ease; }
```

### motion-navigation-load-animation-200-ease

```css
.plyr__menu__container { animation: plyr-popup .2s ease; }
```

### motion-navigation-state-change-height-350-cubic-bezier-4-0-2-1

```css
.plyr__menu__container>div { transition: height .35s cubic-bezier(.4,0,.2,1); }
```

### motion-navigation-state-change-width-350-cubic-bezier-4-0-2-1

```css
.plyr__menu__container>div { transition: width .35s cubic-bezier(.4,0,.2,1); }
```

### motion-card-state-change-all-300-ease

```css
.plyr__menu__container .plyr__control[role=menuitemradio]:before { transition: all .3s ease; }
```

### motion-card-state-change-transform-300-ease

```css
.plyr__menu__container .plyr__control[role=menuitemradio]:after { transition: transform .3s ease; }
```

### motion-card-state-change-opacity-300-ease

```css
.plyr__menu__container .plyr__control[role=menuitemradio]:after { transition: opacity .3s ease; }
```

### motion-component-state-change-box-shadow-300-ease

```css
.plyr--full-ui input[type=range] { transition: box-shadow .3s ease; }
```

### motion-component-state-change-box-shadow-300-ease

```css
.plyr--full-ui input[type=range]::-webkit-slider-runnable-track { transition: box-shadow .3s ease; }
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
