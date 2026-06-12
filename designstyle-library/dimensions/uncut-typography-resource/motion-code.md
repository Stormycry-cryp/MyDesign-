# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| component | load | animation | 2500ms | 0ms | cubic-bezier(0.455, 0.03, 0.515, 0.955) | 组件load：animation scaleY(1) -> scaleY(1)，2500ms cubic-bezier(0.455, 0.03, 0.515, 0.955)，load 触发 |
| button | state-change | background-color | 200ms | 0ms | cubic-bezier(0.075, 0.82, 0.165, 1) | 按钮state-change：background-color，200ms cubic-bezier(0.075, 0.82, 0.165, 1)，state-change 触发 |
| button | state-change | background-color | 200ms | 0ms | cubic-bezier(0.075, 0.82, 0.165, 1) | 按钮state-change：background-color，200ms cubic-bezier(0.075, 0.82, 0.165, 1)，state-change 触发 |
| component | state-change | background-color | 200ms | 0ms | cubic-bezier(0.075, 0.82, 0.165, 1) | 组件state-change：background-color，200ms cubic-bezier(0.075, 0.82, 0.165, 1)，state-change 触发 |
| component | load | transform | 300ms | 0ms | cubic-bezier(0.785, 0.135, 0.15, 0.86) | 组件load：transform missing -> scale(1) rotate(-15deg)，300ms cubic-bezier(0.785, 0.135, 0.15, 0.86)，load 触发 |
| component | state-change | transform | 300ms | 0ms | cubic-bezier(0.785, 0.135, 0.15, 0.86) | 组件state-change：transform，300ms cubic-bezier(0.785, 0.135, 0.15, 0.86)，state-change 触发 |
| component | state-change | background-color | 200ms | 0ms | cubic-bezier(0.075, 0.82, 0.165, 1) | 组件state-change：background-color，200ms cubic-bezier(0.075, 0.82, 0.165, 1)，state-change 触发 |
| component | state-change | transform | 300ms | 0ms | ease | 组件state-change：transform，300ms ease，state-change 触发 |
| component | state-change | color | 300ms | 0ms | ease | 组件state-change：color，300ms ease，state-change 触发 |
| component | load | animation | 6000ms | 400ms | cubic-bezier(0.455, 0.03, 0.515, 0.955) | 组件load：animation rotate(0deg) translateX(100%) -> rotate(0deg) translateX(-100%)，6000ms cubic-bezier(0.455, 0.03, 0.515, 0.955)，load 触发 |
| component | load | animation | 2750ms | 0ms | cubic-bezier(0.785, 0.135, 0.15, 0.86) | 组件load：animation scale(0) translateY(0.5rem) rotate(-45deg) skew(15deg, 15deg) -> 0，2750ms cubic-bezier(0.785, 0.135, 0.15, 0.86)，load 触发 |
| component | load | animation | 2750ms | 0ms | cubic-bezier(0.785, 0.135, 0.15, 0.86) | 组件load：animation scale(0) translateY(1rem) rotate(45deg) skew(15deg, 15deg) -> 0，2750ms cubic-bezier(0.785, 0.135, 0.15, 0.86)，load 触发 |
| component | load | animation | 7000ms | 0ms | cubic-bezier(1, 0, 0, 1) | 组件load：animation translate(0, 0) -> translate(-1%, -2%)，7000ms cubic-bezier(1, 0, 0, 1)，load 触发 |
| component | load | box-shadow | 300ms | 300ms | cubic-bezier(0.215, 0.61, 0.355, 1) | 组件load：box-shadow，300ms cubic-bezier(0.215, 0.61, 0.355, 1)，load 触发 |
| component | load | animation | 150ms | 200ms | linear | 组件load：animation 0 -> 1，150ms linear，load 触发 |
| component | hover | box-shadow | 300ms | 0ms | cubic-bezier(0.215, 0.61, 0.355, 1) | 组件hover：box-shadow，300ms cubic-bezier(0.215, 0.61, 0.355, 1)，hover 触发 |
| component | state-change | transform | 300ms | 100ms | cubic-bezier(0.455, 0.03, 0.515, 0.955) | 组件state-change：transform missing -> perspective(20rem) rotateY(0deg)，300ms cubic-bezier(0.455, 0.03, 0.515, 0.955)，state-change 触发 |
| component | state-change | box-shadow | 300ms | 100ms | cubic-bezier(0.25, 0.46, 0.45, 0.94) | 组件state-change：box-shadow missing -> perspective(20rem) rotateY(0deg)，300ms cubic-bezier(0.25, 0.46, 0.45, 0.94)，state-change 触发 |
| component | hover | transform | 300ms | 0ms | cubic-bezier(0.455, 0.03, 0.515, 0.955) | 组件hover：transform missing -> perspective(20rem) rotateY(-50deg)，300ms cubic-bezier(0.455, 0.03, 0.515, 0.955)，hover 触发 |
| component | hover | box-shadow | 300ms | 100ms | cubic-bezier(0.25, 0.46, 0.45, 0.94) | 组件hover：box-shadow missing -> perspective(20rem) rotateY(-50deg)，300ms cubic-bezier(0.25, 0.46, 0.45, 0.94)，hover 触发 |
| component | state-change | transform | 300ms | 0ms | cubic-bezier(0.6, 0.04, 0.98, 0.335) | 组件state-change：transform missing -> translateX(-200%) scaleX(2.5)，300ms cubic-bezier(0.6, 0.04, 0.98, 0.335)，state-change 触发 |
| component | load | animation | 2500ms | 0ms | cubic-bezier(0.455, 0.03, 0.515, 0.955) | 组件load：animation scaleY(1) scaleX(1) -> scaleY(1) scaleX(1)，2500ms cubic-bezier(0.455, 0.03, 0.515, 0.955)，load 触发 |
| component | hover | transform | 400ms | 150ms | cubic-bezier(0.075, 0.82, 0.165, 1) | 组件hover：transform missing -> translate(0%) scaleX(1)，400ms cubic-bezier(0.075, 0.82, 0.165, 1)，hover 触发 |
| component | state-change | opacity | 300ms | 100ms | linear | 组件state-change：opacity，300ms linear，state-change 触发 |
| component | load | animation | 2500ms | 0ms | cubic-bezier(0.455, 0.03, 0.515, 0.955) | 组件load：animation scaleY(1) -> scaleY(1)，2500ms cubic-bezier(0.455, 0.03, 0.515, 0.955)，load 触发 |
| component | state-change | opacity | 300ms | 0ms | ease | 组件state-change：opacity missing -> translateY(1rem)，300ms ease，state-change 触发 |
| component | state-change | transform | 300ms | 0ms | ease | 组件state-change：transform missing -> translateY(1rem)，300ms ease，state-change 触发 |
| button | state-change | background-color | 300ms | 0ms | ease | 按钮state-change：background-color，300ms ease，state-change 触发 |
| button | state-change | transform | 300ms | 0ms | cubic-bezier(0.075, 0.82, 0.165, 1) | 按钮state-change：transform，300ms cubic-bezier(0.075, 0.82, 0.165, 1)，state-change 触发 |
| button | state-change | background-color | 200ms | 0ms | cubic-bezier(0.075, 0.82, 0.165, 1) | 按钮state-change：background-color，200ms cubic-bezier(0.075, 0.82, 0.165, 1)，state-change 触发 |
| button | state-change | background-color | 200ms | 0ms | cubic-bezier(0.075, 0.82, 0.165, 1) | 按钮state-change：background-color，200ms cubic-bezier(0.075, 0.82, 0.165, 1)，state-change 触发 |
| button | hover | backgroundColor | 200ms | 0ms | cubic-bezier(0.075, 0.82, 0.165, 1) | 按钮hover：backgroundColor missing -> rgba(158, 158, 158, 0.973)，200ms cubic-bezier(0.075, 0.82, 0.165, 1)，hover 触发；样本 Search |
| button | focus | backgroundColor | 200ms | 0ms | cubic-bezier(0.075, 0.82, 0.165, 1) | 按钮focus：backgroundColor missing -> rgba(158, 158, 158, 0.984)，200ms cubic-bezier(0.075, 0.82, 0.165, 1)，focus 触发；样本 Search |
| button | hover | backgroundColor | 200ms | 0ms | cubic-bezier(0.075, 0.82, 0.165, 1) | 按钮hover：backgroundColor missing -> rgb(158, 158, 158)，200ms cubic-bezier(0.075, 0.82, 0.165, 1)，hover 触发；样本 How can I help? |
| button | focus | backgroundColor | 200ms | 0ms | cubic-bezier(0.075, 0.82, 0.165, 1) | 按钮focus：backgroundColor missing -> rgb(158, 158, 158)，200ms cubic-bezier(0.075, 0.82, 0.165, 1)，focus 触发；样本 How can I help? |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: assets/2026-06-12-uncut-typography-resource-motion.json

