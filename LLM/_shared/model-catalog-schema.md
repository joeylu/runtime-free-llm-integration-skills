# Shared Model Catalog Schema

Use this file to keep every `skill-llm-xxxx` model catalog shaped the same way.

## Required Columns

| Column | Meaning |
| --- | --- |
| `Model Type` | One of `chat`, `vision`, `imaging`, or `music` |
| `API Model` | Exact provider model identifier sent over the wire |
| `Display Name` | Short human-readable model name |
| `UI Label` | Ready-to-render dropdown label |
| `Catalog Status` | One of `active`, `deprecated`, or `removed` |
| `Selection Status` | One of `selected`, `not-selected`, or `unreviewed` |
| `Is Default` | `yes` or `no` for the local default choice within one model type |
| `Verification State` | One of `verified`, `inherited`, or `unknown` |
| `Recency Classification` | One of `candidate`, `retired`, or `unreviewed` |
| `Recency Basis Date` | Official date used for the recency decision, or `unreviewed` |
| `Recency Cutoff Date` | Absolute cutoff date used in the last sync review, or `unreviewed` |
| `Price Region` | Pricing region such as `china-mainland`, `global`, or `international` |
| `Price Unit` | Billing unit such as `per-million-tokens` or `per-image` |
| `Input Price` | Exact official input price, or `n/a` / `unknown` |
| `Output Price` | Exact official output price, or `n/a` / `unknown` |
| `Pricing Note` | Human-readable price note for UI or docs |
| `Last Verified At` | Absolute verification date or `unverified` |
| `Source` | Exact official source URL or explicit inherited source note |

## Rules

- Show only `active` rows in selectors by default.
- Keep `UI Label` and `API Model` separate.
- Do not silently delete old rows during sync. Mark them `deprecated` or `removed`.
- Use absolute dates after sync, for example `2026-04-24`.
- If the row was copied from an older skill and not re-checked yet, use `Verification State = inherited`.
- `Catalog Status = active` should only be used together with `Selection Status = selected`.
- Keep at most one `Is Default = yes` row per `Model Type`.
- If a row is outside the confirmed recency boundary, set `Recency Classification = retired`.
- A row marked `retired` should not stay `active`.
- If a row has not been reviewed against a confirmed boundary yet, use `unreviewed` values for the recency fields.
- Keep `Price Region`, `Price Unit`, `Input Price`, and `Output Price` explicit. Do not bury exact prices only inside `Pricing Note`.

## Example

`UI Label` is the user-facing text such as `Qwen35Plus_in0.8rmb_out4.8rmb`, while `API Model` is the submitted value such as `qwen3.5-plus`.
