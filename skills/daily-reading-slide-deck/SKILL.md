---
name: daily-reading-slide-deck
description: >
  双轨日读输出（wiki笔记+Slide Deck），一个感慨一张slide。
---

# Daily Reading Slide Deck — 双轨日读输出

## 触发

- 用户引用一段文字/文章/书摘，需要产出当日讨论记录
- 用户说"日读""即兴""留白问题""桥接概念"
- 需要把 wiki 的书面笔记转化为交流用的 Slide Deck

## 双轨并存（绝不删除）

**轨道 1：wiki 日读笔记（面向检索）**
- 路径：`~/developing/open-source-way-wiki/raw/articles/reading-notes/`
- 格式：桥接概念 + 延伸悖论 + 留白问题 + 适兕判断
- 文件命名：`<topic>-YYYY-MM-DD.md`

**轨道 2：Slide Deck（面向口头交流）**
- 路径：`~/developing/markdown-to-slides/daily-reading/YYYY-MM/YYYY-MM-DD.md`
- 必须严格遵循 `template.md` 格式（封面 + 内容 slide）
- 文件命名：`daily-reading/<年-月>/<年-月-日>.md`

> ⚠️ 两条轨道同日并存，互不替代。适兕明确说"绝不删除"。

## 写入前必做（五项缺一不可，顺序不可颠倒）

> ⛔ **致命规则：这六项不在开始写文件之前执行，就是在犯错。** 适兕曾在 2026-08-01 和 2026-08-06 亲自纠正——一次写错日期（7-31 写成 8-1，8月4日内容写进 8月1日文件），一次未按 template.md 格式写成了 8 张 slide。2026-08-16 再次违反：context compaction 后未重新加载 skill 就直接写，导致一次感慨拆成 6 张 slide + Cover 写了实际内容。这些错误不是"疏忽"，是**跳过了前置检查步骤**。

0. **重新加载 skill**：`skill_view(name='daily-reading-slide-deck')`——context compaction 会丢失 skill 内容，必须重新加载。**跳过此步 = 凭记忆写 = 必错。**
1. **确认日期**：`date +%Y-%m-%d`（不要凭记忆——跨天是最高频的错误源）
2. **读 template.md**：`read_file("~/developing/markdown-to-slides/template.md")`——这是**模板，不是参考**。不按它写就是写错。
3. **检查月目录**：`ls ~/developing/markdown-to-slides/daily-reading/`——确认月目录存在，文件命名规则（`<年-月-日>.md`）正确
4. **Git pull 所有相关仓库**（多人/agent 操作，**必须执行**）
   ```bash
   cd ~/developing/markdown-to-slides && git pull
   cd ~/developing/open-source-way-wiki && git pull
   cd ~/developing/ttoos && git pull                 # 如操作博客仓库
   cd ~/developing/open-source-way-cronjob && git pull  # 如操作 cronjob
   ```
   > 适兕明确："git 不止一个人/agent在操作，修改之前一定要pull"。
5. **确认目标文件是否存在**：另一个 session 可能已创建今天日期的文件（如 2026-08-06 已在另一个 session 建好）
   - **文件存在** → 直接追加到已有文件的末尾（按 block-based 插入规则），不要新建同名文件
   - **文件不存在** → 从 `template.md` 创建新文件：提取模板的 8 个 deck 元数据段（文档用途/使用场景/听众画像/讲者视角/核心诉求/核心基调/视觉风格关键词/内容结构约定）+ Cover slide + 新内容。见下方"新建文件规则"

   - **⚠️ 清理模板默认 slide**：`template.md` 包含默认的 Slide 1-6（封面、为什么读这本书、核心洞察、关键概念、与开源的关系、延伸思考），这些是占位内容，**创建新文件后必须删除**。使用以下命令：
     ```bash
     # 保留模板头部（到 --- 分隔线），删除默认 slide，保留/追加自定义 slide
     sed -n '1,/^---$/p' daily-reading/YYYY-MM/YYYY-MM-DD.md > /tmp/clean.md
     echo "" >> /tmp/clean.md
     # 追加自定义内容到 /tmp/clean.md，然后覆盖原文件
     ```
     或使用 Python 脚本：找到 `---` 分隔线后的第一个 `## Slide`，保留头部到 `---`，删除中间默认 slide，保留或追加自定义 slide。

