# Motion And Code

## Observed
| Selector Role | Trigger | Property | Duration | Delay | Easing | Description |
|---|---|---|---|---|---|---|
| button | load | animation | 2000ms | 0ms | linear | 按钮load：animation rotate(0deg) -> rotate(1turn)，2000ms linear，load 触发 |
| card | state-change | opacity | 200ms | 0ms | linear | 卡片state-change：opacity，200ms linear，state-change 触发 |
| component | state-change | opacity | 200ms | 0ms | linear | 组件state-change：opacity，200ms linear，state-change 触发 |
| reveal | viewport | transform | 250ms | 0ms | cubic-bezier(0, 0, 0.25, 1) | 入场元素viewport：transform，250ms cubic-bezier(0, 0, 0.25, 1)，viewport 触发 |
| card | state-change | all | 50ms | 0ms | linear | 卡片state-change：all missing -> translateY(0.1rem)，50ms linear，state-change 触发 |
| component | load | animation | 1300ms | 0ms | linear | 组件load：animation，1300ms linear，load 触发 |

## Inference
- Motion entries are normalized from declaration-level CSS parse or explicit retained motion evidence.
- Source motion path: assets/2026-06-11-oma-motion.json

## Missing Evidence
- motion-component-state-change-opacity-200-missing lacks easing
- motion-component-load-animation-2000-missing lacks easing
- motion-component-state-change-opacity-150-missing lacks easing
- motion-component-state-change-opacity-40-missing lacks easing

## Snippet Appendix
### motion-button-load-animation-2000-linear

```css
.mapboxgl-ctrl button.mapboxgl-ctrl-geolocate.mapboxgl-ctrl-geolocate-waiting .mapboxgl-ctrl-icon { animation: mapboxgl-spin 2s linear infinite; }
```

### motion-card-state-change-opacity-200-linear

```css
/* zoom and fade animations */
.leaflet-fade-anim .leaflet-tile { transition: opacity 0.2s linear; }
```

### motion-component-state-change-opacity-200-linear

```css
.leaflet-fade-anim .leaflet-popup { transition: opacity 0.2s linear; }
```

### motion-reveal-viewport-transform-250-cubic-bezier-0-0-0-25-1

```css
.leaflet-zoom-anim .leaflet-zoom-animated { transition: transform 0.25s cubic-bezier(0, 0, 0.25, 1); }
```

### motion-card-state-change-all-50-linear

```css
.project-page__filter__list-item:before { transition: all 0.05s linear; }
```

### motion-component-load-animation-1300-linear

```css
.index__static-content { animation: blink 1.3s linear 0ms; }
```

## Do Not Copy
- Do not copy the exact OMA navigation treatment, project names, or red/white alert framing verbatim.
- Do not copy the photographic subject matter or city-scene composition.
- Do not imply motion behavior that was not directly evidenced.
