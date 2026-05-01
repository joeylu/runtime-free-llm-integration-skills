# Gemini Model Catalog

Use this file as the local Gemini model catalog for direct-model work.

Selection context for the current local catalog:

- sync date: `2026-05-01`
- recency boundary: `6 months`
- recency cutoff date: `2025-11-01`
- only rows with `Catalog Status = active` and `Selection Status = selected` are valid local options

Meanings:

- `Catalog Status`: local availability flag used by this skill
- `Selection Status`: whether the row was chosen into the local model set
- `Recency Classification`: whether the row is inside the last confirmed sync boundary

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
| `chat` | `gemini-3-flash-preview` | `Gemini3FlashPreview` | `gemini-3-flash-preview` | `active` | `selected` | `yes` | `verified` | `candidate` | `2026-04-28` | `2025-11-01` | `1048576` | `1048576` | `65536` | `global` | `per-million-tokens` | `$0.50 text/image/video; $1.00 audio` | `$3.00 including thinking tokens` | `standard paid tier; free tier may be available but production billing uses paid tier values` | `2026-05-01` | `model: https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview ; pricing: https://ai.google.dev/gemini-api/docs/pricing ; thinking: https://ai.google.dev/gemini-api/docs/thinking` |
| `chat` | `gemini-3.1-pro-preview` | `Gemini31ProPreview` | `gemini-3.1-pro-preview` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-04-28` | `2025-11-01` | `1048576` | `1048576` | `65536` | `global` | `per-million-tokens` | `$2.00 <=200k tokens; $4.00 >200k tokens` | `$12.00 <=200k tokens; $18.00 >200k tokens, including thinking tokens` | `standard paid tier; customtools sibling endpoint is not selected in this local pass` | `2026-05-01` | `model: https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview ; pricing: https://ai.google.dev/gemini-api/docs/pricing ; thinking: https://ai.google.dev/gemini-api/docs/thinking` |

## Active Vision Models

| Model Type | API Model | Display Name | UI Label | Catalog Status | Selection Status | Is Default | Verification State | Recency Classification | Recency Basis Date | Recency Cutoff Date | Context Window Tokens | Max Input Tokens | Max Output Tokens | Price Region | Price Unit | Input Price | Output Price | Pricing Note | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `vision` | `gemini-3-flash-preview` | `Gemini3FlashVision` | `gemini-3-flash-preview` | `active` | `selected` | `yes` | `verified` | `candidate` | `2026-04-28` | `2025-11-01` | `1048576` | `1048576` | `65536` | `global` | `per-million-tokens` | `$0.50 text/image/video; $1.00 audio` | `$3.00 including thinking tokens` | `model supports text, image, video, audio, and PDF inputs; image input is priced as input tokens` | `2026-05-01` | `model: https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview ; pricing: https://ai.google.dev/gemini-api/docs/pricing ; vision: https://ai.google.dev/gemini-api/docs/text-generation` |
| `vision` | `gemini-3.1-pro-preview` | `Gemini31ProVision` | `gemini-3.1-pro-preview` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-04-28` | `2025-11-01` | `1048576` | `1048576` | `65536` | `global` | `per-million-tokens` | `$2.00 <=200k tokens; $4.00 >200k tokens` | `$12.00 <=200k tokens; $18.00 >200k tokens, including thinking tokens` | `model supports text, image, video, audio, and PDF inputs; image input is priced as input tokens` | `2026-05-01` | `model: https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview ; pricing: https://ai.google.dev/gemini-api/docs/pricing ; vision: https://ai.google.dev/gemini-api/docs/text-generation` |

## Active Imaging Models

| Model Type | API Model | Display Name | UI Label | Catalog Status | Selection Status | Is Default | Verification State | Recency Classification | Recency Basis Date | Recency Cutoff Date | Context Window Tokens | Max Input Tokens | Max Output Tokens | Price Region | Price Unit | Input Price | Output Price | Pricing Note | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `imaging` | `gemini-3.1-flash-image-preview` | `NanoBanana2Preview` | `gemini-3.1-flash-image-preview` | `active` | `selected` | `yes` | `verified` | `candidate` | `2026-04-28` | `2025-11-01` | `131072` | `131072` | `32768` | `global` | `mixed` | `$0.50 per 1M text/image input tokens` | `$3.00 per 1M text/thinking output tokens; $60.00 per 1M image output tokens` | `standard paid tier; image equivalents: $0.045 per 0.5K, $0.067 per 1K, $0.101 per 2K, $0.151 per 4K image` | `2026-05-01` | `model: https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image-preview ; image docs: https://ai.google.dev/gemini-api/docs/image-generation ; pricing: https://ai.google.dev/gemini-api/docs/pricing` |
| `imaging` | `gemini-3-pro-image-preview` | `NanoBananaProPreview` | `gemini-3-pro-image-preview` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-04-28` | `2025-11-01` | `65536` | `65536` | `32768` | `global` | `mixed` | `$2.00 per 1M text/image input tokens` | `$12.00 per 1M text/thinking output tokens; $120.00 per 1M image output tokens` | `standard paid tier; image equivalents: $0.134 per 1K/2K image and $0.24 per 4K image` | `2026-05-01` | `model: https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview ; image docs: https://ai.google.dev/gemini-api/docs/image-generation ; pricing: https://ai.google.dev/gemini-api/docs/pricing` |
| `imaging` | `gemini-2.5-flash-image` | `NanoBanana` | `gemini-2.5-flash-image` | `active` | `selected` | `no` | `verified` | `candidate` | `2026-04-28` | `2025-11-01` | `65536` | `65536` | `32768` | `global` | `mixed` | `$0.30 per 1M text/image input tokens` | `$0.039 per image up to 1024x1024` | `standard paid tier; official docs also describe image output as $30 per 1M tokens with 1290 tokens per <=1024x1024 output image` | `2026-05-01` | `model: https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image ; image docs: https://ai.google.dev/gemini-api/docs/image-generation ; pricing: https://ai.google.dev/gemini-api/docs/pricing` |

## Active Music Models

No locally selected music rows yet.

## Candidate Rows Not Selected In This Local Pass

| Model Type | API Model | Reason |
| --- | --- | --- |
| `chat` | `gemini-3.1-flash-lite-preview` | `candidate-not-selected; useful low-cost Gemini 3 row, but not selected in the first Gemini structure pass` |
| `chat` | `gemini-3.1-pro-preview-customtools` | `candidate-not-selected; specialized custom-tools endpoint needs separate transport notes before local selection` |
| `imaging` | `imagen-4.0-generate-001` | `candidate-not-selected; Imagen family is separate from Nano Banana and needs its own imaging capability pass` |
