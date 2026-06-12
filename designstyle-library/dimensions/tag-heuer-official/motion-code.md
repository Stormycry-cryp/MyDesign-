# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| button | state-change | transform | 250ms | 0ms | ease-out | 按钮state-change：transform，250ms ease-out，state-change 触发 |
| button | state-change | transform | 250ms | 0ms | ease-out | 按钮state-change：transform，250ms ease-out，state-change 触发 |
| button | state-change | all | 800ms | 0ms | cubic-bezier(.77,0,.175,1) | 按钮state-change：all，800ms cubic-bezier(.77,0,.175,1)，state-change 触发 |
| button | state-change | all | 800ms | 0ms | cubic-bezier(.77,0,.175,1) | 按钮state-change：all，800ms cubic-bezier(.77,0,.175,1)，state-change 触发 |
| button | state-change | all | 200ms | 0ms | ease-in-out | 按钮state-change：all，200ms ease-in-out，state-change 触发 |
| navigation | state-change | all | 300ms | 0ms | ease-out | 导航state-change：all，300ms ease-out，state-change 触发 |
| navigation | state-change | all | 500ms | 0ms | ease-in-out | 导航state-change：all，500ms ease-in-out，state-change 触发 |
| card | state-change | transform | 450ms | 0ms | ease | 卡片state-change：transform，450ms ease，state-change 触发 |
| card | state-change | background | 450ms | 0ms | ease | 卡片state-change：background，450ms ease，state-change 触发 |
| card | state-change | transform | 450ms | 0ms | ease | 卡片state-change：transform，450ms ease，state-change 触发 |
| card | state-change | background | 450ms | 0ms | ease | 卡片state-change：background，450ms ease，state-change 触发 |
| component | load | animation | 0ms | 0ms | linear | 组件load：animation，0ms linear，load 触发 |
| component | state-change | all | 800ms | 0ms | cubic-bezier(.77,0,.175,1) | 组件state-change：all missing -> rotate(-90deg)，800ms cubic-bezier(.77,0,.175,1)，state-change 触发 |
| component | state-change | all | 800ms | 0ms | cubic-bezier(.77,0,.175,1) | 组件state-change：all missing -> rotate(-90deg)，800ms cubic-bezier(.77,0,.175,1)，state-change 触发 |
| component | state-change | all | 200ms | 0ms | ease-out | 组件state-change：all，200ms ease-out，state-change 触发 |
| component | state-change | all | 500ms | 0ms | ease-in-out | 组件state-change：all，500ms ease-in-out，state-change 触发 |
| component | state-change | all | 300ms | 0ms | ease-in-out | 组件state-change：all，300ms ease-in-out，state-change 触发 |
| navigation | state-change | top | 300ms | 0ms | ease-out | 导航state-change：top，300ms ease-out，state-change 触发 |
| button | state-change | all | 200ms | 0ms | ease-out | 按钮state-change：all，200ms ease-out，state-change 触发 |
| button | state-change | all | 200ms | 0ms | ease-in-out | 按钮state-change：all，200ms ease-in-out，state-change 触发 |
| navigation | state-change | margin | 400ms | 0ms | ease | 导航state-change：margin，400ms ease，state-change 触发 |
| button | state-change | width | 800ms | 0ms | cubic-bezier(.86,0,.07,1) | 按钮state-change：width，800ms cubic-bezier(.86,0,.07,1)，state-change 触发 |
| button | state-change | transform | 300ms | 0ms | cubic-bezier(.175,.885,.32,1.275) | 按钮state-change：transform，300ms cubic-bezier(.175,.885,.32,1.275)，state-change 触发 |
| button | state-change | opacity | 300ms | 0ms | cubic-bezier(.175,.885,.32,1) | 按钮state-change：opacity，300ms cubic-bezier(.175,.885,.32,1)，state-change 触发 |
| overlay | state-change | all | 400ms | 600ms | cubic-bezier(.165,.84,.44,1) | 浮层state-change：all，400ms cubic-bezier(.165,.84,.44,1)，state-change 触发 |
| overlay | state-change | all | 400ms | 700ms | cubic-bezier(.165,.84,.44,1) | 浮层state-change：all，400ms cubic-bezier(.165,.84,.44,1)，state-change 触发 |
| overlay | state-change | all | 400ms | 100ms | cubic-bezier(.895,.03,.685,.22) | 浮层state-change：all，400ms cubic-bezier(.895,.03,.685,.22)，state-change 触发 |
| overlay | state-change | all | 400ms | 0ms | cubic-bezier(.895,.03,.685,.22) | 浮层state-change：all，400ms cubic-bezier(.895,.03,.685,.22)，state-change 触发 |
| overlay | hover | all | 400ms | 0ms | cubic-bezier(.895,.03,.685,.22) | 浮层hover：all，400ms cubic-bezier(.895,.03,.685,.22)，hover 触发 |
| overlay | hover | all | 400ms | 100ms | cubic-bezier(.895,.03,.685,.22) | 浮层hover：all，400ms cubic-bezier(.895,.03,.685,.22)，hover 触发 |
| overlay | hover | all | 400ms | 700ms | cubic-bezier(.165,.84,.44,1) | 浮层hover：all，400ms cubic-bezier(.165,.84,.44,1)，hover 触发 |
| overlay | hover | all | 400ms | 600ms | cubic-bezier(.165,.84,.44,1) | 浮层hover：all，400ms cubic-bezier(.165,.84,.44,1)，hover 触发 |
| component | load | animation | 5000ms | 0ms | linear | 组件load：animation 0 -> 0，5000ms linear，load 触发 |
| component | state-change | color | 200ms | 0ms | ease-out | 组件state-change：color，200ms ease-out，state-change 触发 |
| navigation | state-change | color | 200ms | 0ms | ease-out | 导航state-change：color，200ms ease-out，state-change 触发 |
| navigation | state-change | color | 200ms | 0ms | ease-out | 导航state-change：color，200ms ease-out，state-change 触发 |
| component | state-change | color | 200ms | 0ms | ease-out | 组件state-change：color，200ms ease-out，state-change 触发 |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: assets/2026-06-11-tag-heuer-official-motion.json

