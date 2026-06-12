# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| component | load | animation | 1000ms | 0ms | linear | 组件load：animation rotate(0deg) -> rotate(360deg)，1000ms linear，load 触发 |
| component | load | animation | 2000ms | 0ms | linear | 组件load：animation rotate(0) -> rotate(359deg)，2000ms linear，load 触发 |
| component | load | animation | 1000ms | 0ms | steps(8) | 组件load：animation rotate(0) -> rotate(359deg)，1000ms steps(8)，load 触发 |
| component | state-change | opacity | 400ms | 0ms | ease | 组件state-change：opacity，400ms ease，state-change 触发 |
| component | state-change | visibility | 400ms | 0ms | ease | 组件state-change：visibility，400ms ease，state-change 触发 |
| reveal | viewport | opacity | 2000ms | 0ms | ease-in-out | 入场元素viewport：opacity，2000ms ease-in-out，viewport 触发 |
| component | state-change | transform | 1000ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：transform missing -> translateY(100%)，1000ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | opacity | 1350ms | 0ms | ease | 组件state-change：opacity，1350ms ease，state-change 触发 |
| component | state-change | visibility | 1350ms | 0ms | ease | 组件state-change：visibility，1350ms ease，state-change 触发 |
| component | load | animation | 1000ms | 0ms | ease-in-out | 组件load：animation scale(0) -> scale(1)，1000ms ease-in-out，load 触发 |
| component | state-change | all | 350ms | 1350ms | ease | 组件state-change：all，350ms ease，state-change 触发 |
| component | state-change | transform | 700ms | 0ms | cubic-bezier(.55,.09,.68,.53) | 组件state-change：transform missing -> translate(-50%,-50%)，700ms cubic-bezier(.55,.09,.68,.53)，state-change 触发 |
| component | state-change | opacity | 700ms | 0ms | cubic-bezier(.55,.09,.68,.53) | 组件state-change：opacity missing -> translate(-50%,-50%)，700ms cubic-bezier(.55,.09,.68,.53)，state-change 触发 |
| component | state-change | visibility | 700ms | 0ms | cubic-bezier(.55,.09,.68,.53) | 组件state-change：visibility missing -> translate(-50%,-50%)，700ms cubic-bezier(.55,.09,.68,.53)，state-change 触发 |
| component | load | animation | 1000ms | 0ms | ease-out | 组件load：animation translateY(-5px) -> translateY(15px)，1000ms ease-out，load 触发 |
| navigation | state-change | transform | 400ms | 0ms | ease | 导航state-change：transform missing -> translateY(-100%)，400ms ease，state-change 触发 |
| navigation | state-change | opacity | 400ms | 0ms | ease | 导航state-change：opacity missing -> translateY(-100%)，400ms ease，state-change 触发 |
| navigation | state-change | visibility | 400ms | 0ms | ease | 导航state-change：visibility missing -> translateY(-100%)，400ms ease，state-change 触发 |
| navigation | state-change | background | 250ms | 0ms | ease | 导航state-change：background，250ms ease，state-change 触发 |
| button | state-change | all | 250ms | 0ms | ease | 按钮state-change：all，250ms ease，state-change 触发 |
| button | state-change | transform | 0ms | 200ms | ease | 按钮state-change：transform，0ms ease，state-change 触发 |
| button | state-change | transform | 0ms | 200ms | ease | 按钮state-change：transform，0ms ease，state-change 触发 |
| button | state-change | top | 200ms | 200ms | ease | 按钮state-change：top，200ms ease，state-change 触发 |
| button | state-change | transform | 200ms | 0ms | ease | 按钮state-change：transform，200ms ease，state-change 触发 |
| button | state-change | top | 200ms | 200ms | ease | 按钮state-change：top，200ms ease，state-change 触发 |
| button | state-change | transform | 200ms | 0ms | ease | 按钮state-change：transform，200ms ease，state-change 触发 |
| button | state-change | top | 200ms | 200ms | ease | 按钮state-change：top，200ms ease，state-change 触发 |
| button | state-change | transform | 200ms | 0ms | ease | 按钮state-change：transform，200ms ease，state-change 触发 |
| button | state-change | top | 200ms | 200ms | ease | 按钮state-change：top，200ms ease，state-change 触发 |
| button | state-change | transform | 200ms | 0ms | ease | 按钮state-change：transform，200ms ease，state-change 触发 |
| button | state-change | top | 200ms | 0ms | ease | 按钮state-change：top，200ms ease，state-change 触发 |
| button | state-change | transform | 200ms | 200ms | ease | 按钮state-change：transform，200ms ease，state-change 触发 |
| button | state-change | top | 200ms | 0ms | ease | 按钮state-change：top，200ms ease，state-change 触发 |
| button | state-change | transform | 200ms | 200ms | ease | 按钮state-change：transform，200ms ease，state-change 触发 |
| button | state-change | top | 200ms | 0ms | ease | 按钮state-change：top，200ms ease，state-change 触发 |
| button | state-change | transform | 200ms | 200ms | ease | 按钮state-change：transform，200ms ease，state-change 触发 |
| button | state-change | top | 200ms | 0ms | ease | 按钮state-change：top，200ms ease，state-change 触发 |
| button | state-change | transform | 200ms | 200ms | ease | 按钮state-change：transform，200ms ease，state-change 触发 |
| button | state-change | opacity | 800ms | 0ms | ease-in-out | 按钮state-change：opacity，800ms ease-in-out，state-change 触发 |
| navigation | state-change | transform | 500ms | 0ms | cubic-bezier(.4,0,.2,1) | 导航state-change：transform missing -> translate3d(100%,0,0)，500ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| navigation | state-change | all | 400ms | 0ms | ease-out | 导航state-change：all missing -> translateY(-50%)，400ms ease-out，state-change 触发 |
| navigation | state-change | all | 300ms | 0ms | ease | 导航state-change：all missing -> translateY(-50%)，300ms ease，state-change 触发 |
| navigation | state-change | all | 400ms | 0ms | ease-in | 导航state-change：all，400ms ease-in，state-change 触发 |
| component | state-change | all | 200ms | 0ms | ease-in | 组件state-change：all missing -> rotate(45deg)，200ms ease-in，state-change 触发 |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: assets/2026-06-12-pagani-official-motion.json

