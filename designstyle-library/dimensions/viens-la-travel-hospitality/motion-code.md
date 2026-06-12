# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| button | hover | backgroundColor | 500ms | 0ms | cubic-bezier(0.25, 0, 0.25, 1) | 按钮hover：backgroundColor rgb(255, 227, 117) -> rgba(0, 0, 0, 0)，500ms cubic-bezier(0.25, 0, 0.25, 1)，hover 触发；样本 DÉCOUVRIR LA VIDÉO DES 15 ANS |
| button | focus | backgroundColor | 500ms | 0ms | cubic-bezier(0.25, 0, 0.25, 1) | 按钮focus：backgroundColor rgb(255, 227, 117) -> rgba(0, 0, 0, 0)，500ms cubic-bezier(0.25, 0, 0.25, 1)，focus 触发；样本 DÉCOUVRIR LA VIDÉO DES 15 ANS |
| button | hover | opacity | 500ms | 0ms | cubic-bezier(0.25, 0, 0.25, 1) | 按钮hover：opacity 1 -> 0.124922，500ms cubic-bezier(0.25, 0, 0.25, 1)，hover 触发；样本 DÉCOUVRIR LA VIDÉO DES 15 ANS |
| button | focus | opacity | 500ms | 0ms | cubic-bezier(0.25, 0, 0.25, 1) | 按钮focus：opacity 1 -> 0.10201，500ms cubic-bezier(0.25, 0, 0.25, 1)，focus 触发；样本 DÉCOUVRIR LA VIDÉO DES 15 ANS |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: missing

## Missing Evidence
- None recorded.

## Snippet Appendix
### motion-button-hover-backgroundcolor-500-cubic-bezier-0-25-0-0-25-1

```css
{"backgroundColor": "rgba(0, 0, 0, 0)", "transition": "box-shadow 0.5s cubic-bezier(0.25, 0, 0.25, 1)"}
```

### motion-button-focus-backgroundcolor-500-cubic-bezier-0-25-0-0-25-1

```css
{"backgroundColor": "rgba(0, 0, 0, 0)", "transition": "box-shadow 0.5s cubic-bezier(0.25, 0, 0.25, 1)"}
```

### motion-button-hover-opacity-500-cubic-bezier-0-25-0-0-25-1

```css
{"opacity": "0.124922", "transition": "opacity 0.5s cubic-bezier(0.25, 0, 0.25, 1)"}
```

### motion-button-focus-opacity-500-cubic-bezier-0-25-0-0-25-1

```css
{"opacity": "0.10201", "transition": "opacity 0.5s cubic-bezier(0.25, 0, 0.25, 1)"}
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
