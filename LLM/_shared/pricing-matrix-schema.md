# Shared Pricing Matrix Schema

Use this file to keep provider pricing data structured and separate from model selection.

`model-catalog.md` decides which models can be selected. `pricing-matrix.md` decides how a selected model is priced.

## Required Columns

| Column | Meaning |
| --- | --- |
| `Model Type` | One of `chat`, `vision`, `imaging`, or `music` |
| `API Model` | Exact provider model identifier sent over the wire |
| `Price Region` | Provider billing region such as `global`, `china-mainland`, or `international` |
| `Price Currency` | ISO 4217 currency code such as `USD`, `CNY`, or `unknown` |
| `Price Unit` | Billing unit such as `per-million-tokens`, `per-image`, or `mixed` |
| `Metered Side` | `input`, `cached-input`, `output`, `image-input`, `image-output`, `audio-input`, or `unknown` |
| `Metered Item` | What is metered, such as `text tokens`, `image tokens`, `audio tokens`, or `image` |
| `Context Band` | The exact official band, such as `all`, `0 < tokens <= 256K`, or `image <= 1024x1024` |
| `Unit Price` | Numeric official price for one `Price Unit`, or `unknown` / `n/a` |
| `Price Condition` | Explicit condition such as `standard`, `batch unsupported`, `prompt_extend=true`, or discount window |
| `Last Verified At` | Absolute verification date or `unverified` |
| `Source` | Exact official source URL or explicit inherited source note |

## Rules

- Keep one row per priceable side, item, region, currency, unit, and context band.
- Do not combine multiple context bands in one price cell.
- Do not combine input and output prices in one row.
- Use `Price Currency = unknown` when the official docs do not clearly expose the currency.
- Use `Context Band = all` only when the price does not vary by context length, token range, image size, or another published band.
- Use `unknown` for missing prices. Do not infer prices from sibling models, unofficial calculators, SDK constants, or runtime billing errors.
- Treat `pricing-matrix.md` as the source of truth for billing UI, estimates, and cost documentation.
- Treat model-catalog price fields as compatibility summaries only; do not parse `Pricing Note` to reconstruct price bands.

## Example

For a tiered model, use separate rows:

| Model Type | API Model | Price Region | Price Currency | Price Unit | Metered Side | Metered Item | Context Band | Unit Price | Price Condition | Last Verified At | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chat` | `qwen3.6-plus` | `china-mainland` | `CNY` | `per-million-tokens` | `input` | `text tokens` | `0 < tokens <= 256K` | `2` | `standard` | `2026-05-01` | `https://help.aliyun.com/zh/model-studio/billing/` |
| `chat` | `qwen3.6-plus` | `china-mainland` | `CNY` | `per-million-tokens` | `input` | `text tokens` | `256K < tokens <= 1M` | `8` | `standard` | `2026-05-01` | `https://help.aliyun.com/zh/model-studio/billing/` |
