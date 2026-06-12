# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| navigation | hover | color | 200ms | 0ms | ease | 导航hover：color rgb(255, 255, 255) -> rgb(127, 127, 127)，200ms ease，hover 触发；样本 Snøhetta |
| navigation | focus | color | 200ms | 0ms | ease | 导航focus：color rgb(255, 255, 255) -> rgb(127, 127, 127)，200ms ease，focus 触发；样本 Snøhetta |
| button | hover | color | 200ms | 0ms | ease | 按钮hover：color rgb(255, 255, 255) -> rgb(134, 134, 134)，200ms ease，hover 触发；样本 Menu |
| button | focus | color | 200ms | 0ms | ease | 按钮focus：color rgb(255, 255, 255) -> rgb(127, 127, 127)，200ms ease，focus 触发；样本 Menu |
| button | hover | color | 300ms | 0ms | cubic-bezier(0.4, 0, 0.2, 1) | 按钮hover：color rgb(0, 0, 0) -> rgb(98, 98, 98)，300ms cubic-bezier(0.4, 0, 0.2, 1)，hover 触发；样本 <- |
| button | focus | color | 300ms | 0ms | cubic-bezier(0.4, 0, 0.2, 1) | 按钮focus：color rgb(0, 0, 0) -> rgb(98, 98, 98)，300ms cubic-bezier(0.4, 0, 0.2, 1)，focus 触发；样本 <- |
| button | hover | color | 300ms | 0ms | cubic-bezier(0.4, 0, 0.2, 1) | 按钮hover：color rgb(0, 0, 0) -> rgb(69, 69, 69)，300ms cubic-bezier(0.4, 0, 0.2, 1)，hover 触发；样本 -> |
| button | focus | color | 300ms | 0ms | cubic-bezier(0.4, 0, 0.2, 1) | 按钮focus：color rgb(0, 0, 0) -> rgb(69, 69, 69)，300ms cubic-bezier(0.4, 0, 0.2, 1)，focus 触发；样本 -> |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: missing

## Missing Evidence
- None recorded.

## Snippet Appendix
### motion-navigation-hover-color-200-ease

```css
{"color": "rgb(127, 127, 127)", "transition": "0.2s"}
```

### motion-navigation-focus-color-200-ease

```css
{"color": "rgb(127, 127, 127)", "transition": "0.2s"}
```

### motion-button-hover-color-200-ease

```css
{"color": "rgb(134, 134, 134)", "transition": "0.2s"}
```

### motion-button-focus-color-200-ease

```css
{"color": "rgb(127, 127, 127)", "transition": "0.2s"}
```

### motion-button-hover-color-300-cubic-bezier-0-4-0-0-2-1

```css
{"color": "rgb(98, 98, 98)", "transition": "color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1)"}
```

### motion-button-focus-color-300-cubic-bezier-0-4-0-0-2-1

```css
{"color": "rgb(98, 98, 98)", "transition": "color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1)"}
```

### motion-button-hover-color-300-cubic-bezier-0-4-0-0-2-1

```css
{"color": "rgb(69, 69, 69)", "transition": "color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1)"}
```

### motion-button-focus-color-300-cubic-bezier-0-4-0-0-2-1

```css
{"color": "rgb(69, 69, 69)", "transition": "color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1)"}
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
