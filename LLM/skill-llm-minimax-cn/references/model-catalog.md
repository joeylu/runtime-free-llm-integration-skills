# MiniMax China Mainland Model Catalog

Use this file as the local MiniMax China Mainland model catalog for direct-model work.

Selection context for the current local catalog:

- initial add-provider date: `2026-05-03`
- recency boundary: `unreviewed`
- recency cutoff date: `unreviewed`
- only rows with `Catalog Status = active` and `Selection Status = selected` are valid local options
- price region: `china-mainland`

International rows are owned by `../skill-llm-minimax-intl` and must not be used by this skill.

## Dropdown Rule

When building a model selector:

- display `API Model`
- submit `API Model`
- keep `UI Label` equal to `API Model` if the column is present
- filter out rows whose `Catalog Status` is not `active`
- filter out rows whose `Selection Status` is not `selected`

## Pricing Rule

Use `pricing-matrix.md` for billing region, currency, context band, metered side, and unit price.

The catalog price columns are compatibility summaries only. Do not parse `Input Price`, `Output Price`, or `Pricing Note` to reconstruct billing.

## Active Chat Models

| Model Type | API Model | Display Name | UI Label | Catalog Status | Selection Status | Is Default | Verification State | Recency Classification | Recency Basis Date | Recency Cutoff Date | Context Window Tokens | Max Input Tokens | Max Output Tokens | Price Region | Price Unit | Input Price | Output Price | Pricing Note | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `MiniMax-M2.7` | `MiniMaxM27` | `MiniMax-M2.7` | `active` | `selected` | `yes` | `verified` | `unreviewed` | `2026-03-18` | `unreviewed` | `204800` | `unknown` | `2048` | `china-mainland` | `per-million-tokens` | `CNY 2.1` | `CNY 8.4` | `standard China Mainland pay-as-you-go pricing; cache read CNY 0.42 and cache write CNY 2.625 per 1M tokens` | `2026-05-03` | `release: https://platform.minimaxi.com/docs/release-notes/models ; api: https://platform.minimaxi.com/docs/api-reference/text-chat-openai ; pricing: https://platform.minimaxi.com/docs/guides/pricing-paygo` |
| `chat` | `MiniMax-M2.7-highspeed` | `MiniMaxM27Highspeed` | `MiniMax-M2.7-highspeed` | `active` | `selected` | `no` | `verified` | `unreviewed` | `2026-03-18` | `unreviewed` | `204800` | `unknown` | `2048` | `china-mainland` | `per-million-tokens` | `CNY 4.2` | `CNY 16.8` | `highspeed China Mainland pay-as-you-go row; cache read CNY 0.42 and cache write CNY 2.625 per 1M tokens` | `2026-05-03` | `release: https://platform.minimaxi.com/docs/release-notes/models ; api: https://platform.minimaxi.com/docs/api-reference/text-chat-openai ; pricing: https://platform.minimaxi.com/docs/guides/pricing-paygo` |

## Active Vision Models

No locally selected MiniMax China Mainland vision rows yet.

## Active Imaging Models

| Model Type | API Model | Display Name | UI Label | Catalog Status | Selection Status | Is Default | Verification State | Recency Classification | Recency Basis Date | Recency Cutoff Date | Context Window Tokens | Max Input Tokens | Max Output Tokens | Price Region | Price Unit | Input Price | Output Price | Pricing Note | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `imaging` | `image-01` | `Image01` | `image-01` | `active` | `selected` | `yes` | `verified` | `unreviewed` | `unreviewed` | `unreviewed` | `n/a` | `n/a` | `n/a` | `china-mainland` | `per-image` | `n/a` | `CNY 0.025` | `China Mainland pay-as-you-go image pricing is per generated image` | `2026-05-03` | `api: https://platform.minimaxi.com/docs/api-reference/image-generation-t2i ; pricing: https://platform.minimaxi.com/docs/guides/pricing-paygo` |

## Active Music Models

| Model Type | API Model | Display Name | UI Label | Catalog Status | Selection Status | Is Default | Verification State | Recency Classification | Recency Basis Date | Recency Cutoff Date | Context Window Tokens | Max Input Tokens | Max Output Tokens | Price Region | Price Unit | Input Price | Output Price | Pricing Note | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `music` | `music-2.6` | `Music26` | `music-2.6` | `active` | `selected` | `yes` | `verified` | `unreviewed` | `unreviewed` | `unreviewed` | `n/a` | `n/a` | `n/a` | `china-mainland` | `unknown` | `unknown` | `unknown` | `official Music Generation API verifies the model and endpoint; no China Mainland pay-as-you-go price row for music-2.6 was selected in this pass` | `2026-05-03` | `api: https://platform.minimaxi.com/docs/api-reference/music-generation ; pricing: https://platform.minimaxi.com/docs/guides/pricing-paygo` |

## Build-Only Video Reference

MiniMax China Mainland build-profile HTTP video generation is documented, but video is not a local catalog model type because `../_shared/model-catalog-schema.md` supports only `chat`, `vision`, `imaging`, and `music`.

Use `references/build-multimodal-http.md` for links, then stop before first-class video implementation unless the owner extends the shared schemas.

## Candidate Rows Not Selected In This Local Pass

| Model Type | API Model | Reason |
| --- | --- | --- |
| `chat` | `MiniMax-M2.5` | `candidate-not-selected; older chat row, not needed for the first M2.7 local set` |
| `imaging` | `image-01-live` | `candidate-not-selected; pricing page lists it with image-01, but this local pass selected only image-01 for the base HTTP image-generation flow` |
