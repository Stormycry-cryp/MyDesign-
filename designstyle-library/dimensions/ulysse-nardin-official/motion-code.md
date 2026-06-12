# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| navigation | hover | color | 300ms | 0ms | cubic-bezier(0, 0, 0.2, 1) | 导航hover：color rgb(255, 255, 255) -> rgb(0, 16, 56)，300ms cubic-bezier(0, 0, 0.2, 1)，hover 触发；样本 Watches About Us Services Boutiques |
| navigation | focus | color | 300ms | 0ms | cubic-bezier(0, 0, 0.2, 1) | 导航focus：color rgb(255, 255, 255) -> rgb(0, 16, 56)，300ms cubic-bezier(0, 0, 0.2, 1)，focus 触发；样本 Watches About Us Services Boutiques |
| button | hover | color | 200ms | 0ms | cubic-bezier(0, 0, 0.2, 1) | 按钮hover：color rgb(255, 255, 255) -> rgb(27, 41, 77)，200ms cubic-bezier(0, 0, 0.2, 1)，hover 触发；样本 Watches |
| button | focus | color | 200ms | 0ms | cubic-bezier(0, 0, 0.2, 1) | 按钮focus：color rgb(255, 255, 255) -> rgb(27, 41, 77)，200ms cubic-bezier(0, 0, 0.2, 1)，focus 触发；样本 Watches |
| button | hover | color | 200ms | 0ms | cubic-bezier(0, 0, 0.2, 1) | 按钮hover：color rgb(255, 255, 255) -> rgb(0, 16, 56)，200ms cubic-bezier(0, 0, 0.2, 1)，hover 触发；样本 About Us |
| button | focus | color | 200ms | 0ms | cubic-bezier(0, 0, 0.2, 1) | 按钮focus：color rgb(255, 255, 255) -> rgb(0, 16, 56)，200ms cubic-bezier(0, 0, 0.2, 1)，focus 触发；样本 About Us |
| button | state-change | color | 300ms | 0ms | linear | 按钮state-change：color rgb(255, 255, 255) -> missing，300ms linear，state-change 触发；样本 Explore the universe |
| button | state-change | color | 300ms | 0ms | linear | 按钮state-change：color rgb(0, 0, 0) -> missing，300ms linear，state-change 触发；样本 Find a store |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: missing

## Missing Evidence
- None recorded.

## Snippet Appendix
### motion-navigation-hover-color-300-cubic-bezier-0-0-0-2-1

```css
{"color": "rgb(0, 16, 56)", "transition": "--header-background-color 0.3s cubic-bezier(0, 0, 0.2, 1), --header-text-color 0.3s cubic-bezier(0, 0, 0.2, 1)"}
```

### motion-navigation-focus-color-300-cubic-bezier-0-0-0-2-1

```css
{"color": "rgb(0, 16, 56)", "transition": "--header-background-color 0.3s cubic-bezier(0, 0, 0.2, 1), --header-text-color 0.3s cubic-bezier(0, 0, 0.2, 1)"}
```

### motion-button-hover-color-200-cubic-bezier-0-0-0-2-1

```css
{"color": "rgb(27, 41, 77)", "transition": "0.2s cubic-bezier(0, 0, 0.2, 1)"}
```

### motion-button-focus-color-200-cubic-bezier-0-0-0-2-1

```css
{"color": "rgb(27, 41, 77)", "transition": "0.2s cubic-bezier(0, 0, 0.2, 1)"}
```

### motion-button-hover-color-200-cubic-bezier-0-0-0-2-1

```css
{"color": "rgb(0, 16, 56)", "transition": "0.2s cubic-bezier(0, 0, 0.2, 1)"}
```

### motion-button-focus-color-200-cubic-bezier-0-0-0-2-1

```css
{"color": "rgb(0, 16, 56)", "transition": "0.2s cubic-bezier(0, 0, 0.2, 1)"}
```

### motion-button-state-change-color-300-linear

```css
{"transition": "color 0.3s linear, border 0.2s linear, background-position 0.3s linear"}
```

### motion-button-state-change-color-300-linear

```css
{"transition": "color 0.3s linear, border 0.2s linear, background-position 0.3s linear"}
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