## Missing Evidence
- motion-component-state-change-all-1000-missing lacks easing
- motion-component-state-change-opacity-1000-missing lacks easing
- motion-component-load-animation-10-missing lacks easing
- motion-component-load-animation-20000-missing lacks easing
- motion-component-load-animation-10000-missing lacks easing
- motion-hero-state-change-transform-100-missing lacks easing
- motion-component-state-change-all-400-missing lacks easing
- motion-component-state-change-opacity-400-missing lacks easing
- motion-component-state-change-left-100-missing lacks easing
- motion-component-state-change-opacity-400-missing lacks easing
- motion-component-state-change-left-100-missing lacks easing

## Snippet Appendix
### motion-button-state-change-transform-250-ease-out

```css
.page-designer-reference .content-accordion .card .card-header .btn .icon:after { transition: transform .25s ease-out; }
```

### motion-button-state-change-transform-250-ease-out

```css
.page-designer-reference .content-accordion .card .card-header .btn .icon:before { transition: transform .25s ease-out; }
```

### motion-button-state-change-all-800-cubic-bezier-77-0-175-1

```css
.page-designer-reference .btn.scroll-to-cta .icon:after { transition: all .8s cubic-bezier(.77,0,.175,1) 0s; }
```

### motion-button-state-change-all-800-cubic-bezier-77-0-175-1

```css
.page-designer-reference .btn.scroll-to-cta .icon:before { transition: all .8s cubic-bezier(.77,0,.175,1) 0s; }
```

### motion-button-state-change-all-200-ease-in-out

```css
.page-designer-reference #faq-accordion .card .card-header .btn.btn-link:before { transition: all .2s ease-in-out; }
```

### motion-navigation-state-change-all-300-ease-out

```css
.page-designer-reference .bannerwithsubmenu-component-block.sticky-nav .container .nav-links.sticky { transition: all .3s ease-out; }
```

### motion-navigation-state-change-all-500-ease-in-out

```css
.page-designer-reference .bannerwithsubmenu-component-block .swiper .swiper-wrapper .swiper-slide .link { transition: all .5s ease-in-out; }
```

### motion-card-state-change-transform-450-ease

```css
.page-designer-reference .card-block.hover-gradient:after { transition: transform .45s ease; }
```

### motion-card-state-change-background-450-ease

```css
.page-designer-reference .card-block.hover-gradient:after { transition: background .45s ease; }
```

### motion-card-state-change-transform-450-ease

```css
.page-designer-reference .card-block .card-block-bg { transition: transform .45s ease; }
```

### motion-card-state-change-background-450-ease

```css
.page-designer-reference .card-block .card-block-bg { transition: background .45s ease; }
```

### motion-component-load-animation-0-linear

```css
.page-designer-reference .presentation-images .presentation-swiper-thumbs .swiper-wrapper .swiper-slide.current [data-anim~=base] { animation: missing missing linear 0ms; }
```

### motion-component-state-change-all-800-cubic-bezier-77-0-175-1

```css
.page-designer-reference .presentation-images .links .link .icon:after { transition: all .8s cubic-bezier(.77,0,.175,1) 0s; }
```