## Missing Evidence
- motion-component-load-animation-1000-missing lacks easing
- motion-component-load-animation-1000-missing lacks easing
- motion-component-load-animation-6000-missing lacks easing
- motion-component-load-animation-5000-missing lacks easing
- motion-component-hover-all-missing-missing lacks duration_ms
- motion-component-hover-all-missing-missing lacks easing
- motion-component-load-animation-1000-missing lacks easing

## Snippet Appendix
### motion-component-load-animation-2500-cubic-bezier-0-455-0-03-0-515-0-955

```css
.breathe { animation: breathe 2.5s cubic-bezier(0.455, 0.03, 0.515, 0.955) infinite; }
```

### motion-button-state-change-background-color-200-cubic-bezier-0-075-0-82-0-165-1

```css
.btn { transition: background-color .2s cubic-bezier(0.075, 0.82, 0.165, 1); }
```

### motion-button-state-change-background-color-200-cubic-bezier-0-075-0-82-0-165-1

```css
.btn--header { transition: background-color .2s cubic-bezier(0.075, 0.82, 0.165, 1); }
```

### motion-component-state-change-background-color-200-cubic-bezier-0-075-0-82-0-165-1

```css
.category__count { transition: background-color .2s cubic-bezier(0.075, 0.82, 0.165, 1); }
```

