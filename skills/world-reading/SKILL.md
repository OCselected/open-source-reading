---
name: world-reading
description: "Read current events as evolving institutional breakpoints."
version: 0.1.0
author: 「开源之道」·适兕 × 「开源之道」·窄廊
license: CC-BY-SA 4.0
platforms: [macos, linux]
metadata:
  hermes:
    tags: [reading, world, breakpoint, institutional-analysis, open-source, agentic, knowledge-network]
    related_skills: [reading-breakpoints, daily-reading-slide-deck, openlibrary]
    category: research
    triggers: [探索世界, 世界阅读, world reading, 制度征兆, 阅读断点, 现实阅读, 征兆, 桥接, bridge concept, regime signal]
---

# World Reading

把世界当作一本正在被共同书写的书来读。

World Reading 不是新闻摘要，也不是“今天的热点是什么”。它用阅读断点的方法记录真实世界的认知跳跃：一个事件、一本书、一个项目、一段制度文本或一次 AI 行为如何触发新的观察路径，并形成可解释、可拒绝、可追溯、可升级的知识网络。

## When to Use

Use this skill when:

- 用户提供书摘、文章、新闻、开源项目事件、政策、组织变化、AI Agent 行为或自己的观察，并希望“追溯 / review / 桥接”。
- 一条信息里有明显的认知跳跃：A 现象 → B 框架 → C 问题。
- 需要判断某件事是否值得进入长期研究网络。
- 需要把 daily-reading、open-source-way-wiki、Open Source Daily、reading-breakpoints 接成同一条研究管线。

Do not use this skill for:

- 简单事实问答。
- 只要求总结一篇文章，且没有桥接、征兆或研究意图。
- 没有证据链接却要求强判断的情况。

## Core Idea

World Reading 的核心对象不是“事件”，而是“阅读现场”。

一个世界断点必须回答：

1. 我看到什么？`current_source`
2. 什么概念触发了我？`trigger_concept`
3. 我跳到了哪里？`jump_to`
4. 连接两者的桥接概念是什么？`bridge_concept`
5. 这个跳跃还留下什么问题？`next_question`
6. 它和开源、组织、治理、公共基础设施、Agentic 生产力有什么关系？`open_source_connection`
7. 什么证据支持它？`evidence_urls`
8. 我可能在哪里误判？`misfit_risk`

没有 `bridge_concept`，就只是摘要。  
没有 `misfit_risk`，就容易把直觉误当成定论。  
没有 `future_tests`，就无法从世界新闻升级为制度征兆。

## Ledger Paths

- Reading breakpoints: `~/developing/open-source-way-wiki/queries/reading-breakpoint-ledger.md`
- Institutional signals: `~/developing/open-source-way-wiki/queries/opensource-regime-signals.md`
- Daily reading source of truth: `~/developing/markdown-to-slides/daily-reading/<YYYY-MM>/<YYYY-MM-DD>.md`
- Method repo: `~/developing/open-source-reading/`

Always read the target ledger before writing. Do not overwrite unrelated entries.

## Workflow

### 1. Identify whether a real breakpoint exists

A real breakpoint has three parts:

```text
current_source → trigger_concept → jump_to
```

If the source only says “I read X” or “this happened,” do not create a strong BP. Ask for or infer the missing trigger, but mark confidence as `weak` if unresolved.

### 2. Name the bridge concept

Write one sentence that explains why A jumps to B.

Good:

```text
横向涌现需要纵向制度锚定。
```

Bad:

```text
曾鸣和 Williamson 都讲组织。
```

The bridge must explain a cognitive move, not just topical similarity.

### 3. Decide confidence

- `weak`: only one source, personal intuition, no evidence URL, or no clear bridge.
- `moderate`: source-linked reading bridge or strong institutional reading, but needs future verification.
- `strong`: official/project/code/policy/financial evidence plus repeated corroboration.

Do not mark a reading-only insight as `strong` unless evidence supports an institutional claim.

### 4. Record the reading breakpoint

Update `reading-breakpoint-ledger.md` using this format:

```text
| BP-YYYY-MM-DD-NNN | date | current_source | trigger_concept | jump_to | bridge_concept | next_question | open_source_connection | confidence | misfit_risk | evidence_urls |
```

If the breakpoint connects to institutional evolution, also record a regime signal.

### 5. Convert to regime signal when needed

A breakpoint should become a regime signal only if it has an institutional test.

Add to `opensource-regime-signals.md`:

```text
| REGIME-YYYY-MM-DD-NNN | date | title | institutional_layer | signal_type | confidence | status | initial_reading | future_tests | evidence_urls |
```

Valid institutional layers:

- Production
- Governance
- Organization
- Agentic
- Infrastructure

`future_tests` must be concrete: what evidence in the next 7/30/90 days would confirm, demote, or falsify the reading?

### 6. Preserve the daily-reading scene

Do not rewrite the daily-reading slide just to add metadata. The slide preserves the reading scene; the wiki preserves the evolving knowledge network.

If needed, add only a short local trace line; do not clutter the slide body.

### 7. Commit only the changed knowledge files

For wiki updates:

```bash
cd ~/developing/open-source-way-wiki
git pull --rebase --autostash origin main
git add queries/reading-breakpoint-ledger.md queries/opensource-regime-signals.md
git commit -m "reading: trace world reading breakpoints"
git push origin main
```

Never use `git add -A` or `git add .`.

## Review Protocol

When reviewing an existing daily-reading file:

1. Read the file.
2. Find explicit or implicit jumps.
3. Check whether each jump has:
   - source
   - trigger
   - destination
   - bridge concept
   - next question
   - evidence
   - misfit risk
4. If the content is strong but unstructured, do not rewrite it. Trace it into the ledgers.
5. If the bridge is weak, say so and mark `weak` or omit from the ledger.

## Example: Agent as Institutional Breakpoint

Input:

```text
曾鸣《智能》讲 agent 第二阶段大爆发；适兕联想到 Agentic AI、Williamson L1-L4、Ostrom、Hayek。
```

Breakpoint:

```text
current_source: 曾鸣《智能》
trigger_concept: 三轴涌现
jump_to: Williamson L1→L4
bridge_concept: 横向涌现需要纵向制度锚定
confidence: moderate
misfit_risk: Williamson 分层不能机械套用于 AI agent 生态
```

Regime signal:

```text
title: Agent 第二阶段从能力验证进入组织验证
institutional_layer: Agentic / Governance / Organization
future_tests: 30-90 天内是否出现 agent contribution policy、agent governance、AI-generated PR 审查规范或 agent-specific OSPO 实践。
```

## Escalation Path

```text
World Reading observation
→ Reading Breakpoint Ledger
→ Open Source Regime Signals
→ Weekly review
→ Wiki analysis
→ ttoos / osbook / public essay
```

Escalate only when a bridge concept repeats or has clear future tests. Do not turn every interesting thought into an essay.

## Pitfalls

- A bridge is not a similarity map. It must explain a cognitive move.
- A reading insight is not institutional proof.
- Daily-reading slides are scenes, not ledgers.
- Do not optimize for speed; preserve the quality of the bridge.
- Do not use vague labels like “相关” or “可能有关”。Name the mechanism.

## Verification

A World Reading update is complete when:

- Each new BP has a bridge concept.
- Each BP has evidence URLs or is marked `weak`.
- Any institutional claim has a future test.
- Ledger rows are chronologically ordered where practical.
- Wiki files are committed and pushed.
- Existing daily-reading slides are not overwritten.
