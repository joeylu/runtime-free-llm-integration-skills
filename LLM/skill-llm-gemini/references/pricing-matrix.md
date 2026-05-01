# Gemini Pricing Matrix

Use this file as the structured billing source for selected Gemini rows.

Do not reconstruct pricing from `model-catalog.md` notes.

| Model Type | API Model | Price Region | Price Currency | Price Unit | Metered Side | Metered Item | Context Band | Unit Price | Price Condition | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `gemini-3-flash-preview` | `global` | `USD` | `per-million-tokens` | `input` | `text tokens` | `all` | `0.50` | `standard paid tier` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `chat` | `gemini-3-flash-preview` | `global` | `USD` | `per-million-tokens` | `output` | `text/thinking tokens` | `all` | `3.00` | `thinking tokens included` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `chat` | `gemini-3.1-pro-preview` | `global` | `USD` | `per-million-tokens` | `input` | `text tokens` | `tokens <= 200K` | `2.00` | `standard paid tier` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `chat` | `gemini-3.1-pro-preview` | `global` | `USD` | `per-million-tokens` | `input` | `text tokens` | `tokens > 200K` | `4.00` | `standard paid tier` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `chat` | `gemini-3.1-pro-preview` | `global` | `USD` | `per-million-tokens` | `output` | `text/thinking tokens` | `tokens <= 200K` | `12.00` | `thinking tokens included` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `chat` | `gemini-3.1-pro-preview` | `global` | `USD` | `per-million-tokens` | `output` | `text/thinking tokens` | `tokens > 200K` | `18.00` | `thinking tokens included` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `vision` | `gemini-3-flash-preview` | `global` | `USD` | `per-million-tokens` | `input` | `text/image/video tokens` | `all` | `0.50` | `standard paid tier` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `vision` | `gemini-3-flash-preview` | `global` | `USD` | `per-million-tokens` | `audio-input` | `audio tokens` | `all` | `1.00` | `standard paid tier` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `vision` | `gemini-3-flash-preview` | `global` | `USD` | `per-million-tokens` | `output` | `text/thinking tokens` | `all` | `3.00` | `thinking tokens included` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `vision` | `gemini-3.1-pro-preview` | `global` | `USD` | `per-million-tokens` | `input` | `text/image/video/audio tokens` | `tokens <= 200K` | `2.00` | `standard paid tier` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `vision` | `gemini-3.1-pro-preview` | `global` | `USD` | `per-million-tokens` | `input` | `text/image/video/audio tokens` | `tokens > 200K` | `4.00` | `standard paid tier` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `vision` | `gemini-3.1-pro-preview` | `global` | `USD` | `per-million-tokens` | `output` | `text/thinking tokens` | `tokens <= 200K` | `12.00` | `thinking tokens included` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `vision` | `gemini-3.1-pro-preview` | `global` | `USD` | `per-million-tokens` | `output` | `text/thinking tokens` | `tokens > 200K` | `18.00` | `thinking tokens included` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `imaging` | `gemini-3.1-flash-image-preview` | `global` | `USD` | `per-million-tokens` | `input` | `text/image tokens` | `all` | `0.50` | `standard paid tier` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `imaging` | `gemini-3.1-flash-image-preview` | `global` | `USD` | `per-million-tokens` | `output` | `text/thinking tokens` | `all` | `3.00` | `thinking tokens included` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `imaging` | `gemini-3.1-flash-image-preview` | `global` | `USD` | `per-million-tokens` | `image-output` | `image tokens` | `all` | `60.00` | `image output token billing` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `imaging` | `gemini-3.1-flash-image-preview` | `global` | `USD` | `per-image` | `image-output` | `image` | `0.5K image` | `0.045` | `equivalent image price` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `imaging` | `gemini-3.1-flash-image-preview` | `global` | `USD` | `per-image` | `image-output` | `image` | `1K image` | `0.067` | `equivalent image price` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `imaging` | `gemini-3.1-flash-image-preview` | `global` | `USD` | `per-image` | `image-output` | `image` | `2K image` | `0.101` | `equivalent image price` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `imaging` | `gemini-3.1-flash-image-preview` | `global` | `USD` | `per-image` | `image-output` | `image` | `4K image` | `0.151` | `equivalent image price` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `imaging` | `gemini-3-pro-image-preview` | `global` | `USD` | `per-million-tokens` | `input` | `text/image tokens` | `all` | `2.00` | `standard paid tier` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `imaging` | `gemini-3-pro-image-preview` | `global` | `USD` | `per-million-tokens` | `output` | `text/thinking tokens` | `all` | `12.00` | `thinking tokens included` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `imaging` | `gemini-3-pro-image-preview` | `global` | `USD` | `per-million-tokens` | `image-output` | `image tokens` | `all` | `120.00` | `image output token billing` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `imaging` | `gemini-3-pro-image-preview` | `global` | `USD` | `per-image` | `image-output` | `image` | `1K or 2K image` | `0.134` | `equivalent image price` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `imaging` | `gemini-3-pro-image-preview` | `global` | `USD` | `per-image` | `image-output` | `image` | `4K image` | `0.24` | `equivalent image price` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `imaging` | `gemini-2.5-flash-image` | `global` | `USD` | `per-million-tokens` | `input` | `text/image tokens` | `all` | `0.30` | `standard paid tier` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `imaging` | `gemini-2.5-flash-image` | `global` | `USD` | `per-million-tokens` | `image-output` | `image tokens` | `all` | `30.00` | `1290 tokens per image <= 1024x1024` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
| `imaging` | `gemini-2.5-flash-image` | `global` | `USD` | `per-image` | `image-output` | `image` | `image <= 1024x1024` | `0.039` | `equivalent image price` | `2026-05-01` | `https://ai.google.dev/gemini-api/docs/pricing` |
