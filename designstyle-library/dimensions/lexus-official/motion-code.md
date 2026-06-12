# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| button | hover | backgroundColor | 150ms | 0ms | cubic-bezier(0.335, 0.015, 0.46, 0.995) | 按钮hover：backgroundColor rgb(255, 255, 255) -> rgba(0, 0, 0, 0)，150ms cubic-bezier(0.335, 0.015, 0.46, 0.995)，hover 触发；样本 LEARN MORE |
| button | focus | backgroundColor | 150ms | 0ms | cubic-bezier(0.335, 0.015, 0.46, 0.995) | 按钮focus：backgroundColor rgb(255, 255, 255) -> rgba(0, 0, 0, 0)，150ms cubic-bezier(0.335, 0.015, 0.46, 0.995)，focus 触发；样本 LEARN MORE |
| button | hover | backgroundColor | 150ms | 0ms | cubic-bezier(0.335, 0.015, 0.46, 0.995) | 按钮hover：backgroundColor rgb(0, 0, 0) -> rgba(0, 0, 0, 0.016)，150ms cubic-bezier(0.335, 0.015, 0.46, 0.995)，hover 触发；样本 EXPLORE |
| button | focus | backgroundColor | 150ms | 0ms | cubic-bezier(0.335, 0.015, 0.46, 0.995) | 按钮focus：backgroundColor rgb(0, 0, 0) -> rgba(0, 0, 0, 0)，150ms cubic-bezier(0.335, 0.015, 0.46, 0.995)，focus 触发；样本 EXPLORE |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: missing

## Missing Evidence
- None recorded.

## Snippet Appendix
### motion-button-hover-backgroundcolor-150-cubic-bezier-0-335-0-015-0-46-0-995

```css
{"backgroundColor": "rgba(0, 0, 0, 0)", "transition": "0.15s cubic-bezier(0.335, 0.015, 0.46, 0.995)"}
```

### motion-button-focus-backgroundcolor-150-cubic-bezier-0-335-0-015-0-46-0-995

```css
{"backgroundColor": "rgba(0, 0, 0, 0)", "transition": "0.15s cubic-bezier(0.335, 0.015, 0.46, 0.995)"}
```

### motion-button-hover-backgroundcolor-150-cubic-bezier-0-335-0-015-0-46-0-995

```css
{"backgroundColor": "rgba(0, 0, 0, 0.016)", "transition": "0.15s cubic-bezier(0.335, 0.015, 0.46, 0.995)"}
```

### motion-button-focus-backgroundcolor-150-cubic-bezier-0-335-0-015-0-46-0-995

```css
{"backgroundColor": "rgba(0, 0, 0, 0)", "transition": "0.15s cubic-bezier(0.335, 0.015, 0.46, 0.995)"}
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
