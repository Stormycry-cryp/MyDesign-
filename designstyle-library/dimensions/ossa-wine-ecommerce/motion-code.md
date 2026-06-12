# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| component | load | animation | 2000ms | 0ms | linear | 组件load：animation rotate(0deg) -> rotate(1turn)，2000ms linear，load 触发 |
| component | load | animation | 1000ms | 0ms | steps(8) | 组件load：animation rotate(0deg) -> rotate(1turn)，1000ms steps(8)，load 触发 |
| button | load | animation | 2000ms | 0ms | linear | 按钮load：animation，2000ms linear，load 触发 |
| component | state-change | all | 200ms | 0ms | ease-in-out | 组件state-change：all，200ms ease-in-out，state-change 触发 |
| button | state-change | color | 250ms | 0ms | ease-in-out | 按钮state-change：color，250ms ease-in-out，state-change 触发 |
| button | state-change | opacity | 250ms | 0ms | ease-in-out | 按钮state-change：opacity，250ms ease-in-out，state-change 触发 |
| navigation | state-change | all | 450ms | 0ms | linear | 导航state-change：all missing -> translateY(-102%)，450ms linear，state-change 触发 |
| navigation | state-change | all | 750ms | 0ms | cubic-bezier(.22,1,.36,1) | 导航state-change：all missing -> translateY(-100vh)，750ms cubic-bezier(.22,1,.36,1)，state-change 触发 |
| navigation | state-change | all | 750ms | 0ms | cubic-bezier(.22,1,.36,1) | 导航state-change：all missing -> translateY(-100%)，750ms cubic-bezier(.22,1,.36,1)，state-change 触发 |
| component | state-change | all | 750ms | 0ms | cubic-bezier(.22,1,.36,1) | 组件state-change：all，750ms cubic-bezier(.22,1,.36,1)，state-change 触发 |
| component | state-change | all | 750ms | 0ms | cubic-bezier(.22,1,.36,1) | 组件state-change：all，750ms cubic-bezier(.22,1,.36,1)，state-change 触发 |
| component | state-change | all | 750ms | 0ms | ease-in-out | 组件state-change：all missing -> translateY(100vh)，750ms ease-in-out，state-change 触发 |
| component | state-change | all | 750ms | 0ms | ease-in-out | 组件state-change：all missing -> translateY(100vh)，750ms ease-in-out，state-change 触发 |
| component | state-change | all | 750ms | 0ms | ease-in-out | 组件state-change：all，750ms ease-in-out，state-change 触发 |
| component | state-change | opacity | 250ms | 0ms | ease-in-out | 组件state-change：opacity，250ms ease-in-out，state-change 触发 |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: assets/2026-06-12-ossa-wine-ecommerce-motion.json

## Missing Evidence
- motion-navigation-state-change-none-important-missing-missing lacks duration_ms
- motion-navigation-state-change-none-important-missing-missing lacks easing
- motion-navigation-state-change-none-important-missing-missing lacks duration_ms
- motion-navigation-state-change-none-important-missing-missing lacks easing
- motion-navigation-state-change-none-important-missing-missing lacks duration_ms
- motion-navigation-state-change-none-important-missing-missing lacks easing
- motion-component-state-change-all-missing-missing lacks duration_ms
- motion-component-state-change-all-missing-missing lacks easing
- motion-component-state-change-all-missing-missing lacks duration_ms
- motion-component-state-change-all-missing-missing lacks easing
- motion-component-state-change-all-missing-missing lacks duration_ms
- motion-component-state-change-all-missing-missing lacks easing

## Snippet Appendix
### motion-component-load-animation-2000-linear

```css
.fa-spin { animation: fa-spin 2s linear infinite; }
```

### motion-component-load-animation-1000-steps-8

```css
.fa-pulse { animation: fa-spin 1s steps(8) infinite; }
```

### motion-button-load-animation-2000-linear

```css
.wc-block-grid__product-add-to-cart.wp-block-button .wp-block-button__link.loading:after { animation: spin 2s linear infinite; }
```

### motion-component-state-change-all-200-ease-in-out

```css
.wc-block-components-notice-banner>.wc-block-components-notice-banner__content .wc-forward { transition: all .2s ease-in-out; }
```

### motion-button-state-change-color-250-ease-in-out

```css
.slick-dots li button::before { transition: color 0.25s ease-in-out; }
```

### motion-button-state-change-opacity-250-ease-in-out

```css
.slick-dots li button::before { transition: opacity 0.25s ease-in-out; }
```

### motion-navigation-state-change-all-450-linear

```css
.menu-drop-holder .menu-drop { transition: all 0.45s linear; }
```

### motion-navigation-state-change-all-750-cubic-bezier-22-1-36-1

```css
.mainNav ul li { transition: all 0.75s cubic-bezier(.22,1,.36,1); }
```

### motion-navigation-state-change-all-750-cubic-bezier-22-1-36-1

```css
#wine-list-menu { transition: all 0.75s cubic-bezier(.22,1,.36,1); }
```

### motion-component-state-change-all-750-cubic-bezier-22-1-36-1

```css
#home-animation .horiz-row { transition: all 0.75s cubic-bezier(.22,1,.36,1); }
```

### motion-component-state-change-all-750-cubic-bezier-22-1-36-1

```css
#home-animation .anim-object { transition: all 0.75s cubic-bezier(.22,1,.36,1); }
```

### motion-component-state-change-all-750-ease-in-out

```css
.home .home-curtain { transition: all 0.75s ease-in-out; }
```

### motion-component-state-change-all-750-ease-in-out

```css
.is-home .home-message { transition: all 0.75s ease-in-out; }
```

### motion-component-state-change-all-750-ease-in-out

```css
#homeBlocks { transition: all 0.75s ease-in-out; }
```

### motion-component-state-change-opacity-250-ease-in-out

```css
.signup-message.signup-close #signup-overlay { transition: opacity 0.25s ease-in-out; }
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
