# OpenAI Pricing Matrix

Use this file as the structured billing source for selected OpenAI rows.

Do not reconstruct pricing from `model-catalog.md` notes.

| Model Type | API Model | Price Region | Price Currency | Price Unit | Metered Side | Metered Item | Context Band | Unit Price | Price Condition | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `gpt-5.5` | `global` | `USD` | `per-million-tokens` | `input` | `text tokens` | `all` | `5.00` | `standard` | `2026-04-30` | `https://openai.com/api/pricing/` |
| `chat` | `gpt-5.5` | `global` | `USD` | `per-million-tokens` | `cached-input` | `text tokens` | `all` | `0.50` | `standard` | `2026-04-30` | `https://openai.com/api/pricing/` |
| `chat` | `gpt-5.5` | `global` | `USD` | `per-million-tokens` | `output` | `text tokens` | `all` | `30.00` | `standard` | `2026-04-30` | `https://openai.com/api/pricing/` |
| `chat` | `gpt-5.4` | `global` | `USD` | `per-million-tokens` | `input` | `text tokens` | `all` | `2.50` | `standard` | `2026-04-30` | `https://openai.com/api/pricing/` |
| `chat` | `gpt-5.4` | `global` | `USD` | `per-million-tokens` | `cached-input` | `text tokens` | `all` | `0.25` | `standard` | `2026-04-30` | `https://openai.com/api/pricing/` |
| `chat` | `gpt-5.4` | `global` | `USD` | `per-million-tokens` | `output` | `text tokens` | `all` | `15.00` | `standard` | `2026-04-30` | `https://openai.com/api/pricing/` |
| `chat` | `gpt-5.4-mini` | `global` | `USD` | `per-million-tokens` | `input` | `text tokens` | `all` | `0.75` | `standard` | `2026-04-30` | `https://openai.com/api/pricing/` |
| `chat` | `gpt-5.4-mini` | `global` | `USD` | `per-million-tokens` | `cached-input` | `text tokens` | `all` | `0.075` | `standard` | `2026-04-30` | `https://openai.com/api/pricing/` |
| `chat` | `gpt-5.4-mini` | `global` | `USD` | `per-million-tokens` | `output` | `text tokens` | `all` | `4.50` | `standard` | `2026-04-30` | `https://openai.com/api/pricing/` |
| `vision` | `gpt-5.5` | `global` | `USD` | `per-million-tokens` | `input` | `text/image tokens` | `all` | `5.00` | `image input is billed as input tokens` | `2026-04-30` | `https://openai.com/api/pricing/` |
| `vision` | `gpt-5.5` | `global` | `USD` | `per-million-tokens` | `cached-input` | `text/image tokens` | `all` | `0.50` | `image input is billed as input tokens` | `2026-04-30` | `https://openai.com/api/pricing/` |
| `vision` | `gpt-5.5` | `global` | `USD` | `per-million-tokens` | `output` | `text tokens` | `all` | `30.00` | `standard` | `2026-04-30` | `https://openai.com/api/pricing/` |
| `vision` | `gpt-5.4` | `global` | `USD` | `per-million-tokens` | `input` | `text/image tokens` | `all` | `2.50` | `image input is billed as input tokens` | `2026-04-30` | `https://openai.com/api/pricing/` |
| `vision` | `gpt-5.4` | `global` | `USD` | `per-million-tokens` | `cached-input` | `text/image tokens` | `all` | `0.25` | `image input is billed as input tokens` | `2026-04-30` | `https://openai.com/api/pricing/` |
| `vision` | `gpt-5.4` | `global` | `USD` | `per-million-tokens` | `output` | `text tokens` | `all` | `15.00` | `standard` | `2026-04-30` | `https://openai.com/api/pricing/` |
| `vision` | `gpt-5.4-mini` | `global` | `USD` | `per-million-tokens` | `input` | `text/image tokens` | `all` | `0.75` | `image input is billed as input tokens` | `2026-04-30` | `https://openai.com/api/pricing/` |
| `vision` | `gpt-5.4-mini` | `global` | `USD` | `per-million-tokens` | `cached-input` | `text/image tokens` | `all` | `0.075` | `image input is billed as input tokens` | `2026-04-30` | `https://openai.com/api/pricing/` |
| `vision` | `gpt-5.4-mini` | `global` | `USD` | `per-million-tokens` | `output` | `text tokens` | `all` | `4.50` | `standard` | `2026-04-30` | `https://openai.com/api/pricing/` |
| `imaging` | `gpt-image-2` | `global` | `USD` | `per-million-tokens` | `input` | `text tokens` | `all` | `5.00` | `Image API path` | `2026-04-30` | `https://openai.com/api/pricing/` |
| `imaging` | `gpt-image-2` | `global` | `USD` | `per-million-tokens` | `cached-input` | `text tokens` | `all` | `1.25` | `Image API path` | `2026-04-30` | `https://openai.com/api/pricing/` |
| `imaging` | `gpt-image-2` | `global` | `USD` | `per-million-tokens` | `image-input` | `image tokens` | `all` | `8.00` | `Image API path` | `2026-04-30` | `https://openai.com/api/pricing/` |
| `imaging` | `gpt-image-2` | `global` | `USD` | `per-million-tokens` | `cached-input` | `image tokens` | `all` | `2.00` | `Image API path` | `2026-04-30` | `https://openai.com/api/pricing/` |
| `imaging` | `gpt-image-2` | `global` | `USD` | `per-million-tokens` | `image-output` | `image tokens` | `all` | `30.00` | `Image API path` | `2026-04-30` | `https://openai.com/api/pricing/` |
