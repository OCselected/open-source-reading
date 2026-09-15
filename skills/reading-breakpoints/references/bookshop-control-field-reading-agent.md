# 书店控制场 × 阅读断点：Reading Agent 原型

> 来源桥接：`https://osbook.opensourceway.blog/posts/bookshop-control-field-agent/` 与 `reading-breakpoints` 的桥接概念。

## 核心桥接

书店二当家 Agent 与阅读断点追踪共享同一个控制场结构：

```text
观察证据
→ 生成假设
→ 解释行动
→ 发现 Misfit
→ 调整策略
```

区别在于对象：

- 书店控制场管理：读者、书、书架、标签、互动、服务策略。
- 阅读断点管理：当前书、触发点、目标书、桥接概念、未解决问题、下一步阅读路径。

当两者结合，书店 Agent 不再只是“推荐书”，而是成为 **Reading Agent**：它观察读者的认知跳跃，命名桥接概念，提出下一步阅读路径，并把每一次误配变成可审计的学习。

## Reading Breakpoint 对象模型

每条阅读断点建议记录以下字段：

| 字段 | 说明 |
|---|---|
| date | 阅读或触发日期 |
| current_source | 当前正在阅读的书、论文、文章或项目 |
| trigger_concept | 触发跳跃的关键概念 |
| jump_to | 被跳到/被关联到的新来源 |
| bridge_concept | 连接两者的桥接概念 |
| next_question | 这次跳跃后仍未解决的问题 |
| open_source_connection | 与开源治理、基础设施、OSPO、Agent、制度的连接 |
| confidence | weak / moderate / strong |
| misfit_risk | 可能误判什么 |
| evidence_urls | 支撑链接 |

## Misfit 类型映射

书店文章中的 Misfit 可以迁移到阅读断点：

| 类型 | 书店场景 | 阅读断点场景 |
|---|---|---|
| Reader Misfit | 读者反复看封面但不翻开 | 读者被概念吸引但无法进入框架 |
| Source Misfit | 某本书被很多人拿起又放下 | 某本书/论文被频繁引用但难被理解 |
| Classification Misfit | 书放在错误书架 | 概念被放进错误理论谱系 |
| Service Misfit | 二当家推荐后读者沉默离开 | Agent 推荐来源后没有产生新桥接 |

## Agent-guided Reading Breakpoints

新启蒙模式不是“AI 替读者读”，而是：

```text
AI 观察认知现场
→ 记录触发点
→ 命名桥接概念
→ 提供下一步阅读路径
→ 解释推荐理由
→ 接受读者拒绝或修正
→ 把断点沉淀进 wiki / daily-reading / osbook
```

关键边界：

1. **可解释**：为什么从 A 跳到 B。
2. **可拒绝**：读者可以否定 Agent 的桥接判断。
3. **可删除**：读者可以删除画像或阅读路径。
4. **可追溯**：每条断点必须能回到 source 与 evidence。
5. **可升级**：重复出现的桥接概念应升级为研究主题或文章线索。

## 与 open-source-reading 的管线关系

```text
reading-breakpoints
  ┣━ 捕捉桥接概念
  ┃
  ├─ bookshop-control-field-reading-agent
  │    ┣━ 把阅读过程理解为控制场
  │    ┣━ 把 Misfit 作为诊断信号
  │    └─ 把推荐转化为解释、验证与修正
  │
  ├─ daily-reading
  │    ┣━ 每日阅读现场
  │    └─ 记录阅读跳跃与窄廊提问
  │
  └─ open-source-way-wiki
       ┣━ queries/reading-breakpoint-ledger.md
       ┣━ queries/opensource-regime-signals.md
       └─ 成熟桥接概念 → 分析文章 / osbook 主题
```

## 最小实践规则

1. 每次从 A 跳到 B，必须记录 `bridge_concept`。
2. 如果只能记录“我读了什么”，还不能成为断点。
3. 如果只能推荐 B，不能说明为什么，推荐失败。
4. 如果桥接概念重复出现 3 次，应升级为 wiki 主题候选。
5. 如果同一 Misfit 反复出现，应修正分类、导读或推荐策略。
6. Agent 的目标不是准确预测偏好，而是帮助读者更准确地问问题。
