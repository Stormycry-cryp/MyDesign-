# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| navigation | hover | backgroundColor | 200ms | 0ms | cubic-bezier(0, 0, 1, 1) | 导航hover：backgroundColor rgba(41, 18, 16, 0.1) -> rgba(10, 5, 4, 0.133)，200ms cubic-bezier(0, 0, 1, 1)，hover 触发；样本 ds-navigation-1 |
| navigation | focus | backgroundColor | 200ms | 0ms | cubic-bezier(0, 0, 1, 1) | 导航focus：backgroundColor rgba(41, 18, 16, 0.1) -> rgba(7, 3, 3, 0.137)，200ms cubic-bezier(0, 0, 1, 1)，focus 触发；样本 ds-navigation-1 |
| button | hover | backgroundColor | 200ms | 0ms | cubic-bezier(0, 0, 1, 1) | 按钮hover：backgroundColor rgba(0, 0, 0, 0) -> rgba(0, 0, 0, 0.063)，200ms cubic-bezier(0, 0, 1, 1)，hover 触发；样本 Products |
| button | focus | backgroundColor | 200ms | 0ms | cubic-bezier(0, 0, 1, 1) | 按钮focus：backgroundColor rgba(0, 0, 0, 0) -> rgba(0, 0, 0, 0.063)，200ms cubic-bezier(0, 0, 1, 1)，focus 触发；样本 Products |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: missing

## Missing Evidence
- None recorded.

## Snippet Appendix
### motion-navigation-hover-backgroundcolor-200-cubic-bezier-0-0-1-1

```css
{"backgroundColor": "rgba(10, 5, 4, 0.133)", "transition": "background 0.2s cubic-bezier(0, 0, 1, 1)"}
```

### motion-navigation-focus-backgroundcolor-200-cubic-bezier-0-0-1-1

```css
{"backgroundColor": "rgba(7, 3, 3, 0.137)", "transition": "background 0.2s cubic-bezier(0, 0, 1, 1)"}
```

### motion-button-hover-backgroundcolor-200-cubic-bezier-0-0-1-1

```css
{"backgroundColor": "rgba(0, 0, 0, 0.063)", "transition": "color 0.2s cubic-bezier(0, 0, 1, 1), background 0.2s cubic-bezier(0, 0, 1, 1)"}
```

### motion-button-focus-backgroundcolor-200-cubic-bezier-0-0-1-1

```css
{"backgroundColor": "rgba(0, 0, 0, 0.063)", "transition": "color 0.2s cubic-bezier(0, 0, 1, 1), background 0.2s cubic-bezier(0, 0, 1, 1)"}
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
