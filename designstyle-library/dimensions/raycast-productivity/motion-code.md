# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| component | load | animation | 2000ms | 0ms | ease-in-out | 组件load：animation translateX(0) -> translateX(-100%)，2000ms ease-in-out，load 触发 |
| button | state-change | box-shadow | 200ms | 0ms | ease-in-out | 按钮state-change：box-shadow，200ms ease-in-out，state-change 触发 |
| button | state-change | transform | 100ms | 0ms | ease-in-out | 按钮state-change：transform，100ms ease-in-out，state-change 触发 |
| component | state-change | opacity | 300ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：opacity missing -> translate(-50%,calc(-50% - 50px))，300ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | width | 300ms | 0ms | ease | 组件state-change：width，300ms ease，state-change 触发 |
| component | state-change | opacity | 400ms | 0ms | ease | 组件state-change：opacity，400ms ease，state-change 触发 |
| component | state-change | all | 300ms | 0ms | ease | 组件state-change：all，300ms ease，state-change 触发 |
| component | state-change | color | 300ms | 0ms | ease | 组件state-change：color，300ms ease，state-change 触发 |
| component | state-change | color | 300ms | 0ms | ease | 组件state-change：color，300ms ease，state-change 触发 |
| component | state-change | opacity | 200ms | 0ms | ease | 组件state-change：opacity，200ms ease，state-change 触发 |
| component | state-change | color | 300ms | 0ms | ease | 组件state-change：color，300ms ease，state-change 触发 |
| component | state-change | opacity | 150ms | 0ms | ease | 组件state-change：opacity，150ms ease，state-change 触发 |
| component | state-change | transform | 150ms | 0ms | ease | 组件state-change：transform，150ms ease，state-change 触发 |
| component | load | animation | 300ms | 0ms | ease | 组件load：animation scale(.8) -> scale(1)，300ms ease，load 触发 |
| component | load | animation | 1500ms | 0ms | cubic-bezier(.455,.03,.515,.955) | 组件load：animation 0 -> 1，1500ms cubic-bezier(.455,.03,.515,.955)，load 触发 |
| component | state-change | opacity | 300ms | 0ms | cubic-bezier(.4,0,.2,1) | 组件state-change：opacity missing -> translate(-50%,calc(-50% - 50px))，300ms cubic-bezier(.4,0,.2,1)，state-change 触发 |
| component | state-change | width | 300ms | 0ms | ease | 组件state-change：width，300ms ease，state-change 触发 |
| component | state-change | opacity | 400ms | 0ms | ease | 组件state-change：opacity，400ms ease，state-change 触发 |
| component | state-change | all | 300ms | 0ms | ease | 组件state-change：all，300ms ease，state-change 触发 |
| component | state-change | color | 300ms | 0ms | ease | 组件state-change：color，300ms ease，state-change 触发 |
| component | state-change | box-shadow | 200ms | 0ms | ease-in-out | 组件state-change：box-shadow，200ms ease-in-out，state-change 触发 |
| component | state-change | box-shadow | 200ms | 0ms | ease-in-out | 组件state-change：box-shadow，200ms ease-in-out，state-change 触发 |
| component | state-change | opacity | 600ms | 0ms | cubic-bezier(.4,0,.22,.96) | 组件state-change：opacity missing -> none，600ms cubic-bezier(.4,0,.22,.96)，state-change 触发 |
| component | state-change | transform | 600ms | 0ms | cubic-bezier(.4,0,.22,.96) | 组件state-change：transform missing -> none，600ms cubic-bezier(.4,0,.22,.96)，state-change 触发 |
| hero | state-change | all | 200ms | 0ms | ease | 首屏state-change：all missing -> translateZ(0)，200ms ease，state-change 触发 |
| hero | viewport | animation | 3000ms | 0ms | linear | 首屏viewport：animation，3000ms linear，viewport 触发 |
| component | state-change | text-underline-offset | 100ms | 0ms | ease-out | 组件state-change：text-underline-offset，100ms ease-out，state-change 触发 |
| component | state-change | transform | 200ms | 0ms | ease-out | 组件state-change：transform，200ms ease-out，state-change 触发 |
| component | state-change | opacity | 400ms | 0ms | ease-out | 组件state-change：opacity，400ms ease-out，state-change 触发 |
| component | state-change | transform | 100ms | 0ms | ease-out | 组件state-change：transform missing -> translateZ(0)，100ms ease-out，state-change 触发 |
| component | load | animation | 1000ms | 0ms | linear | 组件load：animation rotate(0deg) -> rotate(1turn)，1000ms linear，load 触发 |
| navigation | state-change | all | 200ms | 0ms | ease-in-out | 导航state-change：all，200ms ease-in-out，state-change 触发 |
| component | state-change | text-underline-offset | 100ms | 0ms | ease-out | 组件state-change：text-underline-offset，100ms ease-out，state-change 触发 |
| component | state-change | color | 300ms | 0ms | ease | 组件state-change：color，300ms ease，state-change 触发 |
| component | state-change | transform | 1500ms | 0ms | cubic-bezier(.165,.84,.44,1) | 组件state-change：transform missing -> translateY(-37px) translateZ(0)，1500ms cubic-bezier(.165,.84,.44,1)，state-change 触发 |
| button | hover | backgroundColor | 200ms | 0ms | ease, ease, ease-in-out, ease-in-out | 按钮hover：backgroundColor missing -> rgb(252, 252, 252)，200ms ease, ease, ease-in-out, ease-in-out，hover 触发；样本 Download |
| button | focus | backgroundColor | 200ms | 0ms | ease, ease, ease-in-out, ease-in-out | 按钮focus：backgroundColor missing -> rgb(252, 252, 252)，200ms ease, ease, ease-in-out, ease-in-out，focus 触发；样本 Download |
| form | hover | style | 300ms | 0ms | ease, ease | 组件hover：style，300ms ease, ease，hover 触发；样本 ds-form-1 |
| form | focus | style | 300ms | 0ms | ease, ease | 组件focus：style，300ms ease, ease，focus 触发；样本 ds-form-1 |
| form | hover | style | 300ms | 0ms | ease-in-out, ease-in-out, ease-in-out | 组件hover：style，300ms ease-in-out, ease-in-out, ease-in-out，hover 触发；样本 ds-form-2 |
| form | focus | style | 300ms | 0ms | ease-in-out, ease-in-out, ease-in-out | 组件focus：style，300ms ease-in-out, ease-in-out, ease-in-out，focus 触发；样本 ds-form-2 |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: assets/2026-06-12-raycast-productivity-motion.json

