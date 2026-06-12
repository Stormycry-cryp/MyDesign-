# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| component | load | animation | 1000ms | 0ms | linear | 组件load：animation 0 -> 1，1000ms linear，load 触发 |
| component | load | animation | 1000ms | 0ms | linear | 组件load：animation 0 -> 1，1000ms linear，load 触发 |
| component | state-change | color | 350ms | 0ms | ease-in-out | 组件state-change：color，350ms ease-in-out，state-change 触发 |
| component | state-change | opacity | 250ms | 0ms | ease-in-out | 组件state-change：opacity，250ms ease-in-out，state-change 触发 |
| component | state-change | outline | 250ms | 0ms | ease-in-out | 组件state-change：outline，250ms ease-in-out，state-change 触发 |
| component | state-change | border | 250ms | 0ms | ease-in-out | 组件state-change：border，250ms ease-in-out，state-change 触发 |
| navigation | state-change | top | 350ms | 0ms | ease-in-out | 导航state-change：top，350ms ease-in-out，state-change 触发 |
| navigation | state-change | background | 350ms | 0ms | ease-out | 导航state-change：background，350ms ease-out，state-change 触发 |
| navigation | state-change | opacity | 350ms | 0ms | ease-out | 导航state-change：opacity，350ms ease-out，state-change 触发 |
| navigation | state-change | margin | 1000ms | 0ms | ease-out | 导航state-change：margin，1000ms ease-out，state-change 触发 |
| component | state-change | height | 250ms | 0ms | ease-in-out | 组件state-change：height，250ms ease-in-out，state-change 触发 |
| component | state-change | transform | 500ms | 0ms | ease-in-out | 组件state-change：transform，500ms ease-in-out，state-change 触发 |
| component | state-change | opacity | 250ms | 0ms | ease-in-out | 组件state-change：opacity，250ms ease-in-out，state-change 触发 |
| component | state-change | opacity | 2000ms | 0ms | ease-in-out | 组件state-change：opacity，2000ms ease-in-out，state-change 触发 |
| component | state-change | width | 700ms | 0ms | ease-in-out | 组件state-change：width，700ms ease-in-out，state-change 触发 |
| component | state-change | height | 700ms | 0ms | ease-in-out | 组件state-change：height，700ms ease-in-out，state-change 触发 |
| component | load | animation | 1500ms | 0ms | ease-in-out | 组件load：animation scale(0) -> scale(1)，1500ms ease-in-out，load 触发 |
| component | state-change | background | 700ms | 0ms | ease-in-out | 组件state-change：background，700ms ease-in-out，state-change 触发 |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: assets/2026-06-11-pitch-interactive-data-studio-motion.json

## Missing Evidence
- motion-component-state-change-filter-300-missing lacks easing
- motion-component-state-change-opacity-300-missing lacks easing
- motion-component-state-change-filter-300-missing lacks easing
- motion-component-state-change-opacity-300-missing lacks easing
- motion-component-state-change-opacity-300-missing lacks easing

## Snippet Appendix
### motion-component-load-animation-1000-linear

```css
.project .column { animation: fadeIn 1s linear; }
```

### motion-component-load-animation-1000-linear

```css
img { animation: fadeIn 1s linear; }
```

### motion-component-state-change-color-350-ease-in-out

```css
.footer .copyright span { transition: color .35s ease-in-out; }
```

### motion-component-state-change-opacity-250-ease-in-out

```css
.ProjectThumb_projectThumb__fkKmL img { transition: opacity .25s ease-in-out; }
```

### motion-component-state-change-outline-250-ease-in-out

```css
.ProjectThumb_projectThumb__fkKmL img { transition: outline .25s ease-in-out; }
```

### motion-component-state-change-border-250-ease-in-out

```css
.ProjectThumb_projectThumb__fkKmL img { transition: border .25s ease-in-out; }
```

### motion-navigation-state-change-top-350-ease-in-out

```css
.Carousel_miniNav___RYr7 { transition: top .35s ease-in-out; }
```

### motion-navigation-state-change-background-350-ease-out

```css
.Carousel_miniNav___RYr7 .Carousel_carousel__xOvqJ .Carousel_controls__24SHy .Carousel_control__R49N3 { transition: background .35s ease-out; }
```

### motion-navigation-state-change-opacity-350-ease-out

```css
.Carousel_miniNav___RYr7 .Carousel_carousel__xOvqJ .Carousel_controls__24SHy .Carousel_control__R49N3 { transition: opacity .35s ease-out; }
```

### motion-navigation-state-change-margin-1000-ease-out

```css
.Carousel_miniNav___RYr7 .Carousel_carousel__xOvqJ .Carousel_list__Bf5Ul { transition: margin 1s ease-out; }
```

### motion-component-state-change-height-250-ease-in-out

```css
.Project_project__V8eh_ .Project_slideContainer__NxUHH { transition: height .25s ease-in-out; }
```

### motion-component-state-change-transform-500-ease-in-out

```css
.Project_project__V8eh_ .Project_slide__gDe1J { transition: transform .5s ease-in-out; }
```

### motion-component-state-change-opacity-250-ease-in-out

```css
.Project_project__V8eh_ .Project_info__fMMTL .Project_section__sEyKr a { transition: opacity .25s ease-in-out; }
```

### motion-component-state-change-opacity-2000-ease-in-out

```css
.ImageThatFadesIn_imageThatFadesIn__Ctjfj { transition: opacity 2s ease-in-out!important; }
```

### motion-component-state-change-width-700-ease-in-out

```css
.Contact_contact__3Paot { transition: width .7s ease-in-out; }
```

### motion-component-state-change-height-700-ease-in-out

```css
.Contact_contact__3Paot { transition: height .7s ease-in-out; }
```

### motion-component-load-animation-1500-ease-in-out

```css
.Contact_contact__3Paot .Contact_form__4E_4r .Contact_overlay__cmzPa .Contact_loading__ZPZ14 .Contact_dot__wwcuT { animation: Contact_scaleInOut___JIj0 1.5s ease-in-out infinite; }
```

### motion-component-state-change-background-700-ease-in-out

```css
.Contact_contact__3Paot .Contact_submit__kzzM1 { transition: background .7s ease-in-out; }
```

## Do Not Copy
- Do not copy the wordmark, proprietary imagery, product claims, copywriting, exact typefaces, or brand-specific mythology.
- Do not claim a motion library is used unless it appears in direct code evidence above.