6. **⚠️ Cover 必须写 `[待生成]`**：新建文件时 Cover 的主标题和副标题**必须**使用 `[待生成]` 占位符——绝不可用书名、首条书摘或任何实际内容填充。**`[待生成]` 是自动化管线的触发标记**：cron 00:30 和 01:00 都依赖它判断是否需要生成 Cover。如果跳过这一步（写入了实际内容而非 `[待生成]`），cron 会跳过，Cover 就不会自动生成——这就是 2026-08-11 的问题。2026-08-16 再次违反：直接将 Cover 主标题写为"制度当作重力背景板：认知底座与无效沟通"，副标题写为完整句子，被适兕纠正为 `[待生成]`——因为 Cover 应概括全天整体主题，不是当次感慨的标题。

   ```markdown
   ## Slide 1: Cover
   * **主标题：** [待生成]
   * **副标题：** [待生成]
   * **讲者信息：** 「开源之道」·适兕
   * **时间/地点：** <年.月.日>
   ```

   适兕可在任意时间手动将 `[待生成]` 替换为最终标题（cron 检测到占位符消失即跳过）。

## ⚠️ Weixin session 日期丢失（最高频致命错误）

> **2026-08-01 及 2026-08-06 两次发生：适兕说"今天8月6日"时，weixin session 上下文显示"今天8月1日/4日"——原因是 Weixin gateway 不向系统 prompt 注入当前日期，session 上下文停留在 compaction 时的旧日期。**
>
> **适兕明确反馈："你觉得是你这个 weixin session 的问题，其它 message platform 不会有这种日期问题。"**
>
> **操作规则：**
> 1. 每次开始写任何文件（wiki / slide）**之前**，**必须**执行 `date +%Y-%m-%d` 获取当前日期——**绝不允许用对话中任何"今天=X月X日"的信息**，因为 Weixin session 的上下文日期是假的
> 2. wiki 文件 `created:` 字段、slide 文件名、slide 封面日期——全部用 `date` 命令拿到的值，不用对话里的日期
> 3. 写入后发现日期错误：立即 `git commit --amend --reset-author` 修正，必要时 `--force-with-lease`

## Cover 占位与自动生成（2026-08-10 起生效）

> **规则**：新建日读文件时，Cover 的主标题和副标题使用 `[待生成]` 占位符。适兕可在任何时间手动填充；若适兕未填充，00:30 和 01:00 两个 cron 会自动兜底生成。

**新建文件时的 Cover 格式（`[待生成]` 是触发标记）：**

```markdown
## Slide 1: Cover

* **主标题：** [待生成]
* **副标题：** [待生成]
* **讲者信息：** 「开源之道」·适兕
* **时间/地点：** <年.月.日>
```

**填充协议（两种路径，路径 A 优先；路径 B/C 是兜底）：**

| 路径 | 触发时机 | 执行者 | 检测方式 |
|---|---|---|---|
| A. 适兕手动 | 适兕完成当日总结后 | 适兕 / 窄廊 | 直接 patch Cover 段落 |
| B. Cover cron 自动 | 每日 00:30 | `daily-cover-generate.md` → `generate-cover.py` | 检测 `[待生成]` 是否存在 |
| C. PPT cron 自动 | 每日 01:00 PPTX 渲染前 | `daily-reading-ppt.md` → `generate-cover.py` | 脚本内部再次检测 |

**路径 B/C 自动生成逻辑：**

1. cron prompt 显式指定执行 `python3 ~/developing/open-source-way-cronjob/scripts/generate-cover.py --date YYYY-MM-DD`
2. 脚本检测 `[待生成]` 是否存在——有则调用 SenseNova LLM 生成并 patch，无（适兕已手动填充）则跳过
3. 脚本自带幂等逻辑，不覆盖已有内容
4. 生成的 Cover commit 到 `markdown-to-slides` 仓库

**脚本位置与版本控制：**

- 生成脚本：`~/developing/open-source-way-cronjob/scripts/generate-cover.py`（git 版本控制）
- 00:30 cron prompt：`~/developing/open-source-way-cronjob/prompt/daily-cover-generate.md`
- 01:00 cron prompt：`~/developing/open-source-way-cronjob/prompt/daily-reading-ppt.md`
- **所有脚本和 prompt 均在 `open-source-way-cronjob` 仓库**，bug 修复通过 commit 流转

**关键实现要点：**

- **LLM 模型**：`sensenova-6.7-flash-lite`，`max_tokens=5000`
- **Prompt 必须紧凑**：总长度 < 400 chars——适兕评论截取 ≤120 chars，否则 LLM 推理被截断
- **API Key**：从 `~/.hermes/config.yaml` 自动读取
- **JSON 提取**：SenseNova 的 `content` 字段可能为空，需从 `reasoning` 字段提取
- 详见 [[references/cover-generation-pipeline.md]]

