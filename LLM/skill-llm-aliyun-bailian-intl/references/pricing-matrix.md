# Aliyun Bailian International Pricing Matrix

Use this file as the structured billing source for documented Aliyun Bailian International rows.

Do not reconstruct pricing from `model-catalog.md` notes.

| Model Type | API Model | Price Region | Price Currency | Price Unit | Metered Side | Metered Item | Context Band | Billing Plan | Service Tier | List Unit Price | Effective Unit Price | Discount Kind | Valid From | Valid Until | Cache Class | Multiplier | Price Condition | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `qwen3.7-max` | `international` | `USD` | `per-million-tokens` | `input` | `text tokens` | `0 < tokens <= 1M` | `real-time` | `standard` | `2.5` | `1.25` | `limited-time-50-percent` | `2026-07-13` | `unknown` | `none` | `0.5` | `Singapore list price; limited-time 50% discount advertised separately` | `2026-07-13` | `https://www.alibabacloud.com/help/en/model-studio/model-pricing` |
| `chat` | `qwen3.7-max` | `international` | `USD` | `per-million-tokens` | `output` | `text tokens` | `0 < tokens <= 1M` | `real-time` | `standard` | `7.5` | `3.75` | `limited-time-50-percent` | `2026-07-13` | `unknown` | `none` | `0.5` | `Singapore list price; chain of thought plus answer; limited-time 50% discount advertised separately` | `2026-07-13` | `https://www.alibabacloud.com/help/en/model-studio/model-pricing` |
