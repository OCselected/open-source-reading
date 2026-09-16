# World Reading Protocol

## Minimal prompt for a new observation

Use this shape when asking the agent to process an observation:

```text
我读到/观察到：...
触发概念：...
于是跳到：...
我想追溯这个跳跃，请判断是否形成 BP；如果是，请更新 reading-breakpoint-ledger.md。如果涉及制度征兆，也请更新 opensource-regime-signals.md。
```

## Minimal prompt for review

```text
请 review 这个 daily-reading 文件，不按摘要评价，按 world-reading 标准追溯：
- 有哪些触发概念？
- 有哪些跳跃？
- 桥接概念是否成立？
- 哪些应该进入 BP ledger？
- 哪些应该进入 regime signals？
- 哪些不应升级，只保留为 weak 或现场记录？
```

## Confidence checklist

Before writing `moderate` or `strong`, ask:

- Is the bridge mechanism explicit?
- Is the evidence URL present?
- Is the institutional claim falsifiable?
- Could this be mere topical similarity?
- What would prove me wrong?

If any answer is bad, keep the record as `weak` or `moderate`, not `strong`.

## Escalation checklist

Escalate a BP into a regime signal only if all are true:

- It concerns Production / Governance / Organization / Agentic / Infrastructure.
- It can be checked against external evidence.
- It has future tests.
- It does not rely only on personal intuition.


## Architecture / Flow Diagram

The World Reading control field is visualized in:

```text
~/developing/open-source-way-wiki/queries/world-reading-architecture.html
```

Use the diagram when explaining the relationship between:

```text
潜在驱动力
→ Agent + LLM 阅读识别器
→ World Reading 断点结构
→ Reading Breakpoint Ledger
→ Regime Signals
→ Weekly Review
→ Wiki / Essay / Osbook
```

Core framing:

```text
目标：不是预测用户喜欢什么，而是照亮他在寻找什么。
```