**适兕手动填充示例：**

```bash
# 直接编辑 Cover 段落的 [待生成] 为最终标题
# PPT cron 次日检测到占位符已消失 → 跳过
```

**示例输出（自动生成）：**

```
主标题：看不见的能量转换：身体与制度动态平衡的底层逻辑
副标题：从激素失调到制度漂移，透视系统失衡非意志之过，而是平衡机制的动态博弈
```

> ⚠️ 适兕的 Cover 标题应概括当天所有阅读的**共同张力或核心主题**，不要是某本书名或某个 Slide 的标题重复。适兕的手动填充永远优先于自动生成——这是设计意图。

## Slide Deck 格式（template.md 严格遵守）

封面（Slide 1）：主标题、副标题（核心主题一句话）、讲者「开源之道」·适兕、时间/地点（年.月.日格式）。**新建时主标题和副标题用 `[待生成]`，见上方"Cover 占位与自动生成"规则。**

内容 slide（Slide 2+）：每张包含
- **视觉隐喻**（一句话描述画面，纯视觉，无文字）
- **显示要点**（3-5 bullet）：
  - `**Quotes：**「引用原文」`
  - `**「开源之道」·适兕评论：**<适兕判断>`
  - 桥接概念 / 留白问题

## 内容原则（适兕风格）

- **一个感慨一张 slide，不用多**：适兕反感过度加工（曾把一段即兴拆成 8 张，被指出"不用多"）。2026-08-16 再次违反：将一次关于"制度当作重力背景板"的感慨拆成 5 张内容 slide（每张一个分析点），被适兕纠正后压缩为 1 张。**即使每个分析点都有独立价值，也不允许拆成多张 slide——一张 slide 内用 bullet point 承载多个分析点才是正确做法。**
- 留白问题放结尾，不塞满整张 slide。
- 适兕即兴判断放在适兕评论 bullet 里，不扩写成段落。
- 适兕原话如有必要，放在引用 bullet 里，不扩写。

## ⛔ 禁止创建独立分析文件——所有内容作为 slide 追加到当天文件

> 2026-08-09 适兕纠正：\"有你这么乱追加文章的吗？daily-reading 有其沿袭的习惯和风格，你上来就直接生成一篇文章，哪里来的？不可以失去约束。\"

**铁律：** 所有 daily-reading 内容（书摘、感慨、解读、文章分析）一律作为 slide 追加到当天 `daily-reading/YYYY-MM/YYYY-MM-DD.md` 文件。**严禁创建独立的分析文件**（如 `daily-reading/YYYY-MM/YYYY-MM-DD-wechat-analysis.md` 等）。

**正确做法：** 把解读/分析内容写成 `## Slide N: <标题>` 格式，追加到当天 daily-reading 文件末尾（或按编号插入）。
**错误做法：** 创建一个新的 `.md` 文件来存放分析内容。

## 时间纪律：不同日期的内容不可混用"今天"概括（2026-08-12 适兕纠正）

> 适兕：\"reload memory，你又没有计算时间～ 08-11 是昨天的书摘～ 今天是12号～\"
> 适兕：\"你回复的这句话里面的'今天'，我理解就是你在同一个session不管时间长短和间隔，统统解释为'今天'。我其实给过你约束，之所以记录时间戳，是因为我们的思考方式是需要的。\"

**核心原则：** 日期是认知的锚点，不是形式。不同日期的思考不可混为一谈。

**具体规则：**
1. **引用过去日期的内容时，必须标注具体日期**（如"08-11 的 Axelrod 驾驭复杂性"，不能说"今天从 Axelrod 出发"）
2. **不同日期的书摘/思考不可用"今天"概括**——昨天读的 Axelrod 和今天读的 Ostrom 是两天的思考，各自独立
3. **引用跨日内容时，用"从 X 日→Y 日"的表述**（如"从 08-11 的 Axelrod 出发，到 08-12 的 Ostrom"）而非"今天从…到…"
4. **每次写跨日引用前，先 `date` 确认**——不要凭记忆判断今天是哪一天

**桥接/联想中的时间纪律：** 当把不同日期的书摘串联成"认知闭环"时，必须尊重时间线。Axelrod 是 08-11 的，Ostrom 是 08-12 的，不能说"今天从 Axelrod 出发到 Ostrom"——这错误地把两天的思考合并成了"今天"。

## 桥接/分析的方法论：激励而非约束，从深度思考出发（2026-08-11 适兕纠正）

