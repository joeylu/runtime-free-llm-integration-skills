# DeepSeek Model Catalog

Use this file as the local DeepSeek model catalog for direct-model work.

Selection context for the current local catalog:

- sync date: `2026-05-01`
- recency boundary: `6 months`
- recency cutoff date: `2025-11-01`
- only rows with `Catalog Status = active` and `Selection Status = selected` are valid local options

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
| `chat` | `deepseek-v4-flash` | `DeepSeekV4Flash` | `deepseek-v4-flash` | `active` | `selected` | `yes` | `verified` | `candidate` | `2026-04-24` | `2025-11-01` | `1000000` | `unknown` | `393216` | `global` | `per-million-tokens` | `$0.14 cache miss; $0.0028 cache hit` | `$0.28` | `official pricing page lists current Flash pricing; cache-hit input price was reduced from launch price on 2026-04-26 UTC` | `2026-05-01` | `models/pricing: https://api-docs.deepseek.com/quick_start/pricing ; thinking: https://api-docs.deepseek.com/guides/thinking_mode` |
| `chat` | `deepseek-v4-pro` | `DeepSeekV4Pro` | `deepseek-v4-pro` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-04-24` | `2025-11-01` | `1000000` | `unknown` | `393216` | `global` | `per-million-tokens` | `$0.435 cache miss; $0.003625 cache hit` | `$0.87` | `official pricing page lists 75 percent discount until 2026-05-31 15:59 UTC; crossed-out list prices are input $1.74 and output $3.48` | `2026-05-01` | `models/pricing: https://api-docs.deepseek.com/quick_start/pricing ; thinking: https://api-docs.deepseek.com/guides/thinking_mode` |

## Active Vision Models

No locally selected DeepSeek vision rows yet.

## Active Imaging Models

No locally selected DeepSeek imaging rows yet.

## Active Music Models

No locally selected DeepSeek music rows yet.

## Candidate Rows Not Selected In This Local Pass

| Model Type | API Model | Reason |
| --- | --- | --- |
| `chat` | `deepseek-v3.2-exp` | `candidate-not-selected; previous generation experimental row on pricing page` |
| `chat` | `deepseek-chat` | `candidate-not-selected; alias-style row from older docs, not selected for the V4 local set` |
| `chat` | `deepseek-reasoner` | `candidate-not-selected; alias-style row from older docs, not selected for the V4 local set` |
