# DeepSeek Pricing Matrix

- `SchemaVersion: 2`
- `StructuralSnapshotDate: 2026-07-14`
- Prices are never read from model-catalog compatibility summaries.

Read `../../_shared/pricing-matrix-schema.md` first. A row is usable only when its complete billing/deployment/serving scope matches the resolved profile and `Pricing Status = current`.

## Current Matrix

| Request Kind | API Model | API Surface | API Version | Billing Region | Deployment Scope | Serving Region | Service Tier | Price Currency | Price Unit | Metered Side | Metered Item | Price Condition | Unit Price | Effective At | Expires At | Pricing Status | Last Verified At | Evidence Refs | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `text-chat` | `deepseek-v4-flash` | `all-documented-surfaces` | `all-documented-versions` | `global` | `global` | `global` | `standard` | `USD` | `per-million-tokens` | `input` | `cache-miss text tokens` | `all context; current published rate` | `0.14` | `unknown` | `none` | `current` | `2026-07-14` | `evset-deepseek-pricing-matrix-text-chat-deepseek-v4-flash-all-documented-surfaces-all-documented-versions-150e749007` | `Expired launch/discount wording removed; use the rate currently published on the official pricing page.` |
| `text-chat` | `deepseek-v4-flash` | `all-documented-surfaces` | `all-documented-versions` | `global` | `global` | `global` | `standard` | `USD` | `per-million-tokens` | `cached-input` | `cache-hit text tokens` | `all context; current published rate` | `0.0028` | `unknown` | `none` | `current` | `2026-07-14` | `evset-deepseek-pricing-matrix-text-chat-deepseek-v4-flash-all-documented-surfaces-all-documented-versions-80e6e5aa06` | `Expired launch/discount wording removed; use the rate currently published on the official pricing page.` |
| `text-chat` | `deepseek-v4-flash` | `all-documented-surfaces` | `all-documented-versions` | `global` | `global` | `global` | `standard` | `USD` | `per-million-tokens` | `output` | `text tokens` | `all context; current published rate` | `0.28` | `unknown` | `none` | `current` | `2026-07-14` | `evset-deepseek-pricing-matrix-text-chat-deepseek-v4-flash-all-documented-surfaces-all-documented-versions-b81ea6fc22` | `Expired launch/discount wording removed; use the rate currently published on the official pricing page.` |
| `text-chat` | `deepseek-v4-pro` | `all-documented-surfaces` | `all-documented-versions` | `global` | `global` | `global` | `standard` | `USD` | `per-million-tokens` | `input` | `cache-miss text tokens` | `all context; current published rate` | `0.435` | `unknown` | `none` | `current` | `2026-07-14` | `evset-deepseek-pricing-matrix-text-chat-deepseek-v4-pro-all-documented-surfaces-all-documented-versions-7db978f646` | `Expired launch/discount wording removed; use the rate currently published on the official pricing page.` |
| `text-chat` | `deepseek-v4-pro` | `all-documented-surfaces` | `all-documented-versions` | `global` | `global` | `global` | `standard` | `USD` | `per-million-tokens` | `cached-input` | `cache-hit text tokens` | `all context; current published rate` | `0.003625` | `unknown` | `none` | `current` | `2026-07-14` | `evset-deepseek-pricing-matrix-text-chat-deepseek-v4-pro-all-documented-surfaces-all-documented-versions-6b0bddc28d` | `Expired launch/discount wording removed; use the rate currently published on the official pricing page.` |
| `text-chat` | `deepseek-v4-pro` | `all-documented-surfaces` | `all-documented-versions` | `global` | `global` | `global` | `standard` | `USD` | `per-million-tokens` | `output` | `text tokens` | `all context; current published rate` | `0.87` | `unknown` | `none` | `current` | `2026-07-14` | `evset-deepseek-pricing-matrix-text-chat-deepseek-v4-pro-all-documented-surfaces-all-documented-versions-f5996a071c` | `Expired launch/discount wording removed; use the rate currently published on the official pricing page.` |

## Rules

- Do not apply a price across regions, deployment scopes, service tiers, or conditions.
- Promotions require their own effective and expiry window; missing or expired promotions are not estimated.
- `unknown` rows are informative hard stops, not zero cost.
- Claim details and official locators live in `../../_evidence/evidence.json`.
