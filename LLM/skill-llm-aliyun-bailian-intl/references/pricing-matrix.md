# Aliyun Bailian International Pricing Matrix

Use this file as the structured billing source for selected Aliyun Bailian International rows.

Do not reconstruct pricing from `model-catalog.md` notes.

| Model Type | API Model | Price Region | Price Currency | Price Unit | Metered Side | Metered Item | Context Band | Unit Price | Price Condition | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `qwen3.6-max-preview` | `international` | `USD` | `per-million-tokens` | `input` | `text tokens` | `0 < tokens <= 128K` | `9.742` | `standard` | `2026-04-24` | `https://help.aliyun.com/zh/model-studio/billing/` |
| `chat` | `qwen3.6-max-preview` | `international` | `USD` | `per-million-tokens` | `input` | `text tokens` | `128K < tokens <= 256K` | `14.988` | `standard` | `2026-04-24` | `https://help.aliyun.com/zh/model-studio/billing/` |
| `chat` | `qwen3.6-max-preview` | `international` | `USD` | `per-million-tokens` | `output` | `text tokens` | `0 < tokens <= 128K` | `58.455` | `standard` | `2026-04-24` | `https://help.aliyun.com/zh/model-studio/billing/` |
| `chat` | `qwen3.6-max-preview` | `international` | `USD` | `per-million-tokens` | `output` | `text tokens` | `128K < tokens <= 256K` | `89.93` | `standard` | `2026-04-24` | `https://help.aliyun.com/zh/model-studio/billing/` |
