<div align="center">

# DesignStyle

#### 给 Codex 用的视觉风格参考库：把好看的网页/产品页拆成可检索、可套用、可验证的设计证据

[![Release](https://img.shields.io/badge/Release-v0.2.8-3B82F6?style=for-the-badge)](./docs/releases/v0.2.8.md)
[![References](https://img.shields.io/badge/References-95-10B981?style=for-the-badge)](#designstyle-library参考库)
[![Quality](https://img.shields.io/badge/Quality-91.6%2F100-8B5CF6?style=for-the-badge)](./designstyle-library/reviews/2026-06-12-final2-design-system-quality-scores.md)

![Codex](https://img.shields.io/badge/Codex-Skill-10B981?style=flat-square&logo=openai&logoColor=white)
![Design Reference](https://img.shields.io/badge/Design_Reference-Library-3B82F6?style=flat-square)
![Apply Pack](https://img.shields.io/badge/Apply_Pack-CSS%20%2B%20Tailwind%20%2B%20Motion-D97706?style=flat-square)

</div>

做 UI 的时候，最怕的不是没有灵感，而是只剩一句"高级一点"、"像某某网站"。

DesignStyle 干的事很朴素：把一个真实网站、产品页、仪表盘或 app screen 拆成可以复用的证据，包括截图、首屏结构、字体层级、色彩 token、间距节奏、组件状态、动效参数和适用/不适用边界。等下次要做页面时，Agent 先检索这些证据，再把可复用的部分变成页面方案和 Apply Pack，而不是凭感觉乱抄。

这不是灵感图库。它更像一个给 Agent 用的本地视觉记忆库。

---

## 目录

| 名字 | 一句话 | 入口 |
|---|---|---|
| [designstyle（路由器）](#designstyle路由器) | 判断这次是要新增参考、使用参考，还是先新增再使用 | [SKILL.md](./skills/designstyle/SKILL.md) |
| [add-designstyle（入库）](#add-designstyle入库) | 把 URL / 截图 / 页面拆成可复用的 L1-L3 参考和设计系统包 | [SKILL.md](./skills/add-designstyle/SKILL.md) |
| [use-designstyle（套用）](#use-designstyle套用) | 从本地库检索场景匹配的参考，生成方向、Apply Pack 和对照 QA | [SKILL.md](./skills/use-designstyle/SKILL.md) |
| [designstyle-library（参考库）](#designstyle-library参考库) | 95 个有效参考，含截图、L1 cards、L2 dimensions、L3 references、motion 和 tokens | [README](./designstyle-library/README.md) |

---

## 安装

把三个 skill 和本地参考库复制到 Codex 目录：

```bash
rsync -a skills/designstyle ~/.codex/skills/
rsync -a skills/add-designstyle ~/.codex/skills/
rsync -a skills/use-designstyle ~/.codex/skills/
rsync -a designstyle-library/ ~/.codex/designstyle-library/
```

装好之后，Codex 里可以直接说：

```text
/designstyle 参考这个网站，帮我收录成风格库
/designstyle 用库里的 dashboard 参考做一个分析后台
add-designstyle https://example.com
use-designstyle 做一个深色开发者文档站
```

---

## Skills

<a id="designstyle路由器"></a>

<table>
<tr><td>

### designstyle（路由器）

> 当你只说"designstyle"时，它负责先判断应该走哪条路。

它是一个很薄的协调层。用户给了 URL、截图、参考网站，它会路由到 `add-designstyle`；用户要设计页面、重做界面、借鉴本地参考，它会路由到 `use-designstyle`；如果用户说"先学这个，再按这个做一个页面"，它会按 `add-designstyle -> use-designstyle` 顺序执行。

**它解决的问题**

- 不让 Agent 把"新增参考"误当成"马上设计页面"。
- 不让 Agent 在证据不够时硬套风格。
- 统一报告读过哪些证据层：L0 router、L1 card、L2 dimension、L3 full reference、L4 on-demand evidence。

**怎么触发**

```text
/designstyle
designstyle 参考这个网站
帮我学一下这个页面风格
用本地 designstyle 做一个 landing page
```

-> [SKILL.md](./skills/designstyle/SKILL.md)

</td></tr>
</table>

<a id="add-designstyle入库"></a>

<table>
<tr><td>

### add-designstyle（入库）

> 把一个好看的页面，拆成未来真的能拿来用的风格规格。

`add-designstyle` 不写赞美词。它会看页面首屏、截图、DOM/CSS 线索、组件 computed style、hover/focus 状态、动效和证据边界，然后写入本地参考库。一个参考只有通过验证，才算 active usable。

**它会生成什么**

- L3 full reference：`designstyle-library/references/YYYY-MM-DD-<slug>.md`
- L1 card：`designstyle-library/indexes/cards/<slug>.json`
- L2 dimensions：`scene`、`layout-spacing`、`type-copy`、`color-surface`、`assets`、`motion-code`、`components-states`
- Design system pack：`tokens.json`、`palette.md`、`moodboard.svg`、`component-styles.md`
- Apply Pack：`variables.css`、`tailwind.theme.json`、`motion-presets.css`
- Motion evidence：`motion.json`，只把字段完整的动效放进 reusable `items`

**它会挡掉什么**

- Cloudflare / security challenge 页面
- 空白页、404、cookie/region 弹窗污染严重的截图
- 视觉普通、模板感太强、首屏证据不足的候选
- 解析不出的 token 或 motion 参数；这些必须标 `missing`，不能编造
- 完整专有 CSS/JS；只保留短证据片段和可复用参数

**怎么触发**

```text
add-designstyle https://example.com
把这个截图收进设计参考库
拆解这个产品页的视觉系统
这一批官网先做候选筛选，不要直接入库
```

-> [SKILL.md](./skills/add-designstyle/SKILL.md)

</td></tr>
</table>

<a id="use-designstyle套用"></a>

<table>
<tr><td>

### use-designstyle（套用）

> 做页面前先查库，做完后再跟参考对照，不靠一句"像一点"糊弄自己。

`use-designstyle` 会先分析任务场景，再从 L1 cards 里检索候选。检索不是只看风格词，而是先用 category 和 page scope 卡住场景，再按布局、字体、色彩、资产、动效、组件证据分通道打分。

**它的工作流**

- 先写 Task Analysis：要做什么页面、面向谁、需要什么证据等级。
- 搜索场景匹配的参考，输出可借/不可借维度。
- 生成 `work/designstyle-direction-plan.md`，里面必须有 Apply Pack 路径。
- 构建时先落地 `variables.css`、`tailwind.theme.json`、`motion-presets.css`。
- 首轮完成后跑 `compare_against_reference.py`，生成参考对照表。
- 最终 QA 需要截图证据：immediate-load、post-animation、hover/focus、mobile、reduced-motion。

**适合**

- dashboard / docs / landing page / product page / portfolio / app screen
- 想从多个参考里拼出一个新视觉系统
- 想让动效、间距、字体层级和组件状态都有来源可追溯

**不适合**

- 只想随口要一个"高级感"方向，不在乎证据
- 想直接复制某个品牌的图片、文案、logo 或完整页面
- 本地库没有对应场景，还要求实现级还原

**怎么触发**

```text
use-designstyle 做一个 dark analytics dashboard
从库里找奢侈品 landing 的参考，做一个方向 plan
用本地参考重做这个 docs 首页，最后给对照截图
```

-> [SKILL.md](./skills/use-designstyle/SKILL.md)

</td></tr>
</table>

---

## designstyle-library（参考库）

<a id="designstyle-library参考库"></a>

当前 `v0.2.8` 快照包含：

| 层级 | 数量 | 作用 |
|---|---:|---|
| Active L3 references | 95 | 完整 Markdown 证据记录 |
| Active screenshots | 95 | 每个 active reference 一张桌面证据截图 |
| L1 cards | 95 | 快速检索、排序、Style DNA 注入 |
| L2 dimensions | 665 | 每个参考拆成 7 个维度摘要 |
| Component JSON | 95 | 浏览器 computed style、几何、hover/focus 证据 |
| Design-system packs | 95 | tokens、palette、moodboard、component styles、motion |
| Apply Pack files | 285 | `variables.css`、`tailwind.theme.json`、`motion-presets.css` |
| Excluded references | 10 | 被保留但不参与 active retrieval 的失败/阻塞/不适合候选 |

库里覆盖的参考类型包括 SaaS、dashboard、developer platform、docs、analytics、finance、data storytelling、luxury automotive、fashion、jewelry、watch、architecture studio、editorial/culture、typography resource 等。

更多结构说明见 [designstyle-library/README.md](./designstyle-library/README.md)。

---

## v0.2.8 做了什么

`v0.2.8` 是一次把"截图 + CSS 片段堆"升级成"可检索、可套用、可对照"的版本。

**Add 侧**

- `motion.json` 结构化保存 selector role、trigger、property、duration、delay、easing、reduced-motion、source 和人话描述。
- L2 `motion-code.md` 改成清单表在前，snippet 只做附录。
- `tokens.json` 拆成 evidence/apply 两层；聚不出来的值保留 `missing`。
- 每个 design-system pack 生成 `variables.css`、`tailwind.theme.json`、`motion-presets.css`。
- `clean_reference_noise.py --check` 增加截断 CSS、autofill、consent、cookie、captcha 噪声检查。

**Use 侧**

- `search_references.py` 支持结构化 `--need` 查询。
- 检索先硬过滤 category/page scope，再按维度评分。
- Direction plan 必须列 Apply Pack 路径。
- 新增 `compare_against_reference.py`，用截图和 DNA checklist 做生成结果对照。
- 新增 `run_blind_e2e.py`，覆盖 dashboard、luxury landing、docs-site 三个盲测场景。

完整发布说明见 [docs/releases/v0.2.8.md](./docs/releases/v0.2.8.md)。

---

## 验证

发布前验证结果：

- Unit tests：40 passed
- Python compile：passed
- L3 validator：95 valid / 0 invalid
- Progressive validator：95 cards / 0 invalid / 0 errors
- Noise check：passed
- Quality score：91.6 / 100 average
- Search regression：15 / 15 top3，wrong top1 = 0
- Blind E2E：dashboard、luxury landing、docs-site 三个场景全部通过

常用命令：

```bash
python3 -m unittest skills.add-designstyle.tests.test_progressive_library -q
python3 -m py_compile skills/add-designstyle/scripts/*.py skills/use-designstyle/scripts/*.py
python3 skills/add-designstyle/scripts/validate_references.py --library designstyle-library --json
python3 skills/add-designstyle/scripts/validate_progressive_library.py --library designstyle-library --json
python3 skills/add-designstyle/scripts/clean_reference_noise.py --library designstyle-library --check
python3 skills/use-designstyle/scripts/run_search_regression.py --library designstyle-library --json-output designstyle-library/reviews/2026-06-12-final2-search-regression.json
```

---

## 证据边界

DesignStyle 保留的是可迁移设计决策，不是别人的整站源码。

**可以复用**

- 布局结构、比例、间距节奏、组件密度
- 色彩角色、surface grammar、token 命名
- 动效机制、duration/easing/trigger/reduced-motion 策略
- 文案节奏和信息层级，不是原文

**不能直接复用**

- 原始图片、视频、logo、商标、产品名、品牌概念
- 完整专有 CSS/JS
- 原站完整页面编排
- 无法从证据中证明的 token、motion 参数或组件状态

---

## 适合谁

如果你经常让 Codex 做 UI，这个库主要解决三个问题：

- **审美不漂**：先查参考证据，再出方向。
- **实现不虚**：tokens、motion、component state 都有文件可落地。
- **结果可查**：构建后能跟参考截图、Style DNA、QA state 对照。

如果你只是想收集漂亮截图，普通 bookmark 工具更轻。DesignStyle 的价值在于让 Agent 以后真的用得上。

---

<div align="center">

Made for Codex design workflows.

</div>
