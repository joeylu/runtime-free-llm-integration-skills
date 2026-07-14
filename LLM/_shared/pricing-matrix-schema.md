# Shared Pricing Matrix Schema v2

Pricing is selected by an exact billing scope, not by model name alone.

## Required Key

`Request Kind + API Model + API Surface + API Version + Billing Region + Deployment Scope + Serving Region + Service Tier + Metered Side + Metered Item + Price Condition + Effective At`

## Required Columns

| Column | Meaning |
| --- | --- |
| `Request Kind` | Canonical request kind |
| `API Model` | Exact provider model ID |
| `API Surface` | Exact surface, or `all-documented-surfaces` only when the provider explicitly prices the model independently of surface |
| `API Version` | Exact version, `provider-default`, or `all-documented-versions` only when official pricing is version-independent |
| `Billing Region` | Region used for billing, never the vague value `international` when official prices differ by region |
| `Deployment Scope` | Provider scope such as `global`, `international`, `china-mainland`, or `workspace-specific` |
| `Serving Region` | Actual serving/deployment region such as `singapore`, `beijing`, or `global` |
| `Service Tier` | `standard`, `priority`, `batch`, or another exact official tier |
| `Price Currency` | ISO currency code |
| `Price Unit` | Exact billing unit |
| `Metered Side` | `input`, `cached-input`, `cache-write`, `output`, `image-output`, `request`, or another explicit side |
| `Metered Item` | What is measured |
| `Price Condition` | Context band, mode, quality, duration, or other condition |
| `Unit Price` | Numeric price or `unknown` |
| `Effective At` | Official start date/time if known; otherwise `unknown`; never substitute the review date |
| `Expires At` | Promotion/end date, `none`, or `unknown` |
| `Pricing Status` | `current`, `scheduled`, `expired`, `unknown`, or `historical` |
| `Last Verified At` | Exact review date |
| `Evidence Refs` | Pricing evidence-set IDs |
| `Notes` | Non-normative explanation |

## Rules

- `all-documented-surfaces` and `all-documented-versions` are allowed only when the official pricing source prices the model independently of those dimensions.
- A price is usable only when every key dimension needed by the provider is known and `Pricing Status = current`.
- Never apply a Singapore price to Global, US, EU, or another deployment scope.
- Promotions require an explicit effective window when the provider publishes one. Expired rows remain historical and are never used for estimates.
- If the provider shows a current discounted price without an end date, record that current price, `Expires At = unknown`, and do not invent a future rollback.
- Pricing pages are authoritative for price; model cards and examples are not substitutes.
- Do not parse compatibility summaries in `model-catalog.md` for billing.
