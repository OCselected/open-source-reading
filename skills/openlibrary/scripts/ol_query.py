#!/usr/bin/env python3
"""
Open Library 查询工具 — 输入 ISBN/书名片段，输出图书元数据（标题/作者/年份/页数/封面）

用法:
  python3 ol_query.py <查询>          # 用书名/作者搜索
  python3 ol_query.py --isbn 9780262232452  # 用 ISBN 精确查找
  python3 ol_query.py --search "天朝的崩溃" 茅海建  # 按书名+作者搜索
"""

import sys, json, urllib.request, urllib.parse

OL_SEARCH  = "https://openlibrary.org/search.json"
OL_ISBN_URL = "https://openlibrary.org/api/books?format=json&bibkeys=ISBN:{isbn}"


def fetch(url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": "OpenLibraryQuery/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def search(query):
    params = {"q": query, "limit": 10, "fields": "key,title,author_name,first_publish_year,edition_count,publisher"}
    url = OL_SEARCH + "?" + urllib.parse.urlencode(params)
    data = fetch(url)
    results = []
    for d in data.get("docs", []):
        results.append({
            "key":            d.get("key", ""),
            "title":          d.get("title", ""),
            "authors":        ", ".join(d.get("author_name", [])),
            "first_published": str(d.get("first_publish_year", "")) or "未知",
            "edition_count":  d.get("edition_count", ""),
            "publisher":      ", ".join(d.get("publisher", [])[:3]) or "未知",
        })
    return results


def by_isbn(isbn):
    url = OL_ISBN_URL.format(isbn=urllib.parse.quote(isbn))
    data = fetch(url)
    entry = data.get(f"ISBN:{isbn}", {})
    if not entry:
        return None
    info = entry.get("works", [{}])[0] if entry.get("works") else {}
    authors = ", ".join(a.get("name", "") for a in info.get("authors", []))
    titles  = ", ".join(w.get("title", "") for w in info.get("works", []))
    return {
        "title":         titles or entry.get("title", ""),
        "authors":       authors,
        "first_published": str(info.get("first_publish_date", "")) or "未知",
        "isbn":          isbn,
        "cover_url":     f"https://covers.openlibrary.org/b/id/{info.get('covers',[0] or [None])[0] or 0}-M.jpg" if info.get("covers") else None,
        "subject_count": info.get("subject_count", ""),
        "key":           info.get("key", ""),
    }


def main():
    args = sys.argv[1:]
    if not args:
        print("用法:  ol_query.py <书名|作者>  或  ol_query.py --isbn <ISBN>")
        sys.exit(0)

    if args[0] == "--isbn":
        isbn = args[1] if len(args) > 1 else ""
        result = by_isbn(isbn)
        if result:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print(f"[未找到] ISBN {isbn}")
    else:
        query = " ".join(args)
        results = search(query)
        if not results:
            print(f"[未找到] 查询: {query}")
            return
        print(f"共 {len(results)} 条结果 (查询: {query})\n{'='*60}")
        for i, r in enumerate(results, 1):
            print(f"\n[{i}] {r['title']}")
            print(f"    作者: {r['authors']}")
            print(f"    出版年: {r['first_published']}  |  版次: {r['edition_count']}")
            print(f"    出版社: {r['publisher']}")
            print(f"    key: {r['key']}")


if __name__ == "__main__":
    main()