## Missing Evidence
- motion-component-state-change-none-important-missing-missing lacks duration_ms
- motion-component-state-change-none-important-missing-missing lacks easing
- motion-component-load-animation-1000-missing lacks easing
- motion-component-load-animation-1000-missing lacks easing
- motion-component-state-change-all-missing-missing lacks duration_ms
- motion-component-state-change-all-missing-missing lacks easing
- motion-component-state-change-all-missing-cubic-bezier-46-03-52-96 lacks duration_ms

## Snippet Appendix
### motion-component-load-animation-1000-linear

```css
.wpcf7-spinner::before { animation: spin 1000ms linear 0ms; }
```

### motion-component-load-animation-2000-linear

```css
.fa-spin { animation: fa-spin 2s infinite linear; }
```

### motion-component-load-animation-1000-steps-8

```css
.fa-pulse { animation: fa-spin 1s infinite steps(8); }
```

### motion-component-state-change-opacity-400-ease

```css
.content:after { transition: opacity .4s ease 0s; }
```

### motion-component-state-change-visibility-400-ease

```css
.content:after { transition: visibility .4s ease 0s; }
```

### motion-reveal-viewport-opacity-2000-ease-in-out

```css
.js-reveal-content--hidden { transition: opacity 2s ease-in-out; }
```

### motion-component-state-change-transform-1000-cubic-bezier-4-0-2-1

```css
.block { transition: transform 1s cubic-bezier(.4,0,.2,1) 0s; }
```

### motion-component-state-change-opacity-1350-ease

```css
.block:not(.block--children):after { transition: opacity 1.35s ease 0s; }
```

### motion-component-state-change-visibility-1350-ease

```css
.block:not(.block--children):after { transition: visibility 1.35s ease 0s; }
```

### motion-component-load-animation-1000-ease-in-out

```css
.block--loading:before { animation: spinner 1s ease-in-out infinite; }
```

### motion-component-state-change-all-350-ease

```css
.block__close { transition: all .35s ease 1.35s; }
```

### motion-component-state-change-transform-700-cubic-bezier-55-09-68-53

```css
.block__background { transition: transform .7s cubic-bezier(.55,.09,.68,.53) 0s; }
```

### motion-component-state-change-opacity-700-cubic-bezier-55-09-68-53

```css
.block__background { transition: opacity .7s cubic-bezier(.55,.09,.68,.53) 0s; }
```