## Missing Evidence
- motion-component-state-change-opacity-200-missing lacks easing
- motion-component-state-change-transform-200-missing lacks easing
- motion-component-state-change-opacity-200-missing lacks easing
- motion-component-state-change-transform-200-missing lacks easing
- motion-component-load-opacity-200-missing lacks easing
- motion-component-state-change-transform-200-missing lacks easing
- motion-component-state-change-opacity-300-missing lacks easing
- motion-component-state-change-opacity-300-missing lacks easing
- motion-button-state-change-background-image-200-missing lacks easing
- motion-button-state-change-background-color-200-missing lacks easing
- motion-component-load-animation-missing-linear lacks duration_ms
- motion-component-load-animation-missing-linear lacks duration_ms
- motion-component-load-animation-missing-linear lacks duration_ms
- motion-component-load-animation-missing-linear lacks duration_ms
- motion-component-load-animation-missing-linear lacks duration_ms
- motion-component-load-animation-missing-linear lacks duration_ms
- motion-component-state-change-opacity-300-missing lacks easing
- motion-component-load-animation-1100-missing lacks easing
- motion-navigation-load-animation-1100-missing lacks easing
- motion-navigation-load-animation-1100-missing lacks easing
- motion-component-load-animation-1100-missing lacks easing
- motion-component-load-animation-1100-missing lacks easing
- motion-component-state-change-opacity-500-missing lacks easing

