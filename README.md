<div align="center">

# MyDesign

#### 跨平台 AI 设计素材库 + DesignStyle Skills

[![Release](https://img.shields.io/badge/Release-v0.2.8-3B82F6?style=for-the-badge)](./docs/releases/v0.2.8.md)
[![References](https://img.shields.io/badge/References-95-10B981?style=for-the-badge)](#素材库包含什么)
[![Platforms](https://img.shields.io/badge/macOS%20%2B%20Windows-supported-D97706?style=for-the-badge)](#安装)
[![Agents](https://img.shields.io/badge/Codex%20%2F%20Claude%20%2F%20OpenCode%20%2F%20OpenClaw-ready-8B5CF6?style=for-the-badge)](#agent-适配)

![Codex](https://img.shields.io/badge/Codex-Skill-10B981?style=flat-square&logo=openai&logoColor=white)
![Claude](https://img.shields.io/badge/Claude_Code-Skill-D97706?style=flat-square&logo=anthropic&logoColor=white)
![OpenCode](https://img.shields.io/badge/OpenCode-Skill-3B82F6?style=flat-square)
![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-8B5CF6?style=flat-square)

</div>

MyDesign 是给 AI Agent 用的本地设计素材库。

它不是普通截图收藏夹，而是把真实网页、产品页、dashboard、docs、landing page 拆成 Agent 能检索、能套用、能验证的设计证据：截图、首屏结构、字体层级、色彩 token、间距节奏、组件状态、动效参数、Apply Pack 和证据边界。

你可以把它装到 Codex、Claude Code、OpenCode 或 OpenClaw。macOS 和 Windows 都能用。

---

## 目录

| 模块 | 一句话 | 路径 |
|---|---|---|
| `designstyle` | 路由器：判断要新增参考、使用参考，还是先新增再使用 | [skills/designstyle](./skills/designstyle/SKILL.md) |
| `add-designstyle` | 入库：把 URL / 截图 / 页面拆成可复用风格证据 | [skills/add-designstyle](./skills/add-designstyle/SKILL.md) |
| `use-designstyle` | 套用：从素材库检索参考，生成方向、Apply Pack 和对照 QA | [skills/use-designstyle](./skills/use-designstyle/SKILL.md) |
| `designstyle-library` | 素材库：95 个有效参考和完整生成层 | [designstyle-library](./designstyle-library/README.md) |
| `install.py` | macOS / Windows 通用安装器 | [install.py](./install.py) |

---

## 安装

### 推荐方式：Python 安装器

macOS、Windows PowerShell、Git Bash 都可以运行：

```bash
python3 install.py --agent codex
```

安装到多个 Agent：

```bash
python3 install.py --agent codex,claude,opencode,openclaw
```

安装到全部支持的 Agent：

```bash
python3 install.py --agent all
```

只安装 skills，不复制 164MB 素材库：

```bash
python3 install.py --agent codex --skills-only
```

复制素材库到自定义位置：

```bash
python3 install.py --agent codex --library-path /path/to/designstyle-library
```

Windows PowerShell 示例：

```powershell
py -3 .\install.py --agent codex --library-path "$env:USERPROFILE\.codex\designstyle-library"
```

### 手动安装

macOS / Linux:

```bash
mkdir -p ~/.codex/skills
cp -R skills/designstyle ~/.codex/skills/
cp -R skills/add-designstyle ~/.codex/skills/
cp -R skills/use-designstyle ~/.codex/skills/
cp -R designstyle-library ~/.codex/designstyle-library
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force .\skills\designstyle "$env:USERPROFILE\.codex\skills\designstyle"
Copy-Item -Recurse -Force .\skills\add-designstyle "$env:USERPROFILE\.codex\skills\add-designstyle"
Copy-Item -Recurse -Force .\skills\use-designstyle "$env:USERPROFILE\.codex\skills\use-designstyle"
Copy-Item -Recurse -Force .\designstyle-library "$env:USERPROFILE\.codex\designstyle-library"
```

---

## Agent 适配

默认素材库路径是：

```text
~/.codex/designstyle-library
```

所有脚本都支持用环境变量覆盖素材库位置：

```bash
export DESIGNSTYLE_LIBRARY="/absolute/path/to/designstyle-library"
```

Windows PowerShell:

```powershell
$env:DESIGNSTYLE_LIBRARY = "C:\path\to\designstyle-library"
```

| Agent | 默认 skill 安装目录 | 推荐命令 |
|---|---|---|
| Codex | `~/.codex/skills` | `python3 install.py --agent codex` |
| Claude Code | `~/.claude/skills` | `python3 install.py --agent claude` |
| OpenCode | `~/.config/opencode/skills` | `python3 install.py --agent opencode` |
| OpenClaw | `~/.openclaw/skills` | `python3 install.py --agent openclaw` |

如果某个 Agent 不读取上表目录，也可以把 `skills/<name>` 整个文件夹复制到它自己的 skills 目录。核心要求只有两个：

- Agent 能读到三个 `SKILL.md`。
- 脚本能找到 `designstyle-library`，要么放在 `~/.codex/designstyle-library`，要么设置 `DESIGNSTYLE_LIBRARY`。

---

## 怎么用

装好后，可以直接对 Agent 说：

```text
/designstyle 参考这个网站，帮我收录成风格库
/designstyle 用库里的 dashboard 参考做一个分析后台
add-designstyle https://example.com
use-designstyle 做一个深色开发者文档站
```

三个 skill 分工很清楚：

### designstyle

路由器。它判断这次应该走 `add-designstyle`、`use-designstyle`，还是 `add-designstyle -> use-designstyle`。

适合这种话：

```text
designstyle 参考这个网站
用本地 designstyle 做一个 landing page
先学这个页面，再按这个风格做一个 dashboard
```

### add-designstyle

入库工具。它会把 URL、截图或页面拆成 L1/L2/L3 参考、design-system pack、motion evidence 和 Apply Pack。

它会生成：

- L3 reference：`designstyle-library/references/YYYY-MM-DD-<slug>.md`
- L1 card：`designstyle-library/indexes/cards/<slug>.json`
- L2 dimensions：`designstyle-library/dimensions/<slug>/*.md`
- Design system：`tokens.json`、`palette.md`、`moodboard.svg`、`component-styles.md`
- Motion：`motion.json`、`motion-presets.css`
- Apply Pack：`variables.css`、`tailwind.theme.json`、`motion-presets.css`

### use-designstyle

套用工具。它会先检索素材库，再生成方向计划和 Apply Pack；做完后还能用参考截图和 Style DNA 做对照。

它不会只靠"高级感"、"像 Apple"这种词工作。检索会先看 category/page scope，再看字体、色彩、布局、资产、动效和组件证据。

---

## 素材库包含什么

当前 `v0.2.8` 素材库约 164MB，包含：

| 内容 | 数量 | 说明 |
|---|---:|---|
| Active references | 95 | 可检索、可复用的完整 Markdown 风格参考 |
| Screenshots | 95 | 每个 active reference 一张桌面证据截图 |
| Component JSON | 95 | 浏览器 computed style、几何、hover/focus 证据 |
| L1 cards | 95 | 快速检索、排序、Style DNA 注入 |
| L2 dimensions | 665 | 每个参考拆成 7 个维度摘要 |
| Design-system packs | 95 | tokens、palette、moodboard、component styles、motion |
| Apply Pack files | 285 | CSS variables、Tailwind theme、motion presets |
| Excluded references | 10 | 保留但不参与 active retrieval 的失败/阻塞/不适合候选 |
| Reviews / QA evidence | 多组 | 候选筛选、质量评分、搜索回归、blind E2E 对照截图 |

素材库目录：

```text
designstyle-library/
  references/              # L3 完整参考
  references-excluded/     # 被排除的参考
  screenshots/             # active 桌面截图素材
  screenshots-excluded/    # excluded 截图证据
  assets/                  # component-style JSON 与 motion capture
  assets-excluded/         # blocked/rejected evidence
  indexes/cards/           # L1 cards
  dimensions/              # L2 维度摘要
  design-systems/          # tokens / palette / moodboard / motion / Apply Pack
  reviews/                 # 评分、回归、blind E2E、候选报告
```

覆盖类型包括 SaaS、dashboard、developer platform、docs、analytics、finance、data storytelling、luxury automotive、fashion、jewelry、watch、architecture studio、editorial/culture、typography resource 等。

---

## v0.2.8 能力

`v0.2.8` 重点是把"截图 + CSS 片段堆"升级成可应用的风格规格。

**Add 侧**

- `motion.json` 结构化保存 selector role、trigger、property、duration、delay、easing、reduced-motion、source 和人话描述。
- L2 `motion-code.md` 改成清单表在前，snippet 只做附录。
- `tokens.json` 拆成 evidence/apply 两层；聚不出来的值保留 `missing`。
- 每个 design-system pack 生成 `variables.css`、`tailwind.theme.json`、`motion-presets.css`。
- 噪声检查覆盖截断 CSS、autofill、consent、cookie、captcha 和异常 `px` 值。

**Use 侧**

- 支持结构化 `--need` 查询，例如 `motion:L2,palette:dark,scene:dashboard`。
- 检索先硬过滤 category/page scope，再按维度评分。
- Direction plan 必须列 Apply Pack 路径。
- `compare_against_reference.py` 用截图和 DNA checklist 做生成结果对照。
- `run_blind_e2e.py` 覆盖 dashboard、luxury landing、docs-site 三个盲测场景。

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
python skills/add-designstyle/scripts/validate_references.py --library designstyle-library --json
python skills/add-designstyle/scripts/validate_progressive_library.py --library designstyle-library --json
python skills/add-designstyle/scripts/clean_reference_noise.py --library designstyle-library --check
python skills/use-designstyle/scripts/run_search_regression.py --library designstyle-library --json-output designstyle-library/reviews/2026-06-12-final2-search-regression.json
```

Windows PowerShell 如果不展开 `*.py`，可以分目录运行或使用 Git Bash；核心脚本都可以直接传 `--library designstyle-library`。

---

## 证据边界

MyDesign 保留的是可迁移设计决策，不是别人的整站源码。

可以复用：

- 布局结构、比例、间距节奏、组件密度
- 色彩角色、surface grammar、token 命名
- 动效机制、duration/easing/trigger/reduced-motion 策略
- 文案节奏和信息层级

不能直接复用：

- 原始图片、视频、logo、商标、产品名、品牌概念
- 完整专有 CSS/JS
- 原站完整页面编排
- 无法从证据中证明的 token、motion 参数或组件状态

解析不出的值必须保留 `missing`，不能编造。

---

<div align="center">

Built for AI design agents on macOS and Windows.

</div>
