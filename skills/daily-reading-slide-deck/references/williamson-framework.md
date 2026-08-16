# Williamson 社会分析四层框架（不可再错）

## 正确顺序（L1 最深层 → L4 最表层）

| 层次 | 制度层面 | 时间尺度 | 开源对应 |
|------|----------|----------|----------|
| **L1** | 社会嵌入层（Embeddedness）：习俗、传统、文化、规范 | 100–1000 年 | 黑客伦理、开源文化、社区规范 |
| **L2** | 制度环境层（Institutional Environment）：产权、法律、司法、官僚体制 | 10–100 年 | GPL 许可证、开源政策、法律框架 |
| **L3** | 治理机制层（Governance Mechanisms）：市场/混合/层级的契约治理 | 1–10 年 | 开源社区治理、OSPO、do-ocracy |
| **L4** | 资源配置层（Resource Allocation）：价格、数量、激励匹配 | 连续 | 开源贡献激励、声誉系统 |

## 易错点

### ❌ 错误：三层框架（L1具体规则/L2制度环境/L3社会规范）
之前讲义中使用过三层框架，层次定义**完全倒置**：
- 把 L1 写成"具体规则层"（实际 L4）
- 把 L3 写成"社会规范层"（实际 L1）

**修正方法：** 全量搜索 `L1 具体\|L1 日常\|L1 规则\|L1 交换\|三层\|三个层级` 和 `L2 治理结构\|L3 制度环境\|L4 文化\|L4 嵌入\|L4 信任`。

### ❌ 错误：L5 中的"Williamson L1：开源的协作规范"
`lecture-5.md` 中原文 L1=嵌入文化（正确），但若看到 L1=协作规范/L1=交易机制，应改为 L3=治理机制。

### ✅ 正确引用示例
- "Williamson L1（社会嵌入）：开源的协作规范嵌入文化层面"
- "Williamson L2（制度环境）：信息商品需要新的产权界定方式"
- "Williamson L3：治理机制层（市场/混合/层级）决定了项目的演化方向"
- "Williamson L1：社会嵌入层是整个制度金字塔的根基"

## 12讲 U 形曲线（验证正确）

```
L2 制度环境  ← L0-L2 起点（下潜）
L3 治理机制  ← L3-L6 下潜
L1 社会嵌入  ← L7 最深处（文化）
L4 资源配置  ← L8-L11 回弹（终点）
```

## 与 ttoos 博客的一致性

`Institutional-Hierarchy-and-the-Open-Source-Dilemma-in-China.md` 中使用 `Level 1=Embeddedness / Level 2=Institutional Environment / Level 3=Governance` 完全对齐。

## 相关

- `references/williamson-l1-to-l4-correction.md` — 2026-08-12 讲义全量修正记录