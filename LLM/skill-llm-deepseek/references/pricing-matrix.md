# DeepSeek Pricing Matrix

Use this file as the structured billing source for documented DeepSeek rows.

Do not reconstruct pricing from `model-catalog.md` notes.

| Model Type | API Model | Price Region | Price Currency | Price Unit | Metered Side | Metered Item | Context Band | Billing Plan | Service Tier | List Unit Price | Effective Unit Price | Discount Kind | Valid From | Valid Until | Cache Class | Multiplier | Price Condition | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `deepseek-v4-flash` | `global` | `USD` | `per-million-tokens` | `input` | `cache-miss text tokens` | `all` | `real-time` | `standard` | `0.14` | `0.14` | `none` | `2026-07-14` | `open-ended` | `none` | `1` | `standard` | `2026-07-14` | `https://api-docs.deepseek.com/quick_start/pricing` |
| `chat` | `deepseek-v4-flash` | `global` | `USD` | `per-million-tokens` | `cached-input` | `cache-hit text tokens` | `all` | `real-time` | `standard` | `0.0028` | `0.0028` | `none` | `2026-07-14` | `open-ended` | `cache-read` | `1` | `reduced from launch price on 2026-04-26 UTC` | `2026-07-14` | `https://api-docs.deepseek.com/quick_start/pricing` |
| `chat` | `deepseek-v4-flash` | `global` | `USD` | `per-million-tokens` | `output` | `text tokens` | `all` | `real-time` | `standard` | `0.28` | `0.28` | `none` | `2026-07-14` | `open-ended` | `none` | `1` | `standard` | `2026-07-14` | `https://api-docs.deepseek.com/quick_start/pricing` |
| `chat` | `deepseek-v4-pro` | `global` | `USD` | `per-million-tokens` | `input` | `cache-miss text tokens` | `all` | `real-time` | `standard` | `0.435` | `0.435` | `none` | `2026-07-14` | `open-ended` | `none` | `1` | `current published rate` | `2026-07-14` | `https://api-docs.deepseek.com/quick_start/pricing` |
| `chat` | `deepseek-v4-pro` | `global` | `USD` | `per-million-tokens` | `cached-input` | `cache-hit text tokens` | `all` | `real-time` | `standard` | `0.003625` | `0.003625` | `none` | `2026-07-14` | `open-ended` | `cache-read` | `1` | `current published rate` | `2026-07-14` | `https://api-docs.deepseek.com/quick_start/pricing` |
| `chat` | `deepseek-v4-pro` | `global` | `USD` | `per-million-tokens` | `output` | `text tokens` | `all` | `real-time` | `standard` | `0.87` | `0.87` | `none` | `2026-07-14` | `open-ended` | `none` | `1` | `current published rate; list price 3.48` | `2026-07-14` | `https://api-docs.deepseek.com/quick_start/pricing` |
