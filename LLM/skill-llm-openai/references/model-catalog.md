# OpenAI Model Catalog

Use this file as the local OpenAI model catalog for direct-model work.

Selection context for the current local catalog:

- initial verification date: `2026-04-30`
- recency boundary: `not-confirmed`
- recency cutoff date: `unreviewed`
- only rows with `Catalog Status = active` and `Selection Status = selected` are valid local options

Meanings:

- `Catalog Status`: local availability flag used by this skill
- `Selection Status`: whether the row was chosen into the local model set
- `Recency Classification`: whether the row is inside the last confirmed sync boundary

## Dropdown Rule

When building a model selector:

- display `UI Label`
- submit `API Model`
- filter out rows whose `Catalog Status` is not `active`
- filter out rows whose `Selection Status` is not `selected`

## Active Chat Models

| Model Type | API Model | Display Name | UI Label | Catalog Status | Selection Status | Is Default | Verification State | Recency Classification | Recency Basis Date | Recency Cutoff Date | Price Region | Price Unit | Input Price | Output Price | Pricing Note | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `gpt-5.5` | `GPT55` | `GPT55_default_in5usd_out30usd` | `active` | `selected` | `yes` | `verified` | `unreviewed` | `unreviewed` | `unreviewed` | `global` | `per-million-tokens` | `$5.00` | `$30.00` | `flagship model for complex reasoning and coding; cached input $0.50 per 1M tokens` | `2026-04-30` | `models: https://developers.openai.com/api/docs/models ; latest: https://developers.openai.com/api/docs/guides/latest-model ; pricing: https://openai.com/api/pricing/` |
| `chat` | `gpt-5.4` | `GPT54` | `GPT54_in2.5usd_out15usd` | `active` | `selected` | `no` | `verified` | `unreviewed` | `unreviewed` | `unreviewed` | `global` | `per-million-tokens` | `$2.50` | `$15.00` | `more affordable model for coding and professional work; cached input $0.25 per 1M tokens` | `2026-04-30` | `models: https://developers.openai.com/api/docs/models ; pricing: https://openai.com/api/pricing/` |
| `chat` | `gpt-5.4-mini` | `GPT54Mini` | `GPT54Mini_in0.75usd_out4.5usd` | `active` | `selected` | `no` | `verified` | `unreviewed` | `unreviewed` | `unreviewed` | `global` | `per-million-tokens` | `$0.75` | `$4.50` | `strong mini model for lower-latency, lower-cost workloads; cached input $0.075 per 1M tokens` | `2026-04-30` | `models: https://developers.openai.com/api/docs/models ; pricing: https://openai.com/api/pricing/` |

## Active Vision Models

| Model Type | API Model | Display Name | UI Label | Catalog Status | Selection Status | Is Default | Verification State | Recency Classification | Recency Basis Date | Recency Cutoff Date | Price Region | Price Unit | Input Price | Output Price | Pricing Note | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `vision` | `gpt-5.5` | `GPT55Vision` | `GPT55Vision_default_in5usd_out30usd` | `active` | `selected` | `yes` | `verified` | `unreviewed` | `unreviewed` | `unreviewed` | `global` | `per-million-tokens` | `$5.00` | `$30.00` | `all latest OpenAI models support text and image input; image input is billed as input tokens` | `2026-04-30` | `models: https://developers.openai.com/api/docs/models ; latest: https://developers.openai.com/api/docs/guides/latest-model ; pricing: https://openai.com/api/pricing/` |
| `vision` | `gpt-5.4` | `GPT54Vision` | `GPT54Vision_in2.5usd_out15usd` | `active` | `selected` | `no` | `verified` | `unreviewed` | `unreviewed` | `unreviewed` | `global` | `per-million-tokens` | `$2.50` | `$15.00` | `all latest OpenAI models support text and image input; image input is billed as input tokens` | `2026-04-30` | `models: https://developers.openai.com/api/docs/models ; pricing: https://openai.com/api/pricing/` |
| `vision` | `gpt-5.4-mini` | `GPT54MiniVision` | `GPT54MiniVision_in0.75usd_out4.5usd` | `active` | `selected` | `no` | `verified` | `unreviewed` | `unreviewed` | `unreviewed` | `global` | `per-million-tokens` | `$0.75` | `$4.50` | `all latest OpenAI models support text and image input; image input is billed as input tokens` | `2026-04-30` | `models: https://developers.openai.com/api/docs/models ; pricing: https://openai.com/api/pricing/` |

## Active Imaging Models

| Model Type | API Model | Display Name | UI Label | Catalog Status | Selection Status | Is Default | Verification State | Recency Classification | Recency Basis Date | Recency Cutoff Date | Price Region | Price Unit | Input Price | Output Price | Pricing Note | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `imaging` | `gpt-image-2` | `GPTImage2` | `GPTImage2_default_image_in8usd_out30usd` | `active` | `selected` | `yes` | `verified` | `unreviewed` | `unreviewed` | `unreviewed` | `global` | `per-million-tokens` | `image: $8.00; text: $5.00` | `image: $30.00` | `pricing is token based; cached image input $2.00 and cached text input $1.25 per 1M tokens` | `2026-04-30` | `image docs: https://developers.openai.com/api/docs/guides/image-generation ; pricing: https://openai.com/api/pricing/` |

## Active Music Models

No locally selected music rows yet.

## Candidate Rows Not Selected In This Local Pass

| Model Type | API Model | Reason |
| --- | --- | --- |
| `chat` | `gpt-5.5-pro` | `candidate-not-selected; long-running pro path needs separate background-mode rules before becoming a default local option` |
| `chat` | `gpt-5.4-nano` | `candidate-not-selected; useful for low-cost workflows but not selected in this first ChatGPT/OpenAI structure pass` |