### motion-component-load-transform-300-cubic-bezier-0-785-0-135-0-15-0-86

```css
.newcat::before { transition: transform .3s cubic-bezier(0.785, 0.135, 0.15, 0.86); }
```

### motion-component-state-change-transform-300-cubic-bezier-0-785-0-135-0-15-0-86

```css
.countcount { transition: transform .3s cubic-bezier(0.785, 0.135, 0.15, 0.86); }
```

### motion-component-state-change-background-color-200-cubic-bezier-0-075-0-82-0-165-1

```css
.togglethinghy { transition: background-color .2s cubic-bezier(0.075, 0.82, 0.165, 1); }
```

### motion-component-state-change-transform-300-ease

```css
.togglethinghy::before { transition: transform .3s ease; }
```

### motion-component-state-change-color-300-ease

```css
.toggle_label { transition: color .3s ease; }
```

### motion-component-load-animation-6000-cubic-bezier-0-455-0-03-0-515-0-955

```css
.search-results:empty::after { animation: swingAcross 6s .4s cubic-bezier(0.455, 0.03, 0.515, 0.955) infinite backwards; }
```

### motion-component-load-animation-2750-cubic-bezier-0-785-0-135-0-15-0-86

```css
.font-page__authors::before { animation: popAndFade 2.75s cubic-bezier(0.785, 0.135, 0.15, 0.86) infinite backwards; }
```

### motion-component-load-animation-2750-cubic-bezier-0-785-0-135-0-15-0-86

```css
.font-page__authors::after { animation: popAndFadeAlternate 2.75s cubic-bezier(0.785, 0.135, 0.15, 0.86) infinite backwards; }
```

### motion-component-load-animation-7000-cubic-bezier-1-0-0-1

```css
.font-license__dummy-eye { animation: jitter 7s cubic-bezier(1, 0, 0, 1) infinite; }
```

### motion-component-load-box-shadow-300-cubic-bezier-0-215-0-61-0-355-1

```css
.door-cont { transition: box-shadow .3s cubic-bezier(0.215, 0.61, 0.355, 1) .3s; }
```

### motion-component-load-animation-150-linear

```css
.door-cont { animation: fadedoor .15s .2s linear backwards; }
```

### motion-component-hover-box-shadow-300-cubic-bezier-0-215-0-61-0-355-1

```css
.door-cont:hover { transition: box-shadow .3s cubic-bezier(0.215, 0.61, 0.355, 1) 0s; }
```

### motion-component-state-change-transform-300-cubic-bezier-0-455-0-03-0-515-0-955

```css
.door-cont__door { transition: transform .3s cubic-bezier(0.455, 0.03, 0.515, 0.955) .1s; }
```

### motion-component-state-change-box-shadow-300-cubic-bezier-0-25-0-46-0-45-0-94

```css
.door-cont__door { transition: box-shadow .3s cubic-bezier(0.25, 0.46, 0.45, 0.94) .1s; }
```

### motion-component-hover-transform-300-cubic-bezier-0-455-0-03-0-515-0-955

```css
.door-cont:hover .door-cont__door { transition: transform .3s cubic-bezier(0.455, 0.03, 0.515, 0.955) 0s; }
```

### motion-component-hover-box-shadow-300-cubic-bezier-0-25-0-46-0-45-0-94

```css
.door-cont:hover .door-cont__door { transition: box-shadow .3s cubic-bezier(0.25, 0.46, 0.45, 0.94) .1s; }
```

### motion-component-state-change-transform-300-cubic-bezier-0-6-0-04-0-98-0-335

```css
.door-cont__dude { transition: transform .3s cubic-bezier(0.6, 0.04, 0.98, 0.335); }
```

### motion-component-load-animation-2500-cubic-bezier-0-455-0-03-0-515-0-955

```css
.door-cont__dude img { animation: pulsate 2.5s cubic-bezier(0.455, 0.03, 0.515, 0.955) infinite; }
```

### motion-component-hover-transform-400-cubic-bezier-0-075-0-82-0-165-1

```css
.door-cont:hover .door-cont__dude { transition: transform .4s .15s cubic-bezier(0.075, 0.82, 0.165, 1); }
```

### motion-component-state-change-opacity-300-linear

```css
.dooroverlay { transition: opacity .3s .1s linear; }
```

### motion-component-load-animation-2500-cubic-bezier-0-455-0-03-0-515-0-955

```css
.chatbot__avatar-image img { animation: breathe 2.5s 0s cubic-bezier(0.455, 0.03, 0.515, 0.955) infinite; }
```

### motion-component-state-change-opacity-300-ease

```css
.chatbot__message { transition: opacity .3s ease; }
```

### motion-component-state-change-transform-300-ease

```css
.chatbot__message { transition: transform .3s ease; }
```

### motion-button-state-change-background-color-300-ease

```css
.chatbot__feedback-button { transition: background-color .3s ease; }
```

### motion-button-state-change-transform-300-cubic-bezier-0-075-0-82-0-165-1

```css
.chatbot__feedback-button-icon { transition: transform .3s cubic-bezier(0.075, 0.82, 0.165, 1); }
```

### motion-button-state-change-background-color-200-cubic-bezier-0-075-0-82-0-165-1

```css
.btn-qa { transition: background-color .2s cubic-bezier(0.075, 0.82, 0.165, 1); }
```

### motion-button-state-change-background-color-200-cubic-bezier-0-075-0-82-0-165-1

```css
.btn-done { transition: background-color .2s cubic-bezier(0.075, 0.82, 0.165, 1); }
```

### motion-button-hover-backgroundcolor-200-cubic-bezier-0-075-0-82-0-165-1

```css
{"backgroundColor": "rgba(158, 158, 158, 0.973)", "border": "1px solid rgba(0, 0, 0, 0)", "borderBottom": "1px solid rgba(0, 0, 0, 0)", "borderLeft": "1px solid rgba(0, 0, 0, 0)", "borderRight": "1px solid rgba(0, 0, 0, 0)", "borderTop": "1px solid rgba(0, 0, 0, 0)"}
```

### motion-button-focus-backgroundcolor-200-cubic-bezier-0-075-0-82-0-165-1

```css
{"backgroundColor": "rgba(158, 158, 158, 0.984)", "border": "1px solid rgba(0, 0, 0, 0)", "borderBottom": "1px solid rgba(0, 0, 0, 0)", "borderLeft": "1px solid rgba(0, 0, 0, 0)", "borderRight": "1px solid rgba(0, 0, 0, 0)", "borderTop": "1px solid rgba(0, 0, 0, 0)"}
```

### motion-button-hover-backgroundcolor-200-cubic-bezier-0-075-0-82-0-165-1

```css
{"backgroundColor": "rgb(158, 158, 158)"}
```

### motion-button-focus-backgroundcolor-200-cubic-bezier-0-075-0-82-0-165-1

```css
{"backgroundColor": "rgb(158, 158, 158)"}
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
