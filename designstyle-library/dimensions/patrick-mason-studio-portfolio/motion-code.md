# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| button | hover | boxShadow | 200ms | 0ms | cubic-bezier(0.87, 0, 0.13, 1) | 按钮hover：boxShadow missing -> rgba(0, 0, 0, 0.21) 5.332px 5.332px 9.5976px -7.4648px, rgba(255, 255, 255, 0.427) -5.332px -5.332px 7.4648px -2.666px，200ms cubic-bezier(0.87, 0, 0.13, 1)，hover 触发；样本 ? |
| button | focus | boxShadow | 200ms | 0ms | cubic-bezier(0.87, 0, 0.13, 1) | 按钮focus：boxShadow missing -> rgba(0, 0, 0, 0.21) 5.332px 5.332px 9.5976px -7.4648px, rgba(255, 255, 255, 0.427) -5.332px -5.332px 7.4648px -2.666px，200ms cubic-bezier(0.87, 0, 0.13, 1)，focus 触发；样本 ? |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: assets/2026-06-12-patrick-mason-studio-portfolio-motion.json

## Missing Evidence
- None recorded.

## Snippet Appendix
### motion-button-hover-boxshadow-200-cubic-bezier-0-87-0-0-13-1

```css
{"boxShadow": "rgba(0, 0, 0, 0.21) 5.332px 5.332px 9.5976px -7.4648px, rgba(255, 255, 255, 0.427) -5.332px -5.332px 7.4648px -2.666px"}
```

### motion-button-focus-boxshadow-200-cubic-bezier-0-87-0-0-13-1

```css
{"boxShadow": "rgba(0, 0, 0, 0.21) 5.332px 5.332px 9.5976px -7.4648px, rgba(255, 255, 255, 0.427) -5.332px -5.332px 7.4648px -2.666px"}
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
