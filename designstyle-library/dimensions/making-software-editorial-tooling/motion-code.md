# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| button | hover | color | 150ms | 0ms | cubic-bezier(0.4, 0, 0.2, 1) | 按钮hover：color missing -> oklab(0.232162 -0.0119137 -0.131931)，150ms cubic-bezier(0.4, 0, 0.2, 1)，hover 触发；样本 PROGRESS |
| button | focus | color | 150ms | 0ms | cubic-bezier(0.4, 0, 0.2, 1) | 按钮focus：color missing -> oklab(0.232162 -0.0119137 -0.131931)，150ms cubic-bezier(0.4, 0, 0.2, 1)，focus 触发；样本 PROGRESS |
| button | hover | color | 0ms | 0ms | ease | 按钮hover：color missing -> oklch(0.5058 0.2886 264.84)，0ms ease，hover 触发；样本 ↑ |
| button | focus | color | 0ms | 0ms | ease | 按钮focus：color missing -> oklch(0.5058 0.2886 264.84)，0ms ease，focus 触发；样本 ↑ |
| button | hover | color | 0ms | 0ms | ease | 按钮hover：color missing -> oklch(0.5058 0.2886 264.84)，0ms ease，hover 触发；样本 ↓ |
| button | focus | color | 0ms | 0ms | ease | 按钮focus：color missing -> oklch(0.5058 0.2886 264.84)，0ms ease，focus 触发；样本 ↓ |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: assets/2026-06-12-making-software-editorial-tooling-motion.json

## Missing Evidence
- None recorded.

## Snippet Appendix
### motion-button-hover-color-150-cubic-bezier-0-4-0-0-2-1

```css
{"border": "0px solid oklab(0.232162 -0.0119137 -0.131931)", "borderBottom": "0px solid oklab(0.232162 -0.0119137 -0.131931)", "borderLeft": "0px solid oklab(0.232162 -0.0119137 -0.131931)", "borderRight": "0px solid oklab(0.232162 -0.0119137 -0.131931)", "borderTop": "0px solid oklab(0.232162 -0.0119137 -0.131931)", "color": "oklab(0.232162 -0.0119137 -0.131931)"}
```

### motion-button-focus-color-150-cubic-bezier-0-4-0-0-2-1

```css
{"border": "0px solid oklab(0.232162 -0.0119137 -0.131931)", "borderBottom": "0px solid oklab(0.232162 -0.0119137 -0.131931)", "borderLeft": "0px solid oklab(0.232162 -0.0119137 -0.131931)", "borderRight": "0px solid oklab(0.232162 -0.0119137 -0.131931)", "borderTop": "0px solid oklab(0.232162 -0.0119137 -0.131931)", "color": "oklab(0.232162 -0.0119137 -0.131931)"}
```

### motion-button-hover-color-0-ease

```css
{"border": "0px solid oklch(0.5058 0.2886 264.84)", "borderBottom": "0px solid oklch(0.5058 0.2886 264.84)", "borderLeft": "0px solid oklch(0.5058 0.2886 264.84)", "borderRight": "0px solid oklch(0.5058 0.2886 264.84)", "borderTop": "0px solid oklch(0.5058 0.2886 264.84)", "color": "oklch(0.5058 0.2886 264.84)"}
```

### motion-button-focus-color-0-ease

```css
{"border": "0px solid oklch(0.5058 0.2886 264.84)", "borderBottom": "0px solid oklch(0.5058 0.2886 264.84)", "borderLeft": "0px solid oklch(0.5058 0.2886 264.84)", "borderRight": "0px solid oklch(0.5058 0.2886 264.84)", "borderTop": "0px solid oklch(0.5058 0.2886 264.84)", "color": "oklch(0.5058 0.2886 264.84)"}
```

### motion-button-hover-color-0-ease

```css
{"border": "0px solid oklch(0.5058 0.2886 264.84)", "borderBottom": "0px solid oklch(0.5058 0.2886 264.84)", "borderLeft": "0px solid oklch(0.5058 0.2886 264.84)", "borderRight": "0px solid oklch(0.5058 0.2886 264.84)", "borderTop": "0px solid oklch(0.5058 0.2886 264.84)", "color": "oklch(0.5058 0.2886 264.84)"}
```

### motion-button-focus-color-0-ease

```css
{"border": "0px solid oklch(0.5058 0.2886 264.84)", "borderBottom": "0px solid oklch(0.5058 0.2886 264.84)", "borderLeft": "0px solid oklch(0.5058 0.2886 264.84)", "borderRight": "0px solid oklch(0.5058 0.2886 264.84)", "borderTop": "0px solid oklch(0.5058 0.2886 264.84)", "color": "oklch(0.5058 0.2886 264.84)"}
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
