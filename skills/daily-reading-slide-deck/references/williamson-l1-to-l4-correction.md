# Williamson 框架修正记录 — 2026-08-12

## 问题

`markdown-to-slides/open-source-economics-lecture/` 目录下 12 讲讲义使用了一个**三层框架**
（L1=具体规则/L2=制度环境/L3=社会规范），与 Williamson 的正确四层框架（L1→L4 顺序）**完全倒置**。

## 正确框架

```
L1 社会嵌入层（Embeddedness）   — 习俗/文化/规范     — 100-1000 年
L2 制度环境层（Institutional Environment）— 法律/产权 — 10-100 年
L3 治理机制层（Governance Mechanisms）    — 契约/组织 — 1-10 年
L4 资源配置层（Resource Allocation）     — 价格/激励 — 连续
```

## 修正涉及文件（9 个）

| 文件 | 主要修正 |
|------|---------|
| `lecture-0.md` | S2/S3/S5 三层→四层全量重写，29 行 |
| `lecture-0-part-4.md` | 视觉引用 |
| `lecture-1-part-2.md` | 视觉引用 |
| `lecture-5.md` | L1 协作规范 → L1 嵌入文化 |
| `lecture-6.md` | L2→L3（治理机制），三层→四层 |
| `lecture-8.md` | L1→L2（制度环境） |
| `lecture-11.md` | L3→L1（社会嵌入层根基） |
| `what-were-kuosi-done-recently.md` | 三层→四层框架表 |
| `what-were-the-open-source-way-done-recently.md` | 框架表 + 海洋隐喻 |

## 全量验证命令

```bash
grep -rn "L1 具体\|L1 日常\|L1 规则\|L1 交换\|三层\|三个层级" *.md
grep -rn "L2 治理结构\|L3 制度环境\|L4 文化\|L4 嵌入\|L4 信任" *.md
```

## Commit

`0c26369` — fix: Williamson 社会分析框架全量修正

## 根因

之前的窄廊 session 在编写讲义时使用了三层倒置框架。适兕明确指出后，
全量扫描所有 `.md` 文件并修正。

## 预防措施

下次修改讲义时，先加载 `daily-reading-slide-deck/references/williamson-framework.md`
确认当前使用的框架版本。