### motion-component-state-change-visibility-700-cubic-bezier-55-09-68-53

```css
.block__background { transition: visibility .7s cubic-bezier(.55,.09,.68,.53) 0s; }
```

### motion-component-load-animation-1000-ease-out

```css
.scroll-invitation__svg-line { animation: moveLineDown 1s ease-out; }
```

### motion-navigation-state-change-transform-400-ease

```css
.header { transition: transform .4s ease 0s; }
```

### motion-navigation-state-change-opacity-400-ease

```css
.header { transition: opacity .4s ease 0s; }
```

### motion-navigation-state-change-visibility-400-ease

```css
.header { transition: visibility .4s ease 0s; }
```

### motion-navigation-state-change-background-250-ease

```css
.header__logo { transition: background .25s ease 0s; }
```

### motion-button-state-change-all-250-ease

```css
.button { transition: all .25s ease 0s; }
```

### motion-button-state-change-transform-0-ease

```css
.button--hamburger .hamburger-fixed>span { transition: transform 0s ease .2s; }
```

### motion-button-state-change-transform-0-ease

```css
.button--hamburger .hamburger>span { transition: transform 0s ease .2s; }
```

### motion-button-state-change-top-200-ease

```css
.button--hamburger .hamburger-fixed:after { transition: top .2s ease .2s; }
```

### motion-button-state-change-transform-200-ease

```css
.button--hamburger .hamburger-fixed:after { transition: transform .2s ease 0s; }
```

### motion-button-state-change-top-200-ease

```css
.button--hamburger .hamburger-fixed:before { transition: top .2s ease .2s; }
```

### motion-button-state-change-transform-200-ease

```css
.button--hamburger .hamburger-fixed:before { transition: transform .2s ease 0s; }
```

### motion-button-state-change-top-200-ease

```css
.button--hamburger .hamburger:after { transition: top .2s ease .2s; }
```

### motion-button-state-change-transform-200-ease

```css
.button--hamburger .hamburger:after { transition: transform .2s ease 0s; }
```

### motion-button-state-change-top-200-ease

```css
.button--hamburger .hamburger:before { transition: top .2s ease .2s; }
```

### motion-button-state-change-transform-200-ease

```css
.button--hamburger .hamburger:before { transition: transform .2s ease 0s; }
```

### motion-button-state-change-top-200-ease

```css
.button--hamburger .hamburger-fixed.open:after { transition: top .2s ease 0s; }
```

### motion-button-state-change-transform-200-ease

```css
.button--hamburger .hamburger-fixed.open:after { transition: transform .2s ease .2s; }
```

### motion-button-state-change-top-200-ease

```css
.button--hamburger .hamburger-fixed.open:before { transition: top .2s ease 0s; }
```

### motion-button-state-change-transform-200-ease

```css
.button--hamburger .hamburger-fixed.open:before { transition: transform .2s ease .2s; }
```

### motion-button-state-change-top-200-ease

```css
.button--hamburger .hamburger.open:after { transition: top .2s ease 0s; }
```

### motion-button-state-change-transform-200-ease

```css
.button--hamburger .hamburger.open:after { transition: transform .2s ease .2s; }
```

### motion-button-state-change-top-200-ease

```css
.button--hamburger .hamburger.open:before { transition: top .2s ease 0s; }
```

### motion-button-state-change-transform-200-ease

```css
.button--hamburger .hamburger.open:before { transition: transform .2s ease .2s; }
```

### motion-button-state-change-opacity-800-ease-in-out

```css
.button--share { transition: opacity .8s ease-in-out; }
```

### motion-navigation-state-change-transform-500-cubic-bezier-4-0-2-1

```css
.menu { transition: transform .5s cubic-bezier(.4,0,.2,1) 0s; }
```

### motion-navigation-state-change-all-400-ease-out

```css
.menu__main .menu__list { transition: .4s ease-out; }
```

### motion-navigation-state-change-all-300-ease

```css
.menu__main .menu__list .menu__link .sub-menu { transition: .3s ease; }
```

### motion-navigation-state-change-all-400-ease-in

```css
.menu__main.slide-sub .menu__list { transition: .4s ease-in; }
```

### motion-component-state-change-all-200-ease-in

```css
body.page-template-job-positions .job_role_container .mobile_selected_filter i.arrow_filer { transition: .2s transform ease-in; }
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
