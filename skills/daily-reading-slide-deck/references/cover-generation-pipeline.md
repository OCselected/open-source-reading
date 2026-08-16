# Cover 自动生成管线 — 架构与实现细节

> 本文档记录 daily-reading Cover 自动生成管线的三文件架构和 SenseNova LLM 的 JSON 提取陷阱。
> 最后更新：2026-08-10 — 脚本迁入 `open-source-way-cronjob/scripts/`，cron prompt 接管入口。

## 三文件架构（当前）

```
daily-reading/YYYY-MM/YYYY-MM-DD.md                        # 数据源：含 [待生成] 占位
     ↑
open-source-way-cronjob/scripts/generate-cover.py          # LLM 生成逻辑（版本控制）
     ↑
open-source-way-cronjob/prompt/daily-cover-generate.md      # 00:30 cron 入口
open-source-way-cronjob/prompt/daily-reading-ppt.md         # 01:00 cron 前置步骤
```

**数据流：**
1. 新建日读文件时 Cover 写 `[待生成]` 占位符
2. 适兕可在任意时间手动 patch Cover（优先路径）
3. 00:30 cron (`daily-cover-generate.md`) 检测 `[待生成]`，有则生成
4. 01:00 PPT cron 再跑一次（幂等兜底），然后渲染 PPTX
5. 脚本提取所有 Slide 标题 + 适兕评论 + 桥接概念 → LLM → patch Cover

## Cron 入口（双保险）

| Job | 时间 | 作用 | 幂等检测 |
|---|---|---|---|
| 日读 Cover 自动生成 (`daily-cover-generate.md`) | 00:30 | 当天日读总结后预生成 | 检测 `[待生成]` |
| 每日阅读 PPT (`daily-reading-ppt.md`) | 01:00 | PPTX 渲染前兜底生成 | 脚本内部再次检测 |

适兕手动填充后 `[待生成]` 消失 → 两个 cron 都跳过，不覆盖。

## SenseNova 6.7-flash-lite JSON 提取陷阱

### 问题

SenseNova 6.7-flash-lite 在 `response_format={"type": "json_object"}` 模式下行为不稳定：

| 现象 | 原因 |
|---|---|
| `content` 字段为空 | 模型只返回 `reasoning`，JSON 嵌在 `reasoning` 末尾 |
| `reasoning` 被截断 | `max_tokens` 不够，推理未完成，JSON 输出 `{"title":"..."}` |
| `content` 有值 | 模型在推理后追加 JSON 到 `content`（短 prompt 时可靠） |

### 解决方案

**1. max_tokens 必须足够大：**
- 短 prompt (< 200 chars)：`max_tokens=*** 可靠
- 长 prompt (> 300 chars)：`max_tokens=*** 否则 `reasoning` 被截断

**2. Prompt 必须紧凑：**
- 总长度 < 400 chars（实测可靠的上限）
- 适兕评论截取 ≤ 120 chars
- 不要塞入完整 bridge concept 长句

**3. JSON 提取：**

```python
combined = content + reasoning
candidates = list(re.finditer(r'\{[^{}]*"title"[^{}]*"subtitle"[^{}]*\}', combined, re.DOTALL))
for m in candidates:
    try:
        obj = json.loads(m.group())
        if obj.get("title") and obj["title"] not in ("...", ""):
            return obj
    except json.JSONDecodeError:
        continue
```

## Patch 陷阱

**不要用 f-string 中的 `\\1` 做 re.sub 的 backreference：**

```python
# ❌ 不可靠：f-string 中 \\1 被 Python 解释器吃掉
new = re.sub(r'(pattern)', f'\\1{value}', text)

# ✅ 用 str.replace
new = text.replace('[待生成]', value)

# ✅ 或用 re.sub + 字符串拼接
new = re.sub(r'(pattern)', r'\1' + value, text)
```

**不要用 f-string 中的 `\*\*` 做正则匹配：**

```python
# ❌ 不可靠：Python f-string 中 \*\* 的 \* 会被转义
new = re.sub(r'(\*\s*\*\*主标题\s*\*\*\s*[:：]\s*)\[待生成\]', ...)

# ✅ 逐行 replace
for line in cover_block.split("\n"):
    if "[待生成]" in line:
        new_lines.append(line.replace("[待生成]", title))
```

## 文件位置

- 生成脚本：`~/developing/open-source-way-cronjob/scripts/generate-cover.py`（git 版本控制）
- 00:30 cron prompt：`~/developing/open-source-way-cronjob/prompt/daily-cover-generate.md`
- 01:00 cron prompt：`~/developing/open-source-way-cronjob/prompt/daily-reading-ppt.md`
- Skill 入口：`daily-reading-slide-deck` → "Cover 占位与自动生成"章节

## Git 操作规范

- 脚本修改 → commit 到 `open-source-way-cronjob` 仓库
- Cover 填充 → commit 到 `markdown-to-slides` 仓库
- cron prompt 修改 → commit 到 `open-source-way-cronjob` 仓库