---
name: reading-breakpoints
description: |-
  阅读断点追踪（Reading Breakpoints）—— 受 debug 断点启发，记录多书并行阅读时的跳跃轨迹。
  核心不是「读到哪一页了」，而是「为什么从这里跳到了那里」—— 捕捉认知跳跃的桥接概念。
  适用于学术研究者的多书并行阅读场景。
version: 1.0.0
author: 「开源之道」·适兕 × 「开源之道」·窄廊
license: CC-BY-SA 4.0
platforms: [macos, linux]
metadata:
  hermes:
    tags: [reading, knowledge-management, cross-reference, breakpoint, debug-metaphor]
    category: productivity
    triggers: [阅读, 读书, 断点, 跳跃, parallel reading, breakpoint]
---

# 阅读断点追踪（Reading Breakpoints）

> **核心命题**：人类的知识是连接起来的网络。每本书、每位作者、每个章节都是其中的一个节点。任何缺失都是遗憾。读书就是点亮这些节点，找到联系。

> **核心方法**：当你从一本书「跳跃」到另一本书时，那不是分心——而是一个学术直觉在试图连接两个知识域。记录这个跳跃，就是记录你的思想是如何生长的。把一本书读「厚」——不是提炼结论，而是找到它与其他书的连接、发现它背后的制度条件、追问它没有回答的问题。

> **核心根由**：读书不是为了比较哪个视角「对」，而是为了站得更高、更远，减少盲区。同一个事物在不同视角下呈现不同的面——North 看效率，Ostrom 看可持续性，人类学看意义——没有哪个是错的，但任何一个单独看都有盲区。**多视角不是为了选边站，而是为了让不可见变得可见。** 这就是为什么我们同时读经济学、人类学、历史——不是为了找到唯一答案，而是为了看到单一视角必然遗漏的东西。

## 适用场景

- 同时阅读 3-8 本书的研究者
- 经常发现"书 A 的某个观点让我想起书 B"的读者
- 读了很多书但回头看时想不起「为什么要读这本」的人
- 想把自己的阅读模式变成可见知识图谱的人

## 概念体系

### 断点（Breakpoint）

借鉴调试器中的断点概念——不是要停下来，而是要在跳跃发生时**捕获现场状态**：

| 字段 | 说明 | 示例 |
|------|------|------|
| 📖 **当前书** | 你在读什么，读到哪了 | NIE 导论，第三章 |
| 🧠 **关键洞察** | 停在这里时想到了什么 | Ostrom 的 Design Principles 不是书斋推导 |
| 🔄 **跳跃触发** | 为什么从这里跳走 | 想知道这些原则是怎么被发现的 |
| 🎯 **目标书** | 跳到了哪本 | Ostrom: An Intellectual Biography |
| 🏷 **桥接概念** | 连接两本书的核心概念 | 理论生成的制度条件 |

### 桥接概念（Bridge Concept）

这是断点系统的灵魂——不是记录「读了什么」，而是记录**什么想法让你从 A 到了 B**。桥接概念往往才是真正的研究贡献点：

```
书 A: NIE 导论（设计原则理论）
  ┣━ 桥接: 理论生成的制度条件
  ┗━ 书 B: Ostrom 传记（理论诞生的田野现场）
```

### 活跃书堆（Active Book Pile）

当前同时在读的书，每本标注进度和活跃日期。超过 30 天未活跃的自动归档。

## 使用方法

### 1. 日常使用：记录一次跳跃

当你从一本书跳转到另一本书时，告诉你的 AI 助手：

> 「我在读《XXX》第三章，看到 YYY 概念时突然想到了 ZZZ，于是翻开了《AAA》。」

AI 自动记录为一条断点，捕捉桥接概念。

### 2. 定期复盘：看你的跳跃模式

积累 10+ 条断点后，分析模式：

- **中心辐射型**：总从一本书跳到多本 → 那本书是你的框架书
- **链条型**：A→B→C→D 连跳 → 你在追一个深层问题
- **回流型**：经常跳回同一本 → 那里有你没消化完的核心概念

