# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| hero | load | animation | 34000ms | 0ms | linear | 首屏load：animation translate(0) -> translate(calc(-100% - 25px))，34000ms linear，load 触发 |
| navigation | state-change | all | 300ms | 0ms | ease | 导航state-change：all，300ms ease，state-change 触发 |
| button | hover | backgroundColor | 250ms | 0ms | ease | 按钮hover：backgroundColor missing -> rgb(67, 85, 139)，250ms ease，hover 触发；样本 ABOUT |
| button | focus | backgroundColor | 250ms | 0ms | ease | 按钮focus：backgroundColor missing -> rgb(67, 85, 139)，250ms ease，focus 触发；样本 ABOUT |
| button | hover | backgroundColor | 250ms | 0ms | ease | 按钮hover：backgroundColor missing -> rgb(227, 170, 157)，250ms ease，hover 触发；样本 TESTIMONIALS |
| button | focus | backgroundColor | 250ms | 0ms | ease | 按钮focus：backgroundColor missing -> rgb(227, 170, 157)，250ms ease，focus 触发；样本 TESTIMONIALS |
| button | hover | backgroundColor | 250ms | 0ms | ease | 按钮hover：backgroundColor missing -> rgb(217, 154, 95)，250ms ease，hover 触发；样本 CONTACT |
| button | focus | backgroundColor | 250ms | 0ms | ease | 按钮focus：backgroundColor missing -> rgb(217, 154, 95)，250ms ease，focus 触发；样本 CONTACT |
| button | hover | backgroundColor | 250ms | 0ms | ease | 按钮hover：backgroundColor missing -> rgb(67, 85, 139)，250ms ease，hover 触发；样本 INSTAGRAM |
| button | focus | backgroundColor | 250ms | 0ms | ease | 按钮focus：backgroundColor missing -> rgb(52, 72, 131)，250ms ease，focus 触发；样本 INSTAGRAM |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: assets/2026-06-12-middle-name-agency-studio-motion.json

## Missing Evidence
- motion-hero-load-animation-0-missing lacks easing

## Snippet Appendix
### motion-hero-load-animation-34000-linear

```css
.block-hero__marque>span { animation: scroll 34s linear infinite; }
```

### motion-navigation-state-change-all-300-ease

```css
.slideshow__nav a { transition: all .3s ease; }
```

### motion-button-hover-backgroundcolor-250-ease

```css
{"backgroundColor": "rgb(67, 85, 139)", "border": "0px none rgb(200, 205, 222)", "borderBottom": "0px none rgb(200, 205, 222)", "borderLeft": "0px none rgb(200, 205, 222)", "borderRight": "0px none rgb(200, 205, 222)", "borderTop": "0px none rgb(200, 205, 222)", "color": "rgb(200, 205, 222)"}
```

### motion-button-focus-backgroundcolor-250-ease

```css
{"backgroundColor": "rgb(67, 85, 139)", "border": "0px none rgb(200, 205, 222)", "borderBottom": "0px none rgb(200, 205, 222)", "borderLeft": "0px none rgb(200, 205, 222)", "borderRight": "0px none rgb(200, 205, 222)", "borderTop": "0px none rgb(200, 205, 222)", "color": "rgb(200, 205, 222)"}
```

### motion-button-hover-backgroundcolor-250-ease

```css
{"backgroundColor": "rgb(227, 170, 157)", "border": "0px none rgb(199, 205, 221)", "borderBottom": "0px none rgb(199, 205, 221)", "borderLeft": "0px none rgb(199, 205, 221)", "borderRight": "0px none rgb(199, 205, 221)", "borderTop": "0px none rgb(199, 205, 221)", "color": "rgb(199, 205, 221)"}
```

### motion-button-focus-backgroundcolor-250-ease

```css
{"backgroundColor": "rgb(227, 170, 157)", "border": "0px none rgb(199, 205, 221)", "borderBottom": "0px none rgb(199, 205, 221)", "borderLeft": "0px none rgb(199, 205, 221)", "borderRight": "0px none rgb(199, 205, 221)", "borderTop": "0px none rgb(199, 205, 221)", "color": "rgb(199, 205, 221)"}
```

### motion-button-hover-backgroundcolor-250-ease

```css
{"backgroundColor": "rgb(217, 154, 95)", "border": "0px none rgb(200, 205, 222)", "borderBottom": "0px none rgb(200, 205, 222)", "borderLeft": "0px none rgb(200, 205, 222)", "borderRight": "0px none rgb(200, 205, 222)", "borderTop": "0px none rgb(200, 205, 222)", "color": "rgb(200, 205, 222)"}
```

### motion-button-focus-backgroundcolor-250-ease

```css
{"backgroundColor": "rgb(217, 154, 95)", "border": "0px none rgb(200, 205, 222)", "borderBottom": "0px none rgb(200, 205, 222)", "borderLeft": "0px none rgb(200, 205, 222)", "borderRight": "0px none rgb(200, 205, 222)", "borderTop": "0px none rgb(200, 205, 222)", "color": "rgb(200, 205, 222)"}
```

### motion-button-hover-backgroundcolor-250-ease

```css
{"backgroundColor": "rgb(67, 85, 139)", "border": "0px none rgb(200, 205, 222)", "borderBottom": "0px none rgb(200, 205, 222)", "borderLeft": "0px none rgb(200, 205, 222)", "borderRight": "0px none rgb(200, 205, 222)", "borderTop": "0px none rgb(200, 205, 222)", "color": "rgb(200, 205, 222)"}
```

### motion-button-focus-backgroundcolor-250-ease

```css
{"backgroundColor": "rgb(52, 72, 131)", "border": "0px none rgb(216, 220, 231)", "borderBottom": "0px none rgb(216, 220, 231)", "borderLeft": "0px none rgb(216, 220, 231)", "borderRight": "0px none rgb(216, 220, 231)", "borderTop": "0px none rgb(216, 220, 231)", "color": "rgb(216, 220, 231)"}
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
