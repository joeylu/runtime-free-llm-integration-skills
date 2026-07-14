# Aliyun Bailian International / Singapore Pricing Matrix

- `SchemaVersion: 2`
- `StructuralSnapshotDate: 2026-07-14`
- Prices are never read from model-catalog compatibility summaries.

Read `../../_shared/pricing-matrix-schema.md` first. A row is usable only when its complete billing/deployment/serving scope matches the resolved profile and `Pricing Status = current`.

## Current Matrix

| Request Kind | API Model | API Surface | API Version | Billing Region | Deployment Scope | Serving Region | Service Tier | Price Currency | Price Unit | Metered Side | Metered Item | Price Condition | Unit Price | Effective At | Expires At | Pricing Status | Last Verified At | Evidence Refs | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `text-chat` | `qwen3.7-max` | `all-documented-surfaces` | `all-documented-versions` | `singapore` | `international` | `singapore` | `standard` | `USD` | `per-million-tokens` | `input` | `text tokens` | `0 < tokens <= 1M; Singapore list price` | `2.5` | `unknown` | `none` | `current` | `2026-07-14` | `evset-aliyun-bailian-intl-pricing-matrix-text-chat-qwen3-7-max-all-documented-surfaces-all-documented-versions-ac7578d70f` | `Any separately advertised limited-time discount is excluded unless it has its own dated row.` |
| `text-chat` | `qwen3.7-max` | `all-documented-surfaces` | `all-documented-versions` | `singapore` | `international` | `singapore` | `standard` | `USD` | `per-million-tokens` | `output` | `text tokens` | `0 < tokens <= 1M; Singapore list price` | `7.5` | `unknown` | `none` | `current` | `2026-07-14` | `evset-aliyun-bailian-intl-pricing-matrix-text-chat-qwen3-7-max-all-documented-surfaces-all-documented-versions-394ac03737` | `Any separately advertised limited-time discount is excluded unless it has its own dated row.` |

## Rules

- Do not apply a price across regions, deployment scopes, service tiers, or conditions.
- Promotions require their own effective and expiry window; missing or expired promotions are not estimated.
- `unknown` rows are informative hard stops, not zero cost.
- Claim details and official locators live in `../../_evidence/evidence.json`.
