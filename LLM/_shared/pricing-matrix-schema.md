# Shared Pricing Matrix Schema

Use this file to keep provider pricing data structured and separate from capability rules.

## Required Columns

| Column | Meaning |
| --- | --- |
| `Model Type` | compatibility request kind |
| `API Model` | exact provider model identifier |
| `Price Region` | exact provider billing region |
| `Price Currency` | ISO 4217 code or `unknown` |
| `Price Unit` | billing unit such as `per-million-tokens`, `per-image`, or `mixed` |
| `Metered Side` | input/output/cache/image/audio/tool side |
| `Metered Item` | what is metered |
| `Context Band` | exact official token, size, duration, or other band |
| `Billing Plan` | `real-time`, `batch`, or another documented plan |
| `Service Tier` | `standard`, `priority`, `flex`, or provider-defined tier |
| `List Unit Price` | undiscounted published unit price, or `unknown`/`n/a` |
| `Effective Unit Price` | currently applicable unit price, or `unknown`/`n/a` |
| `Discount Kind` | `none`, a structured discount label, or `unknown` |
| `Valid From` | effective start date/time or `unknown` |
| `Valid Until` | effective end date/time, `open-ended`, or `unknown` |
| `Cache Class` | `none`, `cache-read`, `cache-write`, or `cache-storage` |
| `Multiplier` | multiplier from list to effective price when directly documented |
| `Price Condition` | residual constraint that is not represented by structured columns |
| `Last Verified At` | absolute verification date or `unverified` |
| `Source` | exact official source URL |

## Rules

- Keep one row per priceable side, item, region, plan, tier, currency, unit, and context band.
- Do not combine input and output prices in one row.
- Keep list price and temporary effective price separate.
- Never compound a promotional discount with batch, priority, cache, or other discounts unless the provider explicitly documents compounding.
- If a promotion has no published end date, set `Valid Until = unknown`; consumers must refresh before relying on it.
- Use `unknown` for missing prices. Do not infer from sibling models or unofficial calculators.
- Treat this matrix as the source of truth for billing UI and estimates.
