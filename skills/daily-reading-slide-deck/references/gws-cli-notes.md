# gws CLI — 常用命令备忘

## Drive 文件下载

`gws drive files download` 端点需要 path parameter `fileId`，但 `--params` 不接受它。正确做法是用 `get` + `alt: media`：

```bash
# 正确：下载 Drive 文件
gws drive files get --params '{"fileId":"<FILE_ID>","alt":"media"}' -o "文件名.pdf"
```

**错误示范（会报 validationError）：**
```bash
# ❌ 不要这样做
gws drive files download --params '{"fileId":"..."}' -o "xxx.pdf"
gws drive files get "FILE_ID" -o "xxx.pdf"
```

## Drive 文件列表（搜索）

```bash
gws drive files list --params '{"q":"name contains '\''关键词'\''","fields":"files(id,name,mimeType,size)"}'
```

## Calendar 添加事件

```bash
gws calendar events insert \
  --params '{"calendarId":"primary"}' \
  --json '{"summary":"事件标题","start":{"dateTime":"2026-11-14T09:00:00+08:00","timeZone":"Asia/Shanghai"},"end":{"dateTime":"2026-11-15T18:00:00+08:00","timeZone":"Asia/Shanghai"},"location":"地点"}'
```

## 公众号监测列表

路径：`~/.hermes/cron/prompts/china-open-source-daily-en.md`（软链接到
`~/developing/open-source-way-cronjob/prompt/`）。

添加公众号时：
1. 在 **Currently monitored accounts** 追加编号行
2. 在 **Fallback** 追加 `site:mp.weixin.qq.com` 查询
3. 重要事件加 **Notable event** 行到账户条目下
4. `git commit -m "update: 加入<公众号名>到监测列表"` + `git push`
