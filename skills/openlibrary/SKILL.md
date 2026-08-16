---
name: openlibrary
description: 通过 Open Library 公共 API 查询图书元数据（ISBN 精确查询 / 书名-作者搜索），为 reading-breakpoints 素材入库提供元数据填充。
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [book, isbn, openlibrary, metadata, query]
    category: research
    related_skills: [reading-breakpoints, llm-wiki]
---

# Open Library 查询

通过 Open Library 公共 API 查询图书元数据——无需 API key，无需注册。

**用途**：为 `reading-breakpoints` 每日素材入库提供图书元数据（标题、作者、出版年、版次、封面 URL）。

## API 基本信息

- **提供商**：Internet Archive（非营利）
- **Base URL**：`https://openlibrary.org`
- **API Key**：不需要
- **搜索端点**：`https://openlibrary.org/search.json?q=<查询>`
- **ISBN 端点**：`https://openlibrary.org/api/books?format=json&bibkeys=ISBN:<ISBN>`
- **封面端点**：`https://covers.openlibrary.org/b/id/<cover_id>-M.jpg`

## 使用方法

### 命令

```bash
# 按书名/作者搜索（返回最多 10 条结果）
python3 /home/lee/.hermes/skills/openlibrary/scripts/ol_query.py "The Success of Open Source" Weber

# 按 ISBN 精确查询（返回完整元数据，含封面 URL）
python3 /home/lee/.hermes/skills/openlibrary/scripts/ol_query.py --isbn 9780262232452
```

### 返回字段

| 字段 | 说明 |
|------|------|
| `title` | 书名 |
| `authors` | 作者列表（逗号分隔）|
| `first_publish_year` | 首次出版年 |
| `edition_count` | 版次数量 |
| `publisher` | 出版社 |
| `cover_url` | 封面图片 URL（仅 ISBN 查询返回）|
| `key` | Open Library 内部 key，用于链接 |

## 与 reading-breakpoints 的集成流程

当用户在日读中引用一本新书时：

```
1. 用户提供书名/作者 → 触发 ol_query.py 搜索
2. 从返回结果中匹配（注意：Open Library 可能有多条结果，需人工筛选）
3. 用返回的元数据填充 osbook-book-recommendation/<slug>.md 的 frontmatter
4. 如有 ISBN → 用 --isbn 精确查询，获取封面 URL
```

## Open Library 搜索的技巧

### 书名精确匹配
```
ol_query.py --search "天朝的崩溃" 茅海建
```

### 中英文混合
Open Library 支持中英文混合搜索，但中文书在 Open Library 中收录不全。
- 如果搜索结果返回空，先用 Google Books 搜索 ISBN，再回用 `--isbn` 查询 Open Library
- 中国本土出版物（如《天朝的崩溃》）优先用 ISBN 查询

### 作者消歧
同一作者可能有多个条目，优先选择 `first_publish_year` 与已知出版年匹配的条目。

## Pitfalls

- **中文书收录不全**：Open Library 对 1980 年后中国本土出版物覆盖有限——《天朝的崩溃》可能搜不到，但如果有 ISBN 则 `--isbn` 可能返回部分元数据
- **ISBN 格式**：去掉连字符，如 `9780262232452` 而非 `978-0-262-23245-2`
- **封面 URL 为空**：旧书可能没有数字封面，`cover_url` 字段为 `None`
- **同名书**：搜索时加上作者名可显著减少噪音

## 参考

- Open Library 开发者文档：https://openlibrary.org/developers/api
- 相关 skill：[[reading-breakpoints]]（素材入库工作流）