### motion-component-state-change-all-800-cubic-bezier-77-0-175-1

```css
.page-designer-reference .presentation-images .links .link .icon:before { transition: all .8s cubic-bezier(.77,0,.175,1) 0s; }
```

### motion-component-state-change-all-200-ease-out

```css
.page-designer-reference .pictos-block.sticky { transition: all .2s ease-out; }
```

### motion-component-state-change-all-500-ease-in-out

```css
.page-designer-reference .pictos-block .picto { transition: all .5s ease-in-out; }
```

### motion-component-state-change-all-300-ease-in-out

```css
.page-designer-reference .images-block.images-text-parallax .parallax-parent { transition: all .3s ease-in-out; }
```

### motion-navigation-state-change-top-300-ease-out

```css
.page-designer-reference .experience-assets-watchesSubNav .c-Watches.c-Watches--sm { transition: top .3s ease-out; }
```

### motion-button-state-change-all-200-ease-out

```css
.page-designer-reference .plpcta { transition: all .2s ease-out; }
```

### motion-button-state-change-all-200-ease-in-out

```css
.page-designer-reference .collection-items-wrapper .scroll-to-cta.top-sticky { transition: all .2s ease-in-out; }
```

### motion-navigation-state-change-margin-400-ease

```css
.page-designer-reference .sticky-sub-nav-container { transition: margin .4s ease 0s; }
```

### motion-button-state-change-width-800-cubic-bezier-86-0-07-1

```css
.page-designer-reference .herowithsoldat_images-container-cta { transition: width .8s cubic-bezier(.86,0,.07,1); }
```

### motion-button-state-change-transform-300-cubic-bezier-175-885-32-1-275

```css
.page-designer-reference .herowithsoldat_images-container-cta { transition: transform .3s cubic-bezier(.175,.885,.32,1.275); }
```

### motion-button-state-change-opacity-300-cubic-bezier-175-885-32-1

```css
.page-designer-reference .herowithsoldat_images-container-cta { transition: opacity .3s cubic-bezier(.175,.885,.32,1); }
```

### motion-overlay-state-change-all-400-cubic-bezier-165-84-44-1

```css
.page-designer-reference .modal .close .icon span:first-child:before { transition: all .4s cubic-bezier(.165,.84,.44,1) .6s; }
```

### motion-overlay-state-change-all-400-cubic-bezier-165-84-44-1

```css
.page-designer-reference .modal .close .icon span:first-child:after { transition: all .4s cubic-bezier(.165,.84,.44,1) .7s; }
```

### motion-overlay-state-change-all-400-cubic-bezier-895-03-685-22

```css
.page-designer-reference .modal .close .icon span:last-child:before { transition: all .4s cubic-bezier(.895,.03,.685,.22) .1s; }
```

### motion-overlay-state-change-all-400-cubic-bezier-895-03-685-22

```css
.page-designer-reference .modal .close .icon span:last-child:after { transition: all .4s cubic-bezier(.895,.03,.685,.22) 0s; }
```

### motion-overlay-hover-all-400-cubic-bezier-895-03-685-22

```css
.page-designer-reference .modal .close:hover .icon span:first-child:before { transition: all .4s cubic-bezier(.895,.03,.685,.22) 0s; }
```

### motion-overlay-hover-all-400-cubic-bezier-895-03-685-22

```css
.page-designer-reference .modal .close:hover .icon span:first-child:after { transition: all .4s cubic-bezier(.895,.03,.685,.22) .1s; }
```

### motion-overlay-hover-all-400-cubic-bezier-165-84-44-1

```css
.page-designer-reference .modal .close:hover .icon span:last-child:before { transition: all .4s cubic-bezier(.165,.84,.44,1) .7s; }
```

### motion-overlay-hover-all-400-cubic-bezier-165-84-44-1

```css
.page-designer-reference .modal .close:hover .icon span:last-child:after { transition: all .4s cubic-bezier(.165,.84,.44,1) .6s; }
```

### motion-component-load-animation-5000-linear

```css
.page-designer-reference .add-to-basket-alert { animation: fade 5s linear forwards; }
```

### motion-component-state-change-color-200-ease-out

```css
.ais-Breadcrumb-link { transition: color .2s ease-out; }
```

### motion-navigation-state-change-color-200-ease-out

```css
.ais-HierarchicalMenu-link { transition: color .2s ease-out; }
```

### motion-navigation-state-change-color-200-ease-out

```css
.ais-Menu-link { transition: color .2s ease-out; }
```

### motion-component-state-change-color-200-ease-out

```css
.ais-Pagination-link { transition: color .2s ease-out; }
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