### 3. 知识输出：从断点中提炼研究主题

断点中反复出现的桥接概念，往往是潜意识在告诉我们「这里有东西值得深挖」。

## 完整管线：从断点到分享

reading-breakpoints 设计为一条完整管线，而非独立记录工具：

```
阅读断点 (reading-breakpoints)
  ┣━ 捕捉桥接概念（BP-001, BP-002...）
  ┃
  ┣━━━ wiki 推荐条目 (osbook-book-recommendation/)
  ┃       ┣━ 每本书：核心概念、制度分析、开源映射
  ┃       ┗━━━ wiki-to-slides.py → slides/<slug>.md
  ┃               ┗━ 输入 NotebookLM / AI 图像引擎 → 视觉演示文稿
  ┃
  ┗━━━ daily-reading/<YYYY-MM-DD>.md
          ┣━ 使用 template.md 格式（系统提示 + slide outline）
          ┣━ 逐条追加摘抄内容（手工或 AI 辅助）
          ┗━ 输入 NotebookLM → 每日视觉笔记
```

### 文件

| 位置 | 用途 |
|------|------|
| `templates/daily-slide-template.md` | 每日阅读笔记的 slide 模板，含 system prompt + 视觉风格关键词 |
| `~/developing/markdown-to-slides/` | 项目根目录（GitHub: OCselected/markdown-to-slides） |
| `~/developing/markdown-to-slides/daily-reading/` | 逐日阅读笔记（按日期命名） |
| `~/developing/markdown-to-slides/slides/` | wiki 推荐条目的批量 slide 输出 |
| `~/developing/markdown-to-slides/wiki-to-slides.py` | wiki 推荐条目 → slide 格式的转换脚本 |
| `~/developing/markdown-to-slides/template.md` | 标准 slide 模板（含系统提示 + 视觉风格关键词） |

### 工作流：每日阅读笔记

当用户分享阅读摘抄时：

1. 检查 `daily-reading/<YYYY-MM-DD>.md` 是否存在；如不存在，用 `templates/daily-slide-template.md` 创建
2. 将摘抄格式化为 `## Slide N: 标题` 条目：
   - **视觉隐喻** — 一句话描述画面（供 AI 图像生成用）
   - **显示要点** — 摘抄原文或提炼的 3-5 个要点
3. 追加到文件末尾
4. 提交到 git（OCselected/markdown-to-slides 仓库）

### 工作流：wiki 条目转 slide

当需要准备分享材料时：

```bash
cd ~/developing/markdown-to-slides
python3 wiki-to-slides.py                     # 批量转换所有推荐条目
python3 wiki-to-slides.py --slug <书名slug>    # 转换单本书
```

输出为 `slides/<slug>.md`，可直接输入 NotebookLM 或其他 AI 图像引擎。

## wiki 整合

断点追踪建议与 llm-wiki 集成：

```
queries/reading-breakpoints.md     # 断点总表
queries/reading-breakpoints.md     # (每 10 条新增活跃书堆表)
```

每一条断点都可以链接到 wiki 中的已有概念或实体页面。

## 示例断点

`references/bp-001-example.md` 包含一个完整的真实断点记录 (BP-001)：
- 📖 NIE 导论 → 🎯 Ostrom 传记
- 🏷 桥接概念：理论生成的制度条件
- 展示了桥接概念如何从跳跃中涌现为可研究的问题

## 参考文件

| 文件 | 内容 |
|------|------|
| `references/bp-001-example.md` | BP-001 完整断点记录（真实示例）|

## 注意事项

- 这个系统的价值不在于**精度**（不需要精确到页数），而在于**桥接概念的捕捉**
- 不要记录每一条跳跃——只记录那些让你觉得「有意思」的
- 累积 5 条断点后可以做一次小复盘，看看有没有出现频率高的概念
- 跳跃不一定是「读完了一本才跳」——往往是在读的过程中就跳了，这才是最有记录价值的