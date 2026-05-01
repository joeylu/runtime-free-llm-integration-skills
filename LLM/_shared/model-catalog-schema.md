# Shared Model Catalog Schema

Use this file to keep every `skill-llm-xxxx` model catalog shaped the same way.

## Required Columns

| Column | Meaning |
| --- | --- |
| `Model Type` | One of `chat`, `vision`, `imaging`, or `music` |
| `API Model` | Exact provider model identifier sent over the wire |
| `Display Name` | Short human-readable model name |
| `UI Label` | Legacy compatibility label; keep equal to `API Model` for model dropdowns |
| `Catalog Status` | One of `active`, `deprecated`, or `removed` |
| `Selection Status` | One of `selected`, `not-selected`, or `unreviewed` |
| `Is Default` | `yes` or `no` for the local default choice within one model type |
| `Verification State` | One of `verified`, `inherited`, or `unknown` |
| `Recency Classification` | One of `candidate`, `retired`, or `unreviewed` |
| `Recency Basis Date` | Official date used for the recency decision, or `unreviewed` |
| `Recency Cutoff Date` | Absolute cutoff date used in the last sync review, or `unreviewed` |
| `Context Window Tokens` | Official total context window token count, or `unknown` / `n/a` |
| `Max Input Tokens` | Official maximum input token count, or `unknown` / `n/a` |
| `Max Output Tokens` | Official maximum output token count, or `unknown` / `n/a` |
| `Price Region` | Compatibility pricing summary; use `pricing-matrix.md` for structured billing |
| `Price Unit` | Compatibility billing-unit summary; use `pricing-matrix.md` for structured billing |
| `Input Price` | Compatibility input-price summary, or `n/a` / `unknown` |
| `Output Price` | Compatibility output-price summary, or `n/a` / `unknown` |
| `Pricing Note` | Human-readable price note; do not parse it for billing logic |
| `Last Verified At` | Absolute verification date or `unverified` |
| `Source` | Exact official source URL or explicit inherited source note |

## Rules

- Show only `active` rows in selectors by default.
- Use `API Model` as both model dropdown display text and submitted value.
- If a catalog retains `UI Label`, keep it equal to `API Model`. Do not include prices, aliases, or extra marketing text in model option labels.
- Do not silently delete old rows during sync. Mark them `deprecated` or `removed`.
- Use absolute dates after sync, for example `2026-04-24`.
- If the row was copied from an older skill and not re-checked yet, use `Verification State = inherited`.
- `Catalog Status = active` should only be used together with `Selection Status = selected`.
- Keep at most one `Is Default = yes` row per `Model Type`.
- If a row is outside the confirmed recency boundary, set `Recency Classification = retired`.
- A row marked `retired` should not stay `active`.
- If a row has not been reviewed against a confirmed boundary yet, use `unreviewed` values for the recency fields.
- Keep `Context Window Tokens`, `Max Input Tokens`, and `Max Output Tokens` explicit. Use exact official numeric token counts when verified.
- If an official token limit differs by mode, store every exact mode-qualified value in the same field, for example `thinking: 983616; non-thinking: 991808`.
- Use `unknown` when official docs do not clearly expose a context value. Do not infer context limits from pricing tiers, reasoning budgets, sibling models, SDK names, or observed runtime errors.
- Use `n/a` only when a token context value does not apply to the request kind.
- Keep `Price Region`, `Price Unit`, `Input Price`, and `Output Price` explicit as compatibility summaries.
- Use provider `references/pricing-matrix.md` as the source of truth for region, currency, context band, metered side, and unit price.
- Do not make downstream agents parse `Input Price`, `Output Price`, or `Pricing Note` to reconstruct tiered billing.

## Example

For model dropdowns, display and submit the same value: `API Model = qwen3.5-plus`.
