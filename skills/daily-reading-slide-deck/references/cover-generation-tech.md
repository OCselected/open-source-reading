# Cover 生成技术参考

适用于 `daily-reading` Slide Deck Cover 的自动生成（主标题 + 副标题），
脚本路径：`~/developing/open-source-way-cronjob/scripts/generate-cover.py`（版本控制）。

---

## 一、SenseNova 结构化 JSON 输出（关键经验）

SenseNova 6.7 flash lite 在 `response_format: {"type": "json_object"}` 模式下的行为：

| 条件 | 现象 |
|---|---|
| prompt ≤ ~250 chars + `max_tokens: 1000` | `content` 字段有 JSON，但可能截断（`"title":"..."`） |
| prompt > 250 chars + `max_tokens: 3000` | `content` 为空，`reasoning` 含完整推理 + 截断 JSON |
| prompt < 400 chars + `max_tokens: 5000` | **可靠**：`content` 有完整 JSON |

### 验证过的稳定配置

```python
import urllib.request, json

BASE_URL = "https://token.sensenova.cn/v1"
payload = json.dumps({
    "model": "sensenova-6.7-flash-lite",
    "messages": [{"role": "user", "content": prompt}],
    "max_tokens": 5000,          # ← 必须 >= 5000
    "temperature": 0.7,
    "response_format": {"type": "json_object"}
}).encode()
req = urllib.request.Request(
    f"{BASE_URL}/chat/completions",
    data=payload,
    headers={"Content-Type": "application/json",
             "Authorization": f"Bearer {api_key}"}
)
with urllib.request.urlopen(req, timeout=120) as resp:
    data = json.loads(resp.read())
msg = data["choices"][0]["message"]
content = msg.get("content", "") or ""
reasoning = msg.get("reasoning", "") or ""
```

**API Key 来源**：`~/.hermes/config.yaml` 的 `model.api_key` 字段。
不要用 `SENSENOVA_API_KEY` 环境变量（可能不存在）。

### JSON 提取策略

```python
import re

def parse_json(response):
    candidates = list(re.finditer(
        r'\{[^{}]*"title"[^{}]*"subtitle"[^{}]*\}',
        response, re.DOTALL
    ))
    best = None
    for m in candidates:
        try:
            obj = json.loads(m.group())
            if obj.get("title") and obj["title"] not in ("...", ""):
                best = obj
        except json.JSONDecodeError:
            continue
    return best
```

**关键**：选最后一个有效 JSON（模型的最终决定），跳过 `"..."` 截断候选。

### Prompt 构建规则

- 适兕评论截取 ≤ 120 chars（超过则 LLM 推理被截断）
- 移除 `**` markdown 格式（避免干扰 LLM 解析）
- 总 prompt 长度 < 400 chars
- 移除多余格式标记（`**`）

---

## 二、Patch `[待生成]` 正则陷阱

在 f-string 中使用 `re.sub` 配合 `\\*\\*` 会因反斜杠转义行为不可靠导致匹配失败。

**错误写法**（不匹配）：
```python
new_cover = re.sub(
    r'(\*\s*\*\*主标题\s*\*\*\s*[:：]\s*)\[待生成\]',
    f'\\1{title}',
    cover_block
)
```

**正确写法**（逐行字符串替换）：
```python
lines = cover_block.split("\n")
for line in lines:
    if "[待生成]" in line:
        new_lines.append(line.replace("[待生成]", title))
```

---

## 三、Power-User 测试：验证 Prompt 是否可靠

快速验证方法——直接跑 curl 或 Python 一段，观察 `content` 字段：

```python
# 单行测试
prompt = "你是阅读思考者。阅读：[Slide 1] 书摘——xxx。输出JSON: {\"title\":\"一句话\",\"subtitle\":\"副标题\"}"
# 如果 content 非空 → 可靠；如果 content 为空但 reasoning 有 JSON → 需缩短 prompt 或增大 max_tokens
```

---

## 四、Cover 填充协议（设计决策）

| 路径 | 触发时机 | 执行者 | 检测方式 |
|---|---|---|---|
| A. 适兕手动 | 适兕完成当日总结后 | 适兕/窄廊 | 直接 patch Cover 段落 |
| B. cron 自动 | 00:30 Cover cron + 01:00 PPT cron（双层保险） | `generate-cover.py` | 检测 `[待生成]` 是否存在 |

脚本幂等：`[待生成]` 存在才生成，已填充则跳过。