## Snippet Appendix
### motion-component-load-animation-2000-ease-in-out

```css
.search_loadingIndicator__gxtmG { animation: search_nightRider__a2oGM 2s ease-in-out infinite; }
```

### motion-button-state-change-box-shadow-200-ease-in-out

```css
.Button_button__JJiqJ { transition: box-shadow .2s ease-in-out; }
```

### motion-button-state-change-transform-100-ease-in-out

```css
.Button_button__JJiqJ { transition: transform .1s ease-in-out; }
```

### motion-component-state-change-opacity-300-cubic-bezier-4-0-2-1

```css
.Gallery_img__grW93 { transition: opacity .3s cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-width-300-ease

```css
.Gallery_page__9tY2Q { transition: width .3s ease; }
```

### motion-component-state-change-opacity-400-ease

```css
.Gallery_pageDescription__gzbMf { transition: opacity .4s ease; }
```

### motion-component-state-change-all-300-ease

```css
.Gallery_pageDescription__gzbMf>span { transition: all .3s ease; }
```

### motion-component-state-change-color-300-ease

```css
.Reel_next__jGdWP { transition: color .3s ease; }
```

### motion-component-state-change-color-300-ease

```css
.Reel_previous__h1vz0 { transition: color .3s ease; }
```

### motion-component-state-change-opacity-200-ease

```css
.InstallViaWinget_trigger__a4x9E { transition: opacity .2s ease; }
```

### motion-component-state-change-color-300-ease

```css
.InstallViaWinget_copyToClipboard__v4nU2 { transition: color .3s ease; }
```

### motion-component-state-change-opacity-150-ease

```css
.InstallViaWinget_icon__XAk8H { transition: opacity .15s ease; }
```

### motion-component-state-change-transform-150-ease

```css
.InstallViaWinget_icon__XAk8H { transition: transform .15s ease; }
```

### motion-component-load-animation-300-ease

```css
.InstallViaWinget_iconCopied__osOxD { animation: InstallViaWinget_iconSuccess__hI9N1 .3s ease; }
```

### motion-component-load-animation-1500-cubic-bezier-455-03-515-955

```css
.RaycastWindow_loadingIndicator__uCS_m:after { animation: RaycastWindow_loadingSweep__UKb0Y 1.5s cubic-bezier(.455,.03,.515,.955) forwards; }
```

### motion-component-state-change-opacity-300-cubic-bezier-4-0-2-1

```css
.AIShowCase_img__jstSw { transition: opacity .3s cubic-bezier(.4,0,.2,1); }
```

### motion-component-state-change-width-300-ease

```css
.AIShowCase_page__IYgfn { transition: width .3s ease; }
```

### motion-component-state-change-opacity-400-ease

```css
.AIShowCase_pageDescription__U91h0 { transition: opacity .4s ease; }
```

### motion-component-state-change-all-300-ease

```css
.AIShowCase_pageDescription__U91h0>span { transition: all .3s ease; }
```

### motion-component-state-change-color-300-ease

```css
.FeatureWall_wall__BRIeA .FeatureWall_text__KtcCg { transition: color .3s ease; }
```

### motion-component-state-change-box-shadow-200-ease-in-out

```css
.FeatureWall_desktopWrapper__a9h7u { transition: box-shadow .2s ease-in-out; }
```

### motion-component-state-change-box-shadow-200-ease-in-out

```css
.FeatureWall_desktop__y7X6D { transition: box-shadow .2s ease-in-out; }
```

### motion-component-state-change-opacity-600-cubic-bezier-4-0-22-96

```css
.FeatureWall_enterActive__jjjtR { transition: opacity .6s cubic-bezier(.4,0,.22,.96); }
```

### motion-component-state-change-transform-600-cubic-bezier-4-0-22-96

```css
.FeatureWall_enterActive__jjjtR { transition: transform .6s cubic-bezier(.4,0,.22,.96); }
```

### motion-hero-state-change-all-200-ease

```css
.HeroAnnouncement_announcementOuter__T5qC1 { transition: all .2s ease; }
```

### motion-hero-viewport-animation-3000-linear

```css
.HeroAnnouncement_announcementOuter__T5qC1.HeroAnnouncement_animate__T5ctC { animation: HeroAnnouncement_rotating2__GbW_t -.64s linear 3s infinite; }
```

### motion-component-state-change-text-underline-offset-100-ease-out

```css
.SectionParagraph_root__fSzgt a { transition: text-underline-offset .1s ease-out; }
```

### motion-component-state-change-transform-200-ease-out

```css
.ai-chat_root__QQJDJ .ai-chat_popover__jq15c { transition: transform .2s ease-out; }
```

### motion-component-state-change-opacity-400-ease-out

```css
.ai-chat_root__QQJDJ .ai-chat_popover__jq15c { transition: opacity .4s ease-out; }
```

### motion-component-state-change-transform-100-ease-out

```css
.ai-chat_popover__jq15c { transition: transform .1s ease-out; }
```

### motion-component-load-animation-1000-linear

```css
.FeaturebaseContent_spinner__EhePC { animation: FeaturebaseContent_spin__1K7tB 1s linear infinite; }
```

### motion-navigation-state-change-all-200-ease-in-out

```css
.NavLink_navLink__REP72 { transition: all .2s ease-in-out; }
```

### motion-component-state-change-text-underline-offset-100-ease-out

```css
.markdown :where(a):not(:where([class~=not-markdown],[class~=not-markdown] *)) { transition: text-underline-offset .1s ease-out; }
```

### motion-component-state-change-color-300-ease

```css
.ArrowLink_link__WKebC { transition: color .3s ease; }
```

### motion-component-state-change-transform-1500-cubic-bezier-165-84-44-1

```css
.ApiFig1_bottom__XigQ9 { transition: transform 1.5s cubic-bezier(.165,.84,.44,1); }
```

### motion-button-hover-backgroundcolor-200-ease-ease-ease-in-out-ease-in-out

```css
{"backgroundColor": "rgb(252, 252, 252)", "boxShadow": "rgba(0, 0, 0, 0.2) 0px -1px 0.4px 0px inset, rgb(255, 255, 255) 0px 1px 0.4px 0px inset, rgba(0, 0, 0, 0.5) 0px 0px 0px 2px, rgba(255, 255, 255, 0.19) 0px 0px 14px 0px"}
```

### motion-button-focus-backgroundcolor-200-ease-ease-ease-in-out-ease-in-out

```css
{"backgroundColor": "rgb(252, 252, 252)", "boxShadow": "rgba(0, 0, 0, 0.2) 0px -1px 0.4px 0px inset, rgb(255, 255, 255) 0px 1px 0.4px 0px inset, rgba(0, 0, 0, 0.5) 0px 0px 0px 2px, rgba(255, 255, 255, 0.19) 0px 0px 14px 0px"}
```

### motion-form-hover-style-300-ease-ease

```css
{"border": "1px solid rgba(255, 255, 255, 0.184)", "borderBottom": "1px solid rgba(255, 255, 255, 0.184)", "borderLeft": "1px solid rgba(255, 255, 255, 0.184)", "borderRight": "1px solid rgba(255, 255, 255, 0.184)", "borderTop": "1px solid rgba(255, 255, 255, 0.184)"}
```

### motion-form-focus-style-300-ease-ease

```css
{"border": "1px solid rgba(255, 255, 255, 0.184)", "borderBottom": "1px solid rgba(255, 255, 255, 0.184)", "borderLeft": "1px solid rgba(255, 255, 255, 0.184)", "borderRight": "1px solid rgba(255, 255, 255, 0.184)", "borderTop": "1px solid rgba(255, 255, 255, 0.184)"}
```

### motion-form-hover-style-300-ease-in-out-ease-in-out-ease-in-out

```css
{"cursor": "pointer"}
```

### motion-form-focus-style-300-ease-in-out-ease-in-out-ease-in-out

```css
{"cursor": "pointer"}
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
