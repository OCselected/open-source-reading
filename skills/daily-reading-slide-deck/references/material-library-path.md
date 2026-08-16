# 每日推荐素材库写入路径（来自 daily-open-source-reco.md 的规范）

> 2026-08-01 session 记录：适兕明确指出"不是在项目 ttoos 里创建文件"，素材库的写入目标在 wiki，不在博客仓库。

## 写入目标（四层）

把一本新书/论文纳入每日推荐候选，按以下顺序写入四个位置，缺一不可：

1. **`$WIKI_PATH/queries/wiki-book-paper-index.md`** — 主索引
   - 在对应分类（Culture / Economics / Governance 等）追加一行
   - 格式：`| <序号> | <书名> | <作者> | 📅 <排期日期> |`
   - 已推荐标记：`✅ 已推荐 (<日期>)`

2. **`$WIKI_PATH/queries/daily-reading-bridge-index.md`** — 优先级候选
   - 如果有排期：在 `## Priority Candidates` 后或新增 `### Scheduled (排期)` 节追加
   - 如果没有排期：添加到 `## Paper Pool` 或 `### High priority` 列表

3. **`$WIKI_PATH/raw/articles/osbook-book-recommendation/<slug>.md`** — raw 素材
   - frontmatter 含 `title/author/year/ISBN/douban/type: book/scheduled/bridge_from`
   - body 含核心论证 + 桥接概念（不对外发布）

4. **`$WIKI_PATH/log.md`** — 操作日志
   - 格式：`## [YYYY-MM-DD] update | <书/论文名> 入素材库`

## 元数据检索优先级（中文书）

**豆瓣（浏览器）> Goodreads（浏览器）> Open Library（curl）> 通用搜索引擎（最后手段）**

- Open Library 对中国本土出版物覆盖极低（ISBN 前缀 97875478 等整段为空），**不要重试**
- 豆瓣 ISBN 精确页：`https://book.douban.com/isbn/<ISBN>`
- 豆瓣书名搜索：`https://search.douban.com/book/subject_search?search_text=<书名>`
- 封面图 curl（必须加 Referer）：
  ```bash
  curl -sL -A "Mozilla/5.0" -H "Referer: https://book.douban.com/" \
    "https://img3.doubanio.com/view/subject/l/public/s<数字>.jpg" \
    -o /tmp/cover-<slug>.jpg
  ```

## ⚠️ 不写入的地方

- ❌ `~/developing/ttoos/content/posts/osbook-book-recommendation/` — 这是**已发布博客**目录，不是素材库；每日推荐 cron 才写这里
- ❌ `~/developing/ttoos/static/media/` — 封面文件归博客 repo，素材入库阶段不需要

## Git 提交

- wiki：`git add queries/*.md raw/articles/... log.md && git commit -m "feat: <书名> 入素材库（排期 YYYY-MM-DD）" && git push`

## 参考

- prompt 主文件：`open-source-way-cronjob/prompt/daily-open-source-reco.md`
- openlibrary skill（user-owned，未 adopt）：处理 ISBN 查询与豆瓣回退
- book-cover-search skill（user-owned，未 adopt）：豆瓣封面提取
