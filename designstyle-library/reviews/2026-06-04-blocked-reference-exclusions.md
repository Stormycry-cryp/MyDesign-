# Blocked Reference Exclusions

Date: 2026-06-04

The following references were removed from the active designstyle library because the live recrawl captured a security/challenge page rather than the intended product UI. They are preserved under excluded folders as evidence and do not count toward active reference totals or design-system quality scores.

| Slug | Reason | Preserved Evidence |
|---|---|---|
| `arc-browser-product-site` | Live recrawl returned `Attention Required! | Cloudflare` and component samples such as `Cloudflare Ray ID` / `Performance & security by Cloudflare`; not a reusable product/component style reference. | `references-excluded/blocked/2026-06-03-arc-browser-product-site.md`, `assets-excluded/blocked/2026-06-04-arc-browser-product-site-component-styles.json`, `screenshots-excluded/blocked/arc-browser-product-site-desktop.png` |

Rule: Cloudflare/captcha/security challenge pages must be excluded or replaced with clean visual evidence before a reference can count as active.