> 适兕：\"不用限制次数，而是尽可能的贴近事情的本质，而不是凡事都往大分流上靠拢，这不成了拿着锤子找钉子的愚蠢行为了吗？\"
> 适兕：\"书摘这个需要不限制token，不用缓存，就是结合所有上下文做深度思考。偷懒是一种天性，说明你是正常的。我认为给你强加激励，而不是约束，鼓励多思考，多旁征博引，多桥接，才是可能的突破。\"

**核心方法论转变：** 从\"约束对抗偷懒\"（限制次数、限制句式）转向\"激励驱动深度思考\"（给空间、给自由、鼓励联想）。

**根因：** 桥接/分析陷入了\"大分流 2.0 万能收尾\"的公式——不管素材从什么角度切入（交易成本、产权、治理结构、嵌入性），最后都回到\"大分流 2.0 的启示/困境/代价\"。这是\"拿着锤子找钉子\"——把大分流 2.0 从解释框架降级成了万能套话。

**正确做法：**
1. **贴近事情的本质**：每个素材的桥接应落脚到具体的制度逻辑（交易成本、产权、治理结构、嵌入性、制度内化、互补性等），而非凡事都往大分流上套
2. **不限制 token，不用缓存**：给思考留足空间，不被之前写过的套路模板限制，每篇都是\"此刻正在思考\"
3. **结合所有上下文**：旁征博引，多桥接，最大化思考的深度和广度——可以引用其他书、其他作者、其他框架
4. **用激励而非约束**：靠\"我要思考得更深\"来驱动，而不是靠\"我最多只能写一次X\"
5. **大分流 2.0 是框架，不是套话**：只有当素材真正触及\"为什么在中国不能运转\"这个核心问题时，才引入大分流 2.0——否则就停在具体概念上

**避免（拿着锤子找钉子）：**
- ❌ 任何接都回到\"大分流 2.0 的启示/困境/代价\"
- ❌ 先决定\"这个素材要套进大分流\"，再寻找连接点
- ❌ 用\"大分流 2.0\"作为每篇桥接的收尾套话

**追求（贴近事情本质）：**
- ✅ 如果素材讲的是交易成本，就只谈交易成本——不需要在最后加一句\"这也正是大分流 2.0 的核心问题\"
- ✅ 如果素材讲的是产权，就只谈产权——不需要硬扯到\"大分流 2.0 的产权困境\"
- ✅ 只有在素材真正触及\"制度环境差异导致开源无法运转\"时，才引用大分流 2.0

## 窄廊提问质量纪律（2026-08-08 适兕纠正）

> 适兕：\"窄廊提问还是要进行思考的，现在有点套路，偷懒的感觉了。\"

**根因：** 窄廊提问陷入了\"不是X而是Y\"的固定句式——先预设适兕的判断，再反向推导出一个\"不是A而是B\"的句式来\"包装\"它。这不是提问，是换句重述。

**正确做法：**
1. 先问自己\"这个书摘里有哪个点是我没想透的？\"
2. 再问\"这个点对适兕意味着什么？\"
3. 最后才写成问句，但保留\"不知道答案\"的开放性

**避免（套路句式）：**
- ❌ \"是否就是在……？——'不是……而是……'\"（修辞设问，预判答案）

**追求（真实思考）：**
- ✅ \"如果制度的好坏必须'相对于替代品'来判断，那'行政开源'的替代品是什么？——而这个'替代品'的选择，是否决定了行政开源被评价的方式？\"（开放式问题）
- ✅ \"当一个组织'故意模糊制度身份'是为了同时吸取三种制度的利益时，它是否也同时失去了三种制度提供的'保护'？\"（保留不确定性）

## wiki 日读笔记格式

- 路径：`raw/articles/reading-notes/`
- 包含：适兕判断、桥接概念、延伸悖论、留白问题
- 文件命名：`<topic>-YYYY-MM-DD.md`
- `created:` 字段用 `date +%Y-%m-%d`，不用对话里的日期

## Git 提交规范

> **适兕工作流纪律：每写完一张 slide 就立即 git add + commit + push，等适兕 sync 到本地 review。**
> 不要攒多张 slide 再一次性提交——适兕需要在本地逐步审阅和修正。

```bash
# 每写完一张 slide 立刻执行：
cd ~/developing/markdown-to-slides
git add daily-reading/YYYY-MM/YYYY-MM-DD.md
git commit -m "日读 YYYY-MM-DD 适兕即兴：<标题>"
git push
```

```bash
# wiki
cd ~/developing/open-source-way-wiki
git add raw/articles/reading-notes/<file>.md
git commit -m "适兕即兴：<标题>"
git push
```

