# Aliyun Bailian International Model Catalog

Use this file as the local Aliyun Bailian International/Singapore model catalog for direct-model work.

Selection context for the current local catalog:

- sync date: `2026-05-01`
- recency boundary: `6 months`
- recency cutoff date: `2025-11-01`
- only rows with `Catalog Status = active` and `Selection Status = selected` are valid local options
- price region: `international`

China Mainland rows are owned by `../skill-llm-aliyun-bailian-cn` and must not be used by this skill.

## Dropdown Rule

When building a model selector:

- display `API Model`
- submit `API Model`
- keep `UI Label` equal to `API Model` if the column is present
- filter out rows whose `Catalog Status` is not `active`
- filter out rows whose `Selection Status` is not `selected`

## Pricing Rule

Use `pricing-matrix.md` for billing region, currency, context band, metered side, and unit price.

The catalog price columns are compatibility summaries only. Do not parse `Input Price`, `Output Price`, or `Pricing Note` to reconstruct tiered billing.

## Active Chat Models

| Model Type | API Model | Display Name | UI Label | Catalog Status | Selection Status | Is Default | Verification State | Recency Classification | Recency Basis Date | Recency Cutoff Date | Context Window Tokens | Max Input Tokens | Max Output Tokens | Price Region | Price Unit | Input Price | Output Price | Pricing Note | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `qwen3.6-max-preview` | `Qwen36MaxPreview` | `qwen3.6-max-preview` | `active` | `selected` | `yes` | `verified` | `candidate` | `2026-04-20` | `2025-11-01` | `262144` | `unknown` | `65536` | `international` | `per-million-tokens` | `0<Token<=128K: 9.742; 128K<Token<=256K: 14.988` | `0<Token<=128K: 58.455; 128K<Token<=256K: 89.93` | `official help-center pricing currently exposes the exact qwen3.6-max-preview row under international pricing` | `2026-05-01` | `release: https://help.aliyun.com/zh/model-studio/newly-released-models ; pricing: https://help.aliyun.com/zh/model-studio/billing/ ; capability: https://help.aliyun.com/zh/model-studio/text-generation-model` |

## Active Vision Models

No locally selected International vision rows yet.

## Active Imaging Models

No locally selected International imaging rows yet.

## Active Music Models

No locally selected International music rows yet.
