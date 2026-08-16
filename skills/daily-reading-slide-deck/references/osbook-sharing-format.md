# OSBook-Sharing Slide Deck 格式规范

> 来源：2026-08-10 适兕指出 book-sharing slide 缺少视觉隐喻和显示要点。
> 最后更新：2026-08-10 — 全部 27 张 slide 补齐。

## 适用文件

- `~/developing/markdown-to-slides/osbook-sharing/kuosi-sharing-a-brief-history-of-intelligence.md`（Part 1, Slide 0–14）
- `~/developing/markdown-to-slides/osbook-sharing/kuosi-sharing-a-brief-history-of-intelligence-part-2.md`（Part 2, Slide 15–29）
- `~/developing/markdown-to-slides/osbook-sharing/kuosi-sharing-a-brief-history-of-intelligence-part-3.md`（Part 3, Slide 30–44）

## Slide 结构（Part 1 格式，Slide 0–14）

```markdown
## Slide N — 标题

### 视觉隐喻
**一句话描述画面，Bauhaus 几何风格，普鲁士蓝 #1B3B6B + 暖白 #F5F0E8 主调**

### 显示要点
* bullet 1
* bullet 2
* bullet 3
* bullet 4

### 书摘
<原文引用>

### 适兕注
<适兕的判断或桥接分析>

---
```

## Slide 结构（Part 2 格式，Slide 15–26）

```markdown
## Slide N — 标题

### 视觉隐喻
**一句话描述画面，Bauhaus 几何风格，普鲁士蓝 #1B3B6B + 暖白 #F5F0E8 主调**

### 显示要点
* bullet 1
* bullet 2
* bullet 3
* bullet 4

### 书摘
<原文引用>

### 适兕注
<适兕的判断或桥接分析>

### 适兕：桥接概念
**"桥接概念名"（English Name）**——<一句话定义>

### 「开源之道」·适兕评论
<适兕的完整评论，含制度分析桥接>
```

## Part 3 文件头部差异（Slide 30 起）

> ⚠️ Part 3 (`kuosi-sharing-a-brief-history-of-intelligence-part-3.md`) 的文件头部使用了 `template.md` 的 8 段 deck 元数据（文档用途/使用场景/听众画像/讲者视角/核心诉求/核心基调/视觉风格关键词/内容结构约定），而 Part 1/Part 2 使用简洁的文件头部。这是 2026-08-14 创建 Part 3 时引入的新格式。
>
> **Slide 结构本身（视觉隐喻/显示要点/书摘/适兕注/桥接概念/适兕评论）在三个 Part 中一致**，差异仅在文件头部元数据。新 Part 继续沿用 Part 3 的 template 元数据头部格式。

## Part 3 元数据头部格式示例

```markdown
# 读书书摘 — 《智能简史：进化、AI与人脑的突破》
# Part 3（Slides 30+）

# [输入给 NotebookLM / AI 图像生成引擎的系统提示/背景信息]

## 文档用途
...
## 使用场景
...
## 听众画像
...
## 讲者视角
...
## 核心诉求
...
## 核心基调
...
## 视觉风格关键词
...
## 内容结构约定
...
```

1. **一句话描述**，纯视觉，无文字（画面内出现的文字用引号标注，如 `标注5.5亿年`）
2. **风格**：Bauhaus 几何构成，深普鲁士蓝 `#1B3B6B` 为主调，暖白 `#F5F0E8` 为底色，极简主义
3. **核心元素**：用几何形状（圆、方、线）和抽象符号表达概念张力，不依赖图标
4. **暗调学术风格**（dark academic），理性、克制、智识感
5. 参考示例：`暗色背景上一本摊开的厚书，书页中飞出无数细小的发光生物——从细菌到鱼类到灵长类剪影，层层叠加，最终汇聚成一个AI芯片的轮廓。普鲁士蓝主调，羊皮纸质感`

## 显示要点编写规则

- 3–5 个 bullet point
- 提炼 slide 的核心判断，不是对书摘的复述
- 用适兕的判断框架（制度经济学视角、桥接概念、大分流 2.0）
- 用 bullet 直接陈述，不展开段落

## 插入方式

批量插入时用 Python 脚本：

```python
import re
slides = re.split(r'(?m)^## Slide \d+', text)
for i, chunk in enumerate(slides):
    # 在 header 后、第一个 ### 节之前插入视觉隐喻和显示要点
```

插入位置：slide header 之后、第一个 `###` 章节之前（即 `### 书摘` 之前）。

## Git 提交

修改后 `git add` 具体文件路径 + `git commit` + `git push`。

## 与 daily-reading slide 格式的区别

| 维度 | daily-reading | osbook-sharing |
|------|--------------|----------------|
| 路径 | `daily-reading/YYYY-MM/YYYY-MM-DD.md` | `osbook-sharing/kuosi-sharing-*.md` |
| Slide 编号 | 1-N（1 = Cover） | 0-N 或 15-N（续篇） |
| 结构 | 视觉隐喻 + 显示要点 + 留白问题 | 视觉隐喻 + 显示要点 + 书摘 + 适兕注 + 桥接概念 + 适兕评论 |
| Cover | `[待生成]` 占位 | 无独立 Cover（Slide 0 直接是引言） |
| 适用场景 | 每日即兴讨论 | 共读书分享 |