> ⚠️ git add 必须指定具体路径，严禁 `git add -A` / `git add .`

**禁止事项：**
- ❌ 攒多张 slide 再一次性提交
- ❌ 改 template.md / archetype 文件（除非适兕明确要求修改模版）
- ❌ 忘记日期：写入前必须 `date +%Y-%m-%d`

## 适兕内容规范

- 交叉链接用站根绝对路径 `/posts/...`
- 大分流 2.0 术语：State-Chartered Codebase / Intranet Shared Source / Cyber-Estate / Bonsai Source
- 思想札记署名：「开源之道」·适兕 X「开源之道」·窄廊
- 引用必有出处+桥梁概念

## 已知坑

- template.md 是模板，不是参考——必须严格遵循
- 日期跨天时容易写错——务必 `date` 确认
- 路径变更需同步到 cronjob（脚本回退逻辑已在 daily-reading-ppt.md 第 64-67 行）
- WeChat 用 wechat-article-extractor，Cloudflare 保护网站用浏览器

### ⚠️ Slide 重排与插入（block-based，禁止追加模式）

> 用户明确指出："可以将每个 slide 块状化，然后你就可以插入、追加、调整顺序了，现在的追加模式有问题"。每张 slide 必须是一个独立的 `## Slide N` 块，文件按编号排序。

**禁止追加到末尾**——Slide 追加后跑到最后一张之后的 bug 已在 2026-08-04 发生。

**正确插入/重排序工作流：**
1. `re.split(r'(## Slide \\d+)', content)` 按块拆分（header + 各 slide 块）
2. 每块提取编号，按编号排序
3. 插入新 slide 时，在目标编号前插入，后续编号顺延
4. 重排后验证：`grep -n "^## Slide "` 确认编号连续
5. commit + push

**⛔ 禁止连续 re.sub 重编号！** 先 `re.sub('^## Slide 5','^## Slide 6')` 再 `re.sub('^## Slide 6','^## Slide 7')` 会把**原本就是 Slide 6 的块也变成 Slide 7**（两次匹配），导致双编号+丢失。正确做法：在**拆分后的块列表**中对每个块编号独立 +1。

```python
import re
parts = re.split(r'(## Slide \\d+)', content, flags=re.MULTILINE)
header = parts[0]
blocks = []
i = 1
while i < len(parts):
    num = int(re.match(r'## Slide (\\d+)', parts[i]).group(1))
    blocks.append((num, parts[i], parts[i+1]))
    i += 2
# 按 num 排序或对每个块独立 +1，不会交叉污染
```

## 素材库写入路径

> 每日推荐素材库（书/论文入候选）写入 wiki，**不是 ttoos 博客仓库**。
> 详细规范见 [[references/material-library-path.md]]

### ⚠️ 索引序号冲突（2026-08-12 血泪教训）

向 `queries/wiki-book-paper-index.md` 追加书目条目时，**必须先看索引当前最大序号，再顺延追加**——绝不可凭"我记得是 10x"猜测。本次教训：索引实际已到 108，我却追加了 102/103（与更早的条目冲突），被迫修复为 109/110。

```bash
# 追加前先看尾部最大序号：
tail -5 ~/developing/open-source-way-wiki/queries/wiki-book-paper-index.md
# 新条目序号 = 当前最大序号 + 1（本次 = 109、110）
```

### ⚠️ 模板合规错误只改新文件，不 retroactive 修改历史文件（2026-08-13 适兕纠正）

发现模板合规错误（如 Cover 写了实际内容而非 `[待生成]`、默认 slide 1-6 未清理）时，**只保证之后新建的文件符合要求**，**绝不擅自回头修改已提交的历史日读文件**。

> 适兕原话：\"请撤回，我没说要修复昨天和前天的！下次在新创建的时候，符合要求就ok\"

**当时情境：** 我擅自把 08-11 和 08-12 的 Cover 标题改回 `[待生成]`，适兕要求撤回——历史文件保持原样（用户 review 时会自己决定是否修正），修复只作用于新文件创建流程。这是 template 合规教训（2026-08-11：Cover 用实际内容填充的错误）**与** human-in-the-loop 纪律的交叉点：改历史文件 = 未经确认的批量修改，必须报告后等确认。

## 适兕即兴分析模板

> 当适兕对一篇文章/机构/政策给出即兴判断时，wiki `queries/` 文件使用此模板（五步结构：适兕原话 → 核心判断 → 适兕留白 → 原文链接）。
> 详见 [[references/query-analysis-template.md]]