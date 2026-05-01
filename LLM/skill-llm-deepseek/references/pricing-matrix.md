# DeepSeek Pricing Matrix

Use this file as the structured billing source for selected DeepSeek rows.

Do not reconstruct pricing from `model-catalog.md` notes.

| Model Type | API Model | Price Region | Price Currency | Price Unit | Metered Side | Metered Item | Context Band | Unit Price | Price Condition | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `deepseek-v4-flash` | `global` | `USD` | `per-million-tokens` | `input` | `cache-miss text tokens` | `all` | `0.14` | `standard` | `2026-05-01` | `https://api-docs.deepseek.com/quick_start/pricing` |
| `chat` | `deepseek-v4-flash` | `global` | `USD` | `per-million-tokens` | `cached-input` | `cache-hit text tokens` | `all` | `0.0028` | `reduced from launch price on 2026-04-26 UTC` | `2026-05-01` | `https://api-docs.deepseek.com/quick_start/pricing` |
| `chat` | `deepseek-v4-flash` | `global` | `USD` | `per-million-tokens` | `output` | `text tokens` | `all` | `0.28` | `standard` | `2026-05-01` | `https://api-docs.deepseek.com/quick_start/pricing` |
| `chat` | `deepseek-v4-pro` | `global` | `USD` | `per-million-tokens` | `input` | `cache-miss text tokens` | `all` | `0.435` | `discount until 2026-05-31 15:59 UTC; list price 1.74` | `2026-05-01` | `https://api-docs.deepseek.com/quick_start/pricing` |
| `chat` | `deepseek-v4-pro` | `global` | `USD` | `per-million-tokens` | `cached-input` | `cache-hit text tokens` | `all` | `0.003625` | `discount until 2026-05-31 15:59 UTC` | `2026-05-01` | `https://api-docs.deepseek.com/quick_start/pricing` |
| `chat` | `deepseek-v4-pro` | `global` | `USD` | `per-million-tokens` | `output` | `text tokens` | `all` | `0.87` | `discount until 2026-05-31 15:59 UTC; list price 3.48` | `2026-05-01` | `https://api-docs.deepseek.com/quick_start/pricing